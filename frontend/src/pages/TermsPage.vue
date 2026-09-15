<script setup>
const sections = [
  {
    title: 'Acceptance',
    body: 'By using this demo, you agree to these terms. If you do not agree, do not use the app.',
  },
  {
    title: 'What this is',
    body: 'This is a personal portfolio project demonstrating document extraction, classification, and a full-stack build. It is not a financial, legal, tax, or accounting product, and nothing it produces is financial advice.',
  },
  {
    title: 'Use synthetic or non-sensitive data',
    body: 'Do not upload real bank statements, real pay stubs, or any document containing sensitive personal or financial information. Use the synthetic sample documents provided on the Sample Documents page, or your own made-up test data.',
  },
  {
    title: 'No warranty',
    body: 'This app is provided as-is, without warranty of any kind. Extraction, classification, and insights are generated automatically and may be inaccurate or incomplete.',
  },
  {
    title: 'Accounts',
    body: 'You are responsible for the accuracy of the email you sign up with and for keeping your password secure. You may stop using the app or request account deletion at any time.',
  },
  {
    title: 'Acceptable use',
    body: 'Do not attempt to abuse, overload, or reverse the security controls of this demo (rate limits, file validation, and authentication exist to keep it usable for everyone testing it).',
  },
  {
    title: 'Changes',
    body: 'These terms may change as the project evolves. Continued use after a change means you accept the updated terms.',
  },
]
</script>

<template>
  <div class="terms-page">
    <header class="page-header">
      <h1>Terms of service</h1>
      <p class="page-subtitle">
        The ground rules for using this demo application.
      </p>
    </header>

    <div class="legal-sections">
      <section v-for="section in sections" :key="section.title" class="legal-section">
        <h2>{{ section.title }}</h2>
        <p>{{ section.body }}</p>
      </section>
    </div>

    <p class="disclaimer">
      This page was written for a personal portfolio project and has not
      been reviewed by an attorney. It is provided to set clear, honest
      expectations for this specific demo, not as a legally binding
      contract for a real business.
    </p>
  </div>
</template>

<style scoped>
.legal-sections {
  display: flex;
  flex-direction: column;
  gap: var(--space-6);
  margin-bottom: var(--space-6);
  max-width: 72ch;
}

.legal-section h2 {
  font-size: 1.05rem;
  margin-bottom: var(--space-2);
}

.legal-section p {
  color: var(--color-text-muted);
  font-size: 0.92rem;
}

.disclaimer {
  font-size: 0.8rem;
  color: var(--color-text-faint);
  max-width: 72ch;
  padding-top: var(--space-5);
  border-top: 1px solid var(--color-border);
}
</style>
