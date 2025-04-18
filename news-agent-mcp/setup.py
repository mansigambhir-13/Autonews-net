from setuptools import setup, find_packages

setup(
    name="news_agent_mcp",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.68.0",
        "uvicorn>=0.15.0",
        "crewai>=0.1.0",
        "pydantic>=1.8.0",
    ],
)