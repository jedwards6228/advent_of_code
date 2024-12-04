from pathlib import Path

# Get input file
input_file = Path(__file__).with_name('input.txt')

# Parse input file, making a list by new lines and an imbeded list where the left and right contents are separated
report_list = [x.strip('\n').split(' ') for x in open(input_file).readlines()]

# Globals
max_level_dif = 3


def validate_report(report, multiplier):
    
    for i in range(0, len(report)-1):

        # Continue if next item in the report is valid
        if max_level_dif >= multiplier * (report[i] - report[i+1]) > 0:
            continue

        # Fail validation
        else:
            return False
 
    return True


def process_reports(rule):
    safe_reports = 0

    # Iterate through the reports
    for report in report_list:  

        # Convert report to integers
        report = list(map(int, report))

        # Check if increase or decrease (multiplier -1 or 1 respectively.. it's reversed)
        if report[0] > report[-1]:
            mult = 1
        elif report[0] < report[-1]:
            mult = -1

        # Try validating the report:
        valid = validate_report(report, mult)

        # Try adjusted reports for part 2
        if rule > 1:
            i = 0 
            while i < len(report) and valid == False:
                adjusted_report = report.copy()
                adjusted_report.pop(i)
                valid = validate_report(adjusted_report, mult)
                i += 1
        safe_reports += valid

    return safe_reports


# Solve all the problems
def main():
    print (f'The answer to part one is {process_reports(1)}.')
    print (f'The answer to part two is {process_reports(2)}.')
    return


#Run the code
if __name__ == '__main__':
    main()
