students = {
    "Aman": [85, 92, 78],
    "Riya": [95, 88, 91],
    "Karan": [72, 65, 80],
    "Simran": [45, 92, 88],
    "Raj": [90, 91, 95]
}

eligible_for_scholarship = 0
highest_avg = 0.0
highest_scorer = ""

for student, marks in students.items():
    total_marks = 0
    subject_count = 0
    failed_any = False
    all_above_85 = True

    for mark in marks:
        if mark < 40:
            failed_any = True
        if mark < 85:
            all_above_85 = False
        total_marks += mark
        subject_count += 1
        
    avg = total_marks / subject_count
    
    if failed_any:
        status = "Failed"
    elif avg >= 90 and all_above_85:
        status = "Scholarship"
        eligible_for_scholarship += 1
    elif avg > 80:
        status = "Distinction"
    elif avg >= 60:
        status = "Pass"
    else:
        status = "Needs Improvement"
        
    print(f"{student}: {status}")

    if avg > highest_avg:
        highest_avg = avg
        highest_scorer = student

print(f"Total students eligible for scholarship: {eligible_for_scholarship}")
print(f"Highest average marks: {highest_avg}")
print(f"Highest scorer: {highest_scorer}")