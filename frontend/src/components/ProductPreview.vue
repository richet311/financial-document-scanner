<script setup>
import { onBeforeUnmount, onMounted, ref } from 'vue'

// 0 = extracting, 1 = classified, 2 = fields + insight shown. Advances once
// and settles on the final state, rather than looping indefinitely.
const step = ref(0)
let timer = null

onMounted(() => {
  timer = setInterval(() => {
    if (step.value >= 2) {
      clearInterval(timer)
      return
    }
    step.value += 1
  }, 900)
})

onBeforeUnmount(() => {
  clearInterval(timer)
})
</script>

<template>
  <div class="preview-window">
    <div class="file-row">
      <span class="file-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round">
          <rect x="5" y="3" width="14" height="18" rx="2" />
          <line x1="8" y1="8" x2="16" y2="8" />
          <line x1="8" y1="12" x2="16" y2="12" />
          <line x1="8" y1="16" x2="13" y2="16" />
        </svg>
      </span>
      <div class="file-meta">
        <div class="file-name">statement.pdf</div>
        <div class="file-size">214 KB</div>
      </div>
      <span class="file-check" v-if="step >= 1">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M5 13l4 4L19 7" />
        </svg>
      </span>
    </div>

    <div class="preview-row" v-if="step === 0">
      <span class="spinner"></span>
      <span>Extracting document data</span>
    </div>

    <div class="classification-block" v-else>
      <div class="classification-row">
        <span class="doc-type-badge">Bank statement</span>
        <span class="confidence-text">94% confidence</span>
      </div>
      <div class="confidence-track">
        <div class="confidence-fill"></div>
      </div>
    </div>

    <transition name="fade">
      <div class="fields-block" v-if="step >= 2">
        <div class="field-row">
          <span class="field-label">Ending balance</span>
          <span class="field-value">$4,570.00</span>
        </div>

        <div class="metric-grid">
          <div class="metric-tile">
            <span class="metric-label">Income</span>
            <span class="metric-value">$5,200</span>
          </div>
          <div class="metric-tile">
            <span class="metric-label">Expenses</span>
            <span class="metric-value">$3,180</span>
          </div>
          <div class="metric-tile">
            <span class="metric-label">Savings rate</span>
            <span class="metric-value">39%</span>
          </div>
        </div>

        <p class="insight-text">Savings rate is 39% after expenses this period.</p>
      </div>
    </transition>
  </div>
</template>

<style scoped>
.preview-window {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
  width: 100%;
  max-width: 400px;
  padding: var(--space-5);
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
  animation: preview-enter 0.6s ease both;
}

@keyframes preview-enter {
  from {
    opacity: 0;
    transform: translateY(12px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.file-row {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding-bottom: var(--space-4);
  border-bottom: 1px solid var(--color-border);
}

.file-icon {
  color: var(--color-text-faint);
  flex-shrink: 0;
}

.file-icon svg {
  width: 22px;
  height: 22px;
}

.file-meta {
  flex: 1;
  min-width: 0;
}

.file-name {
  font-size: 0.88rem;
  font-weight: 600;
}

.file-size {
  font-size: 0.75rem;
  color: var(--color-text-faint);
}

.file-check {
  width: 18px;
  height: 18px;
  flex-shrink: 0;
  color: var(--color-success);
}

.preview-row {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  font-size: 0.85rem;
  color: var(--color-text-muted);
}

.spinner {
  width: 14px;
  height: 14px;
  border-radius: 50%;
  border: 2px solid var(--color-primary-soft);
  border-top-color: var(--color-primary);
  flex-shrink: 0;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.classification-block {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.classification-row {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  font-size: 0.85rem;
}

.doc-type-badge {
  font-weight: 600;
  color: var(--color-primary);
}

.confidence-text {
  font-size: 0.78rem;
  color: var(--color-text-faint);
}

.confidence-track {
  height: 4px;
  background: var(--color-surface-muted);
  border-radius: 999px;
  overflow: hidden;
}

.confidence-fill {
  height: 100%;
  width: 94%;
  background: var(--color-accent);
  border-radius: 999px;
}

.fields-block {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
  padding-top: var(--space-3);
  border-top: 1px solid var(--color-border);
}

.field-row {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  font-size: 0.85rem;
}

.field-label {
  color: var(--color-text-muted);
}

.field-value {
  font-weight: 600;
}

.metric-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-2);
}

.metric-tile {
  background: var(--color-surface-muted);
  border-radius: var(--radius-sm);
  padding: var(--space-3) var(--space-2);
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.metric-label {
  font-size: 0.68rem;
  color: var(--color-text-faint);
}

.metric-value {
  font-size: 0.95rem;
  font-weight: 700;
}

.insight-text {
  font-size: 0.82rem;
  color: var(--color-text-muted);
  line-height: 1.5;
}

.fade-enter-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.fade-enter-from {
  opacity: 0;
  transform: translateY(4px);
}
</style>
