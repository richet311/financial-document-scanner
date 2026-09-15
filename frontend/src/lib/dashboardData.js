import { supabase } from './supabaseClient'

/**
 * @typedef {Object} ScannedDocument
 * @property {string} id
 * @property {string} filename
 * @property {string|null} documentType
 * @property {number|null} confidence
 * @property {Record<string, number>} fields
 * @property {string[]} insights
 * @property {string} createdAt
 */

export const DOCUMENT_TYPE_LABELS = {
  pay_stub: 'Pay Stub',
  bank_statement: 'Bank Statement',
  budget_sheet: 'Budget Sheet',
}

export const FIELD_LABELS = {
  gross_income: 'Gross income',
  net_income: 'Net income',
  total_expenses: 'Total expenses',
  balance: 'Balance',
}

export function documentTypeLabel(type) {
  if (!type) return 'Unclassified'
  return DOCUMENT_TYPE_LABELS[type] || type.replaceAll('_', ' ')
}

export function fieldLabel(key) {
  return FIELD_LABELS[key] || key.replaceAll('_', ' ')
}

export function formatMoney(value) {
  return `$${Math.round(value).toLocaleString()}`
}

// Mirrors the savings-rate math in backend/app/services/insights.py so the
// dashboard can surface it even though it isn't persisted as its own field.
export function savingsRate(fields) {
  const net = fields?.net_income
  const expenses = fields?.total_expenses
  if (net == null || expenses == null || net === 0) return null
  return ((net - expenses) / net) * 100
}

/** @returns {ScannedDocument} */
function normalizeScan(row) {
  return {
    id: row.id,
    filename: row.filename,
    documentType: row.document_type,
    confidence: row.confidence,
    fields: row.fields || {},
    insights: row.insights || [],
    createdAt: row.created_at,
  }
}

/** @returns {Promise<ScannedDocument[]>} */
export async function fetchRecentScans(limit = 200) {
  const { data, error } = await supabase
    .from('scans')
    .select('*')
    .order('created_at', { ascending: false })
    .limit(limit)
  if (error) throw new Error(error.message)
  return (data ?? []).map(normalizeScan)
}

/** @returns {Promise<ScannedDocument>} */
export async function fetchScanById(id) {
  const { data, error } = await supabase.from('scans').select('*').eq('id', id).single()
  if (error) throw new Error(error.message)
  return normalizeScan(data)
}

/** Fields worth showing for a scan, including the derived savings rate. */
export function overviewRows(scan) {
  if (!scan) return []
  const rows = Object.entries(scan.fields).map(([key, value]) => ({
    label: fieldLabel(key),
    value: formatMoney(value),
  }))
  const rate = savingsRate(scan.fields)
  if (rate != null) {
    rows.push({ label: 'Savings rate', value: `${Math.round(rate)}%` })
  }
  return rows
}

export function formatDate(isoString) {
  return new Date(isoString).toLocaleDateString(undefined, {
    month: 'short',
    day: 'numeric',
    year: 'numeric',
  })
}
