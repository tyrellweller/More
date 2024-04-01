def print_models(printing , complete):
    while printing:
        printed = printing.pop()
        print("printing the " + printed)
        complete.append(printed)
def complete_models(complete):
    for c in complete:
        print(c)