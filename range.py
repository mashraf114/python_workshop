def checkRange(num):
  if num in range(-5,5):
    print("Number is in range")
    return True
  else:
    print("Number is not in range")
    return False
num = int(input("Enter a number: "))
checkRange(num)