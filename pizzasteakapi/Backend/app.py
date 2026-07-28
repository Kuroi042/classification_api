from fastapi import FastAPI
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model 
from fastapi import FastAPI,UploadFile , File
from PIL import Image
import io
app = FastAPI()

model =  load_model("cnnmodel.keras")
class_name = ["pizza","steak"]
## check localhist:8000/docs
@app.post("/predict")
async def predict(file: UploadFile= File(...)):

    image_byte=await file.read()
    image = Image.open(io.BytesIO(image_byte))
    image = image.resize((224,224))
    image = np.array(image)
    image = image.astype(np.float32)
    image = image /255.0
    image =np.expand_dims(image, axis=0)
    pred =  model.predict(image)
    prob = float(pred[0][0])
    pred_class = class_name[int(prob >= 0.5)]

    return {
        # "shape":image.shape,
        # "min":float(image.min()),
        # "max":float(image.max()),
        # "pred" :pred.tolist(),
        # "prediction":class_name[int(np.round(pred))],
        # "confidence": float(pred[0][0])
        "predclass":pred_class,
        "confidence":prob
    }   