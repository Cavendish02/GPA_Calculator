import streamlit as st

grades = {'A+': 4, 'A': 3.7, 'B+': 3.3, 'B': 3, 'C+': 2.7, 'C': 2.4, 'D+': 2, 'D': 1.7, 'F': 0}

def calculate_total_gpa(previous_gpa, previous_semesters, current_gpa, current_semesters):
    return round((previous_gpa * previous_semesters + current_gpa * current_semesters) / (previous_semesters + current_semesters), 3)

def calculate_current_semester_gpa(subjects):
    total_points = 0
    total_hours = 0
    has_failed = False

    for subject in subjects:
        grade = subject['grade']
        hours = subject['hours']
        total_points += grades.get(grade, 0) * hours
        total_hours += hours
        if grade == 'F':
            has_failed = True

    if total_hours == 0:
        return None, has_failed
    return total_points / total_hours, has_failed

st.title("📊 GPA Calculator")

option = st.radio("Select an option:", ["🎓 Calculate GPA for Current Semester", "📈 Calculate Cumulative GPA (CGPA)"])

if option == "🎓 Calculate GPA for Current Semester":
    st.subheader("📚 Enter Subject Details:")
    num_subjects = st.number_input("Number of subjects", min_value=1, step=1, value=1)
    
    subjects = []
    for i in range(num_subjects):
        col1, col2 = st.columns(2)
        with col1:
            grade = st.selectbox(f"Grade for Subject {i+1}:", list(grades.keys()), key=f"grade_{i}")
        with col2:
            hours = st.number_input(f"Credit Hours for Subject {i+1}:", min_value=1, step=1, value=3, key=f"hours_{i}")
        
        subjects.append({"grade": grade, "hours": hours})

    if st.button("🔍 Calculate Semester GPA"):
        gpa, failed = calculate_current_semester_gpa(subjects)
        if gpa is not None:
            st.success(f"📌 Your Semester GPA is: **{round(gpa, 2)}**")
            if failed:
                st.warning("⚠ You have failed one or more subjects.")

elif option == "📈 Calculate Cumulative GPA (CGPA)":
    st.subheader("📊 Enter Previous Semester Details:")
    previous_gpa = st.number_input("Previous Cumulative GPA (CGPA)", min_value=0.0, max_value=4.0, step=0.01)
    previous_semesters = st.number_input("Number of Previous Semesters", min_value=0, step=1, value=1)
    current_gpa = st.number_input("Current Semester GPA", min_value=0.0, max_value=4.0, step=0.01)

    if st.button("📊 Calculate CGPA"):
        if previous_semesters >= 0:
            total_gpa = calculate_total_gpa(previous_gpa, previous_semesters, current_gpa, 1)
            st.success(f"📌 Your Cumulative GPA after {previous_semesters + 1} semesters is: **{total_gpa}**")
        else:
            st.error("⚠ Number of previous semesters must be a non-negative integer.")
