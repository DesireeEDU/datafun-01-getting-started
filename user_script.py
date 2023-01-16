# user_script.py
"""Print useful output showing the following:
    1.sum
    2. average
    3. product
    4. smallest
    5. largest
    6. range.
"""
# number of dags at the daycare on Monday
number1 = int(input('Enter the number of dogs at the daycare on Monday: '))
type(number1)

if number1 < 25:
    print('We need more doggy friends!')

if number1 == 25:
    print('We had a great day with our doggy friends!')

if number1 > 25:
    print('Today it was a doggy party!')

# number of dogs at the daycare on Tuesday
number2 = int(input('Enter the number of dogs at the daycare on Tuesday: '))

if number2 < 25:
    print('We need more doggy friends!')

if number2 == 25:
    print('We had a great day with our doggy friends!')

if number2 > 25:
    print('Today it was a doggy party!')

# number of dogs at the daycare on Wednesday
number3 = int(input('Enter the number of dogs at the daycare on Wednesday: '))

if number3 < 25:
    print('We need more doggy friends!')

if number3 == 25:
    print('We had a great day with our doggy friends!')

if number3 > 25:
    print('Today we had a doggy party!')

# total number of dogs at the daycare from Monday through Wednesday
sum = int(number1 + number2 + number3)

# average
average = float(round(sum / 3, 2))

# product
product = int(number1 * number2 * number3)

# min
smallest = int(min(number1, number2, number3))

# max
largest = int(max(number1, number2, number3))

print()
print(
    f'The sum of all the dogs at the daycare from Monday through Wednesday is {sum}.')
print(
    f'The average number of dogs at the daycare from Monday through Wednesday is {average}.')
print(
    f'The product of the dogs at the daycare from Monday through Wednesday is {product}.')
print(
    f'The smallest number of dogs at the daycare from Monday through Wednesday is {smallest}.')
print(
    f'The largest number of dogs at the daycare from Monday through Wednesday is {largest}.')
print(
    f'The  number of dogs at the daycare from Monday through Wednesday range from {smallest} to {largest}.')
