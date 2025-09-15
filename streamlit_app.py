import streamlit as st
import random

# ---------------- Personality Data ---------------- #
personality_info = {
    "ENFP": {
        "strengths": ["Creative", "Playful", "Optimistic", "Adaptable", "People-person"],
        "weaknesses": ["Easily distracted", "Procrastinates", "Overcommits", "Too impulsive", "Scattered focus"],
        "advice": [
            "Finish one small project before chasing the next shiny idea.",
            "Timers can be adventures. Race yourself!",
            "Write down ideas — not all need adoption.",
            "Boundaries = self-respect, not rudeness.",
            "Rest. Even unicorns need sleep.",
            "Completion gives dopamine too — not just starting.",
            "Make chores a game. Pretend dishes are a side quest.",
            "People like your energy, but it’s okay to go quiet.",
            "Don’t live in drafts — publish something.",
        ],
        "tone": "bubbly"
    },
    "ENTP": {
        "strengths": ["Quick-witted", "Energetic", "Creative", "Argumentative (in a fun way)", "Adaptable"],
        "weaknesses": ["Easily bored", "Scatters focus", "Loves chaos", "Overly competitive"],
        "advice": [
            "Not every debate needs your TED Talk.",
            "Bored? Stick with one project until the end.",
            "Chaos is fun — until your Wi-Fi bill goes unpaid.",
            "Write ideas down. Your brain is a blender.",
            "Celebrate small wins, not just giant brainstorms.",
        ],
        "tone": "playful"
    },
    "ENTJ": {
        "strengths": ["Natural leader", "Efficient", "Confident", "Strategic thinker", "Decisive"],
        "weaknesses": ["Bossy", "Impatient", "Insensitive", "Workaholic"],
        "advice": [
            "Not everyone is a soldier in your army.",
            "Slow down — efficiency isn’t everything.",
            "Compassion > command sometimes.",
            "Celebrate people, not just results.",
            "You don’t always have to win the room.",
        ],
        "tone": "commanding"
    },
    "ENFJ": {
        "strengths": ["Charismatic", "Empathetic", "Inspiring", "Organized", "Supportive"],
        "weaknesses": ["Overcommitted", "Burnout-prone", "Conflict avoidant", "Too selfless"],
        "advice": [
            "You can’t pour from an empty cup.",
            "Boundaries are love, not rejection.",
            "Let people solve their own mess sometimes.",
            "Rest is part of leadership.",
            "Don’t guilt yourself for saying no.",
        ],
        "tone": "warm"
    },
    "INFP": {
        "strengths": ["Idealistic", "Creative", "Loyal", "Empathetic", "Passionate"],
        "weaknesses": ["Overly idealistic", "Easily hurt", "Disorganized", "Escapist"],
        "advice": [
            "The world isn’t always poetry — practical steps matter too.",
            "Feelings are valid, but facts exist.",
            "You’re allowed to be messy, but balance helps.",
            "Don’t vanish into daydreams forever.",
            "Progress > perfection in your vision.",
        ],
        "tone": "dreamy"
    },
    "INFJ": {
        "strengths": ["Empathetic", "Insightful", "Altruistic", "Vision-driven", "Supportive"],
        "weaknesses": ["Burnout-prone", "Overly idealistic", "Too private", "Conflict-avoidant", "Self-sacrificing"],
        "advice": [
            "Protect your empathy battery.",
            "You don’t need to save everyone.",
            "Boundaries are holy, keep them.",
            "Ask for help. Mysteries don’t get solved without clues.",
            "Rest is radical. Do it.",
        ],
        "tone": "gentle"
    },
    "INTP": {
        "strengths": ["Logical", "Curious", "Objective", "Independent", "Abstract thinker"],
        "weaknesses": ["Overthinks", "Procrastinates", "Socially awkward", "Forgetful"],
        "advice": [
            "Ideas are great, but execution matters too.",
            "Perfection kills progress — ship it.",
            "Explaining everything isn’t always needed.",
            "Don’t live in your head forever.",
            "Test your theories in the real world.",
        ],
        "tone": "quirky"
    },
    "INTJ": {
        "strengths": ["Strategic", "Independent", "Visionary", "Efficient", "Analytical"],
        "weaknesses": ["Perfectionist", "Detached", "Overly critical", "Impatient", "Tunnel vision"],
        "advice": [
            "Done > perfect — yes, even for you.",
            "Feelings exist, deal with it.",
            "Big plans are sexy, but dishes still need washing.",
            "Delegate, don’t dominate.",
            "Patience = progress too.",
        ],
        "tone": "sarcastic"
    },
    "ISFP": {
        "strengths": ["Gentle", "Artistic", "Sensitive", "Adaptable", "Warm"],
        "weaknesses": ["Avoids conflict", "Unstructured", "Easily stressed", "Indecisive"],
        "advice": [
            "Express yourself without fear — art heals.",
            "Structure helps creativity, not kills it.",
            "Say no when needed, not just smile.",
            "Balance people-pleasing with self-care.",
        ],
        "tone": "soft"
    },
    "ISFJ": {
        "strengths": ["Loyal", "Caring", "Practical", "Supportive", "Reliable"],
        "weaknesses": ["Overworks", "Avoids conflict", "Too selfless", "Stubborn"],
        "advice": [
            "Care for yourself like you care for others.",
            "Conflict won’t break love.",
            "Delegation is not abandonment.",
            "Rest is productive too.",
        ],
        "tone": "nurturing"
    },
    "ISTP": {
        "strengths": ["Practical", "Problem-solver", "Adventurous", "Independent", "Analytical"],
        "weaknesses": ["Risky", "Detached", "Easily bored", "Impatient"],
        "advice": [
            "Think before leaping, not after.",
            "Projects: finish them, don’t just start.",
            "Silence isn’t always golden in relationships.",
            "Patience adds power to action.",
        ],
        "tone": "chill"
    },
    "ISTJ": {
        "strengths": ["Responsible", "Practical", "Reliable", "Organized", "Detail-oriented"],
        "weaknesses": ["Rigid", "Overly serious", "Stubborn", "Insensitive"],
        "advice": [
            "Rules can bend without chaos.",
            "Life’s not just checklists.",
            "Laugh more — order survives humor.",
            "Flexibility is a skill too.",
        ],
        "tone": "serious"
    },
    "ESTP": {
        "strengths": ["Energetic", "Adventurous", "Spontaneous", "Persuasive", "Practical"],
        "weaknesses": ["Impulsive", "Easily bored", "Risk-taker", "Short-term focused", "Loud"],
        "advice": [
            "Pause before the leap.",
            "Finish what you start — adrenaline there too.",
            "Not everything is a gamble.",
            "Charm is power, but listening is respect.",
            "Budget thrills too.",
        ],
        "tone": "bold"
    },
    "ESFP": {
        "strengths": ["Fun-loving", "Energetic", "Social", "Spontaneous", "Optimistic"],
        "weaknesses": ["Impulsive", "Avoids seriousness", "Easily distracted", "Overspends"],
        "advice": [
            "Fun is fabulous, but responsibilities exist.",
            "Budget so you can party guilt-free.",
            "Deep talks won’t kill the vibe.",
            "Stay focused — sparkle doesn’t fade when serious.",
        ],
        "tone": "sparkly"
    },
    "ESTJ": {
        "strengths": ["Organized", "Efficient", "Practical", "Leader", "Reliable"],
        "weaknesses": ["Bossy", "Rigid", "Insensitive", "Workaholic"],
        "advice": [
            "Not every hill is worth dying on.",
            "Flexibility builds trust too.",
            "Softness ≠ weakness.",
            "People > productivity sometimes.",
        ],
        "tone": "direct"
    },
    "ESFJ": {
        "strengths": ["Caring", "Sociable", "Organized", "Supportive", "Responsible"],
        "weaknesses": ["People-pleaser", "Overcommitted", "Conflict avoidant", "Needy"],
        "advice": [
            "Self-worth isn’t only service.",
            "No is healthy, not selfish.",
            "Conflict can clear the air.",
            "Care for yourself like you care for others.",
        ],
        "tone": "friendly"
    }
}

