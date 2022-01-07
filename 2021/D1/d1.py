input_file = 'input.txt'
measurement_list = [int(x) for x in open(input_file).readlines()]


def count_increase_single():
    count = 0
    for index, measurement in enumerate(measurement_list):
        if index == 0:
            continue
        if measurement > measurement_list[index - 1]:
            count += 1
        else:
            continue
    return count


def count_increase_window():
    count = 0
    for index, measurement in enumerate(measurement_list):
        if index + 3 > len(measurement_list):
            break
        current_window = sum(measurement_list[index:index + 3])
        next_window = sum(measurement_list[index + 1:index + 4])
        if next_window > current_window:
            count += 1
        else:
            continue
    return count



print(f'{count_increase_single()} measurements are larger than the previous one.')
print(f'{count_increase_window()} rolling window measurement increases occur.')
