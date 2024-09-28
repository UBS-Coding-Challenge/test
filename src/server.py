from fastapi import FastAPI
from src.questions.q1_bobby_bug.controller import router as q1_router
from src.questions.q2_dodge_bullet.controller import router as q2_router
from src.questions.q3_bobby_bug_p1.controller import router as q3_router
from src.questions.q5_efficient_hunter_kazuma.controller import router as q5_router
from src.questions.q10_klotski.controller import router as q10_router
from src.questions.q12_clummsy.controller import router as q12_router
from src.questions.q13_digital_colony.controller import router as q13_router

def init_routers(app: FastAPI) -> None:
    app.include_router(q1_router)
    app.include_router(q2_router)
    app.include_router(q3_router)
    app.include_router(q5_router)
    app.include_router(q10_router)
    app.include_router(q12_router)
    app.include_router(q13_router)


def create_app() -> FastAPI:
    app = FastAPI(
        title="<placeholder>",
        description="<placeholder>",
        version="0.1.0"
    )

    init_routers(app)

    @app.get("/health-check")
    async def health_check():
        return "v2"
    
    return app

app = create_app()