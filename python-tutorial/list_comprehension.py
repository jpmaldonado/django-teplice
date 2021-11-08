numbers = (1,2,3,4,5)

squares = []
for number in numbers:
    square = number**2
    squares.append(square)

print(squares)
print('*'*50)

other_squares = [number**2 for number in numbers]
sum_other_squares = sum([number**2 for number in numbers])
print(other_squares)
print(sum_other_squares)

vals = ["1.5", "3.14", "9.87"]
vals_mask = [1 if float(val) < 5 else 0 for val in vals]
print(vals_mask)


# Lambda functions + list comprehension
print('*'*50)
multiply = lambda x, multiplier: x*multiplier
vals = [1,2,3]
my_vals = [multiply(val, 4) for val in vals]
print(my_vals)


print('*'*50)
vals = [(1,2), (3,4)]
other_vals = [multiply(val[0], val[1]) for val in vals]
other_vals = [multiply(x,y) for x,y in vals]
print(other_vals)