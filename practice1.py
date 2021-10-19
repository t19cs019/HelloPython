import random

a = random.randint(0,2)
b = random.randint(0,2)

if a == 0:
    A = 'グー'
elif a == 1:
    A = 'チョキ'
else:
    A = 'パー'
     
if b == 0:
    B = 'グー'
elif b == 1:
    B = 'チョキ'
else:
    B = 'パー'
    
print(a)
print(b)

print('Aの手：', A ,' v.s. Bの手:', B)

if a == b:
    s = '引き分け'
elif (a == 0 and b == 1) or (a == 1 and b == 2) or (a == 2 and b == 0):
    s = 'Aの勝ち'
else:
    s = 'Bの勝ち'
print(s)

