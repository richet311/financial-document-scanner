<script setup>
import { ref } from 'vue'

const emit = defineEmits(['file-selected'])

const isDragging = ref(false)
const fileInput = ref(null)

function pickFile() {
  fileInput.value?.click()
}

function onFileChange(event) {
  const file = event.target.files[0]
  if (file) emit('file-selected', file)
}

function onDrop(event) {
  isDragging.value = false
  const file = event.dataTransfer.files[0]
  if (file) emit('file-selected', file)
}
</script>

<template>
  <div
    class="dropzone"
    :class="{ dragging: isDragging }"
    @dragover.prevent="isDragging = true"
    @dragleave.prevent="isDragging = false"
    @drop.prevent="onDrop"
  >
    <input
      ref="fileInput"
      type="file"
      accept=".pdf,.png,.jpg,.jpeg"
      class="hidden-input"
      @change="onFileChange"
    />
    <div class="dropzone-icon icon">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
        <path d="M7 18a4 4 0 0 1-1-7.9A5 5 0 0 1 16 8a4.5 4.5 0 0 1 1 8.9" />
        <path d="M12 12v7" />
        <path d="M9.5 15.5 12 13l2.5 2.5" />
      </svg>
    </div>
    <p class="dropzone-title">Drag and drop a document, or choose a file</p>
    <button type="button" class="btn btn-secondary" @click="pickFile">Choose file</button>
    <p class="dropzone-meta">Supports PDF, PNG, JPEG &middot; Max 10 MB</p>
  </div>
</template>

<style scoped>
.dropzone {
  border: 1.5px dashed var(--color-border);
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  text-align: center;
  background: var(--color-surface-muted);
  transition: border-color 0.15s ease, background-color 0.15s ease;
}

.dropzone.dragging {
  border-color: var(--color-primary);
  background: var(--color-primary-soft);
}

.hidden-input {
  display: none;
}

.dropzone-icon {
  color: var(--color-primary);
  margin: 0 auto var(--space-3);
  justify-content: center;
}

.dropzone-icon svg {
  width: 26px;
  height: 26px;
}

.dropzone-title {
  font-size: 0.92rem;
  margin-bottom: var(--space-4);
}

.dropzone-meta {
  font-size: 0.78rem;
  color: var(--color-text-faint);
  margin-top: var(--space-3);
}
</style>
