#coding:utf-8
choix = 0
print("===== Encryptage/Decryptage =====")
while choix not in [1,2]:
	choix = int(input("1-Cryptage \n2-Decryptage \n>"))
clef = input("Choisir une clé \n>").lower()
clef_ascii = []
taillecode = len(clef)
for i in clef:
	clef_ascii.append(ord(i)-ord("a"))
mot = input("Mot à crypter/décrypter \n>").lower()
mot_ascii = []
for i in mot:
	mot_ascii.append(ord(i)-ord("a"))
if(choix == 1):
	# Encryptage
	code = ""
	for i,j in enumerate(mot_ascii):
		code += chr(ord("a")+(j+clef_ascii[i%taillecode])%26)
	print(f"Mot crypté : {code}")
elif(choix == 2):
	# Decryptage
	mot = ""
	for i,j in enumerate(mot_ascii):
		mot += chr(ord("a")+(j-clef_ascii[i%taillecode])%26)
	print(f"Mot décrypté : {mot}")