<script setup>
import { computed, ref, watchEffect } from 'vue'
import { authStore } from '../store/auth'
import { documentTypeLabel, fetchRecentScans, savingsRate } from '../lib/dashboardData'
import DashboardHeader from '../components/dashboard/DashboardHeader.vue'
import DashboardSummary from '../components/dashboard/DashboardSummary.vue'
import DashboardEmptyState from '../components/dashboard/DashboardEmptyState.vue'
import DashboardSkeleton from '../components/dashboard/DashboardSkeleton.vue'
import RecentDocuments from '../components/dashboard/RecentDocuments.vue'
import FinancialOverview from '../components/dashboard/FinancialOverview.vue'
import RecentInsights from '../components/dashboard/RecentInsights.vue'

const scans = ref([])
const loading = ref(true)
const error = ref('')

async function load() {
  loading.value = true
  error.value = ''
  try {
    scans.value = await fetchRecentScans()
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
}

watchEffect(() => {
  if (authStore.user) load()
})

const documentsScanned = computed(() => scans.value.length)
const mostRecent = computed(() => scans.value[0] ?? null)

const recentTypeLabel = computed(() =>
  mostRecent.value ? documentTypeLabel(mostRecent.value.documentType) : '—'
)

const latestSavingsRateLabel = computed(() => {
  const withRate = scans.value.find((scan) => savingsRate(scan.fields) != null)
  if (!withRate) return '—'
  return `${Math.round(savingsRate(withRate.fields))}%`
})

const typeCounts = computed(() => {
  const counts = {}
  for (const scan of scans.value) {
    const type = scan.documentType || 'unclassified'
    counts[type] = (counts[type] || 0) + 1
  }
  return counts
})

const showTypeBreakdown = computed(
  () => documentsScanned.value >= 3 && Object.keys(typeCounts.value).length >= 2
)
</script>

<template>
  <div class="dashboard">
    <DashboardHeader />

    <DashboardSkeleton v-if="loading" />

    <div v-else-if="error" class="dash-error card">
      <h2>We couldn't load your dashboard.</h2>
      <p>Your documents are safe. Try refreshing the page.</p>
      <button class="btn btn-secondary" @click="load">Try again</button>
    </div>

    <DashboardEmptyState v-else-if="documentsScanned === 0" />

    <template v-else>
      <DashboardSummary
        :documents-scanned="documentsScanned"
        :recent-type="recentTypeLabel"
        :latest-savings-rate="latestSavingsRateLabel"
      />

      <div class="dashboard-grid">
        <RecentDocuments :documents="scans.slice(0, 8)" />

        <div class="dashboard-side">
          <FinancialOverview :scan="mostRecent" />
          <RecentInsights
            v-if="mostRecent.insights.length"
            :insights="mostRecent.insights"
            :scan-id="mostRecent.id"
          />
          <div v-if="showTypeBreakdown" class="type-breakdown card">
            <h2 class="panel-heading">Document types</h2>
            <div v-for="(count, type) in typeCounts" :key="type" class="type-row">
              <span>{{ documentTypeLabel(type === 'unclassified' ? null : type) }}</span>
              <span class="type-count">{{ count }}</span>
            </div>
          </div>
        </div>
      </div>
    </template>
  </div>
</template>

<style scoped>
.dash-error {
  padding: var(--space-6);
  text-align: center;
}

.dash-error h2 {
  font-size: 1.1rem;
  margin-bottom: var(--space-2);
}

.dash-error p {
  color: var(--color-text-muted);
  font-size: 0.88rem;
  margin-bottom: var(--space-4);
}

.dashboard-grid {
  display: grid;
  grid-template-columns: 65% 1fr;
  gap: var(--space-5);
  align-items: start;
}

.dashboard-side {
  display: flex;
  flex-direction: column;
  gap: var(--space-5);
}

.panel-heading {
  font-size: 1.05rem;
  margin-bottom: var(--space-3);
}

.type-breakdown {
  padding: var(--space-5);
}

.type-row {
  display: flex;
  justify-content: space-between;
  padding: var(--space-2) 0;
  border-bottom: 1px solid var(--color-border);
  font-size: 0.87rem;
  text-transform: capitalize;
}

.type-row:last-child {
  border-bottom: none;
}

.type-count {
  font-weight: 600;
  text-transform: none;
}

@media (max-width: 860px) {
  .dashboard-grid {
    grid-template-columns: 1fr;
  }
}
</style>
