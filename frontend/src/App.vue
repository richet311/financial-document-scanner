<script setup>
import TopNav from './components/TopNav.vue'
import SiteFooter from './components/SiteFooter.vue'
</script>

<template>
  <div class="shell">
    <TopNav />
    <div class="shell-main">
      <RouterView />
    </div>
    <SiteFooter />
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
  max-width: var(--container-max);
  margin: 0 auto;
  padding: var(--space-6);
}

@media (max-width: 640px) {
  .shell-main {
    padding: var(--space-5) var(--space-4);
  }
}
</style>
