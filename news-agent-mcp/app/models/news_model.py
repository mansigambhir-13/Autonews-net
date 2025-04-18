from pydantic import BaseModel, Field

class NewsRequest(BaseModel):
    topic: str = Field(..., description="The news topic to research")

class NewsResponse(BaseModel):
    research: str = ""
    summary: str = ""
    edited_summary: str = ""
    social_post: str = ""
    ethics_review: str = ""
    error: str = None