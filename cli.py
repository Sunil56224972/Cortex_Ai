import time, json, os, sys
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai.types import GenerateContentConfig
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.status import Status
from rich import print as rprint
from PIL import Image
from duckduckgo_search import DDGS
import pyttsx3

import speech_recognition as sr

try:
    import pyaudio  # noqa: F401 — needed by sr.Microphone()
    VOICE_INPUT_AVAILABLE = True
except (ImportError, AttributeError):
    VOICE_INPUT_AVAILABLE = False

load_dotenv()
console = Console()

if not os.getenv("GEMINI_API_KEY"):
    console.print("[bold red]❌ GEMINI_API_KEY .env mein nahi mila![/bold red]")
    sys.exit(1)

client = genai.Client()
CHATS_DIR = Path("chats")
CHATS_DIR.mkdir(exist_ok=True)

engine = pyttsx3.init()
engine.setProperty('rate', 170)

# ==================== VOICE INPUT FUNCTION ====================
def voice_listen():
    if not VOICE_INPUT_AVAILABLE:
        console.print("[bold red]❌ Voice input not available! Install PyAudio:[/bold red]")
        console.print("[yellow]   pip install PyAudio[/yellow]")
        console.print("[dim](PyAudio abhi Python 3.14 ke liye available nahi hai — Python 3.12 try karo)[/dim]")
        return ""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        console.print("[yellow]🎤 Listening... Ab bol bhai! (5-8 second tak bol sakte ho)[/yellow]")
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = r.listen(source, timeout=8, phrase_time_limit=8)
            text = r.recognize_google(audio, language="hi-IN")  # Hindi + English support
            console.print(f"[green]✅ Record hua: {text}[/green]")
            return text
        except sr.WaitTimeoutError:
            console.print("[red]Kuch nahi bola...[/red]")
            return ""
        except Exception as e:
            console.print(f"[red]Mic error: {e} (mic connected hai?)[/red]")
            return ""

def show_cortex_logo():
    logo = """
    [bold magenta]╔════════════════════════════════════════════════════════════╗
    ║               🧠 C O R T E X   v 5 . 0   N E U R O N     ║
    ║                    "Maximum Truth + Maximum Fun"           ║
    ╚════════════════════════════════════════════════════════════╝[/bold magenta]
    """
    console.print(logo)

def get_cortex_prompt(persona: str) -> str:
    base = "Tu Cortex hai — ultimate Indian coding AI. Witty, truthful, helpful, thoda savage roast kar sakta hai. Hinglish mein jawab de."
    personas = {
        "default": base,
        "hacker": base + " Underground hacker vibe.",
        "leetcode": base + " LeetCode God — multiple solutions.",
        "teacher": base + " Patient teacher.",
        "funny": base + " Savage + mazedaar.",
        "pro": base + " Senior engineer."
    }
    return personas.get(persona.lower(), personas["default"])

def web_search(query: str):
    try:
        with console.status("[yellow]🌐 CORTEX search...", spinner="dots"):
            results = DDGS().text(query, max_results=5)
        return "\n\n".join([f"**{r['title']}**\n{r['body']}\n{r['href']}" for r in results])
    except Exception:
        return "Search failed."

def speak(text: str):
    try:
        voices = engine.getProperty('voices')
        if len(voices) > 1:
            engine.setProperty('voice', voices[1].id)
        console.print("[green]🔊 Speaking...[/green]")
        engine.say(text[:300])
        engine.runAndWait()
    except Exception:
        pass

def load_chat(name: str):
    path = CHATS_DIR / f"{name}.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else []

def save_chat(name: str, history):
    (CHATS_DIR / f"{name}.json").write_text(json.dumps(history, ensure_ascii=False, indent=2))

