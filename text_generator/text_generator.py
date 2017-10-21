import random, string
vovels="aeiou"
consonents="bcdfghjklmnpqrstvwxyz"
any=string.ascii_lowercase
letter_input_1=input("Enter a letter?for vovels enter 'v',for consonents enter 'c',for any letter enter 'l':")
letter_input_2=input("Enter a letter?for vovels enter 'v',for consonents enter 'c',for any letter enter 'l':")
letter_input_3=input("Enter a letter?for vovels enter 'v',for consonents enter 'c',for any letter enter 'l':")


def generator():
	if letter_input_1=="v":
		let1=random.choice(vovels)
	elif letter_input_1=="c":
		let1=random.choice(consonents)
	elif letter_input_1=="l":
		let1=random.choice(any)

	else:
		let2=letter_input_2
	if letter_input_2=="v":
		let2=random.choice(vovels)
	elif letter_input_2=="c":
		let2=random.choice(consonents)
	elif letter_input_2=="l":
		let2=random.choice(any)

	else:
		let3=letter_input_3
	if letter_input_3=="v":
		let3=random.choice(vovels)
	elif letter_input_3=="c":
		let3=random.choice(consonents)
	elif letter_input_3=="l":
		let3=random.choice(any)


	name=let1+let2+let3
	return(name)

for i in range(20):
	print(generator())

