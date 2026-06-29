from fastapi import FastAPI
from pydantic import BaseModel


#creating fastapi application
app=FastAPI(title="FastApi Learning")

#get endpoint

@app.get("/greet")
def home():
    return {"message : Welcome to FastAPI"}

#requst Body schema

class User(BaseModel):
    name:str
    age:int

@app.post("/user")
def create_user(user:User):
    return{
        "status":"success",
        "message":f"User{user.name} created",
        "age":user.age
    }

class BreastCancerInput(BaseModel):
    radius_mean: float
    texture_mean: float
    perimeter_mean: float
    area_mean: float
    smoothness_mean: float
    compactness_mean: float
    concavity_mean: float
    concave_points_mean: float
    symmetry_mean: float
    fractal_dimension_mean: float

    radius_se: float
    texture_se: float
    perimeter_se: float
    area_se: float
    smoothness_se: float
    compactness_se: float
    concavity_se: float
    concave_points_se: float
    symmetry_se: float
    fractal_dimension_se: float

    radius_worst: float
    texture_worst: float
    perimeter_worst: float
    area_worst: float
    smoothness_worst: float
    compactness_worst: float
    concavity_worst: float
    concave_points_worst: float
    symmetry_worst: float
    fractal_dimension_worst: float
    
@app.post("/predict")
def predict(input_data:BreastCancerInput):
    pass