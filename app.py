import streamlit as st
import joblib


# ============================================================
# LOAD MODEL
# ============================================================

model = joblib.load("healthguard_model.pkl")


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="HealthGuard AI",
    page_icon="🩺",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title("🩺 HealthGuard AI")

st.subheader(
    "AI-Based Health Risk Prediction & Doctor Consultation Platform"
)

st.write(
    "HealthGuard AI is a healthcare support platform that helps "
    "users understand symptoms, assess potential health risks, "
    "and find appropriate healthcare support."
)

st.warning(
    "⚠️ HealthGuard AI is an AI-assisted screening and information "
    "tool. It does not provide a medical diagnosis."
)


# ============================================================
# FEATURES
# ============================================================

st.header("What can HealthGuard AI do?")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🤖 AI Screening")
    st.write(
        "Assess selected health information and estimate "
        "potential health risk."
    )

with col2:
    st.subheader("📊 Health Dashboard")
    st.write(
        "View health assessment results in a simple "
        "and understandable format."
    )

with col3:
    st.subheader("👨‍⚕️ Doctor Consultation")
    st.write(
        "Find doctors and explore consultation "
        "and appointment options."
    )


# ============================================================
# AI HEALTH SCREENING
# ============================================================

st.header("🤖 AI Health Screening")

st.write(
    "Enter your basic health information below. "
    "HealthGuard AI will use selected information for "
    "a health-risk screening."
)


# ============================================================
# PERSONAL INFORMATION
# ============================================================

st.subheader("👤 Personal Information")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=25,
        step=1
    )

with col2:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )


# ============================================================
# VITAL SIGNS
# ============================================================

st.subheader("🩺 Vital Signs")

col1, col2, col3 = st.columns(3)

with col1:
    blood_pressure = st.number_input(
        "Systolic Blood Pressure (mmHg)",
        min_value=60,
        max_value=250,
        value=120,
        step=1
    )

with col2:
    blood_sugar = st.selectbox(
        "Blood Sugar",
        ["Normal", "Low", "High"]
    )

with col3:
    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=60.0,
        value=22.0,
        step=0.1
    )

col4, col5, col6 = st.columns(3)

with col4:
    oxygen_level = st.number_input(
        "Oxygen Level (SpO₂ %)",
        min_value=70.0,
        max_value=100.0,
        value=98.0,
        step=0.1
    )

with col5:
    heart_rate = st.number_input(
        "Heart Rate (BPM)",
        min_value=30,
        max_value=220,
        value=72,
        step=1
    )

with col6:
    temperature = st.number_input(
        "Body Temperature (°C)",
        min_value=30.0,
        max_value=45.0,
        value=36.5,
        step=0.1
    )

respiratory_rate = st.number_input(
    "Respiratory Rate (breaths/min)",
    min_value=5,
    max_value=60,
    value=16,
    step=1
)


# ============================================================
# LIFESTYLE INFORMATION
# ============================================================

st.subheader("🏃 Lifestyle Information")

col1, col2, col3 = st.columns(3)

with col1:
    smoking = st.selectbox(
        "Do you smoke?",
        ["No", "Yes"]
    )

with col2:
    physical_activity = st.selectbox(
        "Physical Activity",
        ["Low", "Occasional", "Regular", "High"]
    )

with col3:
    sleep_hours = st.number_input(
        "Average Sleep Duration (hours)",
        min_value=0.0,
        max_value=24.0,
        value=7.0,
        step=0.5
    )

water_intake = st.number_input(
    "Daily Water Intake (litres)",
    min_value=0.0,
    max_value=10.0,
    value=2.0,
    step=0.1
)

exercise_frequency = st.selectbox(
    "Exercise Frequency",
    ["Never", "Occasional", "Regular", "Daily"]
)

stress_level = st.selectbox(
    "Stress Level",
    ["Low", "Moderate", "High", "Very High"]
)


# ============================================================
# SYMPTOMS
# ============================================================

st.subheader("🩹 Symptoms")

col1, col2, col3 = st.columns(3)

with col1:
    chest_pain = st.selectbox(
        "Chest Pain",
        ["No", "Yes"]
    )

with col2:
    shortness_breath = st.selectbox(
        "Shortness of Breath",
        ["No", "Yes"]
    )

with col3:
    fatigue = st.selectbox(
        "Fatigue",
        ["No", "Yes"]
    )


# ============================================================
# MEDICAL HISTORY
# ============================================================

st.subheader("📋 Medical History")

col1, col2 = st.columns(2)

with col1:
    family_history = st.selectbox(
        "Family History of Disease",
        ["No", "Yes", "Unknown"]
    )

with col2:
    medications = st.selectbox(
        "Currently Taking Medication?",
        ["No", "Yes"]
    )

