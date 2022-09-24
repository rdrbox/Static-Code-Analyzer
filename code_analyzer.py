from errors_checker import checker
from errors_message import pm

if __name__ == "__main__":

    with open(input(), 'r') as file:
        number_line = 1

        for line in file:
            check_list = checker(line, number_line)
            if check_list:
                line_message = []
                for x, y in check_list:
                    line_message.append(pm(x, y))
                line_message.sort()
                for message in line_message:
                    print(message)
            number_line += 1
