import random

uppercase_letters = "ABCDEFGHIKJLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{},:;.-/?+*# "
special = "`¡™£¢∞§¶•ªº–≠œ∑´®†¥¨ˆøπ“‘«åß∂ƒ©˙∆˚¬…æΩ≈ç√∫˜µ≤≥÷`⁄€‹›ﬁﬂ‡°·‚—±Œ„´‰ˇÁ¨ˆØ∏”’»ÅÍÎÏ˝ÓÔÒÚÆ¸˛Ç◊ı˜Â¯˘¿ "
upper, lower, nums, syms, spec = True, True, True, True, True

all = ""

if upper:
	all += uppercase_letters

if lower:
	all += lowercase_letters

if nums:
	all	+= digits

if syms:
	all += symbols

if spec:
	all += special

length = 20
amount = 10

for x in range(amount):
	password = "".join(random.sample(all, length))
	print("\033[1;33;40m" + password)
