from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import io

app = FastAPI()

# Enable CORS (IMPORTANT for browser requests)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model once
model = load_model("best_model(1).keras")

classes = ["Negative", "Positive"]


def predict_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes))
    img = img.convert("RGB")
    img = img.resize((224, 224))

    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img, verbose=0)
    res = 0
    if pred[0][0] >= 0.5:
        res = 1
    else:
        res = 0
    return classes[res]


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    try:
        image_bytes = await file.read()
        result = predict_image(image_bytes)

        return {
            "success": True,
            "prediction": result
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }