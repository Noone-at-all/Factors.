def CFS():
    arga = int(raw_input('What do you want factored?'))
    if arga < 0:
        arg1 = arga * -1
    elif arga > 0:
        arg1 = arga
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
    v = 0
    Want = int(raw_input('Which difference/sum do you need?'))
    CFDD = {}
    CFSD = {}
    DatInt = 3
    for item in CF:
        Diff = h[v] - CF[v]
        Sum = h[v] + CF[v]
        CFDD[Diff] = 'Diff: %s, factors: %s,(-)%s, sum: %s.' % (Diff, h[v], CF[v], Sum)
        CFSD[Sum] = 'Diff: %s, factors: %s,(+)%s, sum: %s.' % (Diff, h[v], CF[v], Sum)
        v += 1
    if Want in CFDD:
        print CFDD[Want]
        print 'Diff'
    if Want in CFSD:
        print CFSD[Want]
        print 'Sum'
    elif Want not in CFSD and Want not in CFDD:
        print '%s is not achievable with factors of %s' % (Want, arga)
    Want = Want * -1
    print 'Inverted diff/sum input, make changes as needed.'
    if Want in CFDD:
        print CFDD[Want]
        print 'Diff'
        DatInt = 1
    if Want in CFSD:
        print CFSD[Want]
        print 'Sum'
        DatInt = 1
    if Want not in CFSD and Want not in CFDD:
        print '%s is not achievable with factors of %s' % (Want, arga)
        DatInt = 2
    if DatInt == 3:
        print 'You have encountered bug1, the number you want is apparently in one of the the factor lists, but the program didn\'t print it'
    print 'Source EQ: x^2 + %sx + %s' % (Want*-1, arga)
