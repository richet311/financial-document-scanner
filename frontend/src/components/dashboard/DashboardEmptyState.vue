<script setup>
const SUPPORTED_TYPES = ['Bank Statement', 'Pay Stub', 'Budget Sheet']
</script>

<template>
  <div class="empty-state card">
    <h2>No documents yet</h2>
    <p>Scan your first financial document to see extracted information and financial insights here.</p>
    <RouterLink to="/scan" class="btn btn-primary">Scan a document</RouterLink>

    <div class="supported-types">
      <span v-for="type in SUPPORTED_TYPES" :key="type">{{ type }}</span>
    </div>
  </div>
</template>

<style scoped>
.empty-state {
  padding: var(--space-7) var(--space-5);
  text-align: center;
}

.empty-state h2 {
  font-size: 1.2rem;
  margin-bottom: var(--space-2);
}

.empty-state p {
  color: var(--color-text-muted);
  font-size: 0.9rem;
  max-width: 46ch;
  margin: 0 auto var(--space-5);
}

.supported-types {
  display: flex;
  justify-content: center;
  gap: var(--space-4);
  margin-top: var(--space-6);
  padding-top: var(--space-5);
  border-top: 1px solid var(--color-border);
  font-size: 0.82rem;
  color: var(--color-text-faint);
  flex-wrap: wrap;
}

@media (max-width: 560px) {
  .supported-types {
    gap: var(--space-3);
  }
}
</style>
