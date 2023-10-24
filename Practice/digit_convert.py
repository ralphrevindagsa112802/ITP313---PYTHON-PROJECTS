def digit_converter(number):
    number_convert = {
        "1":"One",
        "2":"Two",
        "3":"Three",
        "4":"Four",
        "5":"Five",
        "6":"Six",
        "7":"Seven",
        "8":"Eight",
        "9":"Nine",
        "0":"Zero",
    }

    output = ""

    for ch in number:
        output += number_convert.get(ch, "!") + " "

    return output


number = input("Phone: ")

output = digit_converter(number)

print(output)
