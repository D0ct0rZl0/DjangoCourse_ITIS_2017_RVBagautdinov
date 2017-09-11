def convert_to_rim(number):
    scheme = {
        0: [],
        1: [0],
        2: [0, 0],
        3: [0, 0, 0],
        4: [0, 1],
        5: [1],
        6: [1, 0],
        7: [1, 0, 0],
        8: [1, 0, 0, 0],
        9: [0, 2]
    }
    keys = {
        0: ["I", "V", "X"],
        1: ["X", "L", "C"],
        2: ["C", "D", "M"]
    }

    nors = []

    while number > 0:
        nors.append(number%10)
        number = number//10

    nors.reverse()
    count = nors.__len__() - 1
    answer = ''

    for num in nors:
        if count < 3:
            print(count)
            for key in scheme[num]:
                answer += keys[count][key]
        elif count >= 3:
            for i in range(num):
                answer += "M"
        count -= 1

    print(answer)



convert_to_rim(567)
convert_to_rim(325)
convert_to_rim(101)
convert_to_rim(24)
convert_to_rim(7)
convert_to_rim(99)
convert_to_rim(9999)



