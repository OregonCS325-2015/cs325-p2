# this is a tester file to generate data

import cs325_p2, io

# Part 4
#for A in range(2000, 2201, 10):
#    V = [1,5,10,25,50]
#    C,m = cs325_p2.changeslow(A, V)
#    print 'changeslow for A:',A,'m =',m

# for A in range(2000, 2201, 10):
#     V = [1,5,10,25,50]
#     C,m = cs325_p2.changegreedy(A, V)
#     print 'changegreedy for A:',A,'m =',m

# for A in range(2000, 2201, 10):
#    V = [1,5,10,25,50]
#    m = cs325_p2.changedp(A, V)
#    print 'changedb for A:',A,'m =',m


# Part 5
# io.writeFile('', 'p5v1changeslow2k.txt', 'changeslow, A [2000, 2200], V1=[1,2,6,12,24,48,60]', 'w')
# for A in range(2000, 2201):
#    V1 = [1,2,6,12,24,48,60]
#    C,m = cs325_p2.changeslow(A, V1)
#    print 'changeslow for V1,A:',A,'m =',m
#    io.writeFile('', 'p5v1changeslow2k.txt', str(m))

# io.writeFile('', 'p5v2changeslow2k.txt', 'changeslow, A [2000, 2200], V2=[1,6,13,37,15]', 'w')
# for A in range(2000, 2201):
#    V2 = [1,6,13,37,150]
#    C,m = cs325_p2.changeslow(A, V2)
#    print 'changeslow for V2,A:',A,'m =',m
#    io.writeFile('', 'p5v2changeslow2k.txt', str(m))

# io.writeFile('', 'p5v1changegreedy2k.txt', 'changegreedy, A [2000, 2200], V1=[1,2,6,12,24,48,60]', 'w')
# for A in range(2000, 2201):
#     V1 = [1,2,6,12,24,48,60]
#     C,m = cs325_p2.changegreedy(A, V1)
#     print 'changegreedy for V1,A:',A,'m =',m
#     io.writeFile('', 'p5v1changegreedy2k.txt', str(m))
#
# io.writeFile('', 'p5v2changegreedy2k.txt', 'changegreedy, A [2000, 2200], V2=[1,6,13,37,15]', 'w')
# for A in range(2000, 2201):
#     V2 = [1,6,13,37,150]
#     C,m = cs325_p2.changegreedy(A, V2)
#     print 'changegreedy for V2,A:',A,'m =',m
#     io.writeFile('', 'p5v2changegreedy2k.txt', str(m))

io.writeFile('', 'p5v1changedb2k.txt', 'changedb, A [2000, 2200], V1=[1,2,6,12,24,48,60]', 'w')
for A in range(2000, 2201):
    V1 = [1,2,6,12,24,48,60]
    m = cs325_p2.changedp(A, V1)
    print 'changedb for V1,A:',A,'m =',m
    io.writeFile('', 'p5v1changedb2k.txt', str(m))

io.writeFile('', 'p5v2changedb2k.txt', 'changedb, A [2000, 2200], V2=[1,6,13,37,15]', 'w')
for A in range(2000, 2201):
    V2 = [1,6,13,37,150]
    m = cs325_p2.changedp(A, V2)
    print 'changedb for V2,A:',A,'m =',m
    io.writeFile('', 'p5v2changedb2k.txt', str(m))

# io.writeFile('', 'p5v1changegreedy10k.txt', 'changegreedy, A [10000, 10200], V1=[1,2,6,12,24,48,60]', 'w')
# for A in range(10000, 10201):
#     V1 = [1,2,6,12,24,48,60]
#     C,m = cs325_p2.changegreedy(A, V1)
#     print 'changegreedy for V1,A:',A,'m =',m
#     io.writeFile('', 'p5v1changegreedy10k.txt', str(m))
#
# io.writeFile('', 'p5v2changegreedy10k.txt', 'changegreedy, A [10000, 10200], V2=[1,6,13,37,150]', 'w')
# for A in range(10000, 10201):
#     V2 = [1,6,13,37,150]
#     C,m = cs325_p2.changegreedy(A, V2)
#     print 'changegreedy for V2,A:',A,'m =',m
#     io.writeFile('', 'p5v2changegreedy10k.txt', str(m))

io.writeFile('', 'p5v1changedb10k.txt', 'changedb, A [10000, 10200], V1=[1,2,6,12,24,48,60]', 'w')
for A in range(10000, 10201):
    V1 = [1,2,6,12,24,48,60]
    m = cs325_p2.changedp(A, V1)
    print 'changedb for V1,A:',A,'m =',m
    io.writeFile('', 'p5v1changedb10k.txt', str(m))

io.writeFile('', 'p5v2changedb10k.txt', 'changedby, A [10000, 10200], V2=[1,6,13,37,150]', 'w')
for A in range(10000, 10201):
    V2 = [1,6,13,37,150]
    m = cs325_p2.changedp(A, V2)
    print 'changedb for V2,A:',A,'m =',m
    io.writeFile('', 'p5v2changedb10k.txt', str(m))


# Part 6
# io.writeFile('', 'p5v1changeslow2k.txt', 'changeslow, A [2000, 2200], V1=[1,2,6,12,24,48,60]', 'w')
# for A in range(2000, 2201):
#    V1 = [1,2,6,12,24,48,60]
#    C,m = cs325_p2.changeslow(A, V1)
#    print 'changeslow for V1,A:',A,'m =',m
#    io.writeFile('', 'p5v1changeslow2k.txt', str(m))

# io.writeFile('', 'p5v2changeslow2k.txt', 'changeslow, A [2000, 2200], V2=[1,6,13,37,15]', 'w')
# for A in range(2000, 2201):
#    V2 = [1,6,13,37,150]
#    C,m = cs325_p2.changeslow(A, V2)
#    print 'changeslow for V2,A:',A,'m =',m
#    io.writeFile('', 'p5v2changeslow2k.txt', str(m))

# io.writeFile('', 'p5v1changegreedy2k.txt', 'changegreedy, A [2000, 2200], V1=[1,2,6,12,24,48,60]', 'w')
# for A in range(2000, 2201):
#     V1 = [1,2,6,12,24,48,60]
#     C,m = cs325_p2.changegreedy(A, V1)
#     print 'changegreedy for V1,A:',A,'m =',m
#     io.writeFile('', 'p5v1changegreedy2k.txt', str(m))
#
# io.writeFile('', 'p5v2changegreedy2k.txt', 'changegreedy, A [2000, 2200], V2=[1,6,13,37,15]', 'w')
# for A in range(2000, 2201):
#     V2 = [1,6,13,37,150]
#     C,m = cs325_p2.changegreedy(A, V2)
#     print 'changegreedy for V2,A:',A,'m =',m
#     io.writeFile('', 'p5v2changegreedy2k.txt', str(m))

# io.writeFile('', 'p5v1changedb2k.txt', 'changedb, A [2000, 2200], V1=[1,2,6,12,24,48,60]', 'w')
# for A in range(2000, 2201):
#    V1 = [1,2,6,12,24,48,60]
#    C,m = cs325_p2.changedp(A, V1)
#    print 'changedb for V1,A:',A,'m =',m
#     io.writeFile('', 'p5v1changedb2k.txt', str(m))
#