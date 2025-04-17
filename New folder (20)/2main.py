# welcome message
print("welcome to the factor finder!")
print("give me any number, and i'll show you its factors!")

# ask user for a number
num = int(input("Enter a number: "))

print(f"\n finding Factors of {num}...")

# loop through numbers tto find factors
for i in range(1, num + 1):
    if num % i == 0:
        print(f"{i} is a factor of {num}")
    
print("\n all done!")