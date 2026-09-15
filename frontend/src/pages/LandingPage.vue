<script setup>
import { useRouter } from 'vue-router'
import ProductPreview from '../components/ProductPreview.vue'

const router = useRouter()

const ICONS = {
  shield:
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"><path d="M12 3 L19 6 V11 C19 16 16 19.5 12 21 C8 19.5 5 16 5 11 V6 Z" /><path d="M9 12 L11 14 L15 9.5" /></svg>',
}

const privacyPoints = [
  'Files are validated before processing.',
  'Uploads are processed in memory.',
  'Original files are not permanently stored.',
  'API endpoints are rate limited.',
]

function goToScan() {
  router.push('/scan')
}

function goToSamples() {
  router.push('/samples')
}

function goToPrivacy() {
  router.push('/privacy')
}
</script>

<template>
  <div class="landing">
    <section class="hero">
      <div class="hero-content">
        <h1>Understand your financial<br /> documents instantly.</h1>
        <p class="hero-subtitle">
          Upload a bank statement, pay stub, or budget sheet. Get extracted
          data and financial insights back in seconds.
        </p>

        <div class="hero-actions">
          <button class="btn btn-primary" @click="goToScan">Scan a document</button>
          <button class="btn btn-secondary" @click="goToSamples">View sample documents</button>
        </div>

        <p class="trust-note">
          <span class="icon" v-html="ICONS.shield"></span>
          Files are processed in memory and are not permanently stored.
        </p>
      </div>

      <div class="hero-visual">
        <ProductPreview />
      </div>
    </section>

    <section class="workflow-section">
      <h2 class="section-heading">How it works</h2>

      <div class="workflow-panel">
        <div class="workflow-track">
          <div class="workflow-stage">
            <div class="stage-visual extract-visual">
              <span class="extract-line" style="width: 68%"></span>
              <span class="extract-highlight">
                <span class="extract-highlight-label">Ending balance</span>
                <span class="extract-highlight-value">$4,570.00</span>
              </span>
              <span class="extract-line" style="width: 46%"></span>
            </div>
            <span class="stage-caption">Extract text</span>
          </div>

          <span class="workflow-connector" aria-hidden="true">&rarr;</span>

          <div class="workflow-stage">
            <div class="stage-visual classify-visual">
              <span class="doc-type-chip">Bank statement</span>
              <div class="mini-confidence-track">
                <div class="mini-confidence-fill"></div>
              </div>
              <span class="mini-confidence-label">96% confidence</span>
            </div>
            <span class="stage-caption">Classify document</span>
          </div>

          <span class="workflow-connector" aria-hidden="true">&rarr;</span>

          <div class="workflow-stage">
            <div class="stage-visual analyze-visual">
              <div class="mini-metric-row">
                <span>Income</span>
                <span class="mini-metric-value">$5,200</span>
              </div>
              <div class="mini-metric-row">
                <span>Expenses</span>
                <span class="mini-metric-value">$3,180</span>
              </div>
              <div class="mini-metric-row">
                <span>Savings rate</span>
                <span class="mini-metric-value">39%</span>
              </div>
            </div>
            <span class="stage-caption">Calculate financials</span>
          </div>

          <span class="workflow-connector" aria-hidden="true">&rarr;</span>

          <div class="workflow-stage">
            <div class="stage-visual insight-visual">
              Spending increased 8% this month.
            </div>
            <span class="stage-caption">Generate insight</span>
          </div>
        </div>
      </div>
    </section>

    <section class="privacy-band">
      <span class="privacy-icon icon" v-html="ICONS.shield"></span>
      <div class="privacy-copy">
        <h2 class="section-heading">Your documents stay private.</h2>
        <ul class="privacy-list">
          <li v-for="point in privacyPoints" :key="point">{{ point }}</li>
        </ul>
        <button class="privacy-link" @click="goToPrivacy">Read the full privacy policy</button>
      </div>
    </section>

    <section class="cta-banner">
      <h2 class="section-heading">See what your documents can tell you.</h2>
      <p>Scan a document and receive structured financial insights in seconds.</p>
      <button class="btn btn-primary" @click="goToScan">Scan a document</button>
    </section>
  </div>
</template>

<style scoped>
.landing {
  display: flex;
  flex-direction: column;
  gap: var(--space-6);
}

.hero {
  display: flex;
  align-items: center;
  gap: var(--space-7);
}

.hero-content {
  flex: 1 1 58%;
}

.hero-visual {
  flex: 1 1 42%;
  display: flex;
  justify-content: center;
}

.hero h1 {
  font-size: 2.75rem;
  font-weight: 700;
  letter-spacing: -0.03em;
  line-height: 1.15;
  margin-bottom: var(--space-4);
}

