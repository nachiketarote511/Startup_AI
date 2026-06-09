from fastapi import FastAPI

from routes.analyze import (
    router as analyze_router
)

app = FastAPI(
    title="Startup Intelligence Platform API"
)

app.include_router(
    analyze_router
)


@app.get("/")
def home():

    return {
        "message":
            "Startup Intelligence API Running"
    }