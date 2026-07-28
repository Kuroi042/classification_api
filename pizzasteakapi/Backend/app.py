from fastapi import FastAPI
import tensorflow as tf
from tensorflow.keras.models import load_model
from fastapi import FastAPI,UploadFile , File

app = FastAPI()

model =  load_model("cnnmodel.keras")
## check localhist:8000/docs
@app.post("/predict")
async def predict(file: UploadFile= File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type

    }   