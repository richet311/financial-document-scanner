<script setup>
import { documentTypeLabel, overviewRows } from '../../lib/dashboardData'

const props = defineProps({
  scan: { type: Object, required: true },
})

const rows = overviewRows(props.scan)
</script>

<template>
  <div class="overview-panel card">
    <h2 class="panel-heading">Financial overview</h2>
    <p class="panel-subtext">{{ scan.filename }} &middot; {{ documentTypeLabel(scan.documentType) }}</p>

    <div v-if="rows.length" class="overview-grid">
      <div v-for="row in rows" :key="row.label" class="overview-row">
        <span class="overview-label">{{ row.label }}</span>
        <span class="overview-value">{{ row.value }}</span>
      </div>
    </div>
    <p v-else class="overview-empty">No financial fields were recognized in this document.</p>
  </div>
</template>

<style scoped>
.overview-panel {
  padding: var(--space-5);
}

.panel-heading {
  font-size: 1.05rem;
  margin-bottom: var(--space-1);
}

.panel-subtext {
  font-size: 0.8rem;
  color: var(--color-text-faint);
  margin-bottom: var(--space-4);
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

.overview-empty {
  font-size: 0.85rem;
  color: var(--color-text-muted);
}
</style>
