# gradebook.py
# Name: Prachi kumari
# Date: 02-11-2025
# Title: GradeBook Analyzer - Manual Input Version

def print_menu():
    print("\nGradeBook Analyzer")
    print("1. Enter student data manually")
    print("2. Exit")

def manual_input():
    marks = {}
    while True:
        name = input("Enter student name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        try:
            score = float(input(f"Enter marks for {name}: "))
            marks[name] = score
        except ValueError:
            print("Invalid input. Try again.")
    return marks

def calculate_average(marks):
    return sum(marks.values()) / len(marks)

def calculate_median(marks):
    scores = sorted(marks.values())
    n = len(scores)
    mid = n // 2
    return scores[mid] if n % 2 else (scores[mid - 1] + scores[mid]) / 2

def find_max_score(marks):
    return max(marks.values())

def find_min_score(marks):
    return min(marks.values())

def assign_grades(marks):
    grades = {}
    for name, score in marks.items():
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'
        grades[name] = grade
    return grades

def grade_distribution(grades):
    dist = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for grade in grades.values():
        dist[grade] += 1
    return dist

def pass_fail_lists(marks):
    passed = [name for name, score in marks.items() if score >= 40]
    failed = [name for name, score in marks.items() if score < 40]
    return passed, failed

def print_results_table(marks, grades):
    print("\nName\t\tMarks\tGrade")
    print("-" * 30)
    for name in marks:
        print(f"{name:<10}\t{marks[name]:<6}\t{grades[name]}")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            marks = manual_input()
            if not marks:
                print("No data entered.")
                continue

            avg = calculate_average(marks)
            med = calculate_median(marks)
            max_score = find_max_score(marks)
            min_score = find_min_score(marks)

            print(f"\nAverage: {avg:.2f}")
            print(f"Median: {med:.2f}")
            print(f"Highest: {max_score}")
            print(f"Lowest: {min_score}")

            grades = assign_grades(marks)
            dist = grade_distribution(grades)
            print("\nGrade Distribution:")
            for grade, count in dist.items():
                print(f"{grade}: {count}")

            passed, failed = pass_fail_lists(marks)
            print(f"\nPassed ({len(passed)}): {', '.join(passed)}")
            print(f"Failed ({len(failed)}): {', '.join(failed)}")

            print_results_table(marks, grades)

        elif choice == '2':
            print("Exiting GradeBook Analyzer.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()