from fastapi import APIRouter, Depends
from starlette.responses import HTMLResponse

from models import HousingFeatures, AreaFeatures, PredictionResult
from predict import predict, predictpickle

from worker import LoadPickle

picklemodel = LoadPickle()

# from home import homepage
import security

api = APIRouter()

# Load models at app startup

@api.get("/", response_class=HTMLResponse)
def get_homepage():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Root</title>
    </head>
    <body>
        <h1>Welcome to root.</h1>
        <p>Application running!</p>
    </body>
    </html>
    """

@api.post("/predict", response_model=PredictionResult)
def post_predict(
    housing_features: HousingFeatures,
    authenticated: bool = Depends(security.validate_request),
):
    assert authenticated == True
    return predict(housing_features)

# @app.post("/pickle", dependencies=[Depends(get_current_user)])
@api.post("/predictpickle", response_model=PredictionResult)
async def get_predict_pickel(
    area: int,
    authenticated: bool = Depends(security.validate_request)
):
    assert authenticated == True
    return predictpickle(area, picklemodel)

