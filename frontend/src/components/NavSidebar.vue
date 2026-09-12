<script setup>
import ApiStatus from './ApiStatus.vue'

const ICONS = {
  scan:
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><rect x="4" y="4" width="16" height="16" rx="2" /><line x1="4" y1="12" x2="20" y2="12" stroke-width="2" /><circle cx="12" cy="12" r="1.4" fill="currentColor" stroke="none" /></svg>',
  dashboard:
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="7" height="7" rx="1.2" /><rect x="13" y="4" width="7" height="4" rx="1.2" /><rect x="13" y="10" width="7" height="10" rx="1.2" /><rect x="4" y="13" width="7" height="7" rx="1.2" /></svg>',
}
</script>

<template>
  <aside class="sidebar">
    <div class="brand">
      <div class="brand-mark">FD</div>
      <div>
        <div class="brand-name">Financial Document Scanner</div>
        <div class="brand-tag">Document intelligence demo</div>
      </div>
    </div>

    <nav class="nav">
      <RouterLink to="/" class="nav-link" exact-active-class="nav-link-active">
        <span class="nav-icon icon" v-html="ICONS.scan"></span>
        Scan Document
      </RouterLink>
      <RouterLink to="/dashboard" class="nav-link" exact-active-class="nav-link-active">
        <span class="nav-icon icon" v-html="ICONS.dashboard"></span>
        Dashboard
      </RouterLink>
    </nav>

    <div class="sidebar-footer">
      <ApiStatus />
    </div>
  </aside>
</template>

<style scoped>
.sidebar {
  display: flex;
  flex-direction: column;
  width: 240px;
  flex-shrink: 0;
  background: var(--color-surface);
  border-right: 1px solid var(--color-border);
  padding: var(--space-5) var(--space-4);
  gap: var(--space-6);
}

.brand {
  display: flex;
  align-items: center;
  gap: var(--space-3);
}

.brand-mark {
  width: 36px;
  height: 36px;
  border-radius: var(--radius-sm);
  background: var(--color-primary);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  font-size: 0.85rem;
  flex-shrink: 0;
}

.brand-name {
  font-size: 0.88rem;
  font-weight: 600;
  line-height: 1.25;
}

.brand-tag {
  font-size: 0.75rem;
  color: var(--color-text-muted);
}

.nav {
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
}

.nav-link {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-sm);
  color: var(--color-text-muted);
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 500;
  transition: background-color 0.15s ease, color 0.15s ease;
}

.nav-link:hover {
  background: var(--color-surface-muted);
  color: var(--color-text);
}

.nav-link-active {
  background: var(--color-primary-soft);
  color: var(--color-primary);
}

.nav-icon svg {
  width: 16px;
  height: 16px;
}

.sidebar-footer {
  margin-top: auto;
}
</style>
