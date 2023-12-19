#Employee A: 15.62 miles
#Employee B: 41.85 miles
#Employee C: 32.67 miles
#solution accepts three integer inputs representing the number of times an employee travels to the job site
#solution outputs "Distance: " followed by the total value to two decimal places


# timesTraveledOne = int(input())
# timesTraveledTwo = int(input())
# timesTraveledThree = int(input())
#
# milesTraveledA = 15.62
# milesTraveledB = 41.85
# milesTraveledC = 32.67
#
# totalMilesA = timesTraveledOne * milesTraveledA
# totalMilesB = timesTraveledTwo * milesTraveledB
# totalMilesC = timesTraveledThree * milesTraveledC
#
# totalMilesTraveled = totalMilesA + totalMilesB + totalMilesC
# print(f'Distance: {totalMilesTraveled:.2f} miles')


# =======================================

#there are 16 ounces in a pound and 2000 pounds in a ton
#solution accepts an integer value representing any number of ounces
#solution outputs the converted tons, pounds, and ounces represented by the input value of ounces
#
# ounces = int(input())
#
# tons = ounces // (2000 * 16)
# ounces %= (2000 * 16)
#
# pounds = ounces // 16
# ounces %= 16
#
# print(f'Tons: {tons}')
# print(f'Pounds: {pounds}')
# print(f'Ounces: {ounces}')


# =======================================



# various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]
#
# #use built-in function type()
# #get name by using the built-in attribute __name__
# #solution accepts integer input representing list element index
# #solution outputs data type of list element based on input index value
#
# index_value = int(input())
#
# data_type = type(various_data_types[index_value]).__name__
#
# print(f'Element {index_value}: {data_type}')

# =======================================
#solution accepts three integer values representing base and height measurements of a trapezoid
#first and second integers represent base 1 and base 2; third integer represents height
#solution outputs the trapezoid area in square meters using formula A = ½(b1+b2)h

b1 = int(input())
b2 = int(input())
h = int(input())

area = ((b1 + b2) / 2) * h

print(f'Trapezoid area: {area} square meters')


# =======================================

#solution accepts five integer inputs
#solution outputs three sums of input values; convert before calculating sum
#first output: sum of five inputs maintained as integer values
#second output: sum of five inputs converted to float values
#third output: sum of five inputs converted to string values (concatenate)

value1 = int(input())
value2 = int(input())
value3 = int(input())
value4 = int(input())
value5 = int(input())

sum = value1 + value2 + value3 + value4 + value5
stringSum = str(value1) + str(value2) + str(value3) + str(value4) + str(value5)

print(f'Integer: {sum}')
print(f'Float: {float(sum)}')
print(f'String: {stringSum}')



# =======================================
#hint: modulo (%) and floored division (//) may be used
#solution accepts a 9-digit integer representing an unformatted student identification number (i.e.,"5417543010")
#solution outputs formatted student identification number as a string (i.e.,"541-75-3010")

idNumber = int(input())

# idString = str(idNumber)

firstThree = idNumber // 1000000
middleTwo = (idNumber // 10000) % 100
lastFour = idNumber % 10000

print(f'{firstThree}-{middleTwo}-{lastFour}')



# =======================================

predef_list = [4, -27, 15, 33, -10]

#solution accepts an integer input
#solution outputs Boolean value indicating if integer input is greater than the maximum value when compared to predef_list

input_val = int(input())

isInputGreaterThanList = input_val > max(predef_list)

print(f'Greater Than Max? {isInputGreaterThanList}')

# =======================================

frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

# use try block with exception "Error" when index value is not found in list
# solution accepts an integer input
# solution outputs the corresponding string value for the integer input


try:
    index_value = int(input())
    element = frameworks[index_value]
    print(element)
except IndexError:
    print('Error')

# =======================================

#solution accepts integer input representing a water temperature
#temperature >= 212, water state is "Boiling"
#temperature between 115-211, exclusive of the stop, water state is "Hot"
#temperature between 80-115, water state is "Warm"
#temperature between 33-80, water state is "Cold"
#temperature < 33, water state is "Frozen"
#temperature = 212, safety comment "Caution: Hot!"
#temperature < 33, safety comment "Watch out for ice!"
#solution outputs the water state and potential safety comment based on temperature

temp = int(input())

if temp < 33:
    print('Frozen')
    print('Watch out for ice!')
elif 33 <= temp <= 80:
    print('Cold')
elif 80 <= temp <= 115:
    print('Warm')
elif 115 <= temp <= 211:
    print('Hot')
if temp >= 212:
    if temp == 212:
        print('Boiling')
        print('Caution: Hot!')
    else:
        print('Boiling')



# =======================================
stocks = {'TSLA': 912.86, 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}

#solution accepts an integer input representing the number of stock selections
#solution accepts string inputs equivalent to the integer input identifying the stock selections
#solution outputs the total cost of stock as "Total price: $" followed by the total cost to 2 decimal places

total_cost = 0

numShares = int(input())

for i in range(numShares):
    stock_selection = input()
    if stock_selection in stocks:
        total_cost += stocks[stock_selection]

print(f'Total price: ${total_cost:.2f}')

# =======================================
purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

#cost per item: <10 is full price, 10-20 (inclusive) is 5% discount, and 21+ is 10% discount
#solution accepts a string input representing an item (dictionary key)
#solution accepts an integer input representing the number of items to be purchased
#solution outputs the item and total cost of purchase


groceryItem = input()
numOfItems = int(input())
groceryCost = 0

if numOfItems < 10:
    groceryCost += purchase[groceryItem] * numOfItems
elif 10 <= numOfItems <= 20:
    groceryCost += (purchase[groceryItem] * numOfItems) * 0.95
elif numOfItems >= 20:
    groceryCost += (purchase[groceryItem] * numOfItems) * 0.90

print(f'{groceryItem} ${groceryCost:.2f}')



# =======================================
#open, write, and read text file (e.g., "WordTextFile1.txt") using open(), write(), read()
#solution accepts file input to insert sentence composed of file content into text file on a new line
#solution outputs the text file contents including the new sentence

file_name = input()


file = open(file_name, 'r')
word1 = file.readline().strip()
word2 = file.readline().strip()
word3 = file.readline().strip()

sentence = f"{word1} {word2} {word3}"

file = open(file_name, 'a')
file.write('\n' + sentence)

file = open(file_name, 'r')
updated_contents = file.read()

print(updated_contents)


# =======================================
------------------- CSV MANIPULATION ------------------
# =======================================
#import math module and call factorial()
#solution accepts integer input
#solution outputs the factorial of the integer input
#solution outputs Boolean identification of whether the factorial is >100

import math

input_value = int(input())
factorial = math.factorial(input_value)

isGreaterThan100 = factorial > 100

print(factorial)
print(isGreaterThan100)

# =======================================
#import pigAge module and call pigAge_converter()
#one pig year is equivalent to five human years
#solution accepts integer input representing a pig's age
#solution outputs the human equivalent age for a pig (i.e. "8 is 40 in human years")

import pigAge

inputValue = int(input())

pigAgeConverted = pigAge.pigAge_converter(inputValue)

print(f'{inputValue} is {pigAgeConverted} in human years')