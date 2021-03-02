SECURE =(('#','V'),('^1','l'),('+','p'),(':','o'),('(','f'),(')','m'),('|','d'),
	('_','h'),('/','e'),('*' , 's'), ('$', 'a'),(']', 'i'),('!','c'),
	('<','E'),('>','L'),('"',','),('`','g'),
	(';','1'),('{','2'),('[','3'),('?','4'),('}','5'),
	('&','6'),('\\','7'),("'",'8'),('~','9'),('%','0'))	

def encode(newpass):
	for a,b in SECURE:
		newpass = newpass.replace(b,a)
	return newpass


def decode(allpassword):
	for a,b in SECURE:		
		allpassword = allpassword.replace(a,b)
	return allpassword

i = input('enter "1" to view or "2" to add : \n')
if i=="1":
	with open('pass.txt') as f:
		allpassword = f.read()
		allpassword = decode(allpassword)
	print(allpassword)

elif i == "2":
	newpass = input('enter new password : ')
	new = newpass
	newpass = encode(newpass)
	n=newpass
	with open ('pass.txt','a') as f:
		p = f.write('\n')
		newpass = f.write(str(newpass))	
	print(f'Your password {new} is successfully added as {n}')
	
else:
	print('invalid input... please try again!')

		

