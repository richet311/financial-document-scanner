export const SAMPLE_DOCUMENTS = [
  {
    key: 'pay-stub',
    file: 'sample-pay-stub.pdf',
    title: 'Pay stub',
    description: 'Gross income, deductions, and net pay.',
  },
  {
    key: 'bank-statement',
    file: 'sample-bank-statement.pdf',
    title: 'Bank statement',
    description: 'Opening balance, deposits, withdrawals, and balance.',
  },
  {
    key: 'budget-sheet',
    file: 'sample-budget-sheet.pdf',
    title: 'Budget sheet',
    description: 'Net pay and a breakdown of monthly expenses.',
  },
]

export async function fetchSampleFile(doc) {
  const response = await fetch(`/samples/${doc.file}`)
  if (!response.ok) {
    throw new Error('Could not load the sample file.')
  }
  const blob = await response.blob()
  return new File([blob], doc.file, { type: 'application/pdf' })
}
