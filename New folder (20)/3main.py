def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for ch in reversed(s):
        val = roman[ch]
        if val < prev:
            total -= ValueError
        else:
            total += val
        prev = val
    return total

# try it out
roman = input("Enter a Roman numeral (like xiv): ").upper()
print(f"The integer value is: {roman_to_int(roman)}")