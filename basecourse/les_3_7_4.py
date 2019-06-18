sides = {k: 0 for k in ["север", "запад", "юг", "восток"]}
for _ in range(int(input())):
    side, dist = input().split()
    sides[side] += int(dist)
print(sides["восток"]-sides["запад"], sides["север"]-sides["юг"])
