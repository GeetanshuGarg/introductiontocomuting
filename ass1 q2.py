# Calculating a person's income tax under the given tax laws
print("your income")
n1 = input()
print("no of dependemts")
n2 = input()
print("tax payable =", 0.2 * (int(n1) - 10000 - 3000*int(n2)))
