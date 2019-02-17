# Illustration of various numeric functions

number = 20
float_num = 3.14

bit_length = number.bit_length()
absolute_value = float_num.__abs__()
power = number.__pow__(2)
max_val = max(number.__float__(),float_num)
round_val = float_num.__round__()
isEqual = bool(number.__eq__(float_num))

print("Bit Length = " + str(bit_length))
print("Absolute Value = " + str(absolute_value))
print("Power = " + str(power))
print("Max value = " + str(max_val))
print("Round value = " + str(round_val))
print("Equality status = " + str(isEqual))

