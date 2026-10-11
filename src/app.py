import joblib
from fastapi import FastAPI
from pydantic import BaseModel

# 1. Initialize FastAPI application
app = FastAPI(title="MLOps Prediction API", version="1.0")

# 2. Load the trained model we created earlier
model = joblib.load("model.joblib")


# 3. Define the expected input data structure using Pydantic
class IrisInput(BaseModel):
  sepal_length: float
  sepal_width: float
  petal_length: float
  petal_width: float


# 4. Create a basic home route to check if server is running
@app.get("/")
def home():
  return {"message": "Welcome to the MLOps Model API!"}


# 5. Create the prediction endpoint
@app.post("/predict")
def predict(data: IrisInput):
  # Convert incoming JSON data into a 2D list for scikit-learn
  features = [[
      data.sepal_length,
      data.sepal_width,
      data.petal_length,
      data.petal_width,
  ]]

  # Make a prediction using our trained model
  prediction = model.predict(features)

  # Map the numeric prediction back to Iris flower names
  classes = ["Setosa", "Versicolor", "Virginica"]
  predicted_class = classes[prediction[0]]

  return {"input_received": data.model_dump(), "prediction": predicted_class}