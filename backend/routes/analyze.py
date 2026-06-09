from fastapi import APIRouter

from schemas.startup_input import StartupInput

from services.prediction_pipeline import (
    run_prediction_pipeline
)

router = APIRouter()


@router.post(
    "/analyze-startup"
)
def analyze_startup(
    startup: StartupInput
):

    result = run_prediction_pipeline(
        startup
    )

    return result