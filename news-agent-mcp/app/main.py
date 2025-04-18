from fastapi import FastAPI
from app.presenters.news_presenter import router as news_router

app = FastAPI(title="News Agent MCP Server", version="1.0.0")

# Include the news presenter routes
app.include_router(news_router, prefix="/api/v1", tags=["news"])

@app.get("/")
async def root():
    return {"message": "Welcome to the News Agent MCP Server"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)