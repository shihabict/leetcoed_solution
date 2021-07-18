def sub_lists(l):
    lists = [[]]
    for i in range(len(l)+1):
        for j in range(i):
            lists.append(l[j: i])
    return max([sum(li) for li in lists])


# driver code
l1 = [-1]
print(sub_lists(l1))