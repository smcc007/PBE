#To Do:
#1.) configure all code below the for loop into a function
    #a.) pass in orgTxt and assert it is text
    #b.) pass in shift_by and assert it is an integer
    #c.) constrain the shift to wrap around and only use alphabetic characters.
#2.) read up on main function in python...start creating a class

#Define alphabet of characters for mapping
arr_Alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R','S','T', 'R', 'U', 'V', 'W', 'X', 'Y', 'Z' ]

#Declare local variables
#To be replaced by vairables passed into the scrip
#Or write this as a class.
orgTxt = "BACZ"
cipherTxt = ""
shift_by = 2
shifted_index = 0

#iterate over the entire length of the input string
for x in range(0, len(orgTxt)):
    #print ("Original character: %s, after shift %s " % (input[x], chr(ord(input[x])+shift_by)))
    #find key
    #find character position in arr_Alpha
    print orgTxt[x]
    idx = arr_Alpha.index(orgTxt[x])

    #shift by shift_by value with wrap around length of list
    shifted_index = (idx + shift_by) % len(arr_Alpha)

    cipherTxt += arr_Alpha[shifted_index]

print ("Original text:  %s" %orgTxt)
print ("Output text:    %s" %cipherTxt)
