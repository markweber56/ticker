def between(str,c1,c2):

    between = [] # array of values between divs
    c1idx = [] # indices of c1 (character 1)
    c2idx = [] # indices

    # determine which characer of string to start on
    startIdx = 0
    if str[0] == c2:
        startIdx = 1

    # get indices of characters
    for i in range(0,len(str)):
        if str[i]==c1:
            c1idx.append(i)
        if str[i]==c2:
            c2idx.append(i)

    if c2idx[0]<c1idx[0]:
        c2idx=c2idx[1:]
    '''
    print("starting indices: ",c1idx)
    print("starting indices len: ",len(c1idx))
    print("closing indices: ",c2idx)
    print("closing indices len: ",len(c2idx))
    '''
    
    for i in range(len(c2idx)):
        v = str[c1idx[i]+1:c2idx[i]]
        if len(v)>0:
            between.append(v)

    return between
