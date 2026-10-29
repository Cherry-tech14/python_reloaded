from convertbase import convert_hexadecimal, convert_binary
from convertcase import convert_uppercase, convert_lowercase, convert_cap
from multiplecase import convert_multiple_upper, convert_multiple_lower, convert_multiple_cap
from punctuation import fix_punctuation

sentence = input("Enter your sentence: ")
result = convert_hexadecimal(sentence)
result = convert_binary(result)
result = convert_uppercase(result)
result = convert_lowercase(result)
result = convert_cap(result)
result = convert_multiple_upper(result)
result = convert_multiple_lower(result)
result = convert_multiple_cap(result)
result = fix_punctuation(result)
print(result)