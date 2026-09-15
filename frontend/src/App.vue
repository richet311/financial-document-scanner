<script setup>
import TopNav from './components/TopNav.vue'
</script>

<template>
  <div class="shell">
    <TopNav />
    <div class="shell-main">
      <div class="disclaimer">
        Independent demo project, not affiliated with any bank or financial
        institution. All sample documents are synthetic.
      </div>
      <RouterView />
    </div>
  </div>
</template>

<style scoped>
.shell {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.shell-main {
  flex: 1;
  width: 100%;
  max-width: 1180px;
  margin: 0 auto;
  padding: var(--space-6);
}

.disclaimer {
  font-size: 0.78rem;
  color: var(--color-warning);
  background: var(--color-warning-soft);
  border: 1px solid var(--color-warning);
  border-radius: var(--radius-sm);
  padding: var(--space-2) var(--space-3);
  margin-bottom: var(--space-5);
  display: inline-block;
}
</style>
