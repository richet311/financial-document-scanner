<script setup>
import { computed, ref, watchEffect } from 'vue'
import { authStore, login, logout } from '../store/auth'

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

const username = ref('')
const password = ref('')
const loginError = ref('')
const loggingIn = ref(false)

const history = ref([])
const loadError = ref('')
const loading = ref(false)

async function onLogin() {
  loginError.value = ''
  loggingIn.value = true
  try {
    await login(username.value, password.value)
    password.value = ''
  } catch (err) {
    loginError.value = err.message
  } finally {
    loggingIn.value = false
  }
}

async function loadHistory() {
  if (!authStore.token) return
  loading.value = true
  loadError.value = ''
  try {
    const response = await fetch(`${apiBaseUrl}/api/documents/history`, {
      headers: { Authorization: `Bearer ${authStore.token}` },
    })
    const data = await response.json()
    if (!response.ok) throw new Error(data.detail || 'Could not load history.')
    history.value = data.history
  } catch (err) {
    loadError.value = err.message
  } finally {
    loading.value = false
  }
}

watchEffect(() => {
  if (authStore.token) loadHistory()
})

const totalScans = computed(() => history.value.length)

const typeCounts = computed(() => {
  const counts = {}
  for (const item of history.value) {
    const type = item.document_type || 'unknown'
    counts[type] = (counts[type] || 0) + 1
  }
  return counts
})

const maxTypeCount = computed(() => Math.max(1, ...Object.values(typeCounts.value)))

const averageConfidence = computed(() => {
  const withConfidence = history.value.filter((item) => item.confidence != null)
  if (!withConfidence.length) return null
  const sum = withConfidence.reduce((total, item) => total + item.confidence, 0)
  return (sum / withConfidence.length) * 100
})

function formatTime(isoString) {
  return new Date(isoString).toLocaleString()
}

const ICONS = {
  document:
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><rect x="5" y="3" width="14" height="18" rx="2" /><line x1="8" y1="8" x2="16" y2="8" /><line x1="8" y1="12" x2="16" y2="12" /><line x1="8" y1="16" x2="13" y2="16" /></svg>',
  layers:
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"><path d="M12 3 L21 8 L12 13 L3 8 Z" /><path d="M3 13 L12 18 L21 13" /><path d="M3 17.5 L12 22.5 L21 17.5" /></svg>',
  chart:
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="20" x2="20" y2="20" /><rect x="6" y="13" width="3" height="7" fill="currentColor" stroke="none" /><rect x="11" y="9" width="3" height="11" fill="currentColor" stroke="none" /><rect x="16" y="5" width="3" height="15" fill="currentColor" stroke="none" /></svg>',
}
</script>

