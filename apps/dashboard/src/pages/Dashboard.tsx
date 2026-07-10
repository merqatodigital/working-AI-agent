interface DashboardProps {
  state: any
}

export function Dashboard({ state }: DashboardProps) {
  if (!state) {
    return (
      <div className="p-8">
        <h2 className="text-2xl font-bold text-slate-900 mb-4">Command Center</h2>
        <p className="text-slate-500">Loading resort state...</p>
      </div>
    )
  }

  return (
    <div className="p-8">
      <div className="mb-8">
        <h2 className="text-2xl font-bold text-slate-900">Command Center</h2>
        <p className="text-slate-500">KAPWA Beach Resort — Palawan Island</p>
      </div>

      {/* Key metrics */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
        <MetricCard
          label="Occupancy"
          value={`${state.occupancy_rate}%`}
          color={state.occupancy_rate > 70 ? 'green' : state.occupancy_rate > 40 ? 'yellow' : 'red'}
        />
        <MetricCard
          label="Guests Checked In"
          value={state.guests_checked_in}
          color="blue"
        />
        <MetricCard
          label="Open Tasks"
          value={state.open_tasks}
          color={state.open_tasks > 5 ? 'red' : 'green'}
        />
        <MetricCard
          label="Pending Approvals"
          value={state.pending_approvals}
          color={state.pending_approvals > 0 ? 'yellow' : 'green'}
        />
      </div>

      {/* Room status */}
      <div className="bg-white rounded-xl border border-slate-200 p-6 mb-8">
        <h3 className="text-lg font-semibold text-slate-900 mb-4">Room Status</h3>
        <div className="grid grid-cols-2 md:grid-cols-5 gap-3">
          {Object.entries(state.rooms_by_status || {}).map(([status, count]) => (
            <div key={status} className="text-center p-3 rounded-lg bg-slate-50">
              <div className="text-2xl font-bold text-slate-900">{count as number}</div>
              <div className="text-sm text-slate-500 capitalize">{status}</div>
            </div>
          ))}
        </div>
      </div>

      {/* Agent activity */}
      <div className="bg-white rounded-xl border border-slate-200 p-6">
        <h3 className="text-lg font-semibold text-slate-900 mb-4">Agent Activity Today</h3>
        <div className="text-sm text-slate-600 space-y-2">
          <div>Audit entries logged: {state.audit_entries_today}</div>
          <div>Low stock alerts: {state.low_stock_items}</div>
          <div>Total rooms: {state.total_rooms}</div>
        </div>
      </div>
    </div>
  )
}

function MetricCard({ label, value, color }: { label: string; value: any; color: string }) {
  const colors: Record<string, string> = {
    green: 'bg-green-50 border-green-200 text-green-700',
    yellow: 'bg-yellow-50 border-yellow-200 text-yellow-700',
    red: 'bg-red-50 border-red-200 text-red-700',
    blue: 'bg-blue-50 border-blue-200 text-blue-700',
  }
  return (
    <div className={`rounded-xl border p-4 ${colors[color] || colors.blue}`}>
      <div className="text-sm font-medium opacity-80">{label}</div>
      <div className="text-3xl font-bold mt-1">{value}</div>
    </div>
  )
}
