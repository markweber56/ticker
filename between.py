str = "<div>1234</div><div>text1</div><div></div><div>third thing</div>"

c1 = ">"
c2 = "<"
between = []
c1idx = []
c2idx = []

startIdx = 0
if str[0] == c2:
    startIdx = 1

for i in range(startIdx,len(str)):
    if str[i]==c1:
        c1idx.append(i)
    if str[i]==c2:
        c2idx.append(i)
        
if c2idx[0]<c1idx[0]:
    c2idx = cdix[1:]

print("starting indices: ",c1idx)
print("closing indices: ",c2idx)

for i in range(len(c2idx)):
    v = str[c1idx[i]+1:c2idx[i]]
    if len(v)>0:
        between.append(v)

print('between: ',between)