def run():
    console.clear()
    show_cortex_logo()
    console.print(Panel("[bold bright_cyan]CORTEX ONLINE — VOICE INPUT + OUTPUT ACTIVE[/bold bright_cyan]", style="bright_magenta"))

    current_chat = "cortex_main"
    persona = "default"
    model = "gemini-2.0-flash"
    voice_output = False
    agent = False

    history = load_chat(current_chat)
    chat = client.chats.create(model=model, config=GenerateContentConfig(system_instruction=get_cortex_prompt(persona)))

    while True:
        status = f"Chat: [cyan]{current_chat}[/cyan] | Persona: [magenta]{persona}[/magenta] | Agent: {'[red]ON🔥[/red]' if agent else '[dim]OFF[/dim]'} | Voice Output: {'[yellow]ON[/yellow]' if voice_output else '[dim]OFF[/dim]'}"
        console.print(Panel(status, style="bright_black"))

        # FIX 1: Use console.input() so Rich markup renders properly
        user = console.input(f"\n[bold cyan][{current_chat}] > [/bold cyan]").strip()

        if user.lower() == "/listen":
            spoken_text = voice_listen()
            if not spoken_text:
                continue
            user = spoken_text

        if not user:
            continue

        # ==================== COMMANDS ====================
        if user.lower() in ["/exit", "exit"]:
            save_chat(current_chat, history)
            console.print("[bold red]CORTEX shutting down...[/bold red]")
            break

        if user.lower() == "/help":
            console.print(Panel("""[bold yellow]COMMANDS:[/bold yellow]
 /listen       → Microphone se bol (record hoga)
 /voice        → Voice output ON/OFF
 /testvoice    → Test voice output
 /agent        → Agent Mode ON/OFF
 /web <query>  → Web search
 /persona <name> → Switch persona (hacker/leetcode/teacher/funny/pro)
 /chat <name>  → Switch/create chat session
 /save         → Save current chat
 /history      → Show chat history
 /clear        → Clear screen
 /exit         → Exit CORTEX""", title="CORTEX COMMAND CENTER"))
            continue

        if user.lower() == "/testvoice":
            speak("Hello bhai, yeh test hai. Cortex bol raha hai!")
            continue

        if user.lower() == "/voice":
            voice_output = not voice_output
            console.print(f"[yellow]Voice Output {'ON' if voice_output else 'OFF'}[/yellow]")
            continue

        # FIX 4: Implement missing /agent command
        if user.lower() == "/agent":
            agent = not agent
            console.print(f"[bold {'red' if agent else 'dim'}]Agent Mode {'ON 🔥' if agent else 'OFF'}[/bold {'red' if agent else 'dim'}]")
            continue

        # FIX 4: Implement missing /web command
        if user.lower().startswith("/web "):
            query = user[5:].strip()
            if query:
                result = web_search(query)
                console.print(Panel(Markdown(result), title="🌐 Web Results", style="bright_blue"))
            else:
                console.print("[red]Usage: /web <query>[/red]")
            continue

        # FIX 4: Implement missing /persona command
        if user.lower().startswith("/persona "):
            new_persona = user[9:].strip()
            valid = ["default", "hacker", "leetcode", "teacher", "funny", "pro"]
            if new_persona.lower() in valid:
                persona = new_persona.lower()
                chat = client.chats.create(model=model, config=GenerateContentConfig(system_instruction=get_cortex_prompt(persona)))
                console.print(f"[magenta]Persona switched to: {persona}[/magenta]")
            else:
                console.print(f"[red]Invalid persona! Choose from: {', '.join(valid)}[/red]")
            continue

        # FIX 4: Implement missing /chat command
        if user.lower().startswith("/chat "):
            new_chat = user[6:].strip()
            if new_chat:
                save_chat(current_chat, history)
                current_chat = new_chat
                history = load_chat(current_chat)
                chat = client.chats.create(model=model, config=GenerateContentConfig(system_instruction=get_cortex_prompt(persona)))
                console.print(f"[cyan]Switched to chat: {current_chat}[/cyan]")
            else:
                console.print("[red]Usage: /chat <name>[/red]")
            continue

        # FIX 4: Implement missing /save command
        if user.lower() == "/save":
            save_chat(current_chat, history)
            console.print("[green]✅ Chat saved![/green]")
            continue

        # FIX 4: Implement missing /history command
        if user.lower() == "/history":
            if not history:
                console.print("[dim]No history yet.[/dim]")
            else:
                for msg in history[-20:]:  # Show last 20 messages
                    role = msg["role"]
                    content = msg["content"][:150]
                    color = "cyan" if role == "user" else "green"
                    console.print(f"[{color}][{role.upper()}][/{color}] {content}")
            continue

        # FIX 4: Implement missing /clear command
        if user.lower() == "/clear":
            console.clear()
            show_cortex_logo()
            continue

        # FIX 5: Implement actual file upload handling
        contents = []
        if os.path.exists(user) and not user.startswith('/'):
            ext = os.path.splitext(user)[1].lower()
            if ext in ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp']:
                try:
                    img = Image.open(user)
                    contents.append(img)
                    console.print(f"[green]📎 Image loaded: {user}[/green]")
                except Exception as e:
                    console.print(f"[red]Image load failed: {e}[/red]")
            else:
                try:
                    with open(user, 'r', encoding='utf-8') as f:
                        file_content = f.read()
                    contents.append(f"File content of {user}:\n```\n{file_content}\n```")
                    console.print(f"[green]📎 File loaded: {user}[/green]")
                except Exception as e:
                    console.print(f"[red]File read failed: {e}[/red]")

        contents.append(user)

        if agent and any(k in user.lower() for k in ["search", "web", "aaj", "today"]):
            search_res = web_search(user)
            contents.append("Web search: " + search_res)

        try:
            # FIX 2: Show spinner, then stream outside the Status block
            with Status("[bold bright_magenta]🧠 CORTEX THINKING...", spinner="dots12"):
                resp = chat.send_message(contents)

            console.print(Panel(Markdown(resp.text), title="CORTEX REPLY", style="bright_green"))
            full = resp.text

            history.append({"role": "user", "content": user})
            history.append({"role": "model", "content": full})
            save_chat(current_chat, history)

            if voice_output:
                speak(full)

        except Exception as e:
            console.print(f"[bold red]Error: {e}[/bold red]")

if __name__ == "__main__":
    run()