kata = (0, 4, 132.42222, 10000, 12345.67)

from decimal import Decimal

print("module_0", kata[0], sep="", end=", ")
print("ex_0", kata[1], sep="", end=" : ")
print(round(kata[2], 2), end=", ")
print('{:.2e}'.format(kata[3]), end=", ")
print('{:.2e}'.format(kata[4]))
