
ciphertext = "ab f4 77 ad cd 99 7c 0c 64 2a 15 3e 61 e2 38 d8 8c bb a7 f8 7b a1 c1 95 70 02 6a 24 75 3e 61 e2 38 d8 8c bb b5 ea 69 b3 d3 87 62 17 7f 31 e5 38 67 e4 3f df 8b 8b b3 ec 6f b5 d5 81 64 10 78 36 d5 3e 61 e2 38 d8 8c bb 0e 51 d2 08 68 3c d9 ad d8 05 20 3e 61 e2 38 d8 8c bb 4a 15 96 4c 2c 78 9d ea 9f 1b ac 3e 61 e2 38 d8 8c bb"
cipherlist = ciphertext.split(" ")

intercepts = "38 Eb 8E 09 00 80 04 00 00 ab 00 38 Eb 8E 89 00 15 6d 38 Eb 8E 09 00 80 05 ff ff 81 3f 38 Eb 8E 89 00 15 6d 38 Eb 8E 09 00 80 05 2c 78 20 24 38 Eb 8E 89 00 15 6d"
interceptlist = intercepts.split(" ")
#print(interceptlist[10])
#Cipherlist length is 108, Intercept length is 54
keychain =[]
key = 0
for x in range(0, 8):
#generate keys
	keychain.append(hex(int(cipherlist[x], base=16)^int(cipherlist[x+1], base=16)^int(interceptlist[x], base=16)))
			
print("Cracked Encryption key: ")
for x in keychain:
	
	print(chr(int((x), 0)), end = " ")


print(" ")
print("Decrypted output:")
print("Update")
for x in range (0, 11):
	if key >=7:
		key%=7
	if x ==11:
		keychain.append(hex(int(cipherlist[x], base=16)^int(interceptlist[x], base=16)))
	else:
		print(hex((int(keychain[key], base=16)^int(cipherlist[x], base=16)^int(cipherlist[x+1], base=16))), end = " ")
	key+=1
print(" ")
key=0
print("ack")	
for x in range (11, 18):
	if key >=7:
		key%=7
	if x ==18:
		keychain.append(hex(int(cipherlist[x], base=16)^int(interceptlist[x], base=16)))
	else:
		print(hex((int(keychain[key], base=16)^int(cipherlist[x], base=16)^int(cipherlist[x+1], base=16))), end = " ")
	key+=1
key=0
print(" ")
print("Update")	
for x in range (18, 29):
	if key >=7:
		key%=7
	if x ==29:
		keychain.append(hex(int(cipherlist[x], base=16)^int(interceptlist[x], base=16)))
	else:
		print(hex((int(keychain[key], base=16)^int(cipherlist[x], base=16)^int(cipherlist[x+1], base=16))), end = " ")
	key+=1
key=0
print(" ")
print("Ack")	
for x in range (29, 36):
	if key >=7:
		key%=7
	print(hex((int(keychain[key], base=16)^int(cipherlist[x], base=16)^int(cipherlist[x+1], base=16))), end = " ")
	key+=1

key=0
print(" ")
print("Update")	
for x in range (36, 47):
	if key >=7:
		key%=7
	print(hex((int(keychain[key], base=16)^int(cipherlist[x], base=16)^int(cipherlist[x+1], base=16))), end = " ")
	key+=1

key=0
print(" ")
print("Ack")	
for x in range (47, 54):
	if key >=7:
		key%=7
	print(hex((int(keychain[key], base=16)^int(cipherlist[x], base=16)^int(cipherlist[x+1], base=16))), end = " ")
	key+=1
key=0
print(" ")
print("Update")	
for x in range (54, 65):
	if key >=7:
		key%=7
	print(hex((int(keychain[key], base=16)^int(cipherlist[x], base=16)^int(cipherlist[x+1], base=16))), end = " ")
	key+=1
key=0
print(" ")
print("Ack")	
for x in range (65, 72):
	if key >=7:
		key%=7
	print(hex((int(keychain[key], base=16)^int(cipherlist[x], base=16)^int(cipherlist[x+1], base=16))), end = " ")
	key+=1
key=0
print(" ")
print("Update")	
for x in range (72, 83):
	if key >=7:
		key%=7
	print(hex((int(keychain[key], base=16)^int(cipherlist[x], base=16)^int(cipherlist[x+1], base=16))), end = " ")
	key+=1
key=0
print(" ")
print("Ack")	
for x in range (83, 90):
	if key >=7:
		key%=7
	print(hex((int(keychain[key], base=16)^int(cipherlist[x], base=16)^int(cipherlist[x+1], base=16))), end = " ")
	key+=1
key=0
print(" ")
print("Update")	
for x in range (90, 101):
	if key >=7:
		key%=7
	print(hex((int(keychain[key], base=16)^int(cipherlist[x], base=16)^int(cipherlist[x+1], base=16))), end = " ")
	key+=1
key=0
print(" ")
print("Ack")	
for x in range (101, 108):
	if key >=7:
		key%=7
	if x >=107:
		print(hex((int(keychain[key], base=16)^int(cipherlist[x], base=16))), end = " ")
	if x < 107:
		print(hex((int(keychain[key], base=16)^int(cipherlist[x], base=16)^int(cipherlist[x+1], base=16))), end = " ")
	key+=1
#print(len(keychain1))
#print(len(interceptlist))
	 
#print((hex(0x8c^0x15^0xbb)))
#print((hex(0x6954226854676854^0xabf477adcd997c)))

