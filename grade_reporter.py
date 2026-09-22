scores = [72, 45, 90, 61, 38]

pass_count = 0
fail_count = 0
total_score = 0

for score in scores:
    total_score += score 
    
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
        
    # Print each score with its grade on its own line.
    print(f"Score: {score} - Grade: {grade}")
    
    # Count how many learners passed and failed
    if score >= 50:
        pass_count += 1
    else:
        fail_count += 1

    # Print the final pass/fail counts
print(f"\nNumber of learners who passed: {pass_count}")
print(f"Number of learners who failed: {fail_count}")

    # Add up all the scores and print the average, rounded to one decimal place
average = total_score / len(scores)
print(f"Average score: {round(average, 1)}")