from crewai import Task

def create_research_task(agent, topic: str) -> Task:
    return Task(
        description=f"Search for the latest news and validate technologies on {topic}.",
        agent=agent,
        expected_output="A list of validated news article summaries and insights.",
    )

def create_writing_task(agent, topic: str, research_content: str) -> Task:
    return Task(
        description=f"Write a compelling summary of this research on {topic}: {research_content}",
        agent=agent,
        expected_output="A concise, engaging news summary.",
    )

def create_editing_task(agent, text: str) -> Task:
    return Task(
        description=f"Edit this text for clarity and impact: {text}",
        agent=agent,
        expected_output="Polished and enhanced version of the text.",
    )

def create_social_media_task(agent, topic: str, summary: str) -> Task:
    return Task(
        description=f"Create a viral social media post for {topic} based on: {summary}",
        agent=agent,
        expected_output="A short, catchy, shareable post.",
    )

def create_data_analysis_task(agent, topic: str, data: str) -> Task:
    return Task(
        description=f"Analyze this data on {topic} for trends and insights: {data}",
        agent=agent,
        expected_output="A report of key patterns and insights.",
    )

def create_visual_task(agent, topic: str, summary: str) -> Task:
    return Task(
        description=f"Design a visual representation for this summary on {topic}: {summary}",
        agent=agent,
        expected_output="Description of a visual concept (e.g., chart, infographic).",
    )

def create_feedback_task(agent, topic: str, content: str) -> Task:
    return Task(
        description=f"Analyze engagement potential of this content on {topic}: {content}",
        agent=agent,
        expected_output="Feedback report with improvement suggestions.",
    )

def create_ethics_task(agent, topic: str, content: str) -> Task:
    return Task(
        description=f"Review this content on {topic} for ethical concerns: {content}",
        agent=agent,
        expected_output="Ethics review with recommendations.",
    )