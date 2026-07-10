import { useState, useEffect } from 'react'
import {
  getLLMSettings,
  updateLLMSettings,
  getAvailableModels,
  checkOllamaStatus,
} from '../lib/api'

interface LLMSettings {
  provider: string
  model: string
  base_url: string
  api_key: string
  temperature: number
}

interface ModelOption {
  id: string
  name: string
  cost: string
  category: string
}

interface OllamaStatus {
  status: string
  url: string
  models: string[]
  error?: string
}

export function Settings() {
  const [settings, setSettings] = useState<LLMSettings>({
    provider: 'ollama',
    model: 'qwen2.5:3b',
    base_url: 'http://localhost:11434',
    api_key: '',
    temperature: 0.3,
  })
  const [models, setModels] = useState<ModelOption[]>([])
  const [ollamaStatus, setOllamaStatus] = useState<OllamaStatus | null>(null)
  const [saving, setSaving] = useState(false)
  const [saved, setSaved] = useState(false)

  useEffect(() => {
    getLLMSettings().then((d) => setSettings(d.settings)).catch(console.error)
    getAvailableModels().then((d) => setModels(d.models)).catch(console.error)
    checkOllamaStatus().then(setOllamaStatus).catch(console.error)
  }, [])

  const handleSave = async () => {
    setSaving(true)
    setSaved(false)
    try {
      await updateLLMSettings(settings)
      setSaved(true)
      setTimeout(() => setSaved(false), 3000)
    } catch (err) {
      console.error(err)
    } finally {
      setSaving(false)
    }
  }

  const localModels = models.filter((m) => m.category === 'local')
  const freeModels = models.filter((m) => m.category === 'free')
  const paidModels = models.filter((m) => m.category === 'paid')

  return (
    <div className="p-8 max-w-4xl">
      <div className="mb-8">
        <h2 className="text-2xl font-bold text-slate-900">Agent Settings</h2>
        <p className="text-slate-500">Configure the AI model powering KAPWA</p>
      </div>

      {/* Ollama Status */}
      <div className="bg-white rounded-xl border border-slate-200 p-6 mb-6">
        <h3 className="text-lg font-semibold text-slate-900 mb-4">Ollama Local Connection</h3>
        {ollamaStatus ? (
          <div className="flex items-center gap-3">
            <div
              className={`w-3 h-3 rounded-full ${
                ollamaStatus.status === 'connected' ? 'bg-green-500' : 'bg-red-500'
              }`}
            />
            <div>
              <div className="text-sm font-medium text-slate-900">
                {ollamaStatus.status === 'connected' ? 'Connected' : 'Disconnected'}
              </div>
              <div className="text-xs text-slate-500">{ollamaStatus.url}</div>
              {ollamaStatus.models && ollamaStatus.models.length > 0 && (
                <div className="text-xs text-slate-500 mt-1">
                  Models: {ollamaStatus.models.join(', ')}
                </div>
              )}
              {ollamaStatus.error && (
                <div className="text-xs text-red-500 mt-1">{ollamaStatus.error}</div>
              )}
            </div>
            <button
              onClick={() => checkOllamaStatus().then(setOllamaStatus)}
              className="ml-auto text-sm text-kapwa-600 hover:text-kapwa-700"
            >
              Refresh
            </button>
          </div>
        ) : (
          <div className="text-sm text-slate-500">Checking connection...</div>
        )}
      </div>

      {/* LLM Provider */}
      <div className="bg-white rounded-xl border border-slate-200 p-6 mb-6">
        <h3 className="text-lg font-semibold text-slate-900 mb-4">LLM Provider</h3>
        <div className="grid grid-cols-2 gap-4 mb-6">
          <button
            onClick={() => setSettings({ ...settings, provider: 'ollama', base_url: 'http://localhost:11434' })}
            className={`p-4 rounded-xl border-2 text-left transition-colors ${
              settings.provider === 'ollama'
                ? 'border-kapwa-500 bg-kapwa-50'
                : 'border-slate-200 hover:border-slate-300'
            }`}
          >
            <div className="font-medium text-slate-900">Ollama (Local)</div>
            <div className="text-sm text-slate-500">Free, runs on your machine</div>
          </button>
          <button
            onClick={() => setSettings({ ...settings, provider: 'openrouter', base_url: 'https://openrouter.ai/api/v1' })}
            className={`p-4 rounded-xl border-2 text-left transition-colors ${
              settings.provider === 'openrouter'
                ? 'border-kapwa-500 bg-kapwa-50'
                : 'border-slate-200 hover:border-slate-300'
            }`}
          >
            <div className="font-medium text-slate-900">OpenRouter (Cloud)</div>
            <div className="text-sm text-slate-500">200+ models, free + paid tiers</div>
          </button>
        </div>

        {/* Model Selection */}
        <div className="mb-4">
          <label className="block text-sm font-medium text-slate-700 mb-2">Model</label>
          {settings.provider === 'ollama' ? (
            <select
              value={settings.model}
              onChange={(e) => setSettings({ ...settings, model: e.target.value })}
              className="w-full px-3 py-2 rounded-lg border border-slate-200 text-sm focus:ring-2 focus:ring-kapwa-500 focus:outline-none"
            >
              {localModels.map((m) => (
                <option key={m.id} value={m.id.replace('ollama/', '')}>
                  {m.name} — {m.cost}
                </option>
              ))}
            </select>
          ) : (
            <div className="space-y-3">
              <div>
                <div className="text-xs font-medium text-slate-500 mb-1">FREE / CHEAP</div>
                <div className="grid grid-cols-2 gap-2">
                  {freeModels.map((m) => (
                    <button
                      key={m.id}
                      onClick={() => setSettings({ ...settings, model: m.id })}
                      className={`p-3 rounded-lg border text-left text-sm transition-colors ${
                        settings.model === m.id
                          ? 'border-kapwa-500 bg-kapwa-50'
                          : 'border-slate-200 hover:border-slate-300'
                      }`}
                    >
                      <div className="font-medium">{m.name}</div>
                      <div className="text-xs text-slate-500">{m.cost}</div>
                    </button>
                  ))}
                </div>
              </div>
              <div>
                <div className="text-xs font-medium text-slate-500 mb-1">PREMIUM</div>
                <div className="grid grid-cols-2 gap-2">
                  {paidModels.map((m) => (
                    <button
                      key={m.id}
                      onClick={() => setSettings({ ...settings, model: m.id })}
                      className={`p-3 rounded-lg border text-left text-sm transition-colors ${
                        settings.model === m.id
                          ? 'border-kapwa-500 bg-kapwa-50'
                          : 'border-slate-200 hover:border-slate-300'
                      }`}
                    >
                      <div className="font-medium">{m.name}</div>
                      <div className="text-xs text-slate-500">{m.cost}</div>
                    </button>
                  ))}
                </div>
              </div>
            </div>
          )}
        </div>

        {/* API Key (OpenRouter only) */}
        {settings.provider === 'openrouter' && (
          <div className="mb-4">
            <label className="block text-sm font-medium text-slate-700 mb-2">OpenRouter API Key</label>
            <input
              type="password"
              value={settings.api_key}
              onChange={(e) => setSettings({ ...settings, api_key: e.target.value })}
              placeholder="sk-or-v1-..."
              className="w-full px-3 py-2 rounded-lg border border-slate-200 text-sm focus:ring-2 focus:ring-kapwa-500 focus:outline-none"
            />
            <div className="text-xs text-slate-500 mt-1">
              Get your key at{' '}
              <a href="https://openrouter.ai/keys" target="_blank" className="text-kapwa-600 underline">
                openrouter.ai/keys
              </a>
            </div>
          </div>
        )}

        {/* Base URL override */}
        <div className="mb-4">
          <label className="block text-sm font-medium text-slate-700 mb-2">Base URL</label>
          <input
            type="text"
            value={settings.base_url}
            onChange={(e) => setSettings({ ...settings, base_url: e.target.value })}
            className="w-full px-3 py-2 rounded-lg border border-slate-200 text-sm focus:ring-2 focus:ring-kapwa-500 focus:outline-none"
          />
        </div>

        {/* Temperature */}
        <div className="mb-6">
          <label className="block text-sm font-medium text-slate-700 mb-2">
            Temperature: {settings.temperature}
          </label>
          <input
            type="range"
            min="0"
            max="1"
            step="0.1"
            value={settings.temperature}
            onChange={(e) => setSettings({ ...settings, temperature: parseFloat(e.target.value) })}
            className="w-full"
          />
          <div className="flex justify-between text-xs text-slate-500">
            <span>Precise (0)</span>
            <span>Balanced (0.5)</span>
            <span>Creative (1)</span>
          </div>
        </div>

        {/* Save */}
        <div className="flex items-center gap-3">
          <button
            onClick={handleSave}
            disabled={saving}
            className="px-6 py-2 bg-kapwa-600 text-white rounded-lg text-sm font-medium hover:bg-kapwa-700 disabled:opacity-50 transition-colors"
          >
            {saving ? 'Saving...' : 'Save Settings'}
          </button>
          {saved && (
            <span className="text-sm text-green-600 font-medium">Settings saved!</span>
          )}
        </div>
      </div>
    </div>
  )
}
