<div align="center">

<!-- ANIMATED BANNER -->
<img src="assets/banner.svg" alt="CORTEX v5.0 Banner" width="100%"/>

<br/>

<!-- SHIELD BADGES ROW 1 -->
![Python](https://img.shields.io/badge/Python-3.8+-00ff41?style=for-the-badge&logo=python&logoColor=black&labelColor=000000)
![Gemini](https://img.shields.io/badge/Gemini_2.0_Flash-AI_Core-00ffff?style=for-the-badge&logo=google&logoColor=black&labelColor=000000)
![Voice](https://img.shields.io/badge/Voice_I%2FO-Active-ff00ff?style=for-the-badge&logo=googleassistant&logoColor=black&labelColor=000000)
![Agent](https://img.shields.io/badge/Agent_Mode-Web_Search-ffe600?style=for-the-badge&logo=googlechrome&logoColor=black&labelColor=000000)

<!-- SHIELD BADGES ROW 2 -->
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-ff8800?style=for-the-badge&logo=windows&logoColor=black&labelColor=000000)
![License](https://img.shields.io/badge/License-MIT-00ff41?style=for-the-badge&labelColor=000000)
![Status](https://img.shields.io/badge/Status-ONLINE%20●-00ff41?style=for-the-badge&labelColor=000000)
![Language](https://img.shields.io/badge/Language-Hinglish_AI-ff00ff?style=for-the-badge&labelColor=000000)

<br/><br/>

> **"Ek AI jo samajhta hai — sirf code nahi, tujhe bhi."**
>
> India ka ultimate terminal AI — powered by Gemini 2.0 Flash · Voice I/O · Agent Mode · 6 Personas

</div>

---

<!-- ANIMATED TERMINAL -->
<div align="center">
<img src="assets/terminal.svg" alt="CORTEX Terminal Demo" width="100%"/>
</div>

---

## 🧠 What is CORTEX?

**CORTEX v5.0 Neuron Edition** is a fully-featured terminal AI assistant built for Indian developers. It doesn't live in a browser tab — it lives in your **command line**, speaks **Hinglish**, thinks in code, and runs on **Google Gemini 2.0 Flash**.

```
╔════════════════════════════════════════════════════════════╗
║               🧠 C O R T E X   v 5 . 0   N E U R O N     ║
║                    "Maximum Truth + Maximum Fun"           ║
╚════════════════════════════════════════════════════════════╝
```

| What it does | How |
|---|---|
| 🎤 Listens to your mic | SpeechRecognition + Google STT (hi-IN) |
| 🔊 Talks back to you | pyttsx3 offline TTS, 170 WPM |
| 🌐 Searches the web live | DuckDuckGo DDGS, zero API key |
| 🤖 Switches personalities | 6 Gemini system prompt personas |
| 💾 Remembers conversations | Multi-session JSON persistence |
| 📎 Reads your files & images | PIL + Gemini Vision |
| ⚡ Looks sick doing all of it | Rich terminal UI with Markdown |

---

<!-- ANIMATED FEATURES GRID -->
<div align="center">
<img src="assets/features.svg" alt="CORTEX Features" width="100%"/>
</div>

---

## ✨ Features Deep Dive

<details>
<summary><b>🎤 Voice Input — <code>/listen</code></b></summary>

<br/>

Say `/listen` and speak. CORTEX activates your microphone, auto-calibrates for ambient noise, and captures up to 8 seconds of audio. Powered by **SpeechRecognition** with Google's STT API using the `hi-IN` language model — Hindi and English both work naturally.

```
[cortex_main] > /listen
🎤 Listening... Ab bol bhai! (5-8 second tak bol sakte ho)
✅ Record hua: Docker kya hota hai explain karo
```

</details>

<details>
<summary><b>🔊 Voice Output — <code>/voice</code></b></summary>

<br/>

Toggle TTS with `/voice`. CORTEX reads every reply aloud using **pyttsx3** — fully offline, no API needed. Rate is set to 170 WPM with female voice preference. Speaks the first 300 characters for speed.

```
[cortex_main] > /voice
Voice Output ON 🔊
```

</details>

<details>
<summary><b>🌐 Web Search + Agent Mode — <code>/web</code>, <code>/agent</code></b></summary>

<br/>

Two ways to get live internet data:

- **Manual** — `/web <query>` fires DuckDuckGo, returns top 5 results in a Rich panel with title, body, and URL
- **Auto** — `/agent` ON means CORTEX detects intent keywords (`search`, `aaj`, `today`, `web`) in your message and **automatically** fetches live results before calling Gemini

```
[cortex_main] > /agent
Agent Mode ON 🔥

[cortex_main] > aaj ka latest AI news kya hai?
🌐 CORTEX searching web...
🧠 CORTEX THINKING...
```

</details>

<details>
<summary><b>🎭 6 AI Personas — <code>/persona</code></b></summary>

<br/>

Each persona rewrites the Gemini **system instruction** for the entire chat session — completely changing how CORTEX thinks, responds, and roasts you.

| Persona | Command | Vibe |
|---|---|---|
| 🤖 Default | `/persona default` | Witty · Helpful · Hinglish |
| 💀 Hacker | `/persona hacker` | Underground · Savage · Raw |
| 🧮 LeetCode | `/persona leetcode` | DSA God · Multi-Solution |
| 📚 Teacher | `/persona teacher` | Patient · Step-by-Step |
| 😂 Funny | `/persona funny` | Savage Roast · Mazedaar |
| 👔 Pro | `/persona pro` | Senior Engineer · Precise |

```
[cortex_main] > /persona hacker
Persona switched to: hacker 💀
```

</details>

<details>
<summary><b>💾 Persistent Chat Sessions — <code>/chat</code>, <code>/save</code>, <code>/history</code></b></summary>

<br/>

Every session lives in `chats/<name>.json` and auto-saves after every message. You can:
- Switch or create sessions with `/chat <name>`
- Review the last 20 messages with `/history`
- Force save with `/save`

Sessions survive restarts — never lose a debugging conversation again.

</details>

<details>
<summary><b>📎 Multimodal File + Image Input</b></summary>

<br/>

Type a file path as your message. CORTEX detects it automatically:

- **Images** (`.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`, `.bmp`) → loaded via **PIL**, sent as visual context to Gemini Vision
- **Text/code files** → read as UTF-8 and injected as a formatted code block

```
[cortex_main] > ./screenshot.png
📎 Image loaded: ./screenshot.png
[cortex_main] > yeh error kya bol raha hai aur fix kya hoga?
```

</details>

---

## ⌨️ Command Reference

```
╔══════════════════════════════════════════════════════════════════╗
║                    CORTEX COMMAND CENTER                         ║
╠═══════════════╦══════════════════════════════════════════════════╣
║ /listen        ║  🎤 Mic activate — Hindi+English, 8s window    ║
║ /voice         ║  🔊 Toggle TTS output ON/OFF                   ║
║ /testvoice     ║  Test if voice output is working               ║
║ /agent         ║  🔥 Auto web search mode ON/OFF                ║
║ /web <query>   ║  Manual DuckDuckGo — top 5 results             ║
║ /persona <n>   ║  Switch AI personality (hacker/leetcode/...)   ║
║ /chat <name>   ║  Switch/create session — auto-saves current    ║
║ /save          ║  Manually save session to JSON                  ║
║ /history       ║  Show last 20 messages colour-coded            ║
║ /clear         ║  Clear terminal + re-render logo               ║
║ /help          ║  Show this panel inside terminal               ║
║ /exit          ║  Save + shutdown CORTEX                        ║
╚═══════════════╩══════════════════════════════════════════════════╝
```

---

## ⚙️ How It Works

```
 ┌──────────────────────────────────────────────────────────────┐
 │                   CORTEX PIPELINE                             │
 └──────────────────────────────────────────────────────────────┘

  ① INPUT LAYER
  ├─ Keyboard text
  ├─ /listen → mic → SpeechRecognition → Google STT → text
  └─ File path → PIL (image) or UTF-8 read (text) → contents[]
         │
         ▼
  ② AGENT DECISION ENGINE
  ├─ Agent Mode ON?
  ├─ Scan input for: "search" | "aaj" | "today" | "web"
  └─ Match found → DDGS().text(query, max_results=5) → append to contents[]
         │
         ▼
  ③ GEMINI API CALL
  ├─ chat.send_message(contents)
  ├─ All context merged: text + images + files + search results
  └─ Rich spinner while waiting
         │
         ▼
  ④ RICH RENDER
  ├─ resp.text → Rich Panel(Markdown(...))
  ├─ Code blocks, bold, lists all parsed + coloured in terminal
  └─ history.append({role: user/model, content: ...})
         │
         ▼
  ⑤ MEMORY + VOICE OUTPUT
  ├─ Auto-save to chats/<name>.json
  └─ voice_output ON → engine.say(reply[:300]) → pyttsx3 speaks
```

---

## 🚀 Installation

### Step 1 — Clone

```bash
git clone https://github.com/Sunil56224972/cortex-ai
cd cortex-ai
```

### Step 2 — Install Dependencies

```bash
pip install -r requirements.txt
```

```
# requirements.txt
google-genai
python-dotenv
rich
Pillow
duckduckgo-search
pyttsx3
SpeechRecognition
pyaudio
```

> ⚠️ **pyaudio on Windows** — if it fails, run:
> ```bash
> pip install pipwin && pipwin install pyaudio
> ```

### Step 3 — Configure API Key

```bash
# Create .env in project root
echo "GEMINI_API_KEY=your_key_here" > .env
```

> 🔑 Get your **free** Gemini API key at [aistudio.google.com](https://aistudio.google.com)

### Step 4 — Launch

```bash
# Windows (double-click or CMD)
cortex.bat

# Any platform
python cli.py
```

> 🔒 **Never commit `.env` to GitHub!** Add to `.gitignore`:
> ```
> .env
> chats/
> ```

---

## 📁 Project Structure

```
cortex-ai/
├── 🐍 cli.py               ← Main brain — all logic, commands, voice, search
├── 📦 __init__.py           ← Package init
├── ⚡ cortex.bat            ← Windows launcher (double-click to run)
├── 🔐 .env                  ← API keys — NEVER commit!
├── 📋 requirements.txt      ← Python dependencies
├── 🚫 .gitignore            ← Excludes .env and chats/
├── 🖼️  assets/              ← README SVG assets
│   ├── banner.svg
│   ├── terminal.svg
│   ├── features.svg
│   └── divider.svg
└── 💾 chats/               ← Auto-created — persistent JSON sessions
    ├── cortex_main.json
    └── <your_session>.json
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| 🤖 AI Engine | `google-genai` — Gemini 2.0 Flash | LLM brain + vision |
| 🎨 Terminal UI | `rich` | Panels, markdown, spinners, colours |
| 🎤 Voice In | `SpeechRecognition` + Google STT | Mic → text (hi-IN) |
| 🔊 Voice Out | `pyttsx3` | Offline TTS, no API |
| 🌐 Web Search | `duckduckgo-search` (DDGS) | Live results, no API key |
| 🖼️ Images | `Pillow` (PIL) | Load + send to Gemini Vision |
| ⚙️ Config | `python-dotenv` | .env file loading |
| 🐍 Runtime | Python 3.8+ | Core language |
| 💻 Launcher | Windows `.bat` | One-click startup |

---

## 💡 Usage Examples

**Ask a coding question:**
```bash
[cortex_main] > bhai Python mein async await kaise kaam karta hai?
```

**Analyze an error screenshot:**
```bash
[cortex_main] > C:\Users\Sunil\Desktop\error.png
📎 Image loaded
[cortex_main] > yeh error kya bol raha hai aur fix kya hoga?
```

**LeetCode prep:**
```bash
[cortex_main] > /persona leetcode
[cortex_main] > two sum problem — har approach do with complexity
```

**Live news search:**
```bash
[cortex_main] > /agent
Agent Mode ON 🔥
[cortex_main] > aaj ka latest AI news kya hai?
```

**Full voice session:**
```bash
[cortex_main] > /voice      # TTS ON
[cortex_main] > /listen     # Speak your question
```

---

## 🛣️ Roadmap

- [ ] **Streaming output** — real-time token display, watch Cortex think
- [ ] **`/image <prompt>`** — Imagen integration for AI image gen from terminal
- [ ] **Web dashboard** — Flask UI to manage sessions and view history in browser
- [ ] **Plugin system** — inject your own custom tools and commands
- [ ] **Termux support** — full Android support via Termux
- [ ] **Chat export** — one-command PDF/HTML export of any session

---

## 🤝 Contributing

PRs welcome. Fork karo, branch banao, PR do.

```bash
git checkout -b feature/your-feature-name
git commit -m "feat: added xyz"
git push origin feature/your-feature-name
```

---

## 📄 License

MIT License — free to use, modify, distribute.

---

<div align="center">

<img src="assets/divider.svg" alt="" width="100%"/>

**Built with 🔥 by [Sunil Dev](https://github.com/Sunil56224972)**

`GEMINI 2.0 FLASH` · `VOICE I/O` · `AGENT MODE` · `HINGLISH AI` · `MIT`

<br/>

![Visits](https://visitor-badge.laobi.icu/badge?page_id=Sunil56224972.cortex-ai&left_color=000000&right_color=00ff41&left_text=Visitors)
![Stars](https://img.shields.io/github/stars/Sunil56224972/cortex-ai?style=flat&color=ffe600&labelColor=000000)
![Forks](https://img.shields.io/github/forks/Sunil56224972/cortex-ai?style=flat&color=00ffff&labelColor=000000)

</div>
