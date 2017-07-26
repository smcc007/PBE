#create a first pass at the RSA scheme

#RSA takes advantage of the "hardness" of factoring large numbers
#that is there exists a set of problems for computers that are
#assumed to be impossible to be solved

#For now, this only works for encryption/decryption
#The generateion of the keys will be done later.


import binascii

private_key = 0
public_key = 0

input_text = "Hello World"
output_text = bin(int(binascii.hexlify(input_text), 16))
print binascii.hexlify(input_text)
print int(binascii.hexlify(input_text), 16)
print output_text[2:10]
print output_text[11:19]
print output_text[20:28]

#I have the input text converted to a number which can now be used in the modular arithmatic.
# what is the damn ecncryption scheme

# C = m^e*(mod n)
# where e is the public key
# where m is message (converted to a number) with padding
# n = p*q where p and q are prime numbers.
