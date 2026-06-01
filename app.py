import streamlit as st
import pandas as pd

# Title
st.title("Student Marks Analyzer")

# Input Student Details
student_name = st.text_input("Enter Student Name")

subject1 = st.number_input("Marks in Subject 1", min_value=0, max_value=100)
subject2 = st.number_input("Marks in Subject 2", min_value=0, max_value=100)
subject3 = st.number_input("Marks in Subject 3", min_value=0, max_value=100)

# Calculate Button
if st.button("Analyze Marks"):

    # Calculate Total and Average
    total_marks = subject1 + subject2 + subject3
    average_marks = total_marks / 3

    # Determine Grade
    if average_marks >= 90:
        grade = "A"
    elif average_marks >= 75:
        grade = "B"
    elif average_marks >= 50:
        grade = "C"
    else:
        grade = "Fail"

    # Display Results
    st.header("Student Report")
    st.write("Name:", student_name)
    st.write("Total Marks:", total_marks)
    st.write("Average Marks:", round(average_marks, 2))
    st.write("Grade:", grade)

    # Create DataFrame
    marks_data = pd.DataFrame({
        "Subject": ["Subject 1", "Subject 2", "Subject 3"],
        "Marks": [subject1, subject2, subject3]
    })

    # Visualization
    st.subheader("Bar Chart")
    st.bar_chart(marks_data.set_index("Subject"))

    st.subheader("Line Chart")
    st.line_chart(marks_data.set_index("Subject"))

    # Display Table
    st.subheader("Marks Summary")
    st.dataframe(marks_data)