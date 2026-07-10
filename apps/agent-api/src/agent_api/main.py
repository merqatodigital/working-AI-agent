from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from agent_api.routes.chat import router as chat_router
from agent_api.routes.approvals import router as approvals_router
from agent_api.routes.state import router as state_router
from agent_api.routes.settings import router as settings_router

app = FastAPI(
    title="KAPWA Resort Agent API",
    description="AI-powered resort management agent backend",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix="/api")
app.include_router(approvals_router, prefix="/api")
app.include_router(state_router, prefix="/api")
app.include_router(settings_router, prefix="/api")


@app.get("/health")
def health():
    return {"status": "ok", "service": "kapwa-agent-api"}


@app.get("/", response_class=HTMLResponse)
@app.get("/test", response_class=HTMLResponse)
def test_ui():
    html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>KAPWA Agent Test</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: system-ui, sans-serif; background: #f5f5f5; min-height: 100vh; display: flex; flex-direction: column; align-items: center; padding: 2rem; }
    h1 { color: #1C3A4A; margin-bottom: 0.5rem; }
    .subtitle { color: #666; margin-bottom: 2rem; }
    .card { background: white; border: 1px solid #ddd; border-radius: 12px; padding: 1.5rem; width: 100%; max-width: 600px; margin-bottom: 1.5rem; }
    .card h2 { font-size: 1rem; color: #333; margin-bottom: 1rem; text-transform: uppercase; letter-spacing: 0.05em; }
    label { font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; color: #888; display: block; margin-bottom: 0.4rem; }
    input, select { width: 100%; padding: 0.6rem 0.8rem; border: 1px solid #ddd; border-radius: 6px; font-size: 0.9rem; margin-bottom: 1rem; }
    input:focus, select:focus { outline: none; border-color: #1C3A4A; }
    .row { display: flex; gap: 0.5rem; }
    .row input { flex: 1; }
    button { padding: 0.6rem 1.2rem; border: none; border-radius: 6px; font-size: 0.85rem; font-weight: 600; cursor: pointer; white-space: nowrap; }
    .btn-primary { background: #1C3A4A; color: white; }
    .btn-primary:hover { background: #2a5068; }
    .btn-primary:disabled { opacity: 0.5; cursor: not-allowed; }
    .status { font-size: 0.8rem; margin-top: 0.5rem; display: flex; align-items: center; gap: 0.4rem; }
    .status .dot { width: 8px; height: 8px; border-radius: 50%; }
    .dot-green { background: #22c55e; }
    .dot-red { background: #ef4444; }
    .dot-gray { background: #aaa; }
    .chat-box { background: #f9f9f9; border: 1px solid #eee; border-radius: 8px; padding: 1rem; min-height: 200px; max-height: 400px; overflow-y: auto; margin-bottom: 1rem; }
    .msg { margin-bottom: 0.8rem; }
    .msg-user { text-align: right; }
    .msg-user .bubble { background: #1C3A4A; color: white; display: inline-block; padding: 0.6rem 1rem; border-radius: 12px 12px 0 12px; max-width: 80%; text-align: left; }
    .msg-bot .bubble { background: white; border: 1px solid #ddd; display: inline-block; padding: 0.6rem 1rem; border-radius: 12px 12px 12px 0; max-width: 80%; }
    .meta { font-size: 0.7rem; color: #999; margin-top: 0.3rem; }
    .meta span { display: inline-block; background: #eee; padding: 0.1rem 0.4rem; border-radius: 4px; margin-right: 0.3rem; }
    .loading { color: #999; font-style: italic; }
  </style>
</head>
<body>
  <h1>KAPWA Resort Agent</h1>
  <p class="subtitle">Test connection to the AI backend</p>

  <div class="card">
    <h2>Backend Connection</h2>
    <label>API Base URL</label>
    <div class="row">
      <input type="text" id="baseUrl" value="">
      <button class="btn-primary" onclick="testConnection()">Test</button>
    </div>
    <div class="status" id="connStatus"><span class="dot dot-gray"></span> Not tested</div>
  </div>

  <div class="card">
    <h2>Chat with Agent</h2>
    <div class="chat-box" id="chatBox">
      <div class="msg msg-bot"><div class="bubble">Mabuhay! Ask me anything about the resort.</div></div>
    </div>
    <div class="row">
      <input type="text" id="chatInput" placeholder="Type a message..." onkeypress="if(event.key==='Enter')sendChat()">
      <button class="btn-primary" id="sendBtn" onclick="sendChat()">Send</button>
    </div>
  </div>

<script>
document.getElementById('baseUrl').value = window.location.origin;

function addMessage(role, content, meta, isHtml) {
  const box = document.getElementById('chatBox');
  const div = document.createElement('div');
  div.className = 'msg msg-' + role;
  let metaHtml = '';
  if (meta) {
    metaHtml = '<div class="meta">' +
      (meta.intent ? '<span>' + meta.intent + '</span>' : '') +
      (meta.department ? '<span>' + meta.department + '</span>' : '') +
      (meta.urgency ? '<span>' + meta.urgency + '</span>' : '') +
      '</div>';
  }
  const bubbleContent = isHtml ? content : content.replace(/</g, '&lt;').replace(/\\n/g, '<br>');
  div.innerHTML = '<div class="bubble">' + bubbleContent + '</div>' + metaHtml;
  box.appendChild(div);
  box.scrollTop = box.scrollHeight;
  return div;
}

async function testConnection() {
  const url = document.getElementById('baseUrl').value;
  const el = document.getElementById('connStatus');
  el.innerHTML = '<span class="dot dot-gray"></span> Testing...';
  try {
    const res = await fetch(url + '/health');
    const data = await res.json();
    if (data.status === 'ok') {
      el.innerHTML = '<span class="dot dot-green"></span> Connected to backend';
    } else {
      el.innerHTML = '<span class="dot dot-red"></span> Unexpected response';
    }
  } catch(e) {
    el.innerHTML = '<span class="dot dot-red"></span> ' + e.message;
  }
}

async function sendChat() {
  const input = document.getElementById('chatInput');
  const text = input.value.trim();
  if (!text) return;

  const url = document.getElementById('baseUrl').value;
  addMessage('user', text);
  input.value = '';
  document.getElementById('sendBtn').disabled = true;
  const loadingDiv = addMessage('bot', 'Thinking...', null, false);

  try {
    const res = await fetch(url + '/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: text, thread_id: 'test-' + Date.now() })
    });

    loadingDiv.remove();

    if (!res.ok) {
      addMessage('bot', 'Error: Backend returned ' + res.status);
      return;
    }

    const data = await res.json();
    addMessage('bot', data.response || 'No response', {
      intent: data.intent,
      department: data.department,
      urgency: data.urgency
    });
  } catch(e) {
    loadingDiv.remove();
    addMessage('bot', 'Connection failed: ' + e.message);
  } finally {
    document.getElementById('sendBtn').disabled = false;
  }
}
</script>
</body>
</html>"""
    return HTMLResponse(content=html)