<template>
  <div class="dashboard">
    <header class="page-header">
      <h1>Dashboard</h1>
      <p class="page-subtitle">Session analysis history, behind a demo login.</p>
    </header>

    <div v-if="!authStore.token" class="card login-card">
      <h2>Demo login</h2>
      <p class="hint">
        Illustrates a JWT-protected route — a single hardcoded credential
        pair, not a real user system.
      </p>
      <form class="login-form" @submit.prevent="onLogin">
        <input v-model="username" type="text" placeholder="Username" />
        <input v-model="password" type="password" placeholder="Password" />
        <button type="submit" class="btn btn-primary" :disabled="loggingIn">
          {{ loggingIn ? 'Signing in…' : 'Sign in' }}
        </button>
      </form>
      <p v-if="loginError" class="error">{{ loginError }}</p>
    </div>

    <template v-else>
      <div class="toolbar">
        <span class="signed-in-as">Signed in as <strong>{{ authStore.username }}</strong></span>
        <div class="toolbar-actions">
          <button class="btn btn-secondary" :disabled="loading" @click="loadHistory">
            {{ loading ? 'Refreshing…' : 'Refresh' }}
          </button>
          <button class="btn btn-secondary" @click="logout">Sign out</button>
        </div>
      </div>

      <div class="stats-grid">
        <div class="card stat-card">
          <span class="stat-icon icon" v-html="ICONS.document"></span>
          <div>
            <div class="stat-label">Total scans</div>
            <div class="stat-value">{{ totalScans }}</div>
          </div>
        </div>
        <div class="card stat-card">
          <span class="stat-icon icon" v-html="ICONS.layers"></span>
          <div>
            <div class="stat-label">Document types seen</div>
            <div class="stat-value">{{ Object.keys(typeCounts).length }}</div>
          </div>
        </div>
        <div class="card stat-card">
          <span class="stat-icon icon" v-html="ICONS.chart"></span>
          <div>
            <div class="stat-label">Avg. classifier confidence</div>
            <div class="stat-value">
              {{ averageConfidence != null ? averageConfidence.toFixed(1) + '%' : '—' }}
            </div>
          </div>
        </div>
      </div>

      <div class="card breakdown-card" v-if="totalScans">
        <h2>Breakdown by document type</h2>
        <div class="bar-row" v-for="(count, type) in typeCounts" :key="type">
          <span class="bar-label">{{ type.replaceAll('_', ' ') }}</span>
          <div class="bar-track">
            <div class="bar-fill" :style="{ width: (count / maxTypeCount) * 100 + '%' }"></div>
          </div>
          <span class="bar-count">{{ count }}</span>
        </div>
      </div>

      <div class="card table-card">
        <h2>Recent analyses</h2>
        <p v-if="loadError" class="error">{{ loadError }}</p>
        <p v-else-if="!history.length" class="empty">No analyses recorded yet this session.</p>
        <table v-else class="history-table">
          <thead>
            <tr>
              <th>File</th>
              <th>Type</th>
              <th>Confidence</th>
              <th>Analyzed</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in history" :key="index">
              <td>{{ item.filename }}</td>
              <td class="doc-type-cell">{{ (item.document_type || 'unknown').replaceAll('_', ' ') }}</td>
              <td>{{ item.confidence != null ? (item.confidence * 100).toFixed(1) + '%' : '—' }}</td>
              <td>{{ formatTime(item.analyzed_at) }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </template>
  </div>
</template>

<style scoped>
.page-header {
  margin-bottom: var(--space-5);
}

.page-header h1 {
  font-size: 1.6rem;
  margin-bottom: var(--space-2);
}

.page-subtitle {
  color: var(--color-text-muted);
  font-size: 0.9rem;
}

.login-card {
  padding: var(--space-5);
  max-width: 360px;
}

.login-card h2 {
  font-size: 1.05rem;
  margin-bottom: var(--space-1);
}

.hint {
  font-size: 0.82rem;
  color: var(--color-text-muted);
  margin-bottom: var(--space-4);
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}

.login-form input {
  padding: var(--space-2) var(--space-3);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  background: var(--color-bg);
  color: var(--color-text);
}

.error {
  color: var(--color-danger);
  font-size: 0.85rem;
  margin-top: var(--space-3);
}

.toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: var(--space-5);
}

.signed-in-as {
  font-size: 0.88rem;
  color: var(--color-text-muted);
}

.toolbar-actions {
  display: flex;
  gap: var(--space-2);
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: var(--space-4);
  margin-bottom: var(--space-5);
}

.stat-card {
  padding: var(--space-4);
  display: flex;
  align-items: center;
  gap: var(--space-3);
}

.stat-icon {
  width: 38px;
  height: 38px;
  border-radius: var(--radius-sm);
  background: var(--color-primary-soft);
  color: var(--color-primary);
  align-items: center;
  justify-content: center;
}

.stat-icon :deep(svg) {
  width: 18px;
  height: 18px;
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

.breakdown-card,
.table-card {
  padding: var(--space-5);
  margin-bottom: var(--space-5);
}

.breakdown-card h2,
.table-card h2 {
  font-size: 1rem;
  margin-bottom: var(--space-4);
}

.bar-row {
  display: grid;
  grid-template-columns: 140px 1fr 32px;
  align-items: center;
  gap: var(--space-3);
  margin-bottom: var(--space-2);
  font-size: 0.85rem;
}

.bar-label {
  text-transform: capitalize;
  color: var(--color-text-muted);
}

.bar-track {
  height: 10px;
  background: var(--color-surface-muted);
  border-radius: 999px;
  overflow: hidden;
}

.bar-fill {
  height: 100%;
  background: var(--color-primary);
  border-radius: 999px;
}

.bar-count {
  text-align: right;
  color: var(--color-text-muted);
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
