<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import TopNav from './components/TopNav.vue'
import SiteFooter from './components/SiteFooter.vue'

const route = useRoute()
const isAuthPage = computed(() => route.name === 'login')
</script>

<template>
  <div class="shell">
    <TopNav v-if="!isAuthPage" />
    <div class="shell-main" :class="{ 'shell-main-flush': isAuthPage }">
      <RouterView />
    </div>
    <SiteFooter v-if="!isAuthPage" />
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

.shell-main-flush {
  max-width: none;
  padding: 0;
}

@media (max-width: 640px) {
  .shell-main {
    padding: var(--space-5) var(--space-4);
  }
}
</style>
