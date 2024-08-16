                                                        Grade Tracker

● Overview:

The Grade Tracker is a Python application designed to manage and calculate student grades. 
It allows users to input subject grades, calculate the overall percentage, assign a grade based on the percentage, and compute the GPA. 
The results are displayed to the user and saved to a CSV file.

● Features:
  - Input Student Data: Enter student name and grades for multiple subjects.
  - Show Subject Grades: Display subject names, obtained marks, and grades.
  - Calculate Average Grade: Compute the overall grade based on the percentage.
  - Calculate GPA: Compute the GPA based on the percentage.
  - Save Data: Append student results to a CSV file for record-keeping.


● Installation:

1. Clone the repository:
    `
    git clone https://github.com/yourusername/your-repository.git
    `

2. Navigate to the project directory:
    `
    cd your-repository
    `

3. Ensure you have Python installed: (Python 3.x recommended).

● Usage

1. Run the Program:
    `
    python studentGradeTracker.py
    `

2. Follow the prompts:
    - Enter the student's name.
    - Input the number of subjects.
    - For each subject, provide the subject name and marks obtained.

3. View the Results:
    - The program will display the subject grades, overall grade, percentage, and GPA.
    - Results will be saved to `studentgradefile.csv` in the same directory.

● Code Explanation:
Grade_Tracker Class

- `__init__()`: Initializes the class and calls the `main()` method.
- `take_data()`: Collects student name and grades for each subject.
- `subject_grades_show()`: Displays grades for each subject with their respective grade.
- `average_grade()`: Computes the overall grade based on the percentage.
- `GPA()`: Computes the GPA based on the percentage.
- `show_data()`: Displays student details, subject grades, overall grade, percentage, and GPA.
- `main()`: Main method that orchestrates data collection, display, and saving.
- `save()`: Saves student results to a CSV file.

● CSV File:
The results are saved to `studentgradefile.csv` with the following format:

Student name: [Student Name]
Subject-grade: [Subject Grades Dictionary]
Overall Grade: [Overall Grade]
Percentage: [Percentage]
GPA: [GPA]

Feel free to adjust or modify Student grade tracker as you see fit!
