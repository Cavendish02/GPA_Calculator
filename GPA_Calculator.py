import streamlit as st

# Define grade points
grades = {'A+': 4, 'A': 3.7, 'B+': 3.3, 'B': 3, 'C+': 2.7, 'C': 2.4, 'D+': 2, 'D': 1.7, 'F': 0}

# Function to calculate current semester GPA
def calculate_current_gpa(grades_list):
    total_points = sum(grade * hours for grade, hours in grades_list)
    total_hours = sum(hours for _, hours in grades_list)
    return round(total_points / total_hours, 2) if total_hours > 0 else 0

# Function to calculate CGPA
def calculate_cgpa(previous_gpas):
    return round(sum(previous_gpas) / len(previous_gpas), 2) if previous_gpas else 0

# Streamlit UI
st.title("📊 GPA & CGPA Calculator")

# Sidebar for navigation
option = st.sidebar.radio("Select Calculation Type:", ["Cumulative GPA (CGPA)", "Current Semester GPA"])

# CGPA Calculation
if option == "Cumulative GPA (CGPA)":
    st.subheader("🔢 Enter Your Previous Semester GPAs")
    
    num_semesters = st.number_input("How many semesters have you completed?", min_value=1, step=1, value=1)
    
    gpas = []
    for i in range(num_semesters):
        gpa = st.number_input(f"Enter GPA for Semester {i+1}", min_value=0.0, max_value=4.0, step=0.01, key=f"gpa_{i}")
        gpas.append(gpa)
    
    if st.button("📊 Calculate CGPA"):
        if len(gpas) > 0:
            cgpa = calculate_cgpa(gpas)
            st.success(f"📌 Your Cumulative GPA (CGPA) is: **{cgpa}**")

# Current Semester GPA Calculation
elif option == "Current Semester GPA":
    st.subheader("🎯 Enter Your Grades & Credit Hours")

    grades_list = []
    subject_count = st.number_input("Number of subjects:", min_value=1, step=1, value=1)

    for i in range(subject_count):
        grade = st.selectbox(f"Select Grade for Subject {i+1}", list(grades.keys()), key=f"grade_{i}")
        hours = st.number_input(f"Enter Credit Hours for Subject {i+1}", min_value=1, step=1, value=3, key=f"hours_{i}")
        grades_list.append((grades[grade], hours))

    if st.button("🎯 Calculate Semester GPA"):
        current_gpa = calculate_current_gpa(grades_list)
        st.success(f"📌 Your GPA for this semester is: **{current_gpa}**")
