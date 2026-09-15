<script setup>
import { onBeforeUnmount, onMounted, ref } from 'vue'

// 0 = extracting, 1 = classified, 2 = insights shown. Advances once and
// settles on the final state, rather than looping indefinitely.
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
    <div class="preview-body">
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
        <span class="file-check" :class="{ 'file-check-done': step >= 1 }">
          <svg v-if="step >= 1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M5 13l4 4L19 7" />
          </svg>
        </span>
      </div>

      <div class="preview-row" :class="{ 'preview-row-active': step === 0 }">
        <span class="spinner" v-if="step === 0"></span>
        <span class="row-icon" v-else>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <path d="M5 13l4 4L19 7" />
          </svg>
        </span>
        <span>Extracting document data</span>
      </div>

      <div class="preview-row" :class="{ 'preview-row-active': step === 1 }">
        <span class="row-icon" :class="{ 'row-icon-muted': step < 1 }">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round">
            <path d="M12 3 L21 8 L12 13 L3 8 Z" />
          </svg>
        </span>
        <span v-if="step < 1" class="row-muted">Classifying document type</span>
        <span v-else>
          Classified as
          <strong class="classification-badge">Bank statement</strong>
        </span>
      </div>

      <transition name="fade">
        <div class="insight-grid" v-if="step >= 2">
          <div class="insight-tile">
            <span class="insight-label">Income</span>
            <span class="insight-value">$5,200</span>
          </div>
          <div class="insight-tile">
            <span class="insight-label">Expenses</span>
            <span class="insight-value">$3,180</span>
          </div>
          <div class="insight-tile">
            <span class="insight-label">Savings rate</span>
            <span class="insight-value insight-value-accent">39%</span>
          </div>
        </div>
      </transition>
    </div>
  </div>
</template>

<style scoped>
.preview-window {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
  width: 100%;
  max-width: 380px;
  overflow: hidden;
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

.preview-body {
  padding: var(--space-5);
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
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
  width: 20px;
  height: 20px;
  flex-shrink: 0;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-success);
  transition: transform 0.2s ease;
}

.file-check-done {
  transform: scale(1);
}

.file-check svg {
  width: 14px;
  height: 14px;
}

.preview-row {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  font-size: 0.85rem;
  color: var(--color-text-muted);
}

.preview-row-active {
  color: var(--color-text);
}

.row-icon {
  width: 18px;
  height: 18px;
  flex-shrink: 0;
  color: var(--color-primary);
}

.row-icon-muted {
  color: var(--color-text-faint);
}

.row-muted {
  color: var(--color-text-faint);
}

.classification-badge {
  color: var(--color-primary);
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

.insight-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-2);
}

.insight-tile {
  background: var(--color-surface-muted);
  border-radius: var(--radius-sm);
  padding: var(--space-3) var(--space-2);
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.insight-label {
  font-size: 0.68rem;
  color: var(--color-text-faint);
}

.insight-value {
  font-size: 0.95rem;
  font-weight: 700;
}

.insight-value-accent {
  color: var(--color-accent);
}

.fade-enter-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.fade-enter-from {
  opacity: 0;
  transform: translateY(4px);
}
</style>
