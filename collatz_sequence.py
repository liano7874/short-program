def collatz(number):
  if number % 2 == 0:
    value = number // 2
    return value
  elif number % 2 == 1:
    value = 3 * number + 1
    return value


print("Enter number:")
while True:
  try:
    user_input = int(input())
  except ValueError:
    print("You must enter an integer")
    continue

  result = collatz(user_input)
  print(result)
  if result == 1:
    break
