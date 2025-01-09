import csv

def read_grades(file_grades):
    """Read data from grades.csv and return a list of dictionaries."""
    grades = []
    with open(file_grades, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['Grade'] = int(row['Grade'])
            grades.append(row)
    return grades

def calculate_average_grades(grades):
    """Calculate the average grade for each subject."""
    subject_totals = {}
    subject_counts = {}
    for x in grades:
        subject =x['Subject']
        grade = x['Grade']

        if subject not in subject_totals:
            subject_totals[subject] = 0
            subject_counts[subject] = 0

        subject_totals[subject] += grade
        subject_counts[subject] += 1

    subject_averages = {
        subject: round(subject_totals[subject] / subject_counts[subject], 1)
        for subject in subject_totals
    }

    return subject_averages

def write_average_grades(file_path, averages):
    """Write the average grades to a new CSV file."""
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Subject', 'Average Grade'])
        for subject, avg_grade in averages.items():
            writer.writerow([subject, avg_grade])

# File paths
grades_file = 'grades.csv'
averages_file = 'average_grades.csv'

# Process the grades
grades = read_grades(grades_file)
averages = calculate_average_grades(grades)
write_average_grades(averages_file, averages)

print(f"Grades file created: {grades_file}")
print(f"Average grades have been written to: {averages_file}")