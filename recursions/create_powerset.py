# python 3

def generate_powerset(string, i, answer, powerset):
    if i == len(string):
        powerset.append(answer)
        return

    generate_powerset(string, i+1, answer+string[i], powerset)    # choosing the character
    generate_powerset(string, i+1, answer, powerset)              # not choosing character


def main():
    string = input()
    powerset = []
    generate_powerset(string, 0, '', powerset)
    print(powerset)


if __name__ == '__main__':
    main()
