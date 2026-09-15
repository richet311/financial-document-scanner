<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import {
  documentTypeLabel,
  fetchScanById,
  formatDate,
  overviewRows,
} from '../lib/dashboardData'

const route = useRoute()

const scan = ref(null)
const loading = ref(true)
const error = ref('')

async function load() {
  loading.value = true
  error.value = ''
  try {
    scan.value = await fetchScanById(route.params.id)
  } catch (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
}

onMounted(load)
</script>

<template>
  <div class="scan-detail">
    <RouterLink to="/dashboard" class="back-link">&larr; Back to dashboard</RouterLink>

    <div v-if="loading" class="skeleton-block"></div>

    <div v-else-if="error" class="dash-error card">
      <h2>We couldn't load this report.</h2>
      <p>Your documents are safe. Try refreshing the page.</p>
      <button class="btn btn-secondary" @click="load">Try again</button>
    </div>

    <template v-else-if="scan">
      <section class="card detail-section">
        <h2 class="panel-heading">Overview</h2>
        <div class="overview-row">
          <span class="overview-label">Document</span>
          <span class="overview-value filename">{{ scan.filename }}</span>
        </div>
        <div class="overview-row">
          <span class="overview-label">Type</span>
          <span class="overview-value">
            <span class="badge badge-neutral">{{ documentTypeLabel(scan.documentType) }}</span>
          </span>
        </div>
        <div class="overview-row">
          <span class="overview-label">Scanned</span>
          <span class="overview-value">{{ formatDate(scan.createdAt) }}</span>
        </div>
        <div v-if="scan.confidence != null" class="overview-row">
          <span class="overview-label">Classifier confidence</span>
          <span class="overview-value">{{ (scan.confidence * 100).toFixed(1) }}%</span>
        </div>
      </section>

      <section class="card detail-section">
        <h2 class="panel-heading">Extracted fields</h2>
        <div v-if="overviewRows(scan).length" class="overview-grid">
          <div v-for="row in overviewRows(scan)" :key="row.label" class="overview-row">
            <span class="overview-label">{{ row.label }}</span>
            <span class="overview-value">{{ row.value }}</span>
          </div>
        </div>
        <p v-else class="muted-note">No financial fields were recognized in this document.</p>
      </section>

      <section class="card detail-section">
        <h2 class="panel-heading">Insights</h2>
        <p v-for="(insight, index) in scan.insights" :key="index" class="insight-line">
          {{ insight }}
        </p>
      </section>

      <section class="card detail-section">
        <h2 class="panel-heading">Extracted text</h2>
        <p class="muted-note">Raw extracted text isn't saved for scans yet, so it isn't available here.</p>
      </section>
    </template>
  </div>
</template>

<style scoped>
.scan-detail {
  max-width: 720px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: var(--space-5);
}

.back-link {
  font-size: 0.85rem;
  color: var(--color-text-muted);
  text-decoration: none;
}

.back-link:hover {
  color: var(--color-text);
}

.skeleton-block {
  height: 240px;
  background: var(--color-surface-muted);
  border-radius: var(--radius-lg);
  animation: skeleton-pulse 1.4s ease-in-out infinite;
}

@keyframes skeleton-pulse {
  0%,
  100% {
    opacity: 1;
  }
  50% {
    opacity: 0.55;
  }
}

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

.detail-section {
  padding: var(--space-5);
}

.panel-heading {
  font-size: 1.05rem;
  margin-bottom: var(--space-3);
}

.overview-grid {
  display: flex;
  flex-direction: column;
}

.overview-row {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  padding: var(--space-2) 0;
  border-bottom: 1px solid var(--color-border);
  font-size: 0.88rem;
}

.overview-row:last-child {
  border-bottom: none;
}

.overview-label {
  color: var(--color-text-muted);
}

.overview-value {
  font-weight: 600;
}

.filename {
  font-family: var(--font-mono);
  font-size: 0.85rem;
}

.insight-line {
  background: var(--color-surface-muted);
  border-radius: var(--radius-sm);
  padding: var(--space-3);
  font-size: 0.88rem;
  color: var(--color-text-muted);
  line-height: 1.5;
  margin-bottom: var(--space-2);
}

.insight-line:last-child {
  margin-bottom: 0;
}

.muted-note {
  font-size: 0.85rem;
  color: var(--color-text-muted);
}
</style>
