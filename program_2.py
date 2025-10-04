# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as


import random

def math_quiz():
   #Random number generation
    num1 = random.randint(1, 501)
    num2 = random.randint(1, 501)

   
    print(f"{num1} + {num2} = ?")

   
    answer = int(input("Enter your answer: "))

  
    correct_answer = num1 + num2
    if answer == correct_answer:
        print("Congratulations! That's correct!")
    else:
        print(f"Sorry that is incorrect, the correct answer is {correct_answer}.")

# program
if __name__ == "__main__":
    math_quiz()
    

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.
