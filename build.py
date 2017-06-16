import pandas as p

def solution(pd):
    l=[]
    for i in pd:
        l.append(i)
    return l

pd = p.Series(data=[2,4,6,8,10])
print(solution(pd))
