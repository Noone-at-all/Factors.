def CFS():
    arga = int(raw_input('What do you want factored?'))
    if arga < 0:
        arg1 = arga * -1
    arg2 = arg1
    CF = []
    l = 1
    g = arg1
    for item in range(g):
        if arg1 % l == 0 and arg2 % l == 0:
            CF.append(l)
            l += 1
        else:
            l += 1
    CF.sort()
    h = CF[::-1]
    oh = 0
    FList = []
    for item in CF:
        FList.append(''+ str(h[oh]) +' * '+ str(item) + '')
        oh += 1
    print FList
    v = 0
    Want = int(raw_input('Which difference/sum do you need?'))
    CFDD = {}
    CFSD = {}
    for item in CF:
        Diff = h[v] - CF[v]
        Sum = h[v] + CF[v]
        CFDD[Diff] = 'Diff: %s, factors: %s, %s, sum: %s.' % (Diff, h[v], CF[v], Sum)
        CFSD[Sum] = 'Diff: %s, factors: %s, %s, sum: %s.' % (Diff, h[v], CF[v], Sum)
        v += 1
    if Want < 0:
        Want = Want * -1
        if arga > 0 and Want not in CFDD:
            print 'You\'ll need to change both of the signs to negative.'
        else:
            print 'You\'ll need to change the smaller number\'s sign to negative.'
    if Want in CFDD:
        print CFDD[Want]
        print 'Diff'
    elif Want in CFSD:
        print CFSD[Want]
        print 'Sum'
