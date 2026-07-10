import { useState, useRef, useEffect } from 'react'
import { agentChat } from '../lib/api'

interface Message {
  role: 'user' | 'agent'
  content: string
  metadata?: any
}

export function AgentChat() {
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const messagesEndRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  const sendMessage = async () => {
    if (!input.trim() || loading) return
    const userMsg = input.trim()
    setInput('')
    setMessages((prev) => [...prev, { role: 'user', content: userMsg }])
    setLoading(true)

    try {
      const res = await agentChat(userMsg)
      setMessages((prev) => [
        ...prev,
        {
          role: 'agent',
          content: res.response,
          metadata: {
            intent: res.intent,
            department: res.department,
            urgency: res.urgency,
          },
        },
      ])
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { role: 'agent', content: 'Error connecting to agent. Is the API server running?' },
      ])
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="flex flex-col h-full">
      <div className="p-4 border-b border-slate-200 bg-white">
        <h2 className="text-lg font-semibold text-slate-900">Agent Chat</h2>
        <p className="text-sm text-slate-500">Talk to KAPWA — your resort AI assistant</p>
      </div>

      <div className="flex-1 overflow-auto p-4 space-y-4">
        {messages.length === 0 && (
          <div className="text-center text-slate-400 mt-20">
            <div className="text-4xl mb-4">🤖</div>
            <p className="text-lg font-medium">KAPWA Resort Agent</p>
            <p className="text-sm">Ask me anything about your resort operations</p>
            <div className="mt-6 space-y-2 text-sm">
              <p className="text-slate-500">Try asking:</p>
              <p className="text-kapwa-600">"What's our current occupancy?"</p>
              <p className="text-kapwa-600">"Guest in R102 says AC is broken"</p>
              <p className="text-kapwa-600">"Check available deluxe rooms for July 15"</p>
              <p className="text-kapwa-600">"Who's on housekeeping shift today?"</p>
            </div>
          </div>
        )}

        {messages.map((msg, i) => (
          <div
            key={i}
            className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}
          >
            <div
              className={`max-w-[80%] rounded-2xl px-4 py-3 ${
                msg.role === 'user'
                  ? 'bg-kapwa-600 text-white'
                  : 'bg-white border border-slate-200 text-slate-900'
              }`}
            >
              <div className="whitespace-pre-wrap text-sm">{msg.content}</div>
              {msg.metadata && (
                <div className="mt-2 pt-2 border-t border-slate-200 text-xs text-slate-500 flex gap-3">
                  <span>Intent: {msg.metadata.intent}</span>
                  <span>Dept: {msg.metadata.department}</span>
                  <span>Urgency: {msg.metadata.urgency}</span>
                </div>
              )}
            </div>
          </div>
        ))}

        {loading && (
          <div className="flex justify-start">
            <div className="bg-white border border-slate-200 rounded-2xl px-4 py-3">
              <div className="flex gap-1">
                <div className="w-2 h-2 bg-slate-400 rounded-full animate-bounce" />
                <div className="w-2 h-2 bg-slate-400 rounded-full animate-bounce [animation-delay:0.1s]" />
                <div className="w-2 h-2 bg-slate-400 rounded-full animate-bounce [animation-delay:0.2s]" />
              </div>
            </div>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      <div className="p-4 border-t border-slate-200 bg-white">
        <div className="flex gap-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && sendMessage()}
            placeholder="Ask KAPWA about your resort..."
            className="flex-1 px-4 py-2 rounded-xl border border-slate-200 text-sm focus:outline-none focus:ring-2 focus:ring-kapwa-500 focus:border-transparent"
            disabled={loading}
          />
          <button
            onClick={sendMessage}
            disabled={loading || !input.trim()}
            className="px-4 py-2 bg-kapwa-600 text-white rounded-xl text-sm font-medium hover:bg-kapwa-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  )
}
