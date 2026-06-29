import requests

API_URL="http://127.0.0.1:8000/predict"

payload={
        
    'radius_mean': 14.53,
     'texture_mean': 19.34,
     'perimeter_mean': 94.25,
     'area_mean': 659.7,
     'smoothness_mean': 0.08388,
     'compactness_mean': 0.078,
     'concavity_mean': 0.08817,
     'concave points_mean': 0.02925,
     'symmetry_mean': 0.1473,
     'fractal_dimension_mean': 0.05746,
     'radius_se': 0.2535,
     'texture_se': 1.354,
     'perimeter_se': 1.994,
     'area_se': 23.04,
     'smoothness_se': 0.004147,
     'compactness_se': 0.02048,
     'concavity_se': 0.03379,
     'concave points_se': 0.008848,
     'symmetry_se': 0.01394,
     'fractal_dimension_se': 0.002327,
     'radius_worst': 16.3,
     'texture_worst': 28.39,
     'perimeter_worst': 108.1,
     'area_worst': 830.5,
     'smoothness_worst': 0.1089,
     'compactness_worst': 0.2649,
     'concavity_worst': 0.3779,
     'concave points_worst': 0.09594,
     'symmetry_worst': 0.2471,
     'fractal_dimension_worst': 0.07463
     }

response=requests.post(API_URL,json=payload)
print("Status Code:",response.status_code)
print("Response Json :",response.json())