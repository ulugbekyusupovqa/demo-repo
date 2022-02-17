print("Real MAdrid")

print("Real\nBarcelona")        # in different line

print("My Madrid \"Real\"")     # putting quotation mark

a = "Real Madrid"
print(a + " is the Best Club")

print(a.lower())                            # Everything in a lower case
print(a.upper())                            # Everything in a upper case
print(a.isupper())                          # cheching is a sting "a" is upper case
print(a.upper().isupper())
print(len(a))                               # number of charackters in string "a"
print(a[0])                                 # getting first character in string "a"
print(a.index("d"))                         # finding out where letter "d" is
print(a.replace("Real", "Atletico"))        # replacing "Real" with "Atletico"

print([a.index("R"), a.index("r")])
