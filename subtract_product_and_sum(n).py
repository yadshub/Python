def subtract_product_and_sum(n):
    str_n = str(n)
    product_of_digits = 1
    sum_of_digits = 0
    for number in str_n:
        int_n = int(number)
        product_of_digits *= int_n
        sum_of_digits += int_n
    diff = product_of_digits - sum_of_digits
    return diff