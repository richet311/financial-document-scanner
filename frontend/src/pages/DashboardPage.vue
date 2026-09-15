<script setup>
import { computed, ref, watchEffect } from 'vue'
import { supabase } from '../lib/supabaseClient'
import { authStore } from '../store/auth'

const DOCUMENT_TYPES = ['pay_stub', 'bank_statement', 'budget_sheet']

function isoDate(date) {
  return date.toISOString().slice(0, 10)
}

const today = new Date()
const thirtyDaysAgo = new Date(today)
thirtyDaysAgo.setDate(thirtyDaysAgo.getDate() - 30)

const startDate = ref(isoDate(thirtyDaysAgo))
const endDate = ref(isoDate(today))
const typeFilter = ref('all')

const scans = ref([])
const loading = ref(false)
const loadError = ref('')

async function loadScans() {
  if (!authStore.user) return

  loading.value = true
  loadError.value = ''
  try {
    let query = supabase
      .from('scans')
      .select('*')
      .gte('created_at', `${startDate.value}T00:00:00.000Z`)
      .lte('created_at', `${endDate.value}T23:59:59.999Z`)
      .order('created_at', { ascending: false })

    if (typeFilter.value !== 'all') {
      query = query.eq('document_type', typeFilter.value)
    }

    const { data, error } = await query
    if (error) throw new Error(error.message)
    scans.value = data ?? []
  } catch (err) {
    loadError.value = err.message
  } finally {
    loading.value = false
  }
}

watchEffect(() => {
  if (authStore.user) loadScans()
})

const totalScans = computed(() => scans.value.length)

const typeCounts = computed(() => {
  const counts = {}
  for (const item of scans.value) {
    const type = item.document_type || 'unknown'
    counts[type] = (counts[type] || 0) + 1
  }
  return counts
})

const averageConfidence = computed(() => {
  const withConfidence = scans.value.filter((item) => item.confidence != null)
  if (!withConfidence.length) return null
  const sum = withConfidence.reduce((total, item) => total + item.confidence, 0)
  return (sum / withConfidence.length) * 100
})

const DONUT_COLORS = ['#0b419e', '#ff8000', '#71b603', '#b11616', '#9b9fa6']

const donutSegments = computed(() => {
  const total = totalScans.value
  if (!total) return []

  const radius = 60
  const circumference = 2 * Math.PI * radius
  let cumulative = 0

  return Object.entries(typeCounts.value).map(([type, count], index) => {
    const fraction = count / total
    const dash = fraction * circumference
    const segment = {
      type,
      count,
      percentage: fraction * 100,
      color: DONUT_COLORS[index % DONUT_COLORS.length],
      dasharray: `${dash} ${circumference - dash}`,
      dashoffset: -cumulative * circumference,
    }
    cumulative += fraction
    return segment
  })
})

const dailyCounts = computed(() => {
  const buckets = {}
  for (const item of scans.value) {
    const day = item.created_at.slice(0, 10)
    buckets[day] = (buckets[day] || 0) + 1
  }
  const days = Object.keys(buckets).sort()
  const recentDays = days.slice(-30)
  const maxCount = Math.max(1, ...recentDays.map((day) => buckets[day]))
  return recentDays.map((day) => ({
    day,
    count: buckets[day],
    heightPercent: (buckets[day] / maxCount) * 100,
  }))
})

function formatTime(isoString) {
  return new Date(isoString).toLocaleString()
}

function formatDay(isoDay) {
  return new Date(`${isoDay}T00:00:00`).toLocaleDateString(undefined, {
    month: 'short',
    day: 'numeric',
  })
}
</script>