allergies = st.text_input(
    "Known Allergies",
    placeholder="Example: None, dust, pollen, medicine..."
)

medical_conditions = st.text_input(
    "Existing Medical Conditions",
    placeholder="Example: None, Diabetes, Asthma..."
)


# ============================================================
# ADDITIONAL HEALTH INFORMATION
# ============================================================

st.subheader("🩺 Additional Health Information")

st.write(
    "These details are collected as additional health information. "
    "The current machine-learning model uses seven selected "
    "health features for its prediction."
)

st.write(
    "**Model inputs:** Age, BMI, Heart Rate, Systolic Blood Pressure, "
    "Glucose, Sleep Hours, and Exercise."
)


# ============================================================
# ASSESS HEALTH RISK
# ============================================================

st.divider()

if st.button("🔍 Assess Health Risk", use_container_width=True):

    # --------------------------------------------------------
    # VALIDATION
    # --------------------------------------------------------

    valid_inputs = True

    if not (1 <= age <= 120):
        st.error("Please enter a valid age between 1 and 120.")
        valid_inputs = False

    if not (10 <= bmi <= 60):
        st.error("Please enter a valid BMI between 10 and 60.")
        valid_inputs = False

    if not (30 <= heart_rate <= 220):
        st.error(
            "Please enter a valid heart rate between 30 and 220 BPM."
        )
        valid_inputs = False

    if not (60 <= blood_pressure <= 250):
        st.error(
            "Please enter a valid systolic blood pressure "
            "between 60 and 250 mmHg."
        )
        valid_inputs = False

    if not (0 <= sleep_hours <= 24):
        st.error(
            "Please enter sleep duration between 0 and 24 hours."
        )
        valid_inputs = False

    if not (0 <= water_intake <= 10):
        st.error(
            "Please enter water intake between 0 and 10 litres."
        )
        valid_inputs = False

    if not valid_inputs:
        st.stop()


    # --------------------------------------------------------
    # CONVERT BLOOD SUGAR TO NUMERIC VALUE
    # --------------------------------------------------------

    if blood_sugar == "Low":
        glucose = 60
    elif blood_sugar == "High":
        glucose = 160
    else:
        glucose = 100


    # --------------------------------------------------------
    # CONVERT EXERCISE FREQUENCY TO NUMERIC VALUE
    # --------------------------------------------------------

    if exercise_frequency == "Never":
        exercise = 0
    elif exercise_frequency == "Occasional":
        exercise = 1
    elif exercise_frequency == "Regular":
        exercise = 4
    else:
        exercise = 7


    # --------------------------------------------------------
    # MODEL INPUT
    #
    # IMPORTANT:
    # This order must match the order used while training
    # healthguard_model.pkl
    #
    # 1. Age
    # 2. BMI
    # 3. Heart Rate
    # 4. Systolic Blood Pressure
    # 5. Glucose
    # 6. Sleep
    # 7. Exercise
    # --------------------------------------------------------

    input_data = [[
        age,
        bmi,
        heart_rate,
        blood_pressure,
        glucose,
        sleep_hours,
        exercise
    ]]


    # --------------------------------------------------------
    # CHECK MODEL FEATURE COUNT
    # --------------------------------------------------------

    if hasattr(model, "n_features_in_"):

        expected_features = model.n_features_in_

        if expected_features != 7:
            st.error(
                f"Model configuration error: this model expects "
                f"{expected_features} features, but the application "
                f"is configured for 7 features."
            )
            st.stop()


    # --------------------------------------------------------
    # PREDICTION
    # --------------------------------------------------------

    try:

        prediction = model.predict(input_data)[0]

    except Exception as error:

        st.error(
            "Unable to generate the health-risk prediction."
        )

        st.code(str(error))

        st.stop()


    # --------------------------------------------------------
    # RESULT
    # --------------------------------------------------------

    if prediction == 1:
        risk_level = "Higher"
    else:
        risk_level = "Lower"


    st.success(
        "Health information submitted successfully!"
    )

    st.subheader("🩺 Health Risk Screening Result")


    if risk_level == "Higher":

        st.error(
            "🔴 Higher estimated health risk"
        )

        st.warning(
            "The screening model has identified a higher estimated "
            "risk based on the information provided."
        )

    else:

        st.success(
            "🟢 Lower estimated health risk"
        )

        st.success(
            "The screening model has identified a lower estimated "
            "risk based on the information provided."
        )


    st.info(
        "This is a preliminary AI-project screening demonstration, "
        "not a medical diagnosis. Please consult a qualified "
        "healthcare professional for medical advice."
    )


# ============================================================
# FIND A DOCTOR
# ============================================================

st.divider()

st.header("👨‍⚕️ Find a Doctor")

st.write(
    "Choose a healthcare specialist and explore available doctors."
)


# ============================================================
# DOCTOR DATA
# ============================================================