# ---------------- MBTI Questions ---------------- #
questions = [
    "Do you recharge by being with people 🎉 or by being alone 📚?",
    "Do you make decisions based on facts 📊 or feelings 💖?",
    "Do you prefer structured plans 📅 or going with the flow 🌊?",
    "Do you focus on details 🔍 or big ideas 💡?",
    "Do you love spontaneous adventures ✈️ or cozy routines 🏡?",
    "When stressed, do you argue 💥 or shut down 🙊?",
    "Would you rather brainstorm wild ideas 🌀 or refine existing ones 🛠?",
    "Are you better at leading 🧭 or supporting 🤝?",
    "Do you trust logic 🧠 or your gut ✨?",
    "Do you organize your closet by color 🎨 or just toss clothes in 🧺?",
    "Do you like debating for fun ⚔️ or keeping the peace ☮️?",
    "Do you usually start projects 🚀 or actually finish them ✅?",
    "Do you prefer new experiences 🌍 or familiar comforts ☕?",
    "Do people call you decisive ⚡ or indecisive 🤷?",
    "Do you text first 📱 or wait for others 🕰?",
    "Do you remember birthdays 🎂 or forget constantly 🙈?",
    "Do you plan vacations in detail 🗺 or just wing it 🐦?",
    "Do you multitask 🔄 or focus on one thing 🎯?",
    "Do you like being center of attention 🌟 or observer 👀?",
    "Do you often give advice 🧑‍🏫 or listen silently 👂?",
    "Do you trust tried-and-true ways 🔧 or invent new ones 🧪?",
    "Do you clean stress away 🧹 or binge shows 📺?",
    "Do you share secrets 🤐 or stay mysterious 🕵️?",
    "Do you like tradition 🏰 or rebellion 🦹?",
    "Do you procrastinate ⏳ or do things right away ⏱?",
    "Do you like surprises 🎁 or hate them 😑?",
    "Do you talk through problems 🗣 or think silently 🤔?",
    "Do you like risk-taking 🎲 or playing safe 🛡?",
    "Do you like rules 📏 or bending them 🔥?",
    "Do you like deep talks 🌌 or small talk ☕?",
    "Do you laugh at your own jokes 🤡 or wait for others 😂?",
    "Do you like planning months ahead 📆 or deciding day-of 🌞?"
]

