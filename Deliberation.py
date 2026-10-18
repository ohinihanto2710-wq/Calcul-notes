name=input("Enter your name: ")
print("Hello, " + name + "! Welcome to the marks evaluation program.")
marks=int(input("Enter your marks: "))
print("Your marks are: " + str(marks))
if marks >= 100:
    print("Excellent! You have scored full marks.")
elif marks >= 90:
    print("Great job! You have scored an A grade.")
elif marks >= 80:
    print("Good effort! You have scored a B grade.")
elif marks >= 70:
    print("You have scored a C grade. Keep working hard!")
elif marks >= 60:
    print("You have scored a D grade. Don't give up!")
elif marks >= 50:
    print("You have scored an E grade. You need to improve.")
elif marks >= 40:
    print("You have scored an F grade. You need to work harder.")
elif marks >= 30:
    print("You have scored a G grade. Consider seeking help to improve your performance.")
else:
    print("You have scored below average. Consider seeking help to improve your performance.")