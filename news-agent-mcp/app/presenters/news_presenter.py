from fastapi import APIRouter, HTTPException
from app.controllers.news_controller import NewsController
from app.models.news_model import NewsRequest, NewsResponse

router = APIRouter()

@router.post("/news", response_model=NewsResponse)
async def get_news(request: NewsRequest):
    result = await NewsController.process_news(request.topic)
    if result.error:
        raise HTTPException(status_code=400, detail=result.error)
    return result