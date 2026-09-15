<script setup>
import { useRouter } from 'vue-router'
import { documentTypeLabel, formatDate } from '../../lib/dashboardData'

defineProps({
  documents: { type: Array, required: true },
})

const router = useRouter()

function openScan(id) {
  router.push(`/dashboard/scans/${id}`)
}
</script>

<template>
  <div class="recent-documents card">
    <h2 class="panel-heading">Recent documents</h2>

    <table class="documents-table">
      <thead>
        <tr>
          <th>Document</th>
          <th>Type</th>
          <th>Date</th>
          <th>Status</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="doc in documents" :key="doc.id" class="doc-row" @click="openScan(doc.id)">
          <td class="filename-cell">{{ doc.filename }}</td>
          <td>
            <span class="badge badge-neutral">{{ documentTypeLabel(doc.documentType) }}</span>
          </td>
          <td class="muted-cell">{{ formatDate(doc.createdAt) }}</td>
          <td class="muted-cell">Processed</td>
          <td class="action-cell">
            <RouterLink :to="`/dashboard/scans/${doc.id}`" class="view-link" @click.stop
              >View report &rarr;</RouterLink
            >
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.recent-documents {
  padding: var(--space-5);
}

.panel-heading {
  font-size: 1.05rem;
  margin-bottom: var(--space-4);
}

.documents-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.87rem;
}

.documents-table th {
  text-align: left;
  font-weight: 500;
  color: var(--color-text-muted);
  padding: var(--space-2);
  border-bottom: 1px solid var(--color-border);
}

.documents-table td {
  padding: var(--space-3) var(--space-2);
  border-bottom: 1px solid var(--color-border);
  vertical-align: middle;
}

.doc-row:last-child td {
  border-bottom: none;
}

.doc-row {
  cursor: pointer;
  transition: background-color 0.15s ease;
}

.doc-row:hover {
  background: var(--color-surface-muted);
}

.filename-cell {
  font-weight: 500;
  font-family: var(--font-mono);
  font-size: 0.82rem;
}

.muted-cell {
  color: var(--color-text-muted);
  white-space: nowrap;
}

.action-cell {
  text-align: right;
}

.view-link {
  font-size: 0.83rem;
  color: var(--color-primary);
  text-decoration: none;
  white-space: nowrap;
}

.view-link:hover {
  text-decoration: underline;
}

@media (max-width: 700px) {
  .documents-table thead {
    display: none;
  }

  .documents-table,
  .documents-table tbody,
  .doc-row,
  .documents-table td {
    display: block;
    width: 100%;
  }

  .doc-row {
    padding: var(--space-3) 0;
    border-bottom: 1px solid var(--color-border);
  }

  .documents-table td {
    border-bottom: none;
    padding: 2px 0;
  }

  .action-cell {
    text-align: left;
    margin-top: var(--space-1);
  }
}
</style>
