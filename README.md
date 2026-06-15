# Surface-crack-detection---Computer-vision-classification-project
# Surface Crack Detection using Transfer learning and deploying using Fast API'S and web development

## Overview

This project is an end-to-end Computer Vision application developed to automatically detect whether a surface contains cracks or not using Deep Learning and Transfer Learning techniques.

The model was trained using a pre-trained ResNet architecture and deployed into a production-ready inference pipeline using FastAPI, with a web interface built using HTML, CSS, and JavaScript.

The application allows users to upload an image of a surface and instantly receive a prediction indicating whether the surface is **Positive (Cracked)** or **Negative (Not Cracked)**.

---

## Project Workflow

Dataset → Image Preprocessing → Transfer Learning (ResNet) → Model Training → FastAPI API → Web Interface → Prediction

---

## Model Architecture

### Transfer Learning Backbone

* ResNet (Pre-trained CNN)

### Custom Layers Added

* Global Average Pooling Layer
* Batch Normalization Layer
* Sigmoid Activation Function

### Classification Task

Binary Classification:

* Negative → Surface without cracks
* Positive → Surface with cracks

---

## Model Performance

### Evaluation Metrics

* Accuracy: **99%**

The model achieved high performance in distinguishing cracked and non-cracked surfaces.

---

## Technologies Used

### Machine Learning & Computer Vision

* Python
* TensorFlow / Keras
* NumPy
* PIL (Python Imaging Library)

### Backend

* FastAPI
* Uvicorn

### Frontend

* HTML
* CSS
* JavaScript

---

## Production Pipeline

The project includes a complete deployment pipeline:

1. User uploads an image through the web interface.
2. Frontend sends the image to FastAPI.
3. FastAPI preprocesses the image.
4. The trained model performs inference.
5. Prediction result is returned and displayed on the webpage.

---

## Project Structure

```plaintext
Surface-crack-detection
│
├── Back-end
│   ├── main.py
│   ├── model.keras
│
├── Front-end
│   ├── index.html
│   ├── style.css
│   ├── script.js
│
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd Surface-crack-detection
```

Install dependencies:

```bash
pip install fastapi uvicorn tensorflow pillow numpy python-multipart
```

Run FastAPI:

```bash
cd Back-end
python -m uvicorn main:app --reload
```

Run frontend:

```bash
cd Front-end
python -m http.server 5500
```

Open:

```plaintext
Frontend:
http://127.0.0.1:5500

Backend API:
http://127.0.0.1:8000/docs
```

---

## Features

* Surface crack classification
* Transfer learning with ResNet
* Real-time image upload and prediction
* FastAPI production pipeline
* Interactive web interface
* End-to-end deployment workflow

---

## Future Improvements

* Crack localization using object detection (YOLO)
* Grad-CAM visualization
* Cloud deployment
* Real-time camera detection

---

## Author

Developed by **Yousif Hisham**
