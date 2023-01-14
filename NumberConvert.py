ones = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
        7: "seven", 8: "eight", 9: "nine"}

tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty",
        7: "seventy", 8: "eighty", 9: "ninety"}

beforetwenty = {1: "eleven", 2: "twelve", 3: "thirteen", 4: "fourteen", 5: "fifteen",
                6: "sixteen", 7: "seventeen", 8: "eighteen", 9: "nineteen"}


def converttodigit(number):
    result = []
    if number == 0:
        result.append(0)
    else:
        while number > 0:
            remainder = number % 10
            result.append(remainder)
            number = int(number / 10)
    result.reverse()
    return result


def convertToWord(result):
    word = ""
    if result[0] == 1 and len(result) != 1:
        if result[1] == 0:
            word += "ten"
        else:
            word += beforetwenty.get(result[1]) 
    elif len(result) == 1:
        word += ones.get(result[0])
    else:
        word += tens.get(result[0])
        word += ones.get(result[1])
    return word


def mainConvert(amount):
    number = amount.split(".")
    dollars = convertToWord(converttodigit(int(number[0])))
    cents = convertToWord(converttodigit(int(number[1])))

    if cents == "":
        return(f"{dollars} dollars")
    elif dollars == "":
        return (f"{cents} cents")
    else:
        return(f"{dollars} dollars and {cents} cents")
