
def factorial(number, result = 1):
  if number == 1:
    return result
  else:
    return factorial(number-1, number * result)   

print(factorial(3))
print(factorial(4))
print(factorial(5))


def greatestOfThree(list):
  if list[0] > list[1]:
    if list[0] > list[2]:
      return list[0]
    else:
      return list[2]
  else:
    if list[1] > list[2]:
      return list[1]
    else:
      return list[2]


def isPrime(number):
  if number == 1:
    return False
  else:
    for i in range(2, number):
      print(i, number % i)
      if (number % i) == 0:
        return False

    return True

print(isPrime(7))


def lenOfString(string):
  return len(string)


def fibonacci(n):
  series = [None] * (n+1)
  for i in range(n+1):
    if i == 0:
      series[i] = 0
    elif i == 1:
      series[i] = 1
    else:
      series[i] = series[i-1] + series[i-2]
  
  return series

print(fibonacci(10))


def bubbleSort(list, asc=True):
  flag = True
  while flag:
    flag = False
    for i in range(len(list) -1):
      if asc:
        if list[i] > list[i+1]:
          list[i], list[i+1] = list[i+1], list[i]
          flag = True
      else:
        if list[i] < list[i+1]:
          list[i], list[i+1] = list[i+1], list[i]
          flag = True
  return list

randomlist = [5,1,17,4,3]
print(bubbleSort(randomlist, asc = True))
print(bubbleSort(randomlist, asc = False))

def reverseNumber(number):
  reversedNumber = 0

  while (number != 0):

    remainder = number % 10
    reversedNumber = reversedNumber * 10 + remainder
    number = number // 10
  
  return reversedNumber

num = 234521
print(reverseNumber(num))

def convertStringToList(string):
  list = []
  list[:] = string
  return list


print(convertStringToList("Skardu"))

def convertListToString(list):
  string = ""
  for element in list:
    string += element
  return string
  
list = ['T', 'h', 'i', 's', ' ', 'i', 's']

print(convertListToString(list))