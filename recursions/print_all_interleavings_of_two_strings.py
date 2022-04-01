# python 3

def find_all_interleaving(string1, string2, ans_string, all_strings):
    if not string1 and not string2:
        all_strings.append(ans_string)

    if string1:
        find_all_interleaving(
            string1[1:],
            string2,
            ans_string + string1[0],
            all_strings)
    if string2:
        find_all_interleaving(
            string1,
            string2[1:],
            ans_string + string2[0],
            all_strings)

    return all_strings


def main():
    string1 = input()
    string2 = input()
    all_strings = []

    print(find_all_interleaving(string1, string2, '', all_strings))


if __name__ == '__main__':
    main()
