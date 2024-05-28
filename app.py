import streamlit as st
from streamlit_option_menu import option_menu
import pickle

# Loading the saved models
model_paths = {
    'Cancer_model': 'Saved/cancer_model.sav',
    'Heart_model': 'Saved/Heart_model.sav',
    'Kidney_model': 'Saved/kidney_model.sav',
    'Liver_model': 'Saved/liver_model.sav',
    'Diabetes_model': 'Saved/diabetes_model.sav'
}

models = {}
for model_name, path in model_paths.items():
    try:
        models[model_name] = pickle.load(open(path, 'rb'))
    except FileNotFoundError as e:
        st.error(f"Error loading {model_name}: {e}")

# Sidebar for Navigation
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Home', 'Cancer Prediction', 'Heart Disease Prediction', 'Diabetes Prediction', 'Liver Disease Prediction', 'Kidney Prediction'],
        icons=['house', 'hospital', 'heart', 'activity', 'droplet', 'capsule'],
        default_index=0
    )

# CSS for custom styles
st.markdown(
    """
    <style>
    .main {
        background-image: url('https://i.postimg.cc/905SCbGL/bg1.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-color: rgba(255, 255, 255, 0.8);
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
        color: black;
        margin-top: 20px;
    }
    .content {
        font-size: 20px;
        color: black;
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

    diseases_info = {
        "Cancer": {
            "image": "https://i.postimg.cc/Y98nKRyK/Cancer.jpg",
            "description": "Cancer is a group of diseases characterized by the uncontrolled growth and spread of abnormal cells. If the spread is not controlled, it can result in death.",
            "symptoms": [
                "Changes in bowel or bladder habits", 
                "A sore that does not heal",
                "Unusual bleeding or discharge",
                "Thickening or lump in the breast or other parts of the body",
                "Indigestion or difficulty swallowing",
                "Recent change in a wart or mole"
            ]
        },
        "Heart Disease": {
            "image": "https://i.postimg.cc/Qxzzd6Nj/Heart.jpg",
            "description": "Heart disease refers to various types of conditions that can affect heart function, including coronary artery disease, arrhythmias, and heart defects among others.",
            "symptoms": [
                "Chest pain or discomfort", 
                "Shortness of breath",
                "Pain, numbness, weakness, or coldness in your legs or arms if the blood vessels in those parts of your body are narrowed",
                "Pain in the neck, jaw, throat, upper abdomen, or back"
            ]
        },
        "Diabetes": {
            "image": "https://i.postimg.cc/jSNMdtkh/Diabetes.jpg",
            "description": "Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy. Most of the food you eat is broken down into sugar (glucose) and released into your bloodstream.",
            "symptoms": [
                "Increased thirst", 
                "Frequent urination",
                "Extreme hunger",
                "Unexplained weight loss",
                "Presence of ketones in the urine",
                "Fatigue",
                "Irritability",
                "Blurred vision"
            ]
        },
        "Liver Disease": {
            "image": "https://i.postimg.cc/1zrMwMSn/Liver.jpg",
            "description": "Liver disease is a broad term that covers all the potential problems that cause the liver to fail to perform its designated functions. Usually, more than 75% or three quarters of liver tissue needs to be affected before a decrease in function occurs.",
            "symptoms": [
                "Yellowing of the skin and eyes (jaundice)",
                "Pain and swelling in the abdomen",
                "Swelling in the legs and ankles",
                "Itchy skin",
                "Dark urine color",
                "Pale-colored stool",
                "Chronic fatigue"
            ]
        },
        "Kidney Disease": {
            "image": "https://i.postimg.cc/L4bDtncT/Kidney.jpg",
            "description": "Kidney disease means your kidneys are damaged and can't filter blood the way they should. This can cause wastes to build up in your body and other problems that can harm your health.",
            "symptoms": [
                "Nausea",
                "Vomiting",
                "Loss of appetite",
                "Fatigue and weakness",
                "Sleep problems",
                "Changes in how much you urinate",
                "Decreased mental sharpness",
                "Muscle twitches and cramps",
                "Swelling of feet and ankles"
            ]
        }
    }

    for disease, info in diseases_info.items():
        st.markdown(f"""
        <div class="container">
            <img src="{info['image']}" alt="{disease}" style="width:500px;height:auto;">
            <div>
                <h3 class='subtitle'>{disease}</h3>
                <div class='content'>{info['description']}</div>
                <ul class='content'>
                    {''.join(f"<li>{symptom}</li>" for symptom in info['symptoms'])}
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)

