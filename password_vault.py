SECURE =(('#','V'),('^','l'),('+','p'),(':','o'),('(','f'),(')','m'),('|','d'),
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

def read(i):
	with open(r'C:\\Users\\HP\\Desktop\\Untitled Export\\pass.txt') as f:
		allpassword = f.readlines()
		v=1
		for pas in allpassword:
			pas = decode(pas)
			print(f'{v}.) {pas}',end='')
			v+=1
		return allpassword
	

def append(i):
	newpass = input('enter new password : ')
	new = newpass
	newpass = encode(newpass)
	n=newpass
	with open(r'C:\\Users\\HP\\Desktop\\Untitled Export\\pass.txt','a') as f:
		p = f.write('\n')
		newpass = f.write(str(newpass))	
	print(f'Your password {new} is successfully added as {n}')


def write(r):
	with open(r'C:\\Users\\HP\\Desktop\\Untitled Export\\pass.txt','w') as f:
		for i in r:
			f.write(str(i))
	read(i)

def delete(i):
	r = read(i)
	total_pass = len(r)
	del_pass = int(input('\nenter the password you want to delete : '))
	del_pass = del_pass-1
	if del_pass <= total_pass and del_pass>0:
		r[del_pass] = decode(r[del_pass])
		confirm = input(f'are you sure you want to delete {r[del_pass]} "Y" or "N" : ')
		if confirm == "y":
			delete = r.pop(del_pass)
			print(f'{delete}is deleted successfully...')
			write(r)
		elif confirm == "n":
			read(i)
		else:
			print('invalid input... please try again!')
			
	else:
		print('invalid input... please try again!')

def edit(i):
	r = read(i)
	total_pass = len(r)
	edit_pass = int(input('\n\nenter the password you want to edit : '))
	edit_pass = edit_pass-1
	if edit_pass>0 and edit_pass <= total_pass:
		r[edit_pass] = decode(r[edit_pass])
		confirm = input(f'are you sure you want to edit {r[edit_pass]} "Y" or "N" : ')
		if confirm == "y":
			final = input('enter the new password : \n')
			final = encode(final)
			r[edit_pass] = final + '\n'
			write(r)
		elif confirm == "n":
			read(i)
		else:
			print('invalid input... please try again!')


	else:
		print('invalid input... please try again!')



i = input('enter "1" to view, "2" to add, "3" to edit or "4" to delete : \n')
if i == "1":
	read(i)

elif i == "2":
	append(i)

elif i == "3":
	edit(i)

elif i == "4":
	delete(i)

else:
	print('invalid input... please try again!')
