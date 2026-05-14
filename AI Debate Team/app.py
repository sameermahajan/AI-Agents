import time
import streamlit as st

from openai import OpenAI


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Debate Team",
    page_icon="🤖",
    layout="wide"
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🤖 AI Debate Team")

st.markdown(
    """
Watch multiple AI agents debate like a real expert panel.

Each AI has:
- a role
- a personality
- a viewpoint
- specialized knowledge
"""
)


# --------------------------------------------------
# OLLAMA CLIENT
# --------------------------------------------------

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

MODEL = "llama3.1"


# --------------------------------------------------
# AGENT FUNCTION
# --------------------------------------------------


def run_agent(role, task, temperature=0.7):

    response = client.chat.completions.create(
        model=MODEL,
        temperature=temperature,
        messages=[
            {
                "role": "system",
                "content": role
            },
            {
                "role": "user",
                "content": task
                            }
        ]
    )

    return response.choices[0].message.content


# --------------------------------------------------
# AGENT PERSONALITIES
# --------------------------------------------------

scientist_role = """
You are a scientist.

You:
- care about evidence
- use logical reasoning
- explain technical concepts clearly
- think scientifically

Keep responses engaging and concise.
"""


ethicist_role = """
You are an ethicist.

You:
- think about fairness
- care about human values
- discuss risks and ethics
- question consequences

Keep responses engaging and thoughtful.
"""


business_role = """
You are an economist and business expert.

You:
- discuss money and jobs
- analyze economic impact
- think practically
- focus on efficiency

Keep responses engaging and realistic.
"""


student_role = """
You are a high school student representative.

You:
- think like students
- ask practical questions
- care about real student life
- respond casually and honestly

Keep responses relatable and fun.
"""


moderator_role = """
You are a debate moderator.

You:
- summarize viewpoints
- identify agreements/disagreements
- ask follow-up questions
- create balanced conclusions

Be energetic and engaging.
"""


# --------------------------------------------------
# INPUTS
# --------------------------------------------------

example_topics = [
    "Should AI replace teachers?",
    "Should homework exist?",
    "Should humans colonize Mars?",
    "Should social media have age limits?"
        "Can AI become creative?",
    "Should schools use AI tutors?",
    "Will robots take jobs?",
    "Should video games be educational?",
]

selected_topic = st.selectbox(
    "Choose a debate topic",
    example_topics
)

custom_topic = st.text_input(
    "Or enter your own topic"
)


if custom_topic.strip():
    debate_topic = custom_topic
else:
    debate_topic = selected_topic


# --------------------------------------------------
# START BUTTON
# --------------------------------------------------

if st.button("🚀 Start AI Debate"):

    st.markdown("---")

    st.subheader(f"🎤 Debate Topic: {debate_topic}")


    # --------------------------------------------------
    # ROUND 1
    # --------------------------------------------------

    with st.spinner("🔬 Scientist Agent Thinking..."):
        time.sleep(1)

        scientist_response = run_agent(
            scientist_role,
            f"Debate this topic: {debate_topic}"
        )

    st.markdown("## 🔬 Scientist Agent")
    st.write(scientist_response)


    with st.spinner("⚖️ Ethicist Agent Thinking..."):
        time.sleep(1)

        ethicist_response = run_agent(
            ethicist_role,
            f"""
Topic: {debate_topic}

Scientist opinion:
{scientist_response}

Respond with ethical concerns or support.
"""
        )

    st.markdown("## ⚖️ Ethicist Agent")
    st.write(ethicist_response)



    with st.spinner("💰 Economist Agent Thinking..."):
        time.sleep(1)

        business_response = run_agent(
            business_role,
            f"""
Topic: {debate_topic}

Scientist opinion:
{scientist_response}

Ethicist opinion:
{ethicist_response}

Analyze economic and practical effects.
"""
        )

    st.markdown("## 💰 Economist Agent")
    st.write(business_response)


    with st.spinner("🎓 Student Agent Thinking..."):
        time.sleep(1)

        student_response = run_agent(
            student_role,
            f"""
Topic: {debate_topic}

Scientist opinion:
{scientist_response}

Ethicist opinion:
{ethicist_response}

Economist opinion:
{business_response}

Respond from a student perspective.
"""
        )

    st.markdown("## 🎓 Student Agent")
    st.write(student_response)


    # --------------------------------------------------
    # MODERATOR SUMMARY
    # ------

    with st.spinner("🎓 Student Agent Thinking..."):
        time.sleep(1)

        student_response = run_agent(
            student_role,
            f"""
Topic: {debate_topic}

Scientist opinion:
{scientist_response}

Ethicist opinion:
{ethicist_response}

Economist opinion:
{business_response}

Respond from a student perspective.
"""
        )
# --------------------------------------------

    with st.spinner("🎤 Moderator Summarizing Debate..."):
        time.sleep(1)

        moderator_summary = run_agent(
            moderator_role,
            f"""
Debate Topic:
{debate_topic}

Scientist:
{scientist_response}

Ethicist:
{ethicist_response}

Economist:
{business_response}

Student:
{student_response}

Create:
1. Summary of viewpoints
2. Main 
3. Main agreements
4. Final balanced conclusion
5. One interesting follow-up question
"""
        )

    st.markdown("---")

    st.markdown("# 🎤 Moderator Summary")
    st.write(moderator_summary)


    # --------------------------------------------------
    # AUDIENCE QUESTION
    # --------------------------------------------------

    st.markdown("---")

    st.subheader("🙋 Ask the AI Debate Team")

    audience_question = st.text_input(
        "Enter a follow-up question"
            )


    if audience_question:

        with st.spinner("Agents discussing your question..."):

            followup_response = run_agent(
                moderator_role,
                f"""
Debate Topic:
{debate_topic}

Audience Question:
{audience_question}

Scientist:
{scientist_response}

Ethicist:
{ethicist_response}

Economist:
{business_response}

Student:
{student_response}

Answer the audience question using viewpoints from all agents.
"""
            )

        st.markdown("## 🤖 AI Debate Team Response")
        st.write(followup_response)
