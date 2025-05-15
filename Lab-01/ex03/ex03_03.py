def tao_tuple_tu_list(lst):
    return tuple(lst)
input_list = input("Nhập vào danh sách số, cách nhau bởi dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
my_tuple = tao_tuple_tu_list(numbers)
print("List:", numbers)
print("Tuple tu list:", my_tuple)