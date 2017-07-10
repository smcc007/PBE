import sys

#Define alphabet of characters for mapping, can be extended as required.
arr_Alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R','S','T', 'R', 'U', 'V', 'W', 'X', 'Y', 'Z' ]

#Declare local variables from
orgTxt = (sys.argv[1]).upper()
shift_by = int(sys.argv[2]) #shifted by values

print ("This is the orginal text:   " + orgTxt + "and it will be shifted by %d places" % shift_by)

cipherTxt = ""
shifted_index = 0

#iterate over the entire length of the input string
for x in range(0, len(orgTxt)):
    try: #character shift
        #find character position in arr_Alpha
        idx = arr_Alpha.index(orgTxt[x])
        #shift by shift_by value with wrap around length of list
        shifted_index = (idx + shift_by) % len(arr_Alpha)
        cipherTxt += arr_Alpha[shifted_index]
    except: #if the caeser substitution fails in anyway, keep the orginal
            #character
        cipherTxt += orgTxt[x]

print ("Original text:  %s" %orgTxt)
print ("Output text:    %s" %cipherTxt)
