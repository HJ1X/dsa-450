# python 3

def find_sentences_util(string, start, dictionary, n, res, sentence):
    if start == n:
        res.append(sentence.copy())
        return

    for end in range(n):
        if string[start: end + 1] in dictionary:
            sentence.append(string[start: end+1])
            find_sentences_util(string, end + 1, dictionary, n, res, sentence)
            sentence.pop()


def find_sentences(n, dictionary, string):
    res = []
    sentence = []

    dictionary = set(dictionary)

    find_sentences_util(string, 0, dictionary, n, res, sentence)
    return res


def main():
    dictionary = input().split()
    string = input()
    print(find_sentences(len(string), dictionary, string))


if __name__ == '__main__':
    main()
