import os
filename = input(">>> Enter the name of the ipa: ")
output = input(">>> Enter the name of the output: ")
try:
	p = open('p12file.txt', 'r')
	p12 = p.read()
	p.close()
	f = open('provision.txt','r')
	provision = f.read()
	f.close()
	k = open('password.txt', 'r')
	password = k.read()
	k.close()
except:
	p12 = input("Please enter the name of the .p12 file: ")
	provision = input("Please enter the name of the .mobileprovision file: ")
	password = input("Password of the p12 file: ")
	save_txt = input("Do you want to save them in a txt file so that you won't have to enter their name the next time: ")
	if save_txt == "Y" or save_txt == "y":
		n = open("p12file.txt", 'w')
		n.write(p12)
		n.close()
		g = open('provision.txt', 'w')
		g.write(provision)
		g.close()
		l = open('password.txt', 'w')
		l.write(password)
		l.close()
	else:
		print("Not saving in a txt file")

os.system("sudo chmod a+x zsign")
os.system(f'./zsign -k {p12} -p {password} -m {provision} -o {output} {filename}')



os.system(f"mv {output} signed-ipas")
delete_unsigned = input(f"Do you want to delete the unsigned ipa: {filename}: ")

if delete_unsigned == "y" or delete_unsigned == "Y":
	os.system(f"rm {filename}")
else:
	pass
