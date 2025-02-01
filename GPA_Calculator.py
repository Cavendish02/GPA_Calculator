import streamlit as st

# Define grade points for the new system
grades_new = {
    'A+': 4, 'A': 3.7, 'A-': 3.4, 'B+': 3.2, 'B': 3, 'B-': 2.8, 'C+': 2.6, 'C': 2.4, 'C-': 2.2, 'D+': 2, 'D': 1.5, 'D-': 1, 'F': 0
}

# Function to calculate current semester GPA
def calculate_current_semester_gpa():
    total_points = 0
    total_hours = 0
    has_failed = False
    subject_number = 1

    while True:
        grade = st.text_input(f"Enter letter grade for subject {subject_number} (A+, A, A-, B+, B, B-, C+, C, C-, D+, D, D-, F): ")
        if not grade:
            break
        grade = grade.upper()
        hours = st.number_input(f"Enter the number of hours for subject {subject_number}: ", min_value=1)
        total_points += grades_new.get(grade, 0) * hours
        total_hours += hours
        if grade == 'F':
            has_failed = True

        stop = st.selectbox("Do you want to stop entering subjects?", ["No", "Yes"])
        if stop == "Yes":
            break

        subject_number += 1

    if total_hours == 0:
        st.warning("You did not enter any subjects.")
    else:
        current_gpa = total_points / total_hours
        if has_failed:
            st.error(f"Sorry, you have failed one or more subjects. Your GPA is: {round(current_gpa, 2)}")
        else:
            st.success(f"Your GPA for the current semester is: {round(current_gpa, 2)}")

# Function to calculate CGPA over multiple semesters
def calculate_total_gpa(previous_gpa, previous_semesters, current_gpa, current_semesters):
    total_gpa = (previous_gpa * previous_semesters + current_gpa) / current_semesters
    return round(total_gpa, 3)

def calculate_total_semesters_gpa():
    current_gpa = st.number_input("Enter the GPA for the current semester: ", min_value=0.0, max_value=4.0)
    previous_gpa = st.number_input("Enter the total previous GPA: ", min_value=0.0, max_value=4.0)
    previous_semesters = st.number_input("Enter the number of previous semesters: ", min_value=1)
    num_semesters = previous_semesters + 1
    total_gpa = calculate_total_gpa(previous_gpa, previous_semesters, current_gpa, num_semesters)

    st.write(f"Your GPA over {num_semesters} semesters is: {total_gpa}")

def main():
    system_choice = st.selectbox("Choose your grading system:", ["New System", "Old System"])

    if system_choice == "New System":
        st.subheader("Calculate GPA for the new system")
        calculate_current_semester_gpa()
        st.write("Made in Earth By Mohammed Hassan")
    elif system_choice == "Old System":
        st.subheader("Calculate GPA for the old system")
        calculate_current_semester_gpa()
        st.write("Made in Earth By Mohammed Hassan")

if __name__ == "__main__":
    st.title("GPA Calculator - Faculty of Artificial Intelligence, Kafr El-Sheikh University")
    main()
