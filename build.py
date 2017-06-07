import pandas as pd
def solution(lst):
    """
    Enter your code here
    """
    items = []
    for i in lst:
        items.append(i)
    return items
df = pd.Series(data=[2,4,6,8,10])

print(solution(df))