def render_input_form(input_labels):
    inputs = {}
    for label in input_labels:
        inputs[label] = st.text_input(f"**{label}**")
    return inputs

def predict_disease(model, input_data):
    try:
        input_values = [float(value) for value in input_data.values()]
        prediction = model.predict([input_values])
        return prediction[0] == 1
    except ValueError:
        st.error("Please enter valid numeric values for all fields.")
        return None

# Prediction Pages
if selected == 'Cancer Prediction':
    st.title('Cancer Prediction using ML')
    input_labels = [
        'Radius_mean', 'Texture_mean', 'Perimeter_mean', 'Area_mean',
        'Smoothness_mean', 'Compactness_mean', 'Concavity_mean', 'Concave_points_mean',
        'Symmetry_mean', 'Radius_se', 'Perimeter_se', 'Area_se', 'Compactness_se',
        'Concavity_se', 'Concave_points_se', 'Fractal_dimension_se', 'Radius_worst',
        'Texture_worst', 'Perimeter_worst', 'Area_worst', 'Smoothness_worst',
        'Compactness_worst', 'Concavity_worst', 'Concave_points_worst',
        'Symmetry_worst', 'Fractal_dimension_worst'
    ]
    input_data = render_input_form(input_labels)
    if st.button('**Cancer Test Result**'):
        model = models.get('Cancer_model')
        if model and predict_disease(model, input_data):
            st.success('**The person is having Cancer**')
        else:
            st.success('**The person does not have Cancer**')

if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    input_labels = [
        'Age', 'Sex', 'Chest Pain types', 'Resting Blood Pressure',
        'Serum Cholestoral in mg/dl', 'Fasting Blood Sugar > 120 mg/dl',
        'Resting Electrocardiographic results', 'Maximum Heart Rate achieved',
        'Exercise Induced Angina', 'ST depression induced by exercise',
        'Slope of the peak exercise ST segment', 'Major vessels colored by flourosopy',
        'Thalium stress result'
    ]
    input_data = render_input_form(input_labels)
    if st.button('Heart Disease Test Result'):
        model = models.get('Heart_model')
        if model and predict_disease(model, input_data):
            st.success('**The person is having Heart Disease**')
        else:
            st.success('**The person does not have Heart Disease**')

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    input_labels = [
        'Number of Pregnancies', 'Glucose Level', 'Blood Pressure value', 'Skin Thickness value',
        'Insulin Level', 'BMI value', 'Diabetes Pedigree Function value', 'Age of the Person'
    ]
    input_data = render_input_form(input_labels)
    if st.button('Diabetes Test Result'):
        model = models.get('Diabetes_model')
        if model and predict_disease(model, input_data):
            st.success('**The person is Diabetic**')
        else:
            st.success('**The person is not Diabetic**')

if selected == 'Liver Disease Prediction':
    st.title('Liver Disease Prediction using ML')
    input_labels = [
        'Age', 'Gender', 'Total Bilirubin', 'Direct Bilirubin', 'Alkaline Phosphotase', 'Alamine Aminotransferase',
        'Aspartate Aminotransferase', 'Total Protiens', 'Albumin', 'Albumin and Globulin Ratio'
    ]
    input_data = render_input_form(input_labels)
    if st.button('Liver Disease Test Result'):
        model = models.get('Liver_model')
        if model and predict_disease(model, input_data):
            st.success('**The person is having Liver Disease**')
        else:
            st.success('**The person does not have Liver Disease**')

if selected == 'Kidney Prediction':
    st.title('Kidney Disease Prediction using ML')
    input_labels = [
        'Blood Urea', 'Blood Glucose Random', 'Blood Pressure', 'Specific Gravity', 'Albumin', 'Sugar',
        'Red Blood Cells', 'Pus Cell clumps', 'Bacteria', 'Blood Glucose Fasting', 'Blood Urea Nitrogen', 'Serum Creatinine',
        'Sodium', 'Potassium', 'Hemoglobin', 'Packed Cell Volume', 'White Blood Cell Count', 'Red Blood Cell Count',
        'Hypertension', 'Diabetes Mellitus', 'Coronary Artery Disease', 'Appetite', 'Pedal Edema', 'Anemia'
    ]
    input_data = render_input_form(input_labels)
    if st.button('Kidney Disease Test Result'):
        model = models.get('Kidney_model')
        if model and predict_disease(model, input_data):
            st.success('**The person is having Kidney Disease**')
        else:
            st.success('**The person does not have Kidney Disease**')
