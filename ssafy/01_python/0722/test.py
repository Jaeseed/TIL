def all_list_sum(lst):
    lists = []
    total = 0
    for i in lst:
        lists += i
    print(lists)
    for n in lists:
        total += n
    return total

print(all_list_sum([[1],[2,3],[4,5,6],[7,8,9,10]]))

