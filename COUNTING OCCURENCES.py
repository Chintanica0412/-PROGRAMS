def count_occurrence(numlist, num):
    count = 0
    for value in numlist:
        if value == num:
            count = count + 1
    return count
list1 = [1, 2, 3, 4, 3, 3, 3]
print("List is:", list1)
print("Occurrence of 3:", count_occurrence(list1, 3))
print("Occurrence of 1:", count_occurrence(list1, 1))
print("Occurrence of 4:", count_occurrence(list1, 4))