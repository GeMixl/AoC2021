cuboids = [s.replace('x=','').replace(',y=',' ').replace(',z=',' ').replace('..',' ') for s in open("input_day22.txt").readlines()]
cuboids = [s.replace('on','1').replace('off','0') for s in cuboids]
cuboids = [[int(x) for x in s.split()] for s in cuboids]
#cuboids = [[c[0]] + list(map(lambda x: -50 if x<-50 else x if x<50 else 50, c[1:]))
#           for c
#           in cuboids
#           if (-50<c[1]<50 or -50<c[2]<50) and (-50<c[3]<50 or-50<c[4]<50) and (-50<c[5]<50 or-50<c[6]<50)
#           ] # for part 1

# a cuboid is represented as [+1/-1,xmin,xmax,ymin,ymax,zmin,zmax]
# where +1 is 'added cuboid' and -1 is 'subtracted cuboid'

# return the cuboid at the intersection of cuboids s and t
# if cuboid t is added, the intersection is subtracted, and vice versa
def intersection(s,t):
    mm = [lambda a,b:-b,max,min,max,min,max,min]
    n = [mm[i](s[i],t[i]) for i in range(7)]
    return None if n[1] > n[2] or n[3] > n[4] or n[5] > n[6] else n

cores = []
for cuboid in cuboids:
    toadd = [cuboid] if cuboid[0] == 1 else [] # add cuboid to core if 'on'
    for core in cores:
        inter = intersection(cuboid,core)
        if inter:
            toadd += [inter] # if nonempty, add to the core later
    cores += toadd

def countoncubes(cores):
    oncount = 0
    for c in cores:
        oncount += c[0] * (c[2]-c[1]+1) * (c[4]-c[3]+1) * (c[6]-c[5]+1)
    return oncount

print('On cubes:', countoncubes(cores))