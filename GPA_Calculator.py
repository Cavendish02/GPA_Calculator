import streamlit as st

# Define grade points
grades = {
    'A+': 4, 'A': 3.7, 'A-': 3.4, 'B+': 3.2, 'B': 3, 'B-': 2.8, 
    'C+': 2.6, 'C': 2.4, 'C-': 2.2, 'D+': 2, 'D': 1.5, 'D-': 1, 'F': 0
}

# Function to calculate GPA
def calculate_gpa(grades_dict):
    total_points = 0
    total_hours = 0
    has_failed = False
    subject_number = 1

    st.write("### Enter Subject Details")
    while True:
        # User input for grade
        grade = st.text_input(f"Enter letter grade for subject {subject_number} (A+, A, A-, B+, B, B-, C+, C, C-, D+, D, D-, F): ", key=f"grade_{subject_number}").upper()
        
        if grade == "":
            st.warning("Please enter a grade.")
            continue
        
        if grade not in grades_dict:
            st.error("Invalid grade entered. Please enter a valid grade.")
            continue
        
        # User input for credit hours
        hours = st.number_input(f"Enter the number of hours for subject {subject_number}: ", min_value=1, key=f"hours_{subject_number}")

        # Update total points and total hours
        total_points += grades_dict.get(grade, 0) * hours
        total_hours += hours
        
        # Check for failure in any subject
        if grade == 'F':
            has_failed = True

        subject_number += 1

        # Button to stop adding subjects
        stop = st.selectbox("Do you want to stop entering subjects?", ["No", "Yes"], key=f"stop_{subject_number}")
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
    
    return current_gpa

# Function to calculate CGPA
def calculate_cgpa(previous_gpa, previous_semesters, current_gpa):
    total_gpa = (previous_gpa * previous_semesters + current_gpa) / (previous_semesters + 1)
    return round(total_gpa, 2)

# Main function to display everything on the same page
def main():
    st.title("GPA Calculator - Faculty of Artificial Intelligence, Kafr El-Sheikh University")
    
    st.write("### Choose Your Grading System")
    system_choice = st.selectbox("Select the grading system:", ["New System", "Old System"])

    st.write("### GPA Calculation")
    current_gpa = calculate_gpa(grades)
    
    st.write("---")
    st.write("### CGPA Calculation")
    if current_gpa > 0:  # Only show CGPA calculation if GPA was calculated
        previous_gpa = st.number_input("Enter your cumulative GPA from previous semesters: ", min_value=0.0, max_value=4.0)
        previous_semesters = st.number_input("Enter the number of previous semesters: ", min_value=1)
        
        if st.button("Calculate CGPA"):
            cgpa = calculate_cgpa(previous_gpa, previous_semesters, current_gpa)
            st.success(f"Your Cumulative GPA (CGPA) over {previous_semesters + 1} semesters is: {cgpa}")
    
    st.write("---")
    st.write("Made on Earth By Mohammed Hassan")

if __name__ == "__main__":
    main()