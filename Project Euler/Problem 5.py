def modular():
    i = 20
    while 1:
        i += 20
        if i % 11 == 0 and i % 12 == 0 and i % 13 == 0 and \
                i % 14 == 0 and i % 15 == 0 and i % 16 == 0 and i % 17 == 0 and i % 18 == 0 and i % 19 == 0:
            print(i)
            break
modular()

