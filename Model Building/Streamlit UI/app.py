import streamlit as st
from predictor import predict

#set page config

st.set_page_config(
    page_title="Breast Cancer Detector",
    page_icon="🥩",
    layout="centered"
)

st.title("Breast Cancer Detector ")
st.subheader("Patients Details")
st.write("Enter the **patient details** and their values")

col1,col2,col3=st.columns(3)

with col1:

    radius_mean = st.number_input("radius_mean", min_value=0.0, value=0.0)
    texture_mean = st.number_input("texture_mean", min_value=0.0, value=0.0)
    perimeter_mean = st.number_input("perimeter_mean", min_value=0.0, value=0.0)
    area_mean = st.number_input("area_mean", min_value=0.0, value=0.0)
    smoothness_mean = st.number_input("smoothness_mean", min_value=0.0, value=0.0)
    compactness_mean = st.number_input("compactness_mean", min_value=0.0, value=0.0)
    concavity_mean = st.number_input("concavity_mean", min_value=0.0, value=0.0)
    concave_points_mean = st.number_input("concave_points_mean", min_value=0.0, value=0.0)
    symmetry_mean = st.number_input("symmetry_mean", min_value=0.0, value=0.0)
    fractal_dimension_mean = st.number_input("fractal_dimension_mean", min_value=0.0, value=0.0)
with col2:
    radius_se = st.number_input("radius_se", min_value=0.0, value=0.0)
    texture_se = st.number_input("texture_se", min_value=0.0, value=0.0)
    perimeter_se = st.number_input("perimeter_se", min_value=0.0, value=0.0)
    area_se = st.number_input("area_se", min_value=0.0, value=0.0)
    smoothness_se = st.number_input("smoothness_se", min_value=0.0, value=0.0)
    compactness_se = st.number_input("compactness_se", min_value=0.0, value=0.0)
    concavity_se = st.number_input("concavity_se", min_value=0.0, value=0.0)
    concave_points_se = st.number_input("concave_points_se", min_value=0.0, value=0.0)
    symmetry_se = st.number_input("symmetry_se", min_value=0.0, value=0.0)
    fractal_dimension_se = st.number_input("fractal_dimension_se", min_value=0.0, value=0.0)
with col3:
    radius_worst = st.number_input("radius_worst", min_value=0.0, value=0.0)
    texture_worst = st.number_input("texture_worst", min_value=0.0, value=0.0)
    perimeter_worst = st.number_input("perimeter_worst", min_value=0.0, value=0.0)
    area_worst = st.number_input("area_worst", min_value=0.0, value=0.0)
    smoothness_worst = st.number_input("smoothness_worst", min_value=0.0, value=0.0)
    compactness_worst = st.number_input("compactness_worst", min_value=0.0, value=0.0)
    concavity_worst = st.number_input("concavity_worst", min_value=0.0, value=0.0)
    concave_points_worst = st.number_input("concave_points_worst", min_value=0.0, value=0.0)
    symmetry_worst = st.number_input("symmetry_worst", min_value=0.0, value=0.0)
    fractal_dimension_worst = st.number_input("fractal_dimension_worst", min_value=0.0, value=0.0)
    
    
if st.button("🔴 Predict"):
    input_data= {
        "radius_mean": radius_mean,
        "texture_mean": texture_mean,
        "perimeter_mean": perimeter_mean,
        "area_mean": area_mean,
        "smoothness_mean": smoothness_mean,
        "compactness_mean": compactness_mean,
        "concavity_mean": concavity_mean,
        "concave points_mean": concave_points_mean,
        "symmetry_mean": symmetry_mean,
        "fractal_dimension_mean": fractal_dimension_mean,

        "radius_se": radius_se,
        "texture_se": texture_se,
        "perimeter_se": perimeter_se,
        "area_se": area_se,
        "smoothness_se": smoothness_se,
        "compactness_se": compactness_se,
        "concavity_se": concavity_se,
        "concave points_se": concave_points_se,
        "symmetry_se": symmetry_se,
        "fractal_dimension_se": fractal_dimension_se,

        "radius_worst": radius_worst,
        "texture_worst": texture_worst,
        "perimeter_worst": perimeter_worst,
        "area_worst": area_worst,
        "smoothness_worst": smoothness_worst,
        "compactness_worst": compactness_worst,
        "concavity_worst": concavity_worst,
        "concave points_worst": concave_points_worst,
        "symmetry_worst": symmetry_worst,
        "fractal_dimension_worst": fractal_dimension_worst
    }
    prediction=predict(input_data)
    st.divider()
    if prediction==1:
        st.error("🔰The patient is Maligant")
        
    else:
        st.error("🍒 This patient is Baligant")
            
    