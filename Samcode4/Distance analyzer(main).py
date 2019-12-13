import pickle as p
Distances=p.load(open("Distances(the analyzed).protected" , "rb"))
City=input()
M=int(input())
N=int(input())
cities=[0]*N
for i in range(N):
    cities[i]=input()
ca=[0]*N
for i in range(N):
    ca[i]=cities[i].split()
print(ca)
