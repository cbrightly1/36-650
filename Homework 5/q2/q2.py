# Q2

def remove_punct(input_string):
    punct_list = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    final_string = input_string
    for i in range(len(input_string)):
        for j in range(len(punct_list)):
            if input_string[i] == punct_list[j]:
                final_string = final_string.replace(input_string[i],"",1)
    return str(final_string)

test_string = "Hello in 36-650, & other MSP courses."
test_string2 = "@ever^ay"
print(remove_punct(test_string))
print(remove_punct(test_string2))