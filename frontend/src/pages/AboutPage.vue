<script setup>
const stack = [
  { layer: 'Frontend', choice: 'Vue 3, Vite, plain JavaScript (no TypeScript)' },
  { layer: 'Backend', choice: 'Python, FastAPI' },
  { layer: 'Auth', choice: 'JWT (python-jose, passlib)' },
  { layer: 'Rate limiting', choice: 'slowapi' },
  { layer: 'OCR', choice: 'EasyOCR, PyMuPDF (born-digital PDF text)' },
  { layer: 'Classifier', choice: 'scikit-learn (TF-IDF + logistic regression)' },
  { layer: 'Synthetic data', choice: 'Faker' },
  { layer: 'Hosting', choice: 'Render.com free tier' },
]
</script>

<template>
  <div class="about-page">
    <header class="page-header">
      <h1>About this project</h1>
      <p class="page-subtitle">
        A privacy-first document intelligence pipeline, built as a portfolio
        project to show secure full-stack development and applied ML on a
        problem that is actually useful to nonprofits and individuals working
        on financial literacy.
      </p>
    </header>

    <section class="section">
      <h2>What it does</h2>
      <ol class="flow-list">
        <li>A user uploads a sample financial document (image or PDF).</li>
        <li>
          The backend extracts the text. Born-digital PDFs get their embedded
          text pulled directly; scanned PDFs and images fall back to OCR.
        </li>
        <li>
          A classifier trained on a synthetic, self-generated dataset labels
          the document type, and a rules-based engine pulls out key fields
          and turns them into plain-language insights.
        </li>
        <li>
          The frontend shows the extracted data and insights. The original
          file is never stored; a JWT-protected endpoint feeds the dashboard
          an in-memory history of past analyses for the current session only.
        </li>
      </ol>
    </section>

    <section class="section">
      <h2>Architecture</h2>
      <div class="architecture">
        <div class="arch-box">
          <strong>Frontend</strong>
          <span>Vue 3 + Vite SPA</span>
        </div>
        <div class="arch-arrow">
          <span>HTTPS, rate-limited, CORS-locked</span>
        </div>
        <div class="arch-box">
          <strong>Backend</strong>
          <span>FastAPI · OCR + classification · insight engine · JWT auth</span>
        </div>
      </div>
    </section>

    <section class="section">
      <h2>Tech stack</h2>
      <table class="stack-table">
        <thead>
          <tr>
            <th>Layer</th>
            <th>Choice</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="row in stack" :key="row.layer">
            <td>{{ row.layer }}</td>
            <td>{{ row.choice }}</td>
          </tr>
        </tbody>
      </table>
      <p class="note">
        No paid or credit-card-gated cloud services are used anywhere in this
        project.
      </p>
    </section>

    <section class="section">
      <h2>Source</h2>
      <p>
        The full source, README, and test suite are on GitHub:
        <a href="https://github.com/richet311/financial-document-scanner" target="_blank" rel="noopener">
          github.com/richet311/financial-document-scanner
        </a>
      </p>
    </section>
  </div>
</template>

<style scoped>
.section {
  margin-bottom: var(--space-7);
}

.section h2 {
  font-size: 1.15rem;
  margin-bottom: var(--space-4);
}

.flow-list {
  margin: 0;
  padding-left: 1.2rem;
  color: var(--color-text-muted);
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
  max-width: 68ch;
}

.architecture {
  display: flex;
  align-items: stretch;
  gap: var(--space-4);
  flex-wrap: wrap;
}

.arch-box {
  flex: 1 1 220px;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  padding: var(--space-5);
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  background: var(--color-surface);
}

.arch-box strong {
  color: var(--color-accent);
}

.arch-box span {
  font-size: 0.85rem;
  color: var(--color-text-muted);
}

.arch-arrow {
  flex: 0 0 auto;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.78rem;
  color: var(--color-text-faint);
  text-align: center;
  max-width: 140px;
}

.stack-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.88rem;
  margin-bottom: var(--space-3);
}

.stack-table th {
  text-align: left;
  color: var(--color-text-muted);
  font-weight: 600;
  padding: var(--space-2);
  border-bottom: 1px solid var(--color-border);
}

.stack-table td {
  padding: var(--space-2);
  border-bottom: 1px solid var(--color-border);
}

.stack-table td:first-child {
  font-weight: 600;
  white-space: nowrap;
}

.note {
  font-size: 0.82rem;
  color: var(--color-text-faint);
}

.section a {
  color: var(--color-accent);
}
</style>
