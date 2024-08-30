katz_deli = []
def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        line_string = "The line is currently:"
        for i in range(len(katz_deli)):
            line_string += f" {i+1}. {katz_deli[i]}"
        print(line_string)

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {len(katz_deli)} in line.")
def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        current_customer = katz_deli.pop(0)
        print(f"Currently serving {current_customer}.")
