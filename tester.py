# this is a tester file to generate data

import cs325_p2, io, time

dir = './reports/'

# Part 4
# for A in range(2000, 2201, 10):
#    V = [1,5,10,25,50]
#    start = time.time()
#    C,m = cs325_p2.changeSlow(A, V)
#    stop = time.time()
#    print 'changeslow for A:',A,'m =',m,' time:',stop-start

# for A in range(2000, 2201, 10):
#     V = [1,5,10,25,50]
#     start = time.time()
#     C,m = cs325_p2.changegreedy(A, V)
#     stop = time.time()
#     print 'changegreedy for A:',A,'m =',m,' time:',stop-start
#
# for A in range(2000, 2201, 10):
#    V = [1,5,10,25,50]
#    start = time.time()
#    m = cs325_p2.changedp(A, V)
#    stop = time.time()
#    print 'changedb for A:',A,'m =',m,' time:',stop-start


#######################################################################################################################
# Part 5
Alow = 100
Ahigh = 300

AnormalLow = 10000
AnormalHigh = 10201

io.writeFile(dir, 'p5changeSlowV1Low.txt', 'change slow, A [' + str(Alow) + ', ' + str(Ahigh) + '], V1=[1,2,6,12,24,48,60]', 'w')
io.writeFile(dir, 'p5changeSlowV2Low.txt', 'change slow, A [' + str(Alow) + ', ' + str(Ahigh) + '], V2=[1,6,13,37,15]', 'w')
io.writeFile(dir, 'p5changeGreedyV1Low.txt', 'change greedy, A [' + str(Alow) + ', ' + str(Ahigh) + '], V1=[1,2,6,12,24,48,60]', 'w')
io.writeFile(dir, 'p5changeGreedyV2Low.txt', 'change greedy, A [' + str(Alow) + ', ' + str(Ahigh) + '], V2=[1,6,13,37,15]', 'w')
io.writeFile(dir, 'p5changeDPV1Low.txt', 'change dp, A [' + str(Alow) + ', ' + str(Ahigh) + '], V1=[1,2,6,12,24,48,60]', 'w')
io.writeFile(dir, 'p5changeDPV2Low.txt', 'change dp, A [' + str(Alow) + ', ' + str(Ahigh) + '], V2=[1,6,13,37,15]', 'w')
io.writeFile(dir, 'p5changeGreedyV1High.txt', 'change greedy, A [' + str(AnormalLow) + ', ' + str(AnormalHigh) + '], V1=[1,2,6,12,24,48,60]', 'w')
io.writeFile(dir, 'p5changeGreedyV2High.txt', 'change greedy, A [' + str(AnormalLow) + ', ' + str(AnormalHigh) + '], V2=[1,6,13,37,150]', 'w')
io.writeFile(dir, 'p5changeGDPV1High.txt', 'change dp, A [' + str(AnormalLow) + ', ' + str(AnormalHigh) + '], V1=[1,2,6,12,24,48,60]', 'w')
io.writeFile(dir, 'p5changeGDPV2High.txt', 'change dp, A [' + str(AnormalLow) + ', ' + str(AnormalHigh) + '], V2=[1,6,13,37,150]', 'w')

for A in range(Alow, Ahigh):
    # V1 = [1,2,6,12,24,48,60]
    # start = time.time()
    # C,m = cs325_p2.changeSlow(A, V1)
    # stop = time.time()
    # io.writeFile(dir, 'p5changeSlowV1Low.txt', str(m) + ',' + str(stop-start))
    # V2 = [1,6,13,37,150]
    # start = time.time()
    # C,m = cs325_p2.changeSlow(A, V2)
    # stop = time.time()
    # io.writeFile(dir, 'p5changeSlowV2Low.txt', str(m) + ',' + str(stop-start))

    V1 = [1,2,6,12,24,48,60]
    start = time.time()
    C,m = cs325_p2.changegreedy(A, V1)
    stop = time.time()
    io.writeFile(dir, 'p5changeGreedyV1Low.txt', str(m) + ',' + str(stop-start))
    V2 = [1,6,13,37,150]
    start = time.time()
    C,m = cs325_p2.changegreedy(A, V2)
    stop = time.time()
    io.writeFile(dir, 'p5changeGreedyV2Low.txt', str(m) + ',' + str(stop-start))

    V1 = [1,2,6,12,24,48,60]
    start = time.time()
    m = cs325_p2.changedp(A, V1)
    stop = time.time()
    io.writeFile(dir, 'p5changeDPV1Low.txt', str(m) + ',' + str(stop-start))
    V2 = [1,6,13,37,150]
    start = time.time()
    m = cs325_p2.changedp(A, V2)
    stop = time.time()
    io.writeFile(dir, 'p5changeDPV2Low.txt', str(m) + ',' + str(stop-start))

for A in range(AnormalLow, AnormalHigh):
    V1 = [1,2,6,12,24,48,60]
    start = time.time()
    C,m = cs325_p2.changegreedy(A, V1)
    stop = time.time()
    io.writeFile(dir, 'p5changeGreedyV1High.txt', str(m) + ',' + str(stop-start))

    V2 = [1,6,13,37,150]
    start = time.time()
    C,m = cs325_p2.changegreedy(A, V2)
    stop = time.time()
    io.writeFile(dir, 'p5changeGreedyV2High.txt', str(m) + ',' + str(stop-start))

    V1 = [1,2,6,12,24,48,60]
    start = time.time()
    m = cs325_p2.changedp(A, V1)
    stop = time.time()
    io.writeFile(dir, 'p5changeGDPV1High.txt', str(m) + ',' + str(stop-start))

    V2 = [1,6,13,37,150]
    start = time.time()
    m = cs325_p2.changedp(A, V2)
    stop = time.time()
    io.writeFile(dir, 'p5changeGDPV2High.txt', str(m) + ',' + str(stop-start))

#######################################################################################################################
# Part 6
# Alow = 100
# Ahigh = 300
#
# io.writeFile(dir, 'p6changeslow2.txt', 'changeslow, A [' + str(Alow) + ', ' + str(Ahigh) + ']', 'w')
# io.writeFile(dir, 'p6changegreedy.txt', 'changegreedy, A [' + str(Alow) + ', ' + str(Ahigh) + ']', 'w')
# io.writeFile(dir, 'p6changedb.txt', 'changedb, A [' + str(Alow) + ', ' + str(Ahigh) + ']', 'w')
#
# for A in range(Alow, Ahigh):
#     V = [1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
#     start = time.time()
#     C, m = cs325_p2.changeSlow(A, V)
#     stop = time.time()
#     io.writeFile(dir, 'p6changeslow.txt', str(m) + ',' + str(stop - start))
#     start = time.time()
#     C, m = cs325_p2.changegreedy(A, V)
#     stop = time.time()
#     io.writeFile(dir, 'p6changegreedy.txt', str(m) + ',' + str(stop - start))
#     start = time.time()
#     m = cs325_p2.changedp(A, V)
#     stop = time.time()
#     io.writeFile(dir, 'p6changedb.txt', str(m) + ',' + str(stop - start))
