import streamlit as st

# Grade to GPA mapping (for the old system)
grades_old = {'A+': 4, 'A': 3.7, 'B+': 3.3, 'B': 3, 'C+': 2.7, 'C': 2.4, 'D+': 2, 'D': 1.7, 'F': 0}

# Function to calculate semester GPA for the old system
def calculate_current_gpa(grades_list, grades_mapping):
    total_points = sum(grade * hours for grade, hours in grades_list)
    total_hours = sum(hours for _, hours in grades_list)
    return round(total_points / total_hours, 2) if total_hours > 0 else 0

# Function to calculate CGPA for the old system
def calculate_cgpa(previous_gpas):
    return round(sum(previous_gpas) / len(previous_gpas), 2) if previous_gpas else 0

# Page settings
st.set_page_config(page_title="GPA Calculator", layout="centered")

# Title
st.title("📊 GPA Calculator")

# Description
st.markdown("""
    This GPA calculator is specifically designed for the **Faculty of Artificial Intelligence**,  
    **Kafr El-Sheikh University**. Choose your grading system (Old or New) and calculate your GPA.
""")

# Choose between systems
system_option = st.radio("Choose Grading System:", ["Old System (Old Grading Scheme)", "New System (New Grading Scheme)"])

# Show content based on system choice
if system_option == "Old System (Old Grading Scheme)":
    st.subheader("📌 Old System GPA Calculation")
    
    # Option for GPA Calculation
    option = st.radio("Choose an option:", ["Calculate Semester GPA", "Calculate Cumulative GPA (CGPA)"])

    if option == "Calculate Semester GPA":
        st.subheader("📌 Calculate Your Current Semester GPA")
        grades_list = []
        subject_count = st.number_input("Number of subjects:", min_value=1, step=1, value=1)

        for i in range(subject_count):
            grade = st.selectbox(f"Grade for Subject {i+1}:", list(grades_old.keys()), key=f"grade_{i}")
            hours = st.number_input(f"Credit Hours for Subject {i+1}:", min_value=1, step=1, value=3, key=f"hours_{i}")
            grades_list.append((grades_old[grade], hours))

        if st.button("Calculate GPA"):
            current_gpa = calculate_current_gpa(grades_list, grades_old)
            st.success(f"🎯 Your GPA for this semester is: **{current_gpa}**")

    elif option == "Calculate Cumulative GPA (CGPA)":
        st.subheader("📌 Calculate Your Cumulative GPA")
        num_semesters = st.number_input("How many semesters have you completed?", min_value=1, step=1, value=1)

        gpas = []
        for i in range(num_semesters):
            gpa = st.number_input(f"Enter GPA for Semester {i+1}:", min_value=0.0, max_value=4.0, step=0.01, key=f"gpa_{i}")
            gpas.append(gpa)

        if st.button("Calculate CGPA"):
            if len(gpas) > 0:
                cgpa = calculate_cgpa(gpas)
                st.success(f"🎯 Your Cumulative GPA (CGPA) is: **{cgpa}**")

elif system_option == "New System (New Grading Scheme)":
    st.subheader("📌 New System GPA Calculation (Coming Soon!)")
    st.markdown("The GPA calculation for the new system will be added soon. Stay tuned!")

# Footer
st.markdown("""
    <br><br>
    <hr>
    <center>Made in Earth By Mohammed Hassan</center>
""", unsafe_allow_html=True)
