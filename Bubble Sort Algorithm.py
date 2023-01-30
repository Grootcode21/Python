def bubble(a_list):
    indexing_length = len(a_list) - 1
    sorted_1 = False

    while not sorted_1:
        sorted_1 = True
        for i in range(0, indexing_length):
            if a_list[i] > a_list[i + 1]:
                sorted_1 = False
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
    return a_list


print(bubble([7, 11, -2, 6, 5, 8, 3, 40]))
print(bubble([7, -11, -2, 6, 5, 8, 3, -40]))
