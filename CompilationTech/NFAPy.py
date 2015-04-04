#S,D,F=input()
#S = '011010'
#D = {'1':[(1,2) , (1,4) , (5,6) , (6,6)],'0':[(3,4),(4,5)],0:[(1,2) , (2,3) , (4,5)]}

S = 'a'
D = {'a':[ (1,1) , (1,2) , (2,2) , (3,4) ] , 'b' : [ (1,2) , (2,2) , (2,3) , (4,5) ] , 0 : [(1,2) , (2,3)] }

F = 5

E={1:1}
for i in D[0]:
 for a,b in D[0]:
     E[a]=a|E.get(b,b)
s=E[1]
for c in S:
 t,s=s,0
 for a,b in D[c]:
     s|= int(t/a%2)*int(E.get(b,b))
if F&s>0:
    print("Yes")
else:
    print("No")
#print["Not a chance!","Accepted!"][F&s>0]

'''
F = [5]
E={1:1}
for i in D[0]:
 for a,b in D[0]:
     E[a]=a|E.get(b,b)
print(E)
s=E[1]
for c in S:
 t,s=s,0
 for a,b in D[c]:
     s |= int(t/a%2)*int(E.get(b,b))
ok = False
for fin in F:
    print(fin)
    print(fin&s)
    if fin&s>0:
        print("Yes")
        ok = True
        break
if ok == False:
    print("No")
'''
