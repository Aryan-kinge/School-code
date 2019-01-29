def get_number():
    for i in range(0,1000):
        if not i % 3 or not i % 5:
            yield i

dhruv = sum(get_number())
print(dhruv)
