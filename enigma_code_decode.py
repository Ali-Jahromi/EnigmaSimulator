#!/usr/bin/env python3

alphabet = 'abcdefghijklmnopqrstuvwxyz'
fn = "todays_rotor_state.enigma"
with open(fn, 'r') as inprotors:
    dat = inprotors.readlines()
    rotors = [ line.strip() for line in dat ]
print(rotors)
r1 = rotors[0]
r2 = rotors[1]
r3 = rotors[2]

def reflector(c):
    return alphabet[len(alphabet)-alphabet.find(c)-1]

def enigma_one_char(c):
    c1 = r1[alphabet.find(c)]
    c2 = r2[alphabet.find(c1)]
    c3 = r3[alphabet.find(c2)]
    reflected = reflector(c3)
    c3 = alphabet[r3.find(reflected)]
    c2 = alphabet[r2.find(c3)]
    c1 = alphabet[r1.find(c2)]
    return c1

def rotate_rotors():
    global r1, r2, r3
    r1 = r1[1:] + r1[0]
    if state % 26:
        r2 = r2[1:] + r2[0]
    if state % (26*26):
        r3 = r3[1:] + r3[0]


plain = 'TestPlainText'
cipher = ''
state = 0 
for c in plain:
    state += 1
    cipher += enigma_one_char(c)
    rotate_rotors()
    

print(cipher)
