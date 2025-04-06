def count_bits(n):
    return bin(n).count('1')

number=int(input("What number do you want to count the bits of? "))
print(f"The number of bits in {number} is {count_bits(number)}")
