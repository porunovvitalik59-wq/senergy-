list1 = set(map(int, input().split()))
list2 = set(map(int, input().split()))

common_count = len(list1 & list2)  # пересечение множеств
print(common_count)
