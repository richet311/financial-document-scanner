<script setup>
import ApiStatus from './ApiStatus.vue'
</script>

<template>
  <header class="topbar">
    <div class="topbar-inner">
      <RouterLink to="/" class="brand">
        <span class="brand-mark">Financial</span> Document Scanner
      </RouterLink>

      <nav class="nav">
        <RouterLink to="/" class="nav-link" exact-active-class="nav-link-active">Home</RouterLink>
        <RouterLink to="/scan" class="nav-link" exact-active-class="nav-link-active">Scan Document</RouterLink>
        <RouterLink to="/dashboard" class="nav-link" exact-active-class="nav-link-active">Dashboard</RouterLink>
        <RouterLink to="/samples" class="nav-link" exact-active-class="nav-link-active">Sample Documents</RouterLink>
        <RouterLink to="/security" class="nav-link" exact-active-class="nav-link-active">Security</RouterLink>
        <RouterLink to="/about" class="nav-link" exact-active-class="nav-link-active">About</RouterLink>
      </nav>

      <ApiStatus class="topbar-status" />
    </div>
  </header>
</template>

<style scoped>
.topbar {
  background: var(--color-surface);
  border-bottom: 1px solid var(--color-border);
  position: sticky;
  top: 0;
  z-index: 10;
}

.topbar-inner {
  max-width: 1180px;
  margin: 0 auto;
  padding: var(--space-3) var(--space-6);
  display: flex;
  align-items: center;
  gap: var(--space-6);
}

.brand {
  font-weight: 700;
  font-size: 1.05rem;
  color: var(--color-text);
  text-decoration: none;
  white-space: nowrap;
}

.brand-mark {
  color: var(--color-accent);
}

.nav {
  display: flex;
  align-items: center;
  gap: var(--space-5);
  flex: 1;
  flex-wrap: wrap;
}

.nav-link {
  font-size: 0.88rem;
  font-weight: 500;
  color: var(--color-text-muted);
  text-decoration: none;
  padding: var(--space-2) 0;
  border-bottom: 2px solid transparent;
  transition: color 0.15s ease, border-color 0.15s ease;
}

.nav-link:hover {
  color: var(--color-text);
}

.nav-link-active {
  color: var(--color-accent);
  border-bottom-color: var(--color-accent);
}

.topbar-status {
  white-space: nowrap;
}

@media (max-width: 860px) {
  .topbar-inner {
    flex-wrap: wrap;
    row-gap: var(--space-3);
  }

  .topbar-status {
    display: none;
  }
}
</style>
