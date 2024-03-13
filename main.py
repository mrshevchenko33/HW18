def common_elements():
    list_mul_3 = [i for i in range(1, 101) if i % 3 == 0]
    list_mul_5 = [i for i in range(1, 101) if i % 5 == 0]

    set_mul_3 = set(list_mul_3)
    set_mul_5 = set(list_mul_5)

    common_elements_set = set_mul_3.intersection(set_mul_5)
    return common_elements_set

print(common_elements())