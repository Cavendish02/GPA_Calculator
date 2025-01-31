import streamlit as st

grades = {'A+': 4, 'A': 3.7, 'B+': 3.3, 'B': 3, 'C+': 2.7, 'C': 2.4, 'D+': 2, 'D': 1.7, 'F': 0}

def calculate_total_gpa(previous_gpa, previous_semesters, current_gpa):
    return round((previous_gpa * previous_semesters + current_gpa) / (previous_semesters + 1), 3)

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
    st.subheader("📊 Calculate Your CGPA")

    knows_previous_gpa = st.radio("Do you know your previous CGPA?", ["No, I haven't calculated it before", "Yes, I know it"])

    if knows_previous_gpa == "No, I haven't calculated it before":
        st.subheader("🔢 Enter Previous Semesters' Grades:")
        total_gpa = 0
        total_semesters = st.number_input("How many semesters do you want to enter?", min_value=1, step=1, value=1)
        
        total_points = 0
        total_hours = 0

        for sem in range(total_semesters):
            st.write(f"📚 **Semester {sem+1}:**")
            num_subjects = st.number_input(f"Number of subjects in Semester {sem+1}", min_value=1, step=1, value=1, key=f"num_{sem}")

            for sub in range(num_subjects):
                col1, col2 = st.columns(2)
                with col1:
                    grade = st.selectbox(f"Grade for Subject {sub+1}:", list(grades.keys()), key=f"grade_{sem}_{sub}")
                with col2:
                    hours = st.number_input(f"Credit Hours for Subject {sub+1}:", min_value=1, step=1, value=3, key=f"hours_{sem}_{sub}")
                
                total_points += grades.get(grade, 0) * hours
                total_hours += hours

        if st.button("📊 Calculate Your CGPA from Scratch"):
            if total_hours == 0:
                st.warning("⚠ Please enter at least one subject.")
            else:
                cgpa = round(total_points / total_hours, 2)
                st.success(f"📌 Your Calculated CGPA is: **{cgpa}**")

    else:
        previous_gpa = st.number_input("Your Current CGPA (Before This Semester)", min_value=0.0, max_value=4.0, step=0.01)
        previous_semesters = st.number_input("How Many Semesters Have You Completed?", min_value=1, step=1, value=1)
        current_gpa = st.number_input("Your GPA This Semester", min_value=0.0, max_value=4.0, step=0.01)

        if st.button("📊 Calculate Updated CGPA"):
            total_gpa = calculate_total_gpa(previous_gpa, previous_semesters, current_gpa)
            st.success(f"📌 Your Updated CGPA after {previous_semesters + 1} semesters is: **{total_gpa}**")
