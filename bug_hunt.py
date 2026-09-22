# count = 1
# total = 0

# while count < 5
#     total = total + count
#     count = count + 1

# print("Sum of 1 to 5 is: " + total)

#DEBUGGING: The code above has a few issues that need to be fixed.
count = 1
total = 0

# BUG: Missing a colon (:) at the end of the statement, which causes a SyntaxError.
# BUG: The condition was count < 5, which stops before 5 and prints 10. Changed to count <= 5 to include 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Cannot concatenate a string and an integer (TypeError). Wrapped total in str() to fix it.
print("Sum of 1 to 5 is: " + str(total))