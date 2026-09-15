<template>
  <header class="dash-header">
    <div>
      <h1>Dashboard</h1>
      <p class="dash-subtitle">Review your scanned documents and financial insights.</p>
    </div>
    <RouterLink to="/scan" class="btn btn-primary">Scan document</RouterLink>
  </header>
</template>

<style scoped>
.dash-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: var(--space-4);
  margin-bottom: var(--space-5);
}

.dash-header h1 {
  font-size: 1.7rem;
  margin-bottom: var(--space-1);
}

.dash-subtitle {
  color: var(--color-text-muted);
  font-size: 0.9rem;
}

@media (max-width: 560px) {
  .dash-header {
    flex-direction: column;
    align-items: stretch;
  }
}
</style>
