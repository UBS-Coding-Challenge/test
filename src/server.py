from fastapi import FastAPI
from src.questions.sample.controller import router as q1_router

def init_routers(app: FastAPI) -> None:
    app.include_router(q1_router)

def create_app() -> FastAPI:
    app = FastAPI(
        title="<placeholder>",
        description="<placeholder>",
        version="0.1.0"
    )

    init_routers(app)

    @app.get("/health-check")
    async def health_check():
        return "im good"
    
    return app

app = create_app()