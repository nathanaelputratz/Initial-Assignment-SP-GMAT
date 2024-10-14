def int_to_binary5(number):
    n = 5
    binary = ""

    for i in range(1, n + 1):
        if (number - 2**(n - i) >= 0):
            binary += "1"
            number -= 2**(n - i)
        else:
            binary += "0"
    
    return binary

error_msg = [
    'Container descent rate failure',
    'Science Payload descent rate failure',
    'Container position failure',
    'Science Payload position failure',
    'Release failure'
]

error = int(input(""))
bin_format = int_to_binary5(error)

for i in range(len(bin_format)):
    if (bin_format[i] == "1"):
        print(error_msg[i])

if (bin_format == "00000"):
    print("No error")