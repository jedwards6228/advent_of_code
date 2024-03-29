input_file = 'input.txt'
adapter_list = [int(x.strip('\n')) for x in open(input_file).readlines()]
adapter_list.insert(0, 0)
adapter_list.append(max(adapter_list) + 3)
ascending_list = adapter_list.copy()
ascending_list.sort()  # creates ascending list of adapters including starting (0) and ending (max + 3)


def multiply_joltage_differences():
    difference_list = []  # list containing difference from one adapter to next (1 to 3)
    index = 0
    while index < len(ascending_list) - 1:
        difference = ascending_list[index + 1] - ascending_list[index]
        difference_list.append(difference)
        index += 1
    one_jolt_counter = difference_list.count(1)
    three_jolt_counter = difference_list.count(3)
    return one_jolt_counter * three_jolt_counter


def count_adapter_arrangements():
    variable_counter_list = [1]  # list tracks variables per index of the ascending list, starts with 1 variable
    while len(variable_counter_list) < len(ascending_list):
        variable_counter_list.append(0)
    index = 0
    while index < len(ascending_list):
        i = 1
        max_range = 3
        while index + max_range > len(ascending_list) - 1:  # keeps following loop from exceeding list index
            max_range -= 1
        while i <= max_range:  # increases variable counter for the appropriate index
            if ascending_list[index + i] <= ascending_list[index] + 3:
                variable_counter_list[index + i] = variable_counter_list[index] + variable_counter_list[index + i]
            i += 1
        index += 1
    return variable_counter_list[-1]


print(f"The number of 1-jolt differences multiplied by the "
      f"number of 3-jolt differences is {multiply_joltage_differences()}.")
print(f"The total number of distinct ways to arrange the adapters is {count_adapter_arrangements()}")
