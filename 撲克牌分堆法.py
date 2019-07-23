# coding: utf-8
import random
from random import choice
A=['A','2','3','4','5','6','7','8','9','T','J','Q','K']
B=['♠','♥','♦','♣']
C=[]
small=[]
S=[]
for i in range(len(B)):
    for j in range(len(A)):
        C.append(B[i]+A[j])
for k in range(1,5):      #5-----分4堆
    for j in range(13):      # 13----每堆分13張
        a=random.choice(C)
        small.append(a)
        C.remove(a)
    S=S+[small]        
    small=[]    
print(S)
