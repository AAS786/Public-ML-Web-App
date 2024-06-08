import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import os


# Loading the saved models

cancer_model = pickle.load(open('cancer_model.sav', 'rb'))

heart_model = pickle.load(open('heart_model.sav', 'rb'))

kidney_model = pickle.load(open('kidney_model.sav', 'rb'))

liver_model = pickle.load(open('liver_model.sav', 'rb'))

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))



with st.sidebar:
    st.markdown(
        """
        <div style='text-align: center;'>
            <img src='https://i.postimg.cc/qqZqVx7J/health1-removebg-preview.png' alt='Logo' width='300'>
        </div>
        """,
        unsafe_allow_html=True
    )
    

    selected = option_menu('Multiple Disease Prediction System',
                           ['Home',
                            'Heart Disease Prediction',
                            'Diabetes Prediction',
                            'Liver Prediction',
                            'Cancer Prediction',
                            'Kidney Prediction'],
                           icons = ['house','heart','droplet','bandaid','brightness-high','boxes'],
                           default_index = 0)

# CSS for styling with background image
st.markdown(
    """
    <style>
    .main {
        background-image: url('https://i.postimg.cc/905SCbGL/bg1.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-color: black(255, 255, 255, 0.8);
    }
    .title {
        font-size: 40px;
        font-weight: bold;
    }
    .logo {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 50%;
    }
    .subtitle {
        font-size: 30px;
        font-weight: bold;
        margin-top: 20px;
    }
    .content {
        font-size: 20px;
        margin-top: 10px;
    }
    .stTextInput > div > div > input[type="text"] {
        color: black !important;
    }
    .container {
        display: flex;
        align-items: center;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Image URLs for each disease
heart_img = 'https://i.postimg.cc/KYQZhY1J/heart-disease.jpg'
diabetes_img = 'https://i.postimg.cc/GpMHJKxL/Diabetes-disease.jpg'
liver_img = 'https://i.postimg.cc/7ZkGxfLk/liver-Disease.jpg'
cancer_img = 'https://i.postimg.cc/3RVNzwqz/Cancer-disease.jpg'
kidney_img = 'https://i.postimg.cc/02mKRpPn/Kidney-disease.jpg'



# Home Page
if selected == 'Home':
    st.markdown("""
        <div class='title'>
            <img class='logo' src='https://i.postimg.cc/FFbx5dmj/Health-Logo.png' alt='Logo'>
            <h1 style='text-decoration: underline;'>Machine Learning Health Disease Prediction</h1>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("<div class='content'>Welcome to the Machine Learning Health Disease Prediction system. Use the sidebar to navigate through different disease prediction pages.</div>", unsafe_allow_html=True)
    st.markdown("<h2 class='subtitle'>About the Diseases</h2>", unsafe_allow_html=True)

    # Cancer
    st.markdown("""
    <div class="container">
        <div>
            <h3 class='subtitle' style='text-decoration: underline;'>Cancer</h3>
            <div class='content'>Cancer is a group of diseases characterized by the uncontrolled growth and spread of abnormal cells. If the spread is not controlled, it can result in death.</div>
            <div class='content'><strong>Symptoms:</strong></div>
            <ul class='content'>
                <li>Changes in bowel or bladder habits</li>
                <li>A sore that does not heal</li>
                <li>Unusual bleeding or discharge</li>
                <li>Thickening or lump in the breast or other parts of the body</li>
                <li>Indigestion</li>
                <li>Difficulty swallowing</li>
                <li>Recent change in a wart or mole</li>
            </ul>
        </div>
        <img src="https://i.postimg.cc/3RVNzwqz/Cancer-disease.jpg" width="400">
    </div>
    """, unsafe_allow_html=True)

    # Heart Disease
    st.markdown("""
    <div class="container">
        <div>
            <h3 class='subtitle' style='text-decoration: underline;'>Heart Disease</h3>
            <div class='content'>Heart disease refers to various types of conditions that can affect heart function, including coronary artery disease, arrhythmias, and heart defects among others.</div>
            <div class='content'><strong>Symptoms:</strong></div>
            <ul class='content'>
                <li>Chest pain</li>
                <li>Discomfort</li>
                <li>Shortness of breath</li>
                <li>Pain, numbness</li>
                <li>Weakness</li>
                <li>Coldness in your legs</li> 
                <li>Arms if the blood vessels in those parts of your body</li>
                <li>Pain in the neck</li> 
                <li>Jaw</li>
                <li>Throat</li> 
                <li>Upper abdomen</li>
                <li>Back</li>
            </ul>
        </div>
        <img src="https://i.postimg.cc/KYQZhY1J/heart-disease.jpg" width="400">
    </div>
    """, unsafe_allow_html=True)

    # Diabetes
    st.markdown("""
    <div class="container">
        <div>
            <h3 class='subtitle' style='text-decoration: underline;'>Diabetes</h3>
            <div class='content'>Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy. Most of the food you eat is broken down into sugar (glucose) and released into your bloodstream.</div>
            <div class='content'><strong>Symptoms:</strong></div>
            <ul class='content'>
                <li>Increased thirst</li>
                <li>Frequent urination</li>
                <li>Extreme hunger</li>
                <li>Unexplained weight loss</li>
                <li>Presence of ketones in the urine</li>
                <li>Fatigue</li>
                <li>Irritability</li>
                <li>Blurred vision</li>
            </ul>
        </div>
        <img src="https://i.postimg.cc/GpMHJKxL/Diabetes-disease.jpg" width="400">
    </div>
    """, unsafe_allow_html=True)

    # Liver Disease
    st.markdown("""
    <div class="container">
        <div>
            <h3 class='subtitle' style='text-decoration: underline;'>Liver Disease</h3>
            <div class='content'>Liver disease is a broad term that covers all the potential problems that cause the liver to fail to perform its designated functions. Usually, more than 75% or three quarters of liver tissue needs to be affected before a decrease in function occurs.</div>
            <div class='content'><strong>Symptoms:</strong></div>
            <ul class='content'>
                <li>Yellowing of the skin and eyes (jaundice)</li>
                <li>Pain and swelling in the abdomen</li>
                <li>Swelling in the legs and ankles</li>
                <li>Itchy skin</li>
                <li>Dark urine color</li>
                <li>Pale-colored stool</li>
                <li>Chronic fatigue</li>
            </ul>
        </div>
        <img src="https://i.postimg.cc/7ZkGxfLk/liver-Disease.jpg" width="400">
    </div>
    """, unsafe_allow_html=True)

    # Kidney Disease
    st.markdown("""
    <div class="container">
        <div>
            <h3 class='subtitle' style='text-decoration: underline;'>Kidney Disease</h3>
            <div class='content'>Kidney disease means your kidneys are damaged and can't filter blood the way they should. This can cause wastes to build up in your body and other problems that can harm your health.</div>
            <div class='content'><strong>Symptoms:</strong></div>
            <ul class='content'>
                <li>Nausea</li>
                <li>Vomiting</li>
                <li>Loss of appetite</li>
                <li>Fatigue and weakness</li>
                <li>Sleep problems</li>
                <li>Changes in how much you urinate</li>
                <li>Decreased mental sharpness</li>
                <li>Muscle twitches and cramps</li>
                <li>Swelling of feet and ankles</li>
            </ul>
        </div>
        <img src="https://i.postimg.cc/02mKRpPn/Kidney-disease.jpg" width="400">
    </div>
    """, unsafe_allow_html=True)


# Heart Prediction Page
if (selected == 'Heart Disease Prediction'):
    st.image(heart_img, width=200)  # Small image on the left-hand side

    # Page Title
    #st.title('Heart Prediction using ML')
    st.markdown("<h1 style='text-decoration: underline;'>Heart Disease Prediction using ML</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('**Age**')
    with col2:
        sex = st.text_input('**Sex**')
    with col3:
        cp = st.text_input('**Chest Pain types**')
    with col1:
        trestbps = st.text_input('**Resting Blood Pressure**')
    with col2:
        chol = st.text_input('**Serum Cholestoral in mg/dl**')
    with col3:
        fbs = st.text_input('**Fasting Blood Sugar > 120 mg/dl**')
    with col1:
        restecg = st.text_input('**Resting Electrocardiographic results**')
    with col2:
        thalach = st.text_input('**Maximum Heart Rate achieved**')
    with col3:
        exang = st.text_input('**Exercise Induced Angina**')
    with col1:
        oldpeak = st.text_input('**ST depression induced by exercise**')
    with col2:
        slope = st.text_input('**Slope of the peak exercise ST segment**')
    with col3:
        ca = st.text_input('**Major vessels colored by flourosopy**')
    with col1:
        thal = st.text_input('**Thalium stress result**')

    heart_diagnosis = ''

    
    # Creating Button for Prediction
    if st.button('**Heart Disease Test Result**'):
        heart_prediction = heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if(heart_prediction[0]==1):
            heart_diagnosis = 'The person have a Heart Disease'
            result_color = "red"
            
        else:
            heart_diagnosis = 'The person do not have a Heart Disease'
            result_color = "green"

        st.markdown(f"<h3 style='color: {result_color};'>{heart_diagnosis}</h3>", unsafe_allow_html=True)

    #st.success(heart_diagnosis)




# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    st.image(diabetes_img, width=200)  # Small image on the left-hand side

    # Page Title
    #st.title('Diabetes Prediction using ML')
    st.markdown("<h1 style='text-decoration: underline;'>Diabetes Prediction using ML</h1>", unsafe_allow_html=True)
    # getting the input data from users
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('**Number of Pregnancies**')
    with col2:
        Glucose = st.text_input('**Glucose Level**')
    with col3:
        BloodPressure = st.text_input('**Blood Pressure value**')
    with col1:
        SkinThickness = st.text_input('**Skin Thickness value**')
    with col2:
        Insulin = st.text_input('**Insulin Level**')
    with col3:
        BMI = st.text_input('**BMI value**')
    with col1:
        DiabetesPedigreeFunction = st.text_input('**Diabetes Pedigree Function value**')
    with col2:
        Age = st.text_input('**Age of the Person**')

    # Code for Prediction

    diab_diagnosis = ''

    # Creating Button for Prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if(diab_prediction[0]==1):
            diab_diagnosis = '**The person have a Diabetes**'
            result_color = "red"
            
        else:
            diab_diagnosis = '**The person do not have a Diabetes**'
            result_color = "green"

        st.markdown(f"<h3 style='color: {result_color};'>{diab_diagnosis}</h3>", unsafe_allow_html=True)

    st.success(diab_diagnosis)


        
    
   
# Liver Prediction Page
if (selected == 'Liver Prediction'):
    st.image(liver_img, width=200)  # Small image on the left-hand side

    # Page Title
    #st.title('Liver Prediction using ML')
    st.markdown("<h1 style='text-decoration: underline;'>Liver Prediction using ML</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        Age = st.text_input('**Number of Age**')
    with col2:
        Gender = st.text_input('**Gender**')
    with col1:
        Total_Bilirubin = st.text_input('**Total Bilirubin**')
    with col2:
        Direct_Bilirubin = st.text_input('**Direct Bilirubin value**')
    with col1:
        Alkaline_Phosphotase = st.text_input('**Alkaline Phosphotase value**')
    with col2:
        Alamine = st.text_input('**Alamine Aminotransferase value**')
    with col1:
        Aspartate = st.text_input('**Aspartate Aminotransferase value**')
    with col2:
        Total_Proteins = st.text_input('**Total Proteins value**')
    with col1:
        Albumin = st.text_input('**Albumin**')
    with col2:
        Albumin_Globulin_Ratio = st.text_input('**Albumin and Globulin Ratio value**')

    
    # Code for Prediction
    liver_diagnosis = ''
    
    # Creating Button for Prediction
    if st.button('**Liver Test Result**'):
        
        liver_prediction = liver_model.predict([[Age,Gender,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine,Aspartate,Total_Proteins,Albumin,Albumin_Globulin_Ratio]])
        
        
        if(liver_prediction[0]==1):
            liver_diagnosis = 'The person have a Liver Problem'
            result_color = "red"
            
        else:
            liver_diagnosis = 'The person do not have a Liver Problem'
            result_color = "green"

        st.markdown(f"<h3 style='color: {result_color};'>{liver_diagnosis}</h3>", unsafe_allow_html=True)

    st.success(liver_diagnosis)



# Cancer Prediction Page
if (selected == 'Cancer Prediction'):
    st.image(cancer_img, width=200)  # Small image on the left-hand side

    # Page Title
    #st.title('Cancer Prediction using ML')
    st.markdown("<h1 style='text-decoration: underline;'>Cancer Prediction using ML</h1>", unsafe_allow_html=True)
    #col create
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        radius_mean = st.text_input('**Radius_mean value**')
        smoothness_mean = st.text_input('**Smoothness_mean value**')
        symmetry_mean = st.text_input('**Symmetry_mean**')
        compactness_se = st.text_input('**Compactness_se**')
        radius_worst = st.text_input('**Radius_worst value**')
        smoothness_worst = st.text_input('**Smoothness_worst value**')

    with col2:
        texture_mean = st.text_input('**Texture_mean value**')
        compactness_mean = st.text_input('**Compactness_mean**')
        radius_se = st.text_input('**Radius_se value**')
        concavity_se = st.text_input('**Concavity_se value**')
        texture_worst = st.text_input('**Texture_worst value**')
        compactness_worst = st.text_input('**Compactness_worst value**')
        symmetry_worst = st.text_input('**Symmetry_worst value**')

    with col3:
        perimeter_mean = st.text_input('**Perimeter_mean value**')
        concavity_mean = st.text_input('**Concavity_mean**')
        perimeter_se = st.text_input('**Perimeter_se value**')
        concave_points_se = st.text_input('**Concave_points_se value**')
        perimeter_worst = st.text_input('**Perimeter_worst value**')
        concavity_worst = st.text_input('**Concavity_worst value**')
        fractal_dimension_worst = st.text_input('**Fractal_dimension_worst value**')

    with col4:
        area_mean = st.text_input('**Area_mean value**')
        concave_points_mean = st.text_input('**Concave_points_mean value**')
        area_se = st.text_input('**Area_se value**')
        fractal_dimension_se = st.text_input('**Fractal_dimension_se value**')
        area_worst = st.text_input('**Area_worst value**')
        concave_points_worst = st.text_input('**Concave_points_worst value**')

    # code for prediction
    cancer_diagnosis = ''

    #create button for prediction
    if st.button('**Cancer Test Result**'):
        cancer_prediction = cancer_model.predict([[radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,
                                                   compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,
                                                   radius_se,perimeter_se,area_se,compactness_se,concavity_se,
                                                   concave_points_se,fractal_dimension_se,radius_worst,
                                                   texture_worst,perimeter_worst,area_worst,smoothness_worst,
                                                   compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst
                                                 ]])
        if(cancer_prediction[0]==1):
            cancer_diagnosis = '**The person have a Cancer Problem**'
            result_color = "red"
            
        else:
            cancer_diagnosis = '**The person do not have a Cancer Problem**'
            result_color = "green"

        st.markdown(f"<h3 style='color: {result_color};'>{cancer_diagnosis}</h3>", unsafe_allow_html=True)

    st.success(cancer_diagnosis)



# Kidney Prediction Page


if (selected == 'Kidney Prediction'):
    st.image(kidney_img, width=200)  # Small image on the left-hand side

    # Page Title
    #st.title('Kidney Prediction using ML')
    st.markdown("<h1 style='text-decoration: underline;'>Kidney Prediction using ML</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('**Age in Number**')
        bp = st.text_input('**Blood Pressure**')
        al = st.text_input('**Albumin**')
        su = st.text_input('**Sugar**')
        bgr = st.text_input('**Blood Glucose Random**')
        bu = st.text_input('**Blood Urea**')
        sc = st.text_input('**Serum Creatinine**')
    with col2:
        rbc = st.text_input('**Red Blood Cells**' )
        pc = st.text_input('**Pus Cell**' )
        pcc = st.text_input('**Pus Cell Clumps**' )
        ba = st.text_input('**Bacteria**' )
        pot = st.text_input('**Potassium**')
        wc = st.text_input('**White Blood Cell Count**')
    with col3:
        htn = st.text_input('**Hypertension**' )
        dm = st.text_input('**Diabetes Mellitus**' )
        cad = st.text_input('**Coronary Artery Disease**' )
        pe = st.text_input('**Pedal Edema**' )
        ane = st.text_input('**Anemia**' )
        

    Kidney_diagnosis = ''
    if st.button('**Kidney Test Result**'):

        
        Kidney_prediction = kidney_model.predict([[age,rbc,htn,bp,pc,dm,al,pcc,cad,su,ba,pe,bgr,pot,ane,bu,wc,sc]])
        
        if(Kidney_prediction[0]==1):
            Kidney_diagnosis = '**The person have a Kidney Problem**'
            result_color = "red"
            
        else:
            Kidney_diagnosis = '**The person do not have a Kidney Problem**'
            result_color = "green"

        st.markdown(f"<h3 style='color: {result_color};'>{Kidney_diagnosis}</h3>", unsafe_allow_html=True)

    st.success(Kidney_diagnosis)


