<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const samples = [
  {
    file: 'sample-pay-stub.pdf',
    title: 'Pay stub',
    text: 'A synthetic pay stub with gross income, deductions, and net pay.',
  },
  {
    file: 'sample-bank-statement.pdf',
    title: 'Bank statement',
    text: 'A synthetic account statement with opening balance, deposits, withdrawals, and balance.',
  },
  {
    file: 'sample-budget-sheet.pdf',
    title: 'Budget sheet',
    text: 'A synthetic monthly budget with net pay and a breakdown of expenses.',
  },
]

function goToScan() {
  router.push('/scan')
}
</script>

<template>
  <div class="samples-page">
    <header class="page-header">
      <h1>Sample documents</h1>
      <p class="page-subtitle">
        No real financial document required. Download one of these synthetic
        PDFs and upload it on the Scan page to see the pipeline run end to
        end.
      </p>
    </header>

    <div class="samples-grid">
      <div v-for="sample in samples" :key="sample.file" class="sample-card">
        <h2>{{ sample.title }}</h2>
        <p>{{ sample.text }}</p>
        <div class="sample-actions">
          <a class="btn btn-secondary" :href="`/samples/${sample.file}`" download>Download PDF</a>
          <button class="btn btn-primary" @click="goToScan">Go to Scan</button>
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
.samples-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: var(--space-4);
  margin-bottom: var(--space-5);
}

.sample-card {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}

.sample-card h2 {
  font-size: 1.02rem;
  color: var(--color-accent);
}

.sample-card p {
  font-size: 0.88rem;
  color: var(--color-text-muted);
  flex: 1;
}

.sample-actions {
  display: flex;
  gap: var(--space-2);
  flex-wrap: wrap;
}

.note {
  font-size: 0.8rem;
  color: var(--color-text-faint);
}
</style>
