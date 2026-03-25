import matplotlib.pyplot as plt
import csv
import os

def save_to_csv(name, total, percentage, grade):
    file_exists = os.path.isfile('student_records.csv')
    with open('student_records.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        # Add a header if the file is new
        if not file_exists:
            writer.writerow(['Name', 'Total Marks', 'Percentage', 'Grade'])
        writer.writerow([name, total, f"{percentage:.2f}%", grade])

def main():
    print("--- null-pointer-dark | Student Analysis System ---")
    
    try:
        name = input("Enter Student Name: ")
        # Using the subjects you studied in Class 12
        subjects = ['Mathematics', 'Informatics Practices', 'Physics']
        marks = []

        for sub in subjects:
            score = float(input(f"Enter marks for {sub} (0-100): "))
            if 0 <= score <= 100:
                marks.append(score)
            else:
                print("Error: Marks must be between 0 and 100.")
                return

        total = sum(marks)
        percentage = (total / 300) * 100
        
        # Grading Logic
        if percentage >= 90: grade = "A+"
        elif percentage >= 75: grade = "A"
        elif percentage >= 60: grade = "B"
        else: grade = "C/Pass"

        print(f"\nProcessing results for {name}...")
        print(f"Total: {total}/300 | Percentage: {percentage:.2f}% | Grade: {grade}")

        # 1. Save Data to CSV
        save_to_csv(name, total, percentage, grade)
        print("✔ Data exported to student_records.csv")

        # 2. Generate Visualization
        plt.style.use('dark_background') # Matches your 'dark' aesthetic
        plt.bar(subjects, marks, color=['#1abc9c', '#3498db', '#9b59b6'])
        plt.ylabel('Score')
        plt.title(f'Academic Profile: {name}')
        plt.ylim(0, 105)
        
        print("\nDisplaying Performance Graph...")
        plt.show()

    except ValueError:
        print("Invalid input! Please enter numbers for marks.")

if __name__ == "__main__":
    main()
2
