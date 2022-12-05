import random
grid =10
max_range = grid**2
p1,p2,p3,p4 = 0,0,0,0
v = [0,0,0,0]
dice = [[],[],[],[]]
updates = [[],[],[],[]]
win = [0,0,0,0]
snakes = {99:10, 95:76,91:54,62:22,57:24,52:11,43:17,32:5}
ladder = {4:45,6:25,40:77,47:66,50:93,61:98,68:87}
while True:
    for i in range(4):
        p = v[i]
        n = random.randint(1,6)
        dice[i].append(n)
        if v[i]+n<=max_range:
            v[i] = v[i]+n
            if v[i] in ladder:
                v[i] = ladder[v[i]]
            if v[i] in snakes:
                v[i] = snakes[v[i]]
            updates[i].append(v[i])
            if v[i]==max_range:
                win[i] = 1
                break
        else:
            updates[i].append(v[i])
    else:
        continue
    break

print("Players", "Dice Roll History",  "        Position story", "Win status" )
print("Red", updates[0], win[0])
print("Yellow", updates[1], win[1])
print("Blue", updates[2], win[2])
print("Green", updates[3], win[3])