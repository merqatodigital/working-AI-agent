import { clsx, type ClassValue } from 'clsx'
import { twMerge } from 'tailwind-merge'

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

const AGENT_API_URL = import.meta.env.VITE_AGENT_API_URL || 'http://localhost:8001'

export async function agentChat(message: string, threadId = 'dashboard') {
  const res = await fetch(`${AGENT_API_URL}/api/chat`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message, thread_id: threadId }),
  })
  return res.json()
}

export async function getResortState() {
  const res = await fetch(`${AGENT_API_URL}/api/state`)
  return res.json()
}

export async function getGuests() {
  const res = await fetch(`${AGENT_API_URL}/api/guests`)
  return res.json()
}

export async function getRooms() {
  const res = await fetch(`${AGENT_API_URL}/api/rooms`)
  return res.json()
}

export async function getTasks(department?: string) {
  const url = department
    ? `${AGENT_API_URL}/api/tasks?department=${department}`
    : `${AGENT_API_URL}/api/tasks`
  const res = await fetch(url)
  return res.json()
}

export async function getPendingApprovals() {
  const res = await fetch(`${AGENT_API_URL}/api/approvals/pending`)
  return res.json()
}

export async function decideApproval(approvalId: string, approved: boolean, notes = '') {
  const res = await fetch(`${AGENT_API_URL}/api/approvals/${approvalId}/decide`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ approved, notes }),
  })
  return res.json()
}

export async function getLLMSettings() {
  const res = await fetch(`${AGENT_API_URL}/api/settings/llm`)
  return res.json()
}

export async function updateLLMSettings(settings: {
  provider: string
  model: string
  base_url: string
  api_key: string
  temperature: number
}) {
  const res = await fetch(`${AGENT_API_URL}/api/settings/llm`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(settings),
  })
  return res.json()
}

export async function getAvailableModels() {
  const res = await fetch(`${AGENT_API_URL}/api/settings/models`)
  return res.json()
}

export async function checkOllamaStatus() {
  const res = await fetch(`${AGENT_API_URL}/api/settings/ollama/status`)
  return res.json()
}
