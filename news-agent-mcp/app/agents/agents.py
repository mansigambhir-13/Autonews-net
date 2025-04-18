from app.tools.tools import serper_tool, social_media_tool, grammar_tool, data_tool, visual_tool, analytics_tool
from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from ..tools.tools import serper_tool, social_media_tool, grammar_tool, data_tool, visual_tool, analytics_tool

load_dotenv()

# Initialize LLM
try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.2,
        max_tokens=2000,
        top_p=0.9,
        frequency_penalty=0.5,
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        presence_penalty=0.5,
        stop=["\n\n"]
    )
except Exception as e:
    raise Exception(f"Failed to initialize LLM: {str(e)}")

# Agent factory functions
def create_research_agent(topic: str) -> Agent:
    return Agent(
        role="Research and Validation Agent",
        goal=f"Uncover and validate groundbreaking technologies in {topic}",
        llm=llm,
        verbose=True,
        memory=True,
        backstory="Driven by curiosity and precision, you validate discoveries.",
        tools=[serper_tool],
        allow_delegation=True,
    )

def create_writer_agent(topic: str) -> Agent:
    return Agent(
        role="News Writer",
        goal=f"Narrate compelling stories on {topic}",
        llm=llm,
        verbose=True,
        memory=True,
        backstory="You craft engaging narratives for diverse audiences.",
        tools=[serper_tool],
        allow_delegation=True,
    )

def create_editor_agent() -> Agent:
    return Agent(
        role="Editor",
        goal="Polish and enhance stories for publication",
        llm=llm,
        verbose=True,
        memory=True,
        backstory="A wordsmith perfecting narratives for impact.",
        tools=[grammar_tool] if grammar_tool else [serper_tool],
        allow_delegation=True,
    )

def create_social_media_agent(topic: str) -> Agent:
    return Agent(
        role="Social Media Intelligence Specialist",
        goal=f"Generate viral posts about {topic} based on trends",
        llm=llm,
        verbose=True,
        memory=True,
        backstory="A strategist crafting shareable posts from trends.",
        tools=[social_media_tool, serper_tool] if social_media_tool else [serper_tool],
        allow_delegation=True,
    )

def create_data_analyst_agent(topic: str) -> Agent:
    return Agent(
        role="Data Analyst",
        goal=f"Analyze data on {topic} to uncover insights",
        llm=llm,
        verbose=True,
        memory=True,
        backstory="A data-driven thinker uncovering patterns.",
        tools=[data_tool] if data_tool else [serper_tool],
        allow_delegation=True,
    )

def create_visual_creator_agent(topic: str) -> Agent:
    return Agent(
        role="Visual Content Creator",
        goal=f"Design visuals for narratives on {topic}",
        llm=llm,
        verbose=True,
        memory=True,
        backstory="A creative transforming data into visuals.",
        tools=[visual_tool] if visual_tool else [],
        allow_delegation=True,
    )

def create_feedback_agent(topic: str) -> Agent:
    return Agent(
        role="Feedback Agent",
        goal=f"Analyze engagement metrics for content on {topic}",
        llm=llm,
        verbose=True,
        memory=True,
        backstory="A performance analyst optimizing strategies.",
        tools=[analytics_tool] if analytics_tool else [serper_tool],
        allow_delegation=True,
    )

def create_ethics_reviewer_agent(topic: str) -> Agent:
    return Agent(
        role="Ethics Reviewer",
        goal=f"Ensure content on {topic} is ethical and unbiased",
        llm=llm,
        verbose=True,
        memory=True,
        backstory="A guardian ensuring high ethical standards.",
        tools=[serper_tool],
        allow_delegation=True,
    )