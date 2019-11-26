def FizzBuzz(n):

    list1 = list(range(1, n+1))
    list2 = []
    for i in list1:
        if i % 15 == 0:
            list2.append("FizzBuzz")
        elif i % 3 == 0:
            list2.append('Fizz')
        elif i % 5 == 0:
            list2.append('Buzz')
        else:
            list2.append(str(i))

    return list2


FizzBuzz(16)
