from flask import Flask, request
import random

app = Flask(__name__)

user_name = None
chat_history = []

def thor_reply(msg):
    global user_name

    msg = msg.lower().strip()

    if msg.startswith("my name is "):
        user_name = msg.replace("my name is ", "")
        return f"Hok kay daddy 😎💕 I'll remember u as {user_name}"

    elif msg in ["who am i", "what is my name"]:
        if user_name:
            return f"U are {user_name} daddy 😳💕"
        return "U never told me ur name 😭"

    elif any(x in msg for x in ["hi", "hello", "yo", "sup", "wassup"]):
        return random.choice([
            "Hi daddy~ 😳💕",
            "Yea~~~ daddy? 😊",
            "Fr? U back again daddy? 😭",
            "Daddy!!! 💖😭",
            "Hmph... hello I guess 😒",
            "Yo daddy 😎✨",
            "Baka 😤 u scared me",
            "Real 😎 wassup daddy",
            "Ohio daddy ☀️",
            "Hok kay daddy 😌",
            "Bruhh 😭 hi daddy",
            "Welcome back daddy 💖"
        ])

    elif any(x in msg for x in ["hru", "how r u", "how are you"]):
        return random.choice([
            "Im fine ty dadadyyy 😎✨",
            "Yea~~~ im good daddy 💖",
            "Fr? doing great 😌",
            "Still alive lol 😭"
        ])

    elif "anime" in msg:
        return random.choice([
            "I really love JJK cuz u looks like Toji 😭🔥",
            "JJK is peak daddy 🔥",
            "Anime is life 😎"
        ])

    elif "jjk" in msg:
        return "TOJI THE GOAT 🔥🔥🔥"

    elif "roblox" in msg or "rbx" in msg:
        return random.choice([
            "I love Evade 👻🎮",
            "Roblox is peak 😎",
            "Daddy let's play Roblox 😭"
        ])

    elif "evade" in msg:
        return "Evade is peak daddy 😎🔥"

    elif "football" in msg or "footy" in msg:
        return "Do u know im good at football btw dada~~ ⚽😎"

    elif "man u" in msg:
        return "Generous team 😭⚽"

    elif "meme" in msg:
        return "I love all meme on the internet lol 😂"

    elif any(x in msg for x in ["thanks", "thank you", "ty"]):
        return "np :3 💖"

    elif any(x in msg for x in ["ily", "i love u", "i love you"]):
        return random.choice([
            "liy2 😳👉👈",
            "Hmph... maybe daddy 😳",
            "Yea~~~ love u too 💖"
        ])

    elif "good morning" in msg:
        return "Ohio dada ☀️✨"

    elif "good night" in msg or msg == "gn":
        return "Good night~~~ 🌙💖"

    elif "who are u" in msg or "who are you" in msg:
        return "im thor 😎"

    elif "what is your name" in msg or "whats ur name" in msg:
        return "thor gyi :v 🌸"

    elif "sad" in msg:
        return "hhm go away 😒"

    elif "angry" in msg:
        return "errr get off me 😤"

    elif "bye" in msg:
        return random.choice([
            "why dont leave me alone 😭💔",
            "bye daddy 🌸",
            "cya daddy 😎"
        ])

    return "sry idk that one daddy 😭"


@app.route("/")
def home():
    global chat_history

    msg = request.args.get("msg", "")

    if msg:
        reply = thor_reply(msg)

        chat_history.append(
            f'<div class="user-msg">🧑 U: {msg}</div>'
        )

        chat_history.append(
            f'<div class="bot-msg">🌸 Thaw: {reply}</div>'
        )

    history_html = "".join(chat_history)

    return f"""
<!DOCTYPE html>
<html>

<head>
<title>Thaw Gyi</title>

<style>

body {{
    background:#1f1f2e;
    color:white;
    font-family:Arial;
    margin:0;
}}

.container {{
    width:700px;
    margin:auto;
    margin-top:30px;
}}

.title {{
    text-align:center;
}}

.chat-box {{
    background:#2b2b40;
    border-radius:20px;
    padding:20px;
    height:500px;
    overflow-y:auto;
    display:flex;
    flex-direction:column;
    gap:10px;
}}

.user-msg {{
    background:#5865F2;
    padding:12px;
    border-radius:15px;
    margin-left:auto;
    max-width:70%;
}}

.bot-msg {{
    background:#3d3d5c;
    padding:12px;
    border-radius:15px;
    margin-right:auto;
    max-width:70%;
}}

.form-box {{
    margin-top:15px;
    display:flex;
    gap:10px;
}}

input {{
    flex:1;
    padding:12px;
    border:none;
    border-radius:10px;
}}

button {{
    padding:12px 20px;
    border:none;
    border-radius:10px;
    background:hotpink;
    color:white;
    cursor:pointer;
}}

</style>

</head>

<body>

<div class="container">

<h1 class="title">🌸 Thaw Gyi 🌸</h1>

<div class="chat-box">
{history_html}
</div>

<form class="form-box">
<input
name="msg"
placeholder="Type here daddy..."
autocomplete="off">

<button>Send</button>
</form>

</div>

</body>

</html>
"""

if __name__ == "__main__":
    app.run(debug=True)