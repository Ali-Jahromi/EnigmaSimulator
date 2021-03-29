import random
import pickle

alphabet = 'abcdefghijklmnopqrstuvwxyz'

r1 = list(alphabet)
random.shuffle(r1)
r1 = ''.join(r1)

r2 = list(alphabet)
random.shuffle(r2)
r2 = ''.join(r2)

r3 = list(alphabet)
random.shuffle(r3)
r3 = ''.join(r3)

with open('./todays_rotor_state.enigma', 'w') as out:
    out.write(r1+"\n"+r2+"\n"+r3+"\n")
