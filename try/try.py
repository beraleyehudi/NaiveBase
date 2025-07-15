
def calculate(args, proportion):

    result = 1
    for i in args:
        result *= i/proportion

    return result


non_operational = calculate([3, 4, 1], 6) * 0.3
operational_unit = calculate([4, 2, 6], 10) * 0.4
weak_unit = calculate([4, 7, 1], 11) * 0.3


print(max(non_operational, operational_unit, weak_unit))


dictionary_exemple = {"number_of_colmun":{"classifier":{"attribute":"count", "total":0}}}


def print_menu(title:str, options:list):
    print(title, "\n")
    for i in range(len(options)):
        print(f"{i +1}: {options[i]}")

    choice = int(input("enter your choice:\n"))
    return options[choice - 1]

