<script setup>
const sections = [
  {
    title: 'What this project is',
    body: 'This is an independent portfolio and demo application, not a company or a bank. It is not affiliated with any financial institution. This policy describes how the demo actually handles data today, so you know what happens if you create an account or upload a file.',
  },
  {
    title: 'Account data',
    body: 'If you create an account, your email address and password are stored and managed entirely by Supabase, the authentication provider this app uses. This app never sees or stores your password itself.',
  },
  {
    title: 'Uploaded documents',
    body: 'The original file you upload (PDF, PNG, or JPEG) is processed in memory to extract text and is never written to disk or stored anywhere, whether or not you are signed in.',
  },
  {
    title: 'Scan results',
    body: 'If you are signed in when you upload a document, the derived results (document type, extracted fields, and generated insights, not the original file) are saved to your account in a database so you can see your history and reports later. If you are not signed in, nothing about the scan is saved anywhere once your session ends.',
  },
  {
    title: 'Who can see your data',
    body: 'Scan results are protected by database-level access rules (row-level security), so only your own account can read your own scan history. Nobody else, including other demo users, can see it.',
  },
  {
    title: 'Data retention and deletion',
    body: 'Your account and scan history persist until you delete your account or ask for it to be removed. Since this is a demo project without a support team, deletion requests are handled manually; use the contact information on the project repository.',
  },
  {
    title: 'Third parties',
    body: 'Supabase hosts authentication and the database. No data is sold, shared for advertising, or used for any purpose beyond running this demo.',
  },
]
</script>

<template>
  <div class="privacy-page">
    <header class="page-header">
      <h1>Privacy policy</h1>
      <p class="page-subtitle">
        A plain-language description of what data this demo collects and
        what happens to it.
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
      been reviewed by an attorney. It is provided to be transparent about
      how this specific demo works, not as a legally binding policy for a
      real business.
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
