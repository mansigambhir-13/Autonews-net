from app.crew.crew import run_news_pipeline
from app.models.news_model import NewsResponse

class NewsController:
    @staticmethod
    async def process_news(topic: str) -> NewsResponse:
        """
        Controller to handle the news pipeline logic.
        """
        try:
            # Call the crew pipeline
            results = run_news_pipeline(topic)
            if "error" in results:
                return NewsResponse(
                    research="",
                    summary="",
                    edited_summary="",
                    social_post="",
                    ethics_review="",
                    error=results["error"]
                )
            return NewsResponse(**results)
        except Exception as e:
            return NewsResponse(
                research="",
                summary="",
                edited_summary="",
                social_post="",
                ethics_review="",
                error=f"Controller error: {str(e)}"
            )