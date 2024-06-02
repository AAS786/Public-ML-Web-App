import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import os


# Loading the saved models

cancer_model = pickle.load(open('C:/Users/dell/Downloads/Multiple Disease/Saved/cancer_model.sav','rb'))

heart_model = pickle.load(open('C:/Users/dell/Downloads/Multiple Disease/Saved/heart_model.sav','rb'))

kidney_model = pickle.load(open('C:/Users/dell/Downloads/Multiple Disease/Saved/kidney_model.sav','rb'))

liver_model = pickle.load(open('C:/Users/dell/Downloads/Multiple Disease/Saved/liver_model.sav','rb'))

diabetes_model = pickle.load(open('C:/Users/dell/Downloads/Multiple Disease/Saved/diabetes_model.sav','rb'))


# Sidebar for Navigation
with st.sidebar:
    selected = option_menu('Multiple Disease prediction System',
                           
                           ['Home', 
                            'Cancer prediction', 
                            'Heart Disease prediction', 
                            'Diabetes prediction', 
                            'Liver Disease prediction', 
                            'Kidney prediction'],
                           
                           icons=['home','hospital', 'heart', 'activity', 'droplet', 'capsule'],
                           
                           default_index=0)

# CSS for white background and white font color
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
        color: black;
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
        color: white;
        margin-top: 20px;
    }
    .content {
        font-size: 20px;
        color: white;
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
    .container img {
        width: 150px;
        height: auto;
        margin-right: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Home Page
if selected == 'Home':
    st.markdown("<h1 class='title'>Machine Learning Health Disease Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<div class='content'>Welcome to the Machine Learning Health Disease Prediction system. Use the sidebar to navigate through different disease prediction pages.</div>", unsafe_allow_html=True)
    st.markdown("<h2 class='subtitle'>About the Diseases</h2>", unsafe_allow_html=True)

    # Cancer
    st.markdown("""
    <div class="container">
        <img src="https://i.postimg.cc/Y98nKRyK/Cancer.jpg" alt="Cancer" style="width:500px;height:auto;float: right;">
        <div>
            <h3 class='subtitle'>Cancer</h3>
            <div class='content'>Cancer is a group of diseases characterized by the uncontrolled growth and spread of abnormal cells. If the spread is not controlled, it can result in death.</div>
            <ul class='content'>
                <li>Changes in bowel or bladder habits</li>
                <li>A sore that does not heal</li>
                <li>Unusual bleeding or discharge</li>
                <li>Thickening or lump in the breast or other parts of the body</li>
                <li>Indigestion or difficulty swallowing</li>
                <li>Recent change in a wart or mole</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Heart Disease
    st.markdown("""
    <div class="container">
        <img src="https://i.postimg.cc/Qxzzd6Nj/Heart.jpg" alt="Heart Disease" style="width:500px;height:auto;float: right;">
        <div>
            <h3 class='subtitle'>Heart Disease</h3>
            <div class='content'>Heart disease refers to various types of conditions that can affect heart function, including coronary artery disease, arrhythmias, and heart defects among others.</div>
            <ul class='content'>
                <li>Chest pain or discomfort</li>
                <li>Shortness of breath</li>
                <li>Pain, numbness, weakness, or coldness in your legs or arms if the blood vessels in those parts of your body are narrowed</li>
                <li>Pain in the neck, jaw, throat, upper abdomen, or back</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Diabetes
    st.markdown("""
    <div class="container">
        <img src="https://i.postimg.cc/jSNMdtkh/Diabetes.jpg" alt="Diabetes" style="width:500px;height:auto;float: right;">
        <div>
            <h3 class='subtitle'>Diabetes</h3>
            <div class='content'>Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy. Most of the food you eat is broken down into sugar (glucose) and released into your bloodstream.</div>
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
    </div>
    """, unsafe_allow_html=True)

    # Liver Disease
    st.markdown("""
    <div class="container">
        <img src="https://i.postimg.cc/1zrMwMSn/Liver.jpg" alt="Liver Disease" style="width:500px;height:auto;float: right;">
        <div>
            <h3 class='subtitle'>Liver Disease</h3>
            <div class='content'>Liver disease is a broad term that covers all the potential problems that cause the liver to fail to perform its designated functions. Usually, more than 75% or three quarters of liver tissue needs to be affected before a decrease in function occurs.</div>
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
    </div>
    """, unsafe_allow_html=True)

    # Kidney Disease
    st.markdown("""
    <div class="container">
        <img src="https://i.postimg.cc/L4bDtncT/Kidney.jpg" alt="Kidney Disease" style="width:500px;height:auto;float: right;">
        <div>
            <h3 class='subtitle'>Kidney Disease</h3>
            <div class='content'>Kidney disease means your kidneys are damaged and can't filter blood the way they should. This can cause wastes to build up in your body and other problems that can harm your health.</div>
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
    </div>
    """, unsafe_allow_html=True)


# Cancer prediction Page
if (selected == 'Cancer prediction'):
    
    #page title
    st.title('Cancer prediction using ML')
    
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
                                                   compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,radius_se,perimeter_se,area_se,
                                                   compactness_se,concavity_se,concave_points_se,fractal_dimension_se,radius_worst,texture_worst,
                                                   perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,
                                                   concave_points_worst,symmetry_worst,fractal_dimension_worst]])
        
            
        if (cancer_prediction[0] == 1):
            cancer_diagnosis = '**The person has cancer**'
            
        else:
            cancer_diagnosis = '**The person does not have cancer**'
        
        
    st.success(cancer_diagnosis)