.hero-subtitle {
  color: var(--color-text-muted);
  font-size: 1.05rem;
  max-width: 46ch;
  margin-bottom: var(--space-5);
}

.hero-actions {
  display: flex;
  gap: var(--space-3);
  flex-wrap: wrap;
  margin-bottom: var(--space-4);
}

.trust-note {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  font-size: 0.82rem;
  color: var(--color-text-faint);
}

.trust-note .icon {
  width: 15px;
  height: 15px;
  color: var(--color-text-faint);
}

.trust-note .icon :deep(svg) {
  width: 15px;
  height: 15px;
}

.section-heading {
  font-size: 1.4rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  margin-bottom: var(--space-5);
}

.workflow-panel {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: var(--space-6) var(--space-5);
}

.workflow-track {
  display: flex;
  align-items: stretch;
  gap: var(--space-4);
}

.workflow-stage {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
}

.stage-visual {
  flex: 1;
  background: var(--color-surface-muted);
  border-radius: var(--radius-md);
  padding: var(--space-3);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: var(--space-2);
  min-height: 108px;
}

.stage-caption {
  font-size: 0.78rem;
  color: var(--color-text-muted);
  text-align: center;
}

.workflow-connector {
  flex-shrink: 0;
  align-self: center;
  color: var(--color-text-faint);
  font-size: 1rem;
}

.extract-visual {
  font-family: var(--font-mono);
  font-size: 0.7rem;
}

.extract-line {
  height: 6px;
  border-radius: 3px;
  background: var(--color-border);
}

.extract-highlight {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-2);
  background: var(--color-primary-soft);
  border-radius: var(--radius-sm);
  padding: var(--space-1) var(--space-2);
  white-space: nowrap;
}

.extract-highlight-label {
  color: var(--color-primary);
}

.extract-highlight-value {
  color: var(--color-primary);
  font-weight: 700;
}

.classify-visual {
  align-items: flex-start;
}

.doc-type-chip {
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--color-primary);
}

.mini-confidence-track {
  width: 100%;
  height: 4px;
  background: var(--color-border);
  border-radius: 999px;
  overflow: hidden;
}

.mini-confidence-fill {
  height: 100%;
  width: 96%;
  background: var(--color-accent);
  border-radius: 999px;
}

.mini-confidence-label {
  font-size: 0.72rem;
  color: var(--color-text-faint);
}

.mini-metric-row {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  font-size: 0.75rem;
  color: var(--color-text-muted);
}

.mini-metric-value {
  font-weight: 700;
  color: var(--color-text);
}

.insight-visual {
  background: var(--color-warning-soft);
  color: var(--color-warning);
  font-size: 0.78rem;
  font-weight: 500;
  line-height: 1.4;
  padding: var(--space-3);
}

.privacy-band {
  display: flex;
  align-items: flex-start;
  gap: var(--space-4);
  padding: var(--space-6) 0;
  border-top: 1px solid var(--color-border);
}

.privacy-icon {
  flex-shrink: 0;
  color: var(--color-primary);
  margin-top: 2px;
}

.privacy-icon :deep(svg) {
  width: 22px;
  height: 22px;
}

.privacy-copy .section-heading,
.cta-banner .section-heading {
  font-size: 1.15rem;
  margin-bottom: var(--space-3);
}

.privacy-list {
  margin: 0 0 var(--space-3);
  padding: 0;
  list-style: none;
  display: grid;
  grid-template-columns: repeat(2, auto);
  gap: var(--space-2) var(--space-6);
  color: var(--color-text-muted);
  font-size: 0.85rem;
}

.privacy-list li {
  display: flex;
  align-items: center;
  gap: var(--space-2);
}

.privacy-list li::before {
  content: '';
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: var(--color-text-faint);
  flex-shrink: 0;
}

.privacy-link {
  background: none;
  border: none;
  padding: 0;
  color: var(--color-primary);
  font-size: 0.85rem;
  font-weight: 500;
  cursor: pointer;
}

.privacy-link:hover {
  text-decoration: underline;
}

.cta-banner {
  text-align: center;
  padding: var(--space-6) var(--space-5);
  border-top: 1px solid var(--color-border);
}

.cta-banner p {
  color: var(--color-text-muted);
  margin-bottom: var(--space-5);
}

@media (max-width: 860px) {
  .hero {
    flex-direction: column;
    align-items: stretch;
  }

  .hero h1 {
    font-size: 2.1rem;
  }

  .hero h1 br {
    display: none;
  }

  .workflow-panel {
    padding: var(--space-5) var(--space-4);
  }

  .workflow-track {
    flex-direction: column;
  }

  .workflow-connector {
    transform: rotate(90deg);
    align-self: center;
  }

  .privacy-band {
    flex-direction: column;
  }

  .privacy-list {
    grid-template-columns: 1fr;
  }
}
</style>
