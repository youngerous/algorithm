while True:
    try:
        nn = int(input())
        ones, count = 1, 1
        while True:
            if ones % nn == 0:
                print(count)
                break
            else:
                count += 1
                ones = ones * 10 + 1
    except:
        break
