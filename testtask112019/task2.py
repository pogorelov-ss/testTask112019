# sort matrix. snail
def sort_matrix_clockwise(size_x, size_y):
    result = list()
    input_array = [list(zip(range(size_x), [i] * size_x)) for i in range(size_y)]
    while len(input_array) > 0 and len(input_array[0]) > 0:
        for el in input_array:
            print(el)
        print('-----')
        if len(input_array[0]) > 1:
            result.append('right')
            result += input_array[0]
            del input_array[0]
        else:
            result.append('right')
            result += input_array[0]
            del input_array[0]
            result.append('down')
            result += input_array
            break

        if len(input_array) > 0:
            result.append('down')
            for el in input_array:
                result += [el[-1]]
                del el[-1]
            if input_array[-1]:
                result.append('left')
                result += input_array[-1][::-1]
                del input_array[-1]
            result.append('up')
            for el in reversed(input_array):
                result.append(el[0])
                del el[0]
    return result


# reverse bits
def revbits1(n):
    return int(bin(n)[2:][::-1], 2)


def revbits2(n):
    rev = 0
    while n:
        rev <<= 1
        rev += n & 1
        n >>= 1
    return rev