doctor_data = {

    "General Physician": [

        {
            "name": "Dr. Ananya Sharma",
            "experience": "8 years",
            "rating": "4.8/5",
            "hospital": "HealthCare Medical Center",
            "fee": "₹500"
        },

        {
            "name": "Dr. Rahul Kumar",
            "experience": "10 years",
            "rating": "4.7/5",
            "hospital": "City Care Hospital",
            "fee": "₹600"
        }

    ],

    "Cardiologist": [

        {
            "name": "Dr. Arjun Mehta",
            "experience": "12 years",
            "rating": "4.9/5",
            "hospital": "HeartCare Hospital",
            "fee": "₹800"
        },

        {
            "name": "Dr. Priya Nair",
            "experience": "9 years",
            "rating": "4.8/5",
            "hospital": "Apollo Medical Center",
            "fee": "₹750"
        }

    ],

    "Diabetologist": [

        {
            "name": "Dr. Vikram Singh",
            "experience": "11 years",
            "rating": "4.8/5",
            "hospital": "Diabetes Care Clinic",
            "fee": "₹700"
        },

        {
            "name": "Dr. Neha Patel",
            "experience": "7 years",
            "rating": "4.7/5",
            "hospital": "Wellness Hospital",
            "fee": "₹600"
        }

    ],

    "Dermatologist": [

        {
            "name": "Dr. Meera Rao",
            "experience": "9 years",
            "rating": "4.8/5",
            "hospital": "SkinCare Clinic",
            "fee": "₹650"
        },

        {
            "name": "Dr. Karan Shah",
            "experience": "8 years",
            "rating": "4.7/5",
            "hospital": "Derma Health Center",
            "fee": "₹600"
        }

    ],

    "Psychologist": [

        {
            "name": "Dr. Kavya Menon",
            "experience": "10 years",
            "rating": "4.9/5",
            "hospital": "Mind Wellness Center",
            "fee": "₹700"
        },

        {
            "name": "Dr. Rohan Das",
            "experience": "6 years",
            "rating": "4.7/5",
            "hospital": "Mental Wellness Clinic",
            "fee": "₹600"
        }

    ]
}


# ============================================================
# SELECT SPECIALTY
# ============================================================

specialty = st.selectbox(
    "🩺 Select Doctor Specialty",
    list(doctor_data.keys())
)


available_doctors = doctor_data[specialty]


doctor_names = [
    doctor["name"]
    for doctor in available_doctors
]


selected_doctor_name = st.selectbox(
    "👨‍⚕️ Select Doctor",
    doctor_names
)


selected_doctor = next(
    doctor
    for doctor in available_doctors
    if doctor["name"] == selected_doctor_name
)


# ============================================================
# DOCTOR INFORMATION
# ============================================================

st.subheader("Doctor Information")

col1, col2 = st.columns(2)

with col1:

    st.write(
        f"### 👨‍⚕️ {selected_doctor['name']}"
    )

    st.write(
        f"🩺 **Specialization:** {specialty}"
    )

    st.write(
        f"⭐ **Rating:** {selected_doctor['rating']}"
    )

    st.write(
        f"🎓 **Experience:** {selected_doctor['experience']}"
    )


with col2:

    st.write(
        f"🏥 **Hospital:** {selected_doctor['hospital']}"
    )

    st.write(
        "💻 **Consultation:** Online / In-person"
    )

    st.write(
        f"💰 **Consultation Fee:** {selected_doctor['fee']}"
    )


# ============================================================
# APPOINTMENT
# ============================================================

st.subheader("📅 Book an Appointment")

appointment_date = st.date_input(
    "Select Appointment Date"
)


appointment_time = st.selectbox(
    "Select Appointment Time",
    [
        "09:00 AM",
        "10:00 AM",
        "11:00 AM",
        "02:00 PM",
        "03:00 PM",
        "04:00 PM"
    ]
)


consultation_type = st.radio(
    "Consultation Type",
    ["💻 Online", "🏥 In-person"],
    horizontal=True
)


if st.button("📅 Book Appointment", use_container_width=True):

    st.success(
        f"Appointment booked successfully with "
        f"{selected_doctor['name']}!"
    )

    st.write(
        f"**Specialization:** {specialty}"
    )

    st.write(
        f"**Date:** {appointment_date}"
    )

    st.write(
        f"**Time:** {appointment_time}"
    )

    st.write(
        f"**Type:** {consultation_type}"
    )

    st.write(
        f"**Consultation Fee:** {selected_doctor['fee']}"
    )

    st.info(
        "This is a demonstration appointment for the "
        "HealthGuard AI project. It does not create a real "
        "hospital appointment."
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🩺 HealthGuard AI | AI-assisted health screening "
    "demonstration project | Not a medical diagnosis"
)