sum_of_squares = []
square_of_sum = []
for i in range(0,101):
    sum_of_squares.append(i ** 2)
    square_of_sum.append(i)


mayank = sum(sum_of_squares)
sam = sum(square_of_sum) ** 2

print(sam - mayank)