# Heart Disease prediction Page
if (selected == 'Heart Disease prediction'):
    
    #page title
    st.title('Heart Disease prediction using ML')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholesterol in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.text_input('Thalium stress result')

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):

        heart_prediction = heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,]])
        
            
        if (heart_prediction[0] == 1):
            heart_diagnosis = '**The person has heart problem**'
            
        else:
            heart_diagnosis = '**The person does not have heart problem**'
        
        
    st.success(heart_diagnosis)
    

# Diabetes prediction Page
if (selected == 'Diabetes prediction'):
    
    #page title
    st.title('Diabetes prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''
    
    if st.button('Diabetes Test Result'):

        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if (diab_prediction[0] == 1):
            diab_diagnosis = '**The person has diabetes problem**'
            
        else:
            diab_diagnosis = '**The person does not have diabetes problem**'
        
        
    st.success(diab_diagnosis)



# Liver Disease prediction Page
if (selected == 'liver prediction'):
    
    #page title
    st.title('Liver prediction using ML')
    
    col1, col2 = st.columns(2)
    
    with col1:
        Age = st.text_input('Age')
    with col2:
        Total_Bilirubin = st.text_input('Total Bilirubin')
    with col1:
        Direct_Bilirubin = st.text_input('Direct Bilirubin value')
    with col2:
        Alkaline_Phosphotase = st.text_input('Alkaline Phosphotase value')
    with col1:
        Alamine_Aminotransferase = st.text_input('Alamine Aminotransferase value')
    with col2:
        Aspartate_Aminotransferase = st.text_input('Aspartate Aminotransferase value')
    with col1:
        Total_Proteins = st.text_input('Total Proteins value')
    with col2:
        Albumin = st.text_input('Albumin')
    with col1:
        Albumin_and_Globulin_Ratio = st.text_input('Albumin and Globulin Ratio value')
    with col2:
        Gender_Male = st.selectbox('Gender', ('True', 'False'))

    liver_diagnosis = ''
    
    if st.button('Liver Test Result'):

        # Convert inputs to numerical data
        Age = int(Age)
        Total_Bilirubin = float(Total_Bilirubin)
        Direct_Bilirubin = float(Direct_Bilirubin)
        Alkaline_Phosphotase = int(Alkaline_Phosphotase)
        Alamine_Aminotransferase = int(Alamine_Aminotransferase)
        Aspartate_Aminotransferase = int(Aspartate_Aminotransferase)
        Total_Proteins = float(Total_Proteins)
        Albumin = float(Albumin)
        Albumin_and_Globulin_Ratio = float(Albumin_and_Globulin_Ratio)
        Gender_Male = 1 if Gender_Male == 'Male' else 0
        
        liver_prediction = liver_model.predict([[Age,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,
                                                 Alamine_Aminotransferase,Aspartate_Aminotransferase,
                                                 Total_Proteins,Albumin,Albumin_and_Globulin_Ratio,Gender_Male]])
        
        if (liver_prediction[0] == 1):
            liver_diagnosis = 'The person is having a liver problem'
            
        else:
            liver_diagnosis = 'The person is not having a liver problem'
        
        
    st.success(liver_diagnosis)



# Kidney prediction Page
if (selected == 'Kidney prediction'):
    
    #page title
    st.title('Kidney prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age in Number')
        bp = st.text_input('Blood Pressure')
        al = st.text_input('Albumin')
        su = st.text_input('Sugar')
        bgr = st.text_input('Blood Glucose Random')
        bu = st.text_input('Blood Urea')
        sc = st.text_input('Serum Creatinine')
    with col2:
        rbc = st.selectbox('Red Blood Cells', ['normal', 'abnormal'])
        pc = st.selectbox('Pus Cell', ['normal', 'abnormal'])
        pcc = st.selectbox('Pus Cell Clumps', ['notpresent', 'present'])
        ba = st.selectbox('Bacteria', ['notpresent', 'present'])
        pot = st.text_input('Potassium')
        wc = st.text_input('White Blood Cell Count')
    with col3:
        htn = st.selectbox('Hypertension', ['yes', 'no'])
        dm = st.selectbox('Diabetes Mellitus', ['yes', 'no'])
        cad = st.selectbox('Coronary Artery Disease', ['yes', 'no'])
        pe = st.selectbox('Pedal Edema', ['yes', 'no'])
        ane = st.selectbox('Anemia', ['yes', 'no'])

    kidney_diagnosis = ''
    if st.button('Kidney Test Result'):

        kidney_prediction = kidney_model.predict([[age,bp,al,su,rbc,pc,pcc,ba,bgr,bu,sc,pot,wc,htn,dm,cad,pe,ane]])
        
        
        
            
        if (kidney_prediction[0] == 1):
            
            kidney_diagnosis = 'The person is having Kidney Problem'
        else:
            
            kidney_diagnosis = 'The person does not have Kidney Problem'
        
        
    st.success(kidney_diagnosis)
