input_file = "input.txt"
matrix = [[str(bit) for bit in str(pwr.strip('\n'))] for pwr in open(input_file).readlines()]


def binary_to_decimal(binary):
    # reverse binary list
    binary.reverse()
    # set initial bit and total value
    bit_value = 1
    total_value = 0
    # add the value for every "on" bit
    for bit in binary:
        if bit == "1":
            total_value += bit_value
        else:
            total_value += 0
        bit_value += bit_value
    return total_value


def find_rates():
    gamma = []
    epsilon = []
    for x in range(len(matrix[0])):
        col_list = [col[x] for col in matrix]
        if col_list.count('0') > col_list.count('1'):
            gamma.append('0')
            epsilon.append('1')
        else:
            gamma.append('1')
            epsilon.append('0')
    return gamma, epsilon


def main():
    gamma, epsilon = find_rates()
    pwr_con = binary_to_decimal(gamma) * binary_to_decimal(epsilon)
    print(f"The power consumption is {pwr_con}.")


if __name__ == "__main__":
    main()
