from collections import Counter


input_file = "input.txt"
with open(input_file) as f:
    matrix = [[int(bit) for bit in str(pwr.strip('\n'))] for pwr in f.readlines()]


def binary_to_decimal(binary):
    # reverse binary list
    binary.reverse()
    # set initial bit and total value
    bit_value = 1
    total_value = 0
    # add the value for every "on" bit
    for bit in binary:
        if bit == 1:
            total_value += bit_value
        else:
            total_value += 0
        bit_value += bit_value
    return total_value


def find_most_common_bit(bit_list):
    counter = Counter(bit_list)
    if counter[0] == counter[1]:
        return 1
    else:
        return counter.most_common()[0][0]


def find_rates():
    gamma = []
    epsilon = []
    oxy_gen = matrix.copy()
    co2_scrub = matrix.copy()
    for col in range(len(matrix[0])):
        most_common_bit = find_most_common_bit([row[col] for row in matrix])
        most_common_bit_oxy_gen = find_most_common_bit([row[col] for row in oxy_gen])
        least_common_bit_co2 = int(not find_most_common_bit([row[col] for row in co2_scrub]))
        # add most common bit to gamma
        gamma.append(most_common_bit)
        # add the least common bit to epsilon
        epsilon.append(int(not most_common_bit))
        temp_list = []
        for row in oxy_gen:
            if row[col] == most_common_bit_oxy_gen:
                temp_list.append(row)
            else:
                continue
        if len(oxy_gen) > 1:
            oxy_gen = temp_list.copy()
        temp_list.clear()
        for row in co2_scrub:
            if row[col] == least_common_bit_co2:
                temp_list.append(row)
            else:
                continue
        if len(co2_scrub) > 1:
            co2_scrub = temp_list.copy()
    return gamma, epsilon, oxy_gen[0], co2_scrub[0]


def main():
    gamma, epsilon, oxy_gen, co2_scrub = find_rates()
    pwr_con = binary_to_decimal(gamma) * binary_to_decimal(epsilon)
    lif_sup = binary_to_decimal(oxy_gen) * binary_to_decimal(co2_scrub)
    print(f"The power consumption is {pwr_con}.\n"
          f"The life support rating is {lif_sup}")


if __name__ == "__main__":
    main()
