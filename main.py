from fastapi import FastAPI
from pydantic import BaseModel
from model.model import predict_pipeline
from model.model import __version__ as model_version


app = FastAPI()

class InputText(BaseModel):
    text: str


class PredictionOutput(BaseModel):
    language: str


@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}


@app.post("/predict", response_model=PredictionOutput)
def predict(payload: InputText):
    print(payload.text)
    language = predict_pipeline(payload.text)
    return {"language": language}
