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
    @click="pickFile"
  >
    <input
      ref="fileInput"
      type="file"
      accept=".pdf,.png,.jpg,.jpeg"
      class="hidden-input"
      @change="onFileChange"
    />
    <div class="dropzone-icon">⬆</div>
    <p class="dropzone-title">Drop a document here, or click to browse</p>
    <p class="dropzone-hint">PDF, PNG, or JPEG — never stored, processed in memory only</p>
  </div>
</template>

<style scoped>
.dropzone {
  border: 1.5px dashed var(--color-border);
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  text-align: center;
  cursor: pointer;
  background: var(--color-surface-muted);
  transition: border-color 0.15s ease, background-color 0.15s ease;
}

.dropzone:hover,
.dropzone.dragging {
  border-color: var(--color-primary);
  background: var(--color-primary-soft);
}

.hidden-input {
  display: none;
}

.dropzone-icon {
  font-size: 1.5rem;
  color: var(--color-primary);
  margin-bottom: var(--space-2);
}

.dropzone-title {
  font-weight: 500;
  margin-bottom: var(--space-1);
}

.dropzone-hint {
  font-size: 0.8rem;
  color: var(--color-text-muted);
}
</style>
