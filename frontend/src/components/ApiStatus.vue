<script setup>
import { onMounted, ref } from 'vue'

const status = ref('checking')
const detail = ref('')

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

onMounted(async () => {
  try {
    const response = await fetch(`${apiBaseUrl}/api/health`)
    if (!response.ok) {
      throw new Error(`API responded with status ${response.status}`)
    }
    const data = await response.json()
    status.value = 'connected'
    detail.value = data.service
  } catch (error) {
    status.value = 'unreachable'
    detail.value = error.message
    console.error('Health check failed:', error)
  }
})
</script>

<template>
  <div class="api-status" :class="status" :title="detail">
    <span class="dot"></span>
    <span v-if="status === 'checking'">Checking API...</span>
    <span v-else-if="status === 'connected'">API connected</span>
    <span v-else>API unreachable</span>
  </div>
</template>

<style scoped>
.api-status {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-sm);
  font-size: 0.78rem;
  color: var(--color-text-muted);
  background: var(--color-surface-muted);
  border: 1px solid var(--color-border);
}

.dot {
  width: 0.5rem;
  height: 0.5rem;
  border-radius: 50%;
  background: var(--color-text-faint);
  flex-shrink: 0;
}

.connected .dot {
  background: var(--color-success);
}

.unreachable .dot {
  background: var(--color-danger);
}
</style>
