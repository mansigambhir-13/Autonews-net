
import os
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os
load_dotenv()

# Initialize SerperDevTool
try:
    serper_tool = SerperDevTool(
        name="SerperDevTool",
        description="A tool to search for the latest news and trends.",
        api_key=os.getenv("SERPER_API_KEY"),
    )
except Exception as e:
    raise Exception(f"Failed to initialize SerperDevTool: {str(e)}")

# Placeholder tools
social_media_tool = None
grammar_tool = None
data_tool = None
visual_tool = None
analytics_tool = None
bias_detection_tool = None