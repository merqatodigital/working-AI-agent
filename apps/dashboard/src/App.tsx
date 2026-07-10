import { useState, useEffect } from 'react'
import { getResortState } from './lib/api'
import { Dashboard } from './pages/Dashboard'
import { AgentChat } from './pages/AgentChat'
import { Settings } from './pages/Settings'

type Page = 'dashboard' | 'chat' | 'bookings' | 'rooms' | 'staff' | 'inventory' | 'approvals' | 'settings'

const NAV_ITEMS: { id: Page; label: string; icon: string }[] = [
  { id: 'dashboard', label: 'Command Center', icon: '🏠' },
  { id: 'chat', label: 'Agent Chat', icon: '🤖' },
  { id: 'bookings', label: 'Bookings', icon: '📅' },
  { id: 'rooms', label: 'Rooms', icon: '🚪' },
  { id: 'staff', label: 'Staff', icon: '👥' },
  { id: 'inventory', label: 'Inventory', icon: '📦' },
  { id: 'approvals', label: 'Approvals', icon: '✅' },
  { id: 'settings', label: 'Agent Settings', icon: '⚙️' },
]

function App() {
  const [page, setPage] = useState<Page>('dashboard')
  const [resortState, setResortState] = useState<any>(null)

  useEffect(() => {
    getResortState().then(setResortState).catch(console.error)
    const interval = setInterval(() => {
      getResortState().then(setResortState).catch(console.error)
    }, 30000)
    return () => clearInterval(interval)
  }, [])

  return (
    <div className="flex h-screen bg-slate-50">
      {/* Sidebar */}
      <aside className="w-64 bg-white border-r border-slate-200 flex flex-col">
        <div className="p-6 border-b border-slate-200">
          <h1 className="text-xl font-bold text-slate-900">KAPWA</h1>
          <p className="text-sm text-slate-500">Resort Operating System</p>
          <p className="text-xs text-slate-400 mt-1">Palawan Island, Philippines</p>
        </div>
        <nav className="flex-1 p-4 space-y-1">
          {NAV_ITEMS.map((item) => (
            <button
              key={item.id}
              onClick={() => setPage(item.id)}
              className={`w-full flex items-center gap-3 px-3 py-2 rounded-lg text-sm font-medium transition-colors ${
                page === item.id
                  ? 'bg-kapwa-50 text-kapwa-700 border border-kapwa-200'
                  : 'text-slate-600 hover:bg-slate-100'
              }`}
            >
              <span>{item.icon}</span>
              {item.label}
            </button>
          ))}
        </nav>
        <div className="p-4 border-t border-slate-200">
          {resortState && (
            <div className="text-xs text-slate-500 space-y-1">
              <div>Occupancy: {resortState.occupancy_rate}%</div>
              <div>Guests: {resortState.guests_checked_in}</div>
              <div>Open Tasks: {resortState.open_tasks}</div>
            </div>
          )}
        </div>
      </aside>

      {/* Main content */}
      <main className="flex-1 overflow-auto">
        {page === 'dashboard' && <Dashboard state={resortState} />}
        {page === 'chat' && <AgentChat />}
        {page === 'bookings' && <PlaceholderPage title="Bookings" />}
        {page === 'rooms' && <PlaceholderPage title="Rooms" />}
        {page === 'staff' && <PlaceholderPage title="Staff & Tasks" />}
        {page === 'inventory' && <PlaceholderPage title="Inventory" />}
        {page === 'approvals' && <PlaceholderPage title="Pending Approvals" />}
        {page === 'settings' && <Settings />}
      </main>
    </div>
  )
}

function PlaceholderPage({ title }: { title: string }) {
  return (
    <div className="p-8">
      <h2 className="text-2xl font-bold text-slate-900 mb-4">{title}</h2>
      <p className="text-slate-500">This page will be built when connected to Lovable.dev + Supabase.</p>
    </div>
  )
}

export default App
