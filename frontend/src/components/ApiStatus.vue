<script setup>
import { onMounted, ref } from 'vue'

const status = ref('checking')
const detail = ref('')

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

const LABELS = {
  checking: 'Checking API...',
  connected: 'API connected',
  unreachable: 'API unreachable',
}

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
  <span class="api-status" :class="status" :title="detail || LABELS[status]">
    <span class="dot"></span>
  </span>
</template>

<style scoped>
.api-status {
  display: inline-flex;
  align-items: center;
}

.dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--color-text-faint);
}

.connected .dot {
  background: var(--color-success);
}

.unreachable .dot {
  background: var(--color-danger);
}
</style>
