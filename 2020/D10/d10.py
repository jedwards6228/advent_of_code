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
    print(ascending_list)
    print(difference_list)
    return one_jolt_counter * three_jolt_counter


def count_adapter_arrangements():
    pass


print(f"The number of 1-jolt differences multiplied by the "
      f"number of 3-jolt differences is {multiply_joltage_differences()}.")
print(f"The total number of distinct ways to arrange the adapters is {count_adapter_arrangements()}")

# Part 2
# We need to have a counter for unique variations
# We don't need to store them
# Can skip adapters
# 1
# *3
# *2
# = 6 + 1 (original) = 7
# so for each possible adapter, multiply the running split count by that amount
