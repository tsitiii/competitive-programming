# Problem: C - Penalty Shootout - https://codeforces.com/gym/596141/problem/C

t =int(input())


def check(round, p1,p2):
    c1 = (10-(round-1))//2
    c2 = 10-(round-1) - c1
    if p1+c1 < p2 or p2+c2 < p1:
        return round-1
    return -1

def Roundd(p1, p2, round):
    if check(round,p1,p2) != -1:
        return check(round,p1,p2)
    if round == 10:
        return round
    if round %2 ==0:
        if string[round-1] == '?':
            return min(Roundd(p1, p2, round+1), Roundd(p1,p2+1, round+1))
        else:
            return Roundd(p1, p2+int(string[round-1]), round + 1)
    else:
        if string[round-1] == '?':
            return min(Roundd(p1, p2, round+1), Roundd(p1 +1 ,p2, round+1))
        else:
            return Roundd(p1 + int(string[round-1]), p2, round + 1)
for _ in range(t):
    string = input()
    print(Roundd(0,0,1))
