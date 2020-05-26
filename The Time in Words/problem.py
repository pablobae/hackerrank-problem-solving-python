import os

numbers_in_words = {
    '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight',
    '9': 'nine',
    '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '16': 'sixteen',
    '17': 'seventeen', '18': 'eighteen', '19': 'nineteen', '20': 'twenty', '21': 'twenty one', '22': 'twenty two',
    '23': 'twenty three', '24': 'twenty four', '25': 'twenty five', '26': 'twenty six', '27': 'twenty seven',
    '28': 'twenty eight', '29': 'twenty nine'
}


def timeInWords(hour, minute):
    if str(hour) not in numbers_in_words.keys() or not 0 <= minute <= 59:
        output = 'Time provided is not valid'
    else:
        if minute == 0:
            output = numbers_in_words[str(hour)] + ' o\' clock'
        elif minute == 15:
            output = 'quarter past ' + numbers_in_words[str(hour)]
        elif minute == 30:
            output = 'half past ' + numbers_in_words[str(hour)]
        elif minute == 45:
            if hour == 12:
                hour = 1
            else:
                hour = hour + 1
            output = 'quarter to ' + numbers_in_words[str(hour)]
        elif minute == 1:
            output = numbers_in_words[str(minute)] + ' minute past ' + numbers_in_words[str(hour)]
        elif minute < 30:
            output = numbers_in_words[str(minute)] + ' minutes past ' + numbers_in_words[str(hour)]
        elif minute == 59:
            if hour == 12:
                hour = 1
            else:
                hour = hour + 1
            output = numbers_in_words[str(60 - minute)] + ' minute to ' + numbers_in_words[str(hour + 1)]
        else:
            if hour == 12:
                hour = 1
            else:
                hour = hour + 1
            output = numbers_in_words[str(60 - minute)] + ' minutes to ' + numbers_in_words[str(hour)]

    return output


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = open('output.txt', 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