<template>
  <div class="dashboard">
    <header class="page-header">
      <h1>Dashboard</h1>
      <p class="page-subtitle">Your saved scan history and reports.</p>
    </header>

    <div class="filters">
      <label>
        From
        <input v-model="startDate" type="date" />
      </label>
      <label>
        To
        <input v-model="endDate" type="date" />
      </label>
      <label>
        Document type
        <select v-model="typeFilter">
          <option value="all">All types</option>
          <option v-for="type in DOCUMENT_TYPES" :key="type" :value="type">
            {{ type.replaceAll('_', ' ') }}
          </option>
        </select>
      </label>
      <button class="btn btn-secondary" :disabled="loading" @click="loadScans">
        {{ loading ? 'Refreshing...' : 'Refresh' }}
      </button>
    </div>

    <p v-if="loadError" class="error">{{ loadError }}</p>

    <div class="stats-grid">
      <div class="card stat-card">
        <div class="stat-label">Total scans</div>
        <div class="stat-value">{{ totalScans }}</div>
      </div>
      <div class="card stat-card">
        <div class="stat-label">Document types seen</div>
        <div class="stat-value">{{ Object.keys(typeCounts).length }}</div>
      </div>
      <div class="card stat-card">
        <div class="stat-label">Avg. classifier confidence</div>
        <div class="stat-value">
          {{ averageConfidence != null ? averageConfidence.toFixed(1) + '%' : '—' }}
        </div>
      </div>
    </div>

    <div class="charts-row" v-if="totalScans">
      <div class="card chart-card">
        <h2>Scans by day</h2>
        <div class="bar-chart">
          <div v-for="bucket in dailyCounts" :key="bucket.day" class="bar-column">
            <div class="bar-track">
              <div class="bar-fill" :style="{ height: bucket.heightPercent + '%' }"></div>
            </div>
            <span class="bar-day-label">{{ formatDay(bucket.day) }}</span>
          </div>
        </div>
      </div>

      <div class="card chart-card donut-card">
        <h2>Breakdown by document type</h2>
        <div class="donut-row">
          <svg viewBox="0 0 140 140" class="donut">
            <circle
              v-for="segment in donutSegments"
              :key="segment.type"
              cx="70"
              cy="70"
              r="60"
              fill="none"
              :stroke="segment.color"
              stroke-width="20"
              :stroke-dasharray="segment.dasharray"
              :stroke-dashoffset="segment.dashoffset"
              transform="rotate(-90 70 70)"
            />
          </svg>
          <ul class="donut-legend">
            <li v-for="segment in donutSegments" :key="segment.type">
              <span class="legend-swatch" :style="{ background: segment.color }"></span>
              {{ segment.type.replaceAll('_', ' ') }}
              <strong>{{ segment.percentage.toFixed(0) }}%</strong>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <div class="card table-card">
      <h2>Scan history</h2>
      <p v-if="!scans.length && !loading" class="empty">No scans in this range yet.</p>
      <table v-else-if="scans.length" class="history-table">
        <thead>
          <tr>
            <th>File</th>
            <th>Type</th>
            <th>Confidence</th>
            <th>Analyzed</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in scans" :key="item.id">
            <td>{{ item.filename }}</td>
            <td class="doc-type-cell">{{ (item.document_type || 'unknown').replaceAll('_', ' ') }}</td>
            <td>{{ item.confidence != null ? (item.confidence * 100).toFixed(1) + '%' : '—' }}</td>
            <td>{{ formatTime(item.created_at) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style scoped>
.filters {
  display: flex;
  align-items: flex-end;
  gap: var(--space-4);
  flex-wrap: wrap;
  margin-bottom: var(--space-5);
}

.filters label {
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
  font-size: 0.8rem;
  color: var(--color-text-muted);
}

.filters input,
.filters select {
  padding: var(--space-2) var(--space-3);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  background: var(--color-bg);
  color: var(--color-text);
  font-size: 0.88rem;
}

.error {
  color: var(--color-danger);
  font-size: 0.85rem;
  margin-bottom: var(--space-4);
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: var(--space-4);
  margin-bottom: var(--space-5);
}

.stat-card {
  padding: var(--space-4);
}

.stat-label {
  font-size: 0.8rem;
  color: var(--color-text-muted);
  margin-bottom: var(--space-2);
}

.stat-value {
  font-size: 1.6rem;
  font-weight: 700;
}

.charts-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: var(--space-4);
  margin-bottom: var(--space-5);
}

.chart-card {
  padding: var(--space-5);
}

.chart-card h2 {
  font-size: 1rem;
  margin-bottom: var(--space-4);
}

.bar-chart {
  display: flex;
  align-items: flex-end;
  gap: var(--space-2);
  height: 160px;
  overflow-x: auto;
}

.bar-column {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-1);
  min-width: 20px;
  flex: 1;
  height: 100%;
  justify-content: flex-end;
}

.bar-track {
  width: 100%;
  max-width: 22px;
  height: 130px;
  display: flex;
  align-items: flex-end;
  background: var(--color-surface-muted);
  border-radius: var(--radius-sm);
  overflow: hidden;
}

.bar-fill {
  width: 100%;
  background: var(--color-primary);
  border-radius: var(--radius-sm) var(--radius-sm) 0 0;
}

.bar-day-label {
  font-size: 0.68rem;
  color: var(--color-text-faint);
  white-space: nowrap;
}

.donut-row {
  display: flex;
  align-items: center;
  gap: var(--space-5);
  flex-wrap: wrap;
}

.donut {
  width: 140px;
  height: 140px;
  flex-shrink: 0;
}

.donut-legend {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  font-size: 0.85rem;
  color: var(--color-text-muted);
}

.donut-legend li {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  text-transform: capitalize;
}

.donut-legend strong {
  margin-left: auto;
  color: var(--color-text);
}

.legend-swatch {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  flex-shrink: 0;
}

.table-card {
  padding: var(--space-5);
}

.table-card h2 {
  font-size: 1rem;
  margin-bottom: var(--space-4);
}

.empty {
  color: var(--color-text-muted);
  font-size: 0.88rem;
}

.history-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.85rem;
}

.history-table th {
  text-align: left;
  color: var(--color-text-muted);
  font-weight: 500;
  padding: var(--space-2) var(--space-2);
  border-bottom: 1px solid var(--color-border);
}

.history-table td {
  padding: var(--space-2);
  border-bottom: 1px solid var(--color-border);
}

.doc-type-cell {
  text-transform: capitalize;
}
</style>