# ---------------- Streamlit App ---------------- #
st.set_page_config(page_title="M-Persona", page_icon="🤖", layout="centered")

st.title("🤖 Your M-Persona")
st.write("Answer a few funny questions and let me roast you lovingly with your MBTI type 😈✨")

# Initialize session state
if "answers" not in st.session_state:
    st.session_state.answers = []
if "stage" not in st.session_state:
    st.session_state.stage = "questions"
if "mbti" not in st.session_state:
    st.session_state.mbti = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- Question Stage ---------------- #
if st.session_state.stage == "questions":
    for i, q in enumerate(questions, 1):
        st.radio(f"{i}. {q}", ["Option A", "Option B"], key=f"q{i}")

    if st.button("Submit Answers"):
        # Fake MBTI assignment (you can replace with logic later)
        st.session_state.mbti = random.choice(list(personality_info.keys()))
        st.session_state.stage = "results"
        st.rerun()

# ---------------- Results Stage ---------------- #
elif st.session_state.stage == "results":
    mbti = st.session_state.mbti
    info = personality_info[mbti]

    st.subheader(f"🥳 Your MBTI Type: **{mbti}**")
    st.write(f"### 🌟 Strengths: {', '.join(info['strengths'])}")
    st.write(f"### 😬 Weaknesses: {', '.join(info['weaknesses'])}")

    st.markdown("### 💡 Advice from your M-Persona:")
    for tip in info['advice']:
        st.write(f"- {tip}")

    st.success("You can now chat with your M-Persona about your weaknesses below ⬇️")

    # ---------------- Chat Feature ---------------- #
    st.subheader("💬 Chat With Your M-Persona")
    user_input = st.text_input("Ask me for help (e.g., 'How do I stop procrastinating?')")

    if st.button("Send"):
        if user_input:
            tone = info['tone']
            advice = random.choice(info['advice'])
            bot_reply = f"In my {tone} tone: {advice}"
            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("MBTI Buddy", bot_reply))
            st.rerun()

    for speaker, message in st.session_state.chat_history:
        st.write(f"**{speaker}:** {message}")

    if st.button("Restart Quiz"):
        st.session_state.stage = "questions"
        st.session_state.answers = []
        st.session_state.mbti = None
        st.session_state.chat_history = []
        st.rerun()
