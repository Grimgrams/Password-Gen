#there are two ways to execute the script 1 use an ide or if you are on unix use the python3 {filename} command in the terminal.
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
	print(password)
