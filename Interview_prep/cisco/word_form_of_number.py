# python 3

# Write a function to print word form of a number having up to 3 digits

def find_word_form(num):
    if len(str(num)) > 3:
        return 'Numbers with more than 3 digits are not supported'

    single_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    double_digits = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
                     'nineteen']
    tens_digits = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    word_form = ''
    if len(str(num)) == 3:
        hundreds_prefix = single_digits[num // 100] + ' ' + 'hundred '
        word_form += hundreds_prefix
        num %= 100

    if len(str(num)) == 2:
        if num//10 == 1:
            word_form += double_digits[num % 10]
            return word_form
        else:
            word_form += tens_digits[num // 10] + ' '
            num %= 10

    if len(str(num)) == 1:
        if len(word_form) > 0 and num == 0:
            return word_form

        word_form += single_digits[num]
        return word_form


def main():
    num = int(input())
    print(find_word_form(num))


if __name__ == '__main__':
    main()
