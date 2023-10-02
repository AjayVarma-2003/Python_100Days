# Write your code here 👇
target = 100
for numbers in range (1, target+1):
  if numbers % 3 == 0 and numbers % 5 == 0:
    print("FizzBuzz")
  elif numbers % 3 == 0:
    print("Fizz")
  elif numbers % 5 == 0:
    print("Buzz")
  else:
    print(numbers)