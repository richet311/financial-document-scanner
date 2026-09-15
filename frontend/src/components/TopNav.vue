<script setup>
import { useRouter } from 'vue-router'
import ApiStatus from './ApiStatus.vue'
import { authStore, signOut } from '../store/auth'

const router = useRouter()

async function onSignOut() {
  await signOut()
  router.push('/')
}
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
        <RouterLink to="/privacy" class="nav-link" exact-active-class="nav-link-active">Privacy</RouterLink>
        <RouterLink to="/terms" class="nav-link" exact-active-class="nav-link-active">Terms</RouterLink>
      </nav>

      <ApiStatus class="topbar-status" />

      <div class="auth-area">
        <template v-if="authStore.user">
          <span class="account-email">{{ authStore.user.email }}</span>
          <button class="btn btn-secondary" @click="onSignOut">Sign out</button>
        </template>
        <RouterLink v-else to="/login" class="btn btn-primary">Sign in</RouterLink>
      </div>
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
  gap: var(--space-5);
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
  color: var(--color-primary);
  border-bottom-color: var(--color-primary);
}

.topbar-status {
  white-space: nowrap;
}

.auth-area {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  white-space: nowrap;
}

.account-email {
  font-size: 0.82rem;
  color: var(--color-text-muted);
  max-width: 160px;
  overflow: hidden;
  text-overflow: ellipsis;
}

.auth-area .btn {
  padding: var(--space-1) var(--space-4);
  font-size: 0.85rem;
}

@media (max-width: 960px) {
  .topbar-inner {
    flex-wrap: wrap;
    row-gap: var(--space-3);
  }

  .topbar-status {
    display: none;
  }
}
</style>
