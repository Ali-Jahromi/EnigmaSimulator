#!/usr/bin/env python3

alphabet = 'abcdefghijklmnopqrstuvwxyz'
plugAlphabet = 'abcdefghijklmnopqrstuvwxyz'
textAfterPlug = ''
fn = "todays_rotor_state.enigma"
with open(fn, 'r') as inprotors:
    dat = inprotors.readlines()
    rotors = [ line.strip() for line in dat ]

ctr = 1
for i in rotors:
    print(f"Rotor{ctr}: {i}")
    ctr += 1
r1 = rotors[0]
r2 = rotors[1]
r3 = rotors[2]

print(f"Alphabet: {alphabet}")
def plugBoard(swappingPairList):
    global plugAlphabet
    for pair in swappingPairList:
        tmpList = list(plugAlphabet)
        tmp = tmpList[plugAlphabet.find(pair[0])]
        tmpList[plugAlphabet.find(pair[0])] = tmpList[plugAlphabet.find(pair[1])]
        tmpList[plugAlphabet.find(pair[1])] = tmp
        plugAlphabet = ''.join(tmpList)
    print(f"Alphabet after connecting plugboard: {plugAlphabet}")

def reflector(c):
    return alphabet[len(alphabet)-alphabet.find(c)-1]

def enigma_one_char(c):
    #In the first and last assignments using plugAlphabet to use the swapped list of words from plugboard
    global textAfterPlug
    c1 = r1[plugAlphabet.find(c)]
    textAfterPlug += plugAlphabet[alphabet.find(c)]
    c2 = r2[alphabet.find(c1)]
    c3 = r3[alphabet.find(c2)]
    reflected = reflector(c3)
    c3 = alphabet[r3.find(reflected)]
    c2 = alphabet[r2.find(c3)]
    c1 = plugAlphabet[r1.find(c2)]
    return c1

def rotate_rotors():
    global r1, r2, r3
    r1 = r1[1:] + r1[0]
    if state % 26:
        r2 = r2[1:] + r2[0]
    if state % (26*26):
        r3 = r3[1:] + r3[0]


plain = 'aliqabqabfg'
cipher = ''
state = 0
plugPairs = [['a','b'], ['z', 'y'], ['i','q']]
plugBoard(plugPairs)
print(f"Plaintext: {plain}")
for c in plain:
    state += 1
    cipher += enigma_one_char(c)
    rotate_rotors()
print(f"Text After Plugboard: {textAfterPlug}")
print(f"Cipher-text: {cipher}")
