n , k = map(int, input().split())
frequencies = {}
top = set()

for i in range(n):
    name = input()
    if name in frequencies:
        frequencies[name] += 1
    else:
        frequencies[name] = 1
    
    if frequencies[name]>=k:
        top.add(name)
        
top = sorted(top)

for i in top:
    print(i)
        
    