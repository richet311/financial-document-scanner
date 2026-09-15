<script setup>
import { useRouter } from 'vue-router'
import { SAMPLE_DOCUMENTS } from '../lib/sampleDocuments'

const router = useRouter()

function useSample(doc) {
  router.push({ path: '/scan', query: { sample: doc.key } })
}
</script>

<template>
  <div class="samples-page">
    <header class="page-header">
      <h1>Sample documents</h1>
      <p class="page-subtitle">
        No real financial document required. Use one of these synthetic
        documents to see the pipeline run end to end.
      </p>
    </header>

    <div class="samples-grid">
      <div v-for="doc in SAMPLE_DOCUMENTS" :key="doc.key" class="sample-card">
        <div class="doc-thumb">
          <span class="doc-thumb-tag">PDF</span>
          <span class="doc-thumb-line" style="width: 70%"></span>
          <span class="doc-thumb-line" style="width: 90%"></span>
          <span class="doc-thumb-line" style="width: 55%"></span>
          <span class="doc-thumb-line" style="width: 80%"></span>
        </div>

        <div class="sample-info">
          <h2>{{ doc.title }}</h2>
          <p>{{ doc.description }}</p>
        </div>

        <div class="sample-actions">
          <button class="btn btn-primary" @click="useSample(doc)">Use sample</button>
          <a class="download-link" :href="`/samples/${doc.file}`" download>Download</a>
        </div>
      </div>
    </div>

    <p class="note">
      These files are generated from the same synthetic templates used to
      train the classifier. Names, amounts, and account numbers are entirely
      made up.
    </p>
  </div>
</template>

<style scoped>
.samples-page {
  max-width: 780px;
}

.samples-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-5);
  margin-bottom: var(--space-5);
}

.sample-card {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}

.doc-thumb {
  position: relative;
  width: 100%;
  aspect-ratio: 4 / 3;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  padding: var(--space-4) var(--space-3);
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  justify-content: center;
}

.doc-thumb-tag {
  position: absolute;
  top: var(--space-2);
  right: var(--space-2);
  font-size: 0.62rem;
  font-weight: 700;
  letter-spacing: 0.03em;
  color: var(--color-text-faint);
  border: 1px solid var(--color-border);
  border-radius: 3px;
  padding: 1px 5px;
}

.doc-thumb-line {
  height: 6px;
  border-radius: 3px;
  background: var(--color-surface-muted);
}

.sample-info h2 {
  font-size: 0.95rem;
  margin-bottom: var(--space-1);
}

.sample-info p {
  font-size: 0.83rem;
  color: var(--color-text-muted);
}

.sample-actions {
  display: flex;
  align-items: center;
  gap: var(--space-3);
}

.download-link {
  font-size: 0.82rem;
  color: var(--color-text-muted);
  text-decoration: none;
}

.download-link:hover {
  color: var(--color-text);
  text-decoration: underline;
}

.note {
  font-size: 0.8rem;
  color: var(--color-text-faint);
}

@media (max-width: 700px) {
  .samples-grid {
    grid-template-columns: 1fr;
  }
}
</style>
