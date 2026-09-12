<script setup>
defineProps({
  result: {
    type: Object,
    required: true,
  },
})

function insightTone(insight) {
  if (insight.toLowerCase().includes('exceed')) return 'danger'
  if (insight.toLowerCase().includes('not enough recognizable')) return 'neutral'
  return 'success'
}

function formatFieldName(key) {
  return key.replaceAll('_', ' ')
}
</script>

<template>
  <div class="results card">
    <div class="results-header">
      <div>
        <span class="badge badge-neutral doc-type">
          {{ (result.document_type || 'unknown').replaceAll('_', ' ') }}
        </span>
      </div>
      <span class="filename">{{ result.filename }}</span>
    </div>

    <div v-if="result.confidence" class="confidence-row">
      <span class="confidence-label">Classifier confidence</span>
      <div class="confidence-track">
        <div class="confidence-fill" :style="{ width: result.confidence * 100 + '%' }"></div>
      </div>
      <span class="confidence-value">{{ (result.confidence * 100).toFixed(1) }}%</span>
    </div>

    <div v-if="Object.keys(result.fields || {}).length" class="fields-grid">
      <div v-for="(value, key) in result.fields" :key="key" class="field-tile">
        <div class="field-label">{{ formatFieldName(key) }}</div>
        <div class="field-value">${{ value.toFixed(2) }}</div>
      </div>
    </div>

    <div class="insights">
      <div
        v-for="(insight, index) in result.insights"
        :key="index"
        class="insight"
        :class="`insight-${insightTone(insight)}`"
      >
        {{ insight }}
      </div>
    </div>

    <details class="raw-text">
      <summary>Raw extracted text</summary>
      <pre>{{ result.extracted_text }}</pre>
    </details>
  </div>
</template>

<style scoped>
.results {
  padding: var(--space-5);
  margin-top: var(--space-5);
}

.results-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: var(--space-4);
  flex-wrap: wrap;
  gap: var(--space-2);
}

.doc-type {
  text-transform: capitalize;
  font-size: 0.82rem;
}

.confidence {
  margin-left: var(--space-2);
  font-size: 0.82rem;
  color: var(--color-text-muted);
}

.filename {
  font-size: 0.82rem;
  color: var(--color-text-faint);
  font-family: var(--font-mono);
}

.confidence-row {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  margin-bottom: var(--space-4);
}

.confidence-label {
  font-size: 0.78rem;
  color: var(--color-text-muted);
  white-space: nowrap;
}

.confidence-track {
  flex: 1;
  height: 6px;
  background: var(--color-surface-muted);
  border-radius: 999px;
  overflow: hidden;
}

.confidence-fill {
  height: 100%;
  background: var(--color-accent);
  border-radius: 999px;
}

.confidence-value {
  font-size: 0.78rem;
  color: var(--color-text-muted);
  font-variant-numeric: tabular-nums;
}

.fields-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: var(--space-3);
  margin-bottom: var(--space-4);
}

.field-tile {
  background: var(--color-surface-muted);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  padding: var(--space-3);
}

.field-label {
  font-size: 0.75rem;
  color: var(--color-text-muted);
  text-transform: capitalize;
  margin-bottom: var(--space-1);
}

.field-value {
  font-size: 1.1rem;
  font-weight: 600;
}

.insights {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  margin-bottom: var(--space-4);
}

.insight {
  padding: var(--space-3);
  border-radius: var(--radius-sm);
  font-size: 0.88rem;
  border: 1px solid transparent;
}

.insight-success {
  background: var(--color-success-soft);
  color: var(--color-success);
}

.insight-danger {
  background: var(--color-danger-soft);
  color: var(--color-danger);
}

.insight-neutral {
  background: var(--color-surface-muted);
  color: var(--color-text-muted);
  border-color: var(--color-border);
}

.raw-text summary {
  cursor: pointer;
  font-size: 0.82rem;
  color: var(--color-text-muted);
}

.raw-text pre {
  white-space: pre-wrap;
  font-family: var(--font-mono);
  font-size: 0.8rem;
  background: var(--color-surface-muted);
  border-radius: var(--radius-sm);
  padding: var(--space-3);
  margin-top: var(--space-2);
}
</style>
