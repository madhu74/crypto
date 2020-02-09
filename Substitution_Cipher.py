"""
This is a program to break the substitution cipher
"""
from collections import OrderedDict
# http://practicalcryptography.com/ciphers/simple-substitution-cipher/

input_string = """ztrfqvdjrzqt
rci wzyabi wdmwrzrdrzqt jzacif zw g jzacif rcgr cgw miit zt dwi hqf ygtx cdtvfivw qh xigfw (gt iojibbitr czwrqfx zw 
lzsit zt wzyqt wztlcw 'rci jqvi mqqk'). zr mgwzjgbbx jqtwzwrw qh wdmwrzrdrztl isifx abgztrior jcgfgjrif hqf g vzhhifitr 
jzacifrior jcgfgjrif. zr vzhhifw hfqy rci jgiwgf jzacif zt rcgr rci jzacif gbacgmir zw tqr wzyabx rci gbacgmir wczhriv, 
zr zw jqyabiribx udymbiv.
rci wzyabi wdmwrzrdrzqt jzacif qhhifw sifx bzrrbi jqyydtzjgrzqt wijdfzrx, gtv zr pzbb mi wcqpt rcgr zr jgt mi igwzbx 
mfqkit isit mx cgtv, iwaijzgbbx gw rci yiwwgliw mijqyi bqtlif (yqfi rcgt wisifgb cdtvfiv jzacifrior jcgfgjrifw).""".upper()

TRUTH_DICT = {"a": 8.167, "b": 1.492, "c": 2.202, "d": 4.253, "e": 12.702, "f": 2.228, "g": 2.015, "h": 6.094,
              "i": 6.966, "j": 0.153,
              "k": 1.292, "l": 4.025, "m": 2.406, "n": 6.749, "o": 7.507, "p": 1.929, "q": 0.095, "r": 5.987,
              "s": 6.327, "t": 9.356, "u": 2.758, "v": 0.978,
              "w": 2.560, "x": 0.150, "y": 1.994, "z": 0.077}  # from https://en.wikipedia.org/wiki/Letter_frequency

current_frequency_dict = {}
alphabet_count = 0
#building the fequency dictionary
for value in input_string:
    if value.isalpha():
        if value in current_frequency_dict.keys():
            current_frequency_dict[value] = current_frequency_dict[value] + 1
        else:
            current_frequency_dict[value] = 1
        alphabet_count = alphabet_count + 1

frequency_percent_dict = {}

for value in current_frequency_dict:
    frequency_percent_dict[value] = (current_frequency_dict[value] / alphabet_count) * 100

print("Frequency_dict", current_frequency_dict)
print("alphabet_count", alphabet_count)
print("frequency_percent_dict", frequency_percent_dict)

new_dict = OrderedDict(sorted(frequency_percent_dict.items(), key=lambda t: t[1], reverse=True))
SORTED_TRUTH_DICT = OrderedDict(sorted(TRUTH_DICT.items(), key=lambda t: t[1], reverse=True))
print(new_dict)
print(SORTED_TRUTH_DICT)

i = 0 # keeping the substitution down to 4 characters.

for (key, value), (key1, value1) in zip(new_dict.items(), SORTED_TRUTH_DICT.items()):
    if key in input_string and i < 2:
        input_string = input_string.replace(key, key1) # replacing the characters
        i = i+1

print(input_string)
bag_dict = {}

# "tCe" -> "the"
# thGt -> "that"
# "I"->"e", "R" ->"t", -> worked with frequency analysis
# "C" -> "H", "G"-> "a", -> looking for three and 2 letter words
# aW -> "as" and "haW" -> "has"
# so W -> s
# ZT, Zt Zs -> "could be is and it since t and s already substituted then Z->i"
# iT -> could be is or in in two letter words "T" -> "N"
input_string = input_string.replace("C", "h")
input_string = input_string.replace("G", "a")
input_string = input_string.replace("W", "s")
input_string = input_string.replace("Z", "i")
input_string = input_string.replace("T", "n")
# the letter intFQVDJtiQn could be "introduction" FQVDJ -> roduc
# print(input_string)

for i,j in zip([i for i in "FQVDJ"], [j for j in "roduc"]):
    if i in input_string:
        input_string = input_string.replace(i,j)
# suMstitution -> substitution
input_string = input_string.replace("M", "b")
# ciAher -> cipher
input_string = input_string.replace("A", "p")
# oHHers and diHHers H-> f
input_string = input_string.replace("H", "f")
# aBphabet and alphabets B-> L
input_string = input_string.replace("B", "l")
# siYple -> simple "Y" -> "M"
input_string = input_string.replace("Y", "m")
# print(input_string)

'''introduction
the simple substitution cipher is a cipher that has been in use for manX hundreds of Xears (an eOcellent historX is
LiSen in simon sinLhs 'the code booK'). it basicallX consists of substitutinL eSerX plainteOt character for a different
cipherteOt character. it differs from the caesar cipher in that the cipher alphabet is not simplX the alphabet shifted,
it is completelX Uumbled.
the simple substitution cipher offers SerX little communication securitX, and it Pill be shoPn that it can be easilX
broKen eSen bX hand, especiallX as the messaLes become lonLer (more than seSeral hundred cipherteOt characters).'''

# easilX and especiallX X-> y  messaLes and lonLer L -> g
input_string = input_string.replace("X", "y")
input_string = input_string.replace("L", "g")
# print(input_string)

'''introduction
the simple substitution cipher is a cipher that has been in use for many hundreds of years (an eOcellent history is
giSen in simon singhs 'the code booK'). it basically consists of substituting eSery plainteOt character for a different
cipherteOt character. it differs from the caesar cipher in that the cipher alphabet is not simply the alphabet shifted,
it is completely Uumbled.
the simple substitution cipher offers Sery little communication security, and it Pill be shoPn that it can be easily
broKen eSen by hand, especially as the messages become longer (more than seSeral hundred cipherteOt characters).'''

# eOcellent ->  excellent, plainteOt -> plainteOt O->x

input_string = input_string.replace("O", "x")

# broKen  eSen broken even K-> k S ->v
input_string = input_string.replace("K", "k")
input_string = input_string.replace("S", "v")
# Uumbled "U" -> "j" and jumbles and shoPn and Pill P -> w
input_string = input_string.replace("U", "j")
input_string = input_string.replace("P", "w")

print(input_string)