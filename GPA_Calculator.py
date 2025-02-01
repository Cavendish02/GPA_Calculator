import streamlit as st

# Define grade points for the old system
grades_old = {
    'A+': 4, 'A': 3.7, 'A-': 3.4, 'B+': 3.2, 'B': 3, 'B-': 2.8, 'C+': 2.6, 'C': 2.4, 'C-': 2.2, 'D+': 2, 'D': 1.5, 'D-': 1, 'F': 0
}

# Define grade points for the new system
grades_new = {
    'A+': 4, 'A': 3.7, 'A-': 3.4, 'B+': 3.2, 'B': 3, 'B-': 2.8, 'C+': 2.6, 'C': 2.4, 'C-': 2.2, 'D+': 2, 'D': 1.5, 'D-': 1, 'F': 0
}

# Function to calculate GPA
def calculate_gpa(grades_dict):
    total_points = 0
    total_hours = 0
    has_failed = False
    subject_number = 1

    while True:
        # User input for grade
        grade = st.text_input(f"Enter letter grade for subject {subject_number} (A+, A, A-, B+, B, B-, C+, C, C-, D+, D, D-, F): ")
        if grade == "":
            break
        grade = grade.upper()
        
        # User input for credit hours
        hours = st.number_input(f"Enter the number of hours for subject {subject_number}: ", min_value=1)

        # Update total points and total hours
        total_points += grades_dict.get(grade, 0) * hours
        total_hours += hours
        
        # Check for failure in any subject
        if grade == 'F':
            has_failed = True

        subject_number += 1

        # Button to stop adding subjects
        stop = st.selectbox("Do you want to stop entering subjects?", ["No", "Yes"])
        if stop == "Yes":
            break
    
    if total_hours == 0:
        st.warning("You did not enter any subjects.")
    else:
        current_gpa = total_points / total_hours
        if has_failed:
            st.error(f"Sorry, you have failed one or more subjects. Your GPA is: {round(current_gpa, 2)}")
        else:
            st.success(f"Your GPA for the current semester is: {round(current_gpa, 2)}")

# Function to calculate CGPA
def calculate_cgpa(previous_gpa, previous_semesters, current_gpa, current_semesters):
    total_gpa = (previous_gpa * previous_semesters + current_gpa) / current_semesters
    return round(total_gpa, 3)

# Main function to display everything on the same page
def main():
    st.title("GPA Calculator - Faculty of Artificial Intelligence, Kafr El-Sheikh University")
    
    # Select the system
    system_choice = st.selectbox("Choose your grading system:", ["New System", "Old System"])

    # Handle system choice
    if system_choice == "Old System":
        st.subheader("Calculate GPA for the old system")
        calculate_gpa(grades_old)
        st.write("Made in Earth By Mohammed Hassan")
        
        st.subheader("CGPA Calculation")
        current_gpa = st.number_input("Enter the GPA for the current semester: ", min_value=0.0, max_value=4.0)
        previous_gpa = st.number_input("Enter the total previous GPA: ", min_value=0.0, max_value=4.0)
        previous_semesters = st.number_input("Enter the number of previous semesters: ", min_value=1)
        num_semesters = previous_semesters + 1
        total_gpa = calculate_cgpa(previous_gpa, previous_semesters, current_gpa, num_semesters)

        st.write(f"Your GPA over {num_semesters} semesters is: {total_gpa}")
        
    elif system_choice == "New System":
        st.subheader("Calculate GPA for the new system")
        calculate_gpa(grades_new)
        st.write("Made in Earth By Mohammed Hassan")
        
        st.subheader("CGPA Calculation")
        current_gpa = st.number_input("Enter the GPA for the current semester: ", min_value=0.0, max_value=4.0)
        previous_gpa = st.number_input("Enter the total previous GPA: ", min_value=0.0, max_value=4.0)
        previous_semesters = st.number_input("Enter the number of previous semesters: ", min_value=1)
        num_semesters = previous_semesters + 1
        total_gpa = calculate_cgpa(previous_gpa, previous_semesters, current_gpa, num_semesters)

        st.write(f"Your GPA over {num_semesters} semesters is: {total_gpa}")

if __name__ == "__main__":
    main()
