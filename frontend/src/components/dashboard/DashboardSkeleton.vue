<template>
  <div class="skeleton">
    <div class="skeleton-block skeleton-summary"></div>
    <div class="skeleton-grid">
      <div class="skeleton-block skeleton-table"></div>
      <div class="skeleton-block skeleton-panel"></div>
    </div>
  </div>
</template>

<style scoped>
.skeleton {
  display: flex;
  flex-direction: column;
  gap: var(--space-5);
}

.skeleton-block {
  background: var(--color-surface-muted);
  border-radius: var(--radius-lg);
  animation: skeleton-pulse 1.4s ease-in-out infinite;
}

.skeleton-summary {
  height: 84px;
}

.skeleton-grid {
  display: grid;
  grid-template-columns: 65% 1fr;
  gap: var(--space-5);
}

.skeleton-table {
  height: 340px;
}

.skeleton-panel {
  height: 340px;
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

@media (max-width: 860px) {
  .skeleton-grid {
    grid-template-columns: 1fr;
  }
}
</style>
