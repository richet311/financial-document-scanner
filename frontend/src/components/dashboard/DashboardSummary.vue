<script setup>
defineProps({
  documentsScanned: { type: Number, required: true },
  recentType: { type: String, required: true },
  latestSavingsRate: { type: String, required: true },
})
</script>

<template>
  <div class="summary-bar card">
    <div class="summary-item">
      <span class="summary-label">Documents scanned</span>
      <span class="summary-value">{{ documentsScanned }}</span>
    </div>
    <div class="summary-item">
      <span class="summary-label">Recent document type</span>
      <span class="summary-value">{{ recentType }}</span>
    </div>
    <div class="summary-item">
      <span class="summary-label">Latest savings rate</span>
      <span class="summary-value">{{ latestSavingsRate }}</span>
    </div>
  </div>
</template>

<style scoped>
.summary-bar {
  display: flex;
  margin-bottom: var(--space-5);
}

.summary-item {
  flex: 1;
  padding: var(--space-4) var(--space-5);
  border-right: 1px solid var(--color-border);
}

.summary-item:last-child {
  border-right: none;
}

.summary-label {
  display: block;
  font-size: 0.78rem;
  color: var(--color-text-muted);
  margin-bottom: var(--space-2);
}

.summary-value {
  display: block;
  font-size: 1.5rem;
  font-weight: 700;
  text-transform: capitalize;
}

@media (max-width: 560px) {
  .summary-bar {
    flex-direction: column;
  }

  .summary-item {
    border-right: none;
    border-bottom: 1px solid var(--color-border);
  }

  .summary-item:last-child {
    border-bottom: none;
  }
}
</style>
