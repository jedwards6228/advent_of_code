input_file = 'test.txt'
adapter_list = [int(x.strip('\n')) for x in open(input_file).readlines()]
adapter_list.insert(0, 0)
adapter_list.append(max(adapter_list) + 3)
ascending_list = adapter_list.copy()
ascending_list.sort()
difference_list = []


def multiply_joltage_differences():
    global difference_list
    index = 0
    while index < len(ascending_list) - 1:
        difference = ascending_list[index + 1] - ascending_list[index]
        difference_list.append(difference)
        index += 1
    one_jolt_counter = difference_list.count(1)
    three_jolt_counter = difference_list.count(3)
    return one_jolt_counter * three_jolt_counter


def count_adapter_arrangements():
    var_counter = 1
    index = 0
    while index < len(ascending_list) - 1:
        multiplier = 0
        i = 3
        while i > 0:
            if ascending_list[index] + i in ascending_list:
                multiplier += 1
            i -= 1
        if multiplier > 1:
            var_counter += multiplier
        index += 1
    return var_counter


print(f"The number of 1-jolt differences multiplied by the "
      f"number of 3-jolt differences is {multiply_joltage_differences()}.")
print(f"The total number of distinct ways to arrange the adapters is {count_adapter_arrangements()}")


