<script setup>
defineProps({
  insights: { type: Array, required: true },
  scanId: { type: String, required: true },
})
</script>

<template>
  <div class="insights-panel card">
    <h2 class="panel-heading">Recent insight</h2>

    <p v-for="(insight, index) in insights" :key="index" class="insight-line">
      {{ insight }}
    </p>

    <RouterLink :to="`/dashboard/scans/${scanId}`" class="panel-link">View full analysis &rarr;</RouterLink>
  </div>
</template>

<style scoped>
.insights-panel {
  padding: var(--space-5);
}

.panel-heading {
  font-size: 1.05rem;
  margin-bottom: var(--space-4);
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

.panel-link {
  display: inline-block;
  margin-top: var(--space-2);
  font-size: 0.85rem;
  font-weight: 500;
  color: var(--color-primary);
  text-decoration: none;
}

.panel-link:hover {
  text-decoration: underline;
}
</style>
