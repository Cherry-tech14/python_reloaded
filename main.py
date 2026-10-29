from convertbase import convert_hexadecimal, convert_binary
from convertcase import convert_uppercase, convert_lowercase, convert_cap

sentence = input("Enter your sentence: ")
result = convert_hexadecimal(sentence)
result = convert_binary(result)
result = convert_uppercase(result)
result = convert_lowercase(result)
result = convert_cap(result)

print(result)