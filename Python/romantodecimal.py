#Convert roman numerals to numbers

def roman_to_int(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for i in range(len(s)):
        if i > 0 and roman_dict[s[i]] > roman_dict[s[i-1]]:
            int_val += roman_dict[s[i]] - 2*roman_dict[s[i-1]]
            continue
        int_val += roman_dict[s[i]]
    return int_val

#Test the function

print(roman_to_int('III'))  # Expected output: 3
print(roman_to_int('IV'))  # Expected output: 4
print(roman_to_int('IX'))  # Expected output: 9
print(roman_to_int('LVIII'))  # Expected output: 58
print(roman_to_int('MCMXCIV'))  # Expected output: 1994