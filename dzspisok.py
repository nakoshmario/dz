
# list1 = [1, 3, 5, 7]
# list2 = [2, 4, 6, 8]
# list3 = [9, 11, 13, 15]
# list4 = [10, 12, 14, 16]


# list_all = list1 + list2 + list3 + list4

# sortirovka= int(input('отсортировать в рост(1/2) или в убыль: '))

# if sortirovka == 1:
#     list_all.sort()
# if sortirovka == 2:
#     list_all.sort(reverse=True)


# print(list_all)


# value_number= input("выбирите цифру  для поиска: ")
# value = int(value_index)


# found_index = -1
# for i in range(len(list_all)):
#     if list_all[i] == value:
#         found_index = i
#         break

# if found_index == -1:
#     print(f"цифрам{value} не найдена")
# else:
#     print(f"цифра {value} находится на {found_index} индексе.")

list1 = [1, 3, 5, 7,1, 3, 5, 7]
list2 = [2, 4, 6, 8,2,4,8]
list3 = [9, 11, 13, 15,9,11,13]
list4 = [10, 12, 14, 16,10,12,16]

list_combined = list1 + list2 + list3 + list4
numbers = list1+list2+list3+list4

def uniq_val(list1,list2,list3,list4):
    res = []

    for val in list1:
        if val not in res:
            res.append(val)
    for val in list2:
        if val not in res:
            res.append(val)
    for val in list3:
        if val not in res:
            res.append(val)
    for val in list4:
        if val not in res:
            res.append(val)
    return res
numbers = uniq_val(list1,list2,list3,list4)


def sortirovka(numbers):
    ansver_human = int(input('введите сортировку по росту или убыванию (1 или 2): '))
    if ansver_human == 1:
        numbers.sort()
    if ansver_human == 2:
        numbers.reverse()
    print(numbers)

# линейный поиск
# def find_index(numbers):
#     val_choose = int(input('введите значение для поиска: '))

#     val = val_choose
    
#     found_index = -1
#     for i in range(len(numbers)):
#         if numbers[i] == val:
#             found_index = i
#             break
#     print(numbers)

#     if found_index == -1:
#         print(f"цифрам{val} не найдена")
#     else:
#         print(f"цифра {val} находится на {found_index} индексе.")
    # ---------------

# бинарный поиск
    
num = int(input('введите число для поиска: '))
def bin_find(numbers,x):
    print(numbers)
    left = 0
    rigth = len(numbers) -1
    mid = 0


    while left <= rigth:
        mid = (left + rigth) // 2

        if numbers[mid] == x:
          
            print(f'цифра стоит под индксом {mid}')
           
        
            return True
        if numbers[mid] < x:
            left = mid + 1
        else:
            rigth = mid - 1
    print(f'{num} такого числа в списке нет')

    return False
        


sortirovka(numbers)
bin_find(numbers,num)

# find_index(numbers) поиск линейный