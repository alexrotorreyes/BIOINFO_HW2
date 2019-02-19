#BIOINFO HW2

from Bio.Seq import Seq
for x in range(10):
    ctr = x+1
    f = open("s%i.txt" %(ctr), "r")
    if f.mode == 'r':
            s = Seq(f.read())

    src = s.reverse_complement()

    print('seq %s is %i bases long' % ("1", len(s)))
    print('reverse complement is %s' % s.reverse_complement())

    aa = 0
    ac = 0
    at = 0
    ag = 0

    ca = 0
    cc = 0
    ct = 0
    cg = 0

    ga = 0
    gc = 0
    gt = 0
    gg = 0

    ta = 0
    tc = 0
    tt = 0
    tg = 0

    ccgg = 0
    agct = 0
    gatc = 0
    catg = 0
    acgt = 0
    aatt = 0

    a = 0
    c = 0
    g = 0
    t = 0

    aa = src.count_overlap("aa")
    ac = src.count_overlap("ac")
    at = src.count_overlap("at")
    ag = src.count_overlap("ag")

    ca = src.count_overlap("ca")
    cc = src.count_overlap("cc")
    ct = src.count_overlap("ct")
    cg = src.count_overlap("cg")

    ga = src.count_overlap("ga")
    gc = src.count_overlap("gc")
    gt = src.count_overlap("gt")
    gg = src.count_overlap("gg")

    ta = src.count_overlap("ta")
    tc = src.count_overlap("tc")
    tt = src.count_overlap("tt")
    tg = src.count_overlap("tg")

    a = src.count_overlap("a")
    c = src.count_overlap("c")
    t = src.count_overlap("t")
    g = src.count_overlap("g")

    ccgg = cc + gg
    agct = ag + ct
    gatc = ga + tc
    catg = ca + tg
    acgt = ac + gt
    aatt = aa + tt

    total = aa + ac + at + ag + ca + cc + ct + cg + ga + gc + gt + gg + ta + tc + tt + tg

    print("aa: ", aa)
    print("ac: ",  ac)
    print("at: ",  at)
    print("ag: ",  ag)

    print("ca: ", ca)
    print("cc: ", cc)
    print("ct: ", ct)
    print("cg: ", cg)

    print("ga: ", ga)
    print("gc: ", gc)
    print("gt: ", gt)
    print("gg: ", gg)

    print("ta: ", ta)
    print("tc: ", tc)
    print("tt: ", tt)
    print("tg: ", tg)

    print("total: ", total)

    #OBSERVED FREQUENCY
    o = cg/total


    #EXPECTED FREQUENCY
    e = (c/len(src))*(g/len(src))

    r = o/e

    print("o: ", o)
    print("e: ", e)
    print("r: ", r)