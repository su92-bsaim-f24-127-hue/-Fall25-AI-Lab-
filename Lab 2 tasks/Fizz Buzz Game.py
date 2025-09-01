import random

print("fizz buzz game start") 
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
      return "fizzbuzz"
    elif n % 3 == 0:
     return "fizz"
    elif n % 5 == 0:
     return "buzz"
    else:
     return "No"     
score = 0 
numbers = []  

for i in range(5):  
    number = random.randint(1, 100)
    numbers.append(number)   
    print("Number is", number)

    if i == 0:
        check_number = number
    else:
        check_number = numbers[-2] + number
       # print("Check number is", check_number)

    user_answer = input("Your answer: ")
    if user_answer == fizzbuzz(check_number):
        print("Correct!")
        score += 1
    else: 
        print("Incorrect!")
        break

print("Your score is", score)
print("fizz buzz game end") 