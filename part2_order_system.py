student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

print(f"\nReport Card for {student_name}\n")

# Grade function
def get_grade(m):
    if 90 <= m <= 100:
        return "A+"
    elif 80 <= m <= 89:
        return "A"
    elif 70 <= m <= 79:
        return "B"
    elif 60 <= m <= 69:
        return "C"
    else:
        return "F"

# Print subject, marks, grade
for i in range(len(subjects)):
    print(f"{subjects[i]} : {marks[i]} ({get_grade(marks[i])})")

# Calculations
total = sum(marks)
average = round(total / len(marks), 2)

# Highest & Lowest
max_marks = max(marks)
min_marks = min(marks)

max_index = marks.index(max_marks)
min_index = marks.index(min_marks)


print(f"Total Marks : {total}")
print(f"Average Marks : {average}")
print(f"Highest Scoring Subject : {subjects[max_index]} ({max_marks})")
print(f"Lowest Scoring Subject : {subjects[min_index]} ({min_marks})")


# ---- While Loop: Add new subjects ----
new_count = 0

print("\nAdd new subjects (type 'done' to stop):")

while True:
    sub = input("Enter subject name: ")
    
    if sub.lower() == "done":
        break
    
    marks_input = input("Enter marks (0-100): ")
    
    # Validation
    if not marks_input.isdigit():
        print("Invalid input! Marks must be numeric.")
        continue
    
    m = int(marks_input)
    
    if m < 0 or m > 100:
        print("Marks should be between 0 and 100.")
        continue
    
    # Add valid data
    subjects.append(sub)
    marks.append(m)
    new_count += 1


# Final output
updated_avg = round(sum(marks) / len(marks), 2)

print("\nFinal Summary:")
print(f"New Subjects Added : {new_count}")
print(f"Updated Average    : {updated_avg}") 
