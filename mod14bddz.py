# numbers = []

# while True:
#     num = int(input('введите набор чисел(-1)для выхода: '))
#     if num == -1:
#         break
#     numbers.append(num)

# while True:
#     human_choose = int(input('если хотите добавить число-1.если хотите удалить число-2.показать содержимое списка-3.проверить есть ли значение в списке-4.заменить значения в списке-5.: '))

#     if human_choose == 1:
#         num1 = int(input('введите число для добавления: '))
#         numbers.append(num1)
#         print(numbers)
#         print('-------------------')
#         continue
        
        
#     if human_choose == 2:
#         delnum = int(input('ввдеите число для удаления: '))
#         numbers.remove(delnum)
#         print(numbers)
#         print('-------------------')
#         continue

#     if human_choose == 3:
#         spisok_show = int(input('введите 1 для отображения по росту 2 в обратном порядке: '))
#         if spisok_show == 1:
#             numbers.sort()
#         if spisok_show == 2:
#             numbers.reverse()
#         print(numbers)
#         print('-------------------')
#         continue

#     if  human_choose == 4:
#         num_find=int(input("Введите число для поиска: "))

#         find_num = -1
#         for i in range(len(numbers)):
#             if numbers[i] == num_find:
#                 find_num = i
#                 break
#         print(numbers)
#         print('-------------------')
        
#         if num_find == -1:
#             print(f'выбранная вами цифра {num_find} не найдены')
#             print('-------------------')
#         else:
#             print(f'цифра {num_find} находится на  {find_num} индексе')
#             print('-------------------')
#         continue

#     # if human_choose == 5:
#     #     human_answer = int(input('хотите изменить весь список -1.его отдельные значения -2: '))

#     #     if human_answer == 1:
#     #         while True:
#     #             new_value = int(input('введите новые значения для нового списка(-1 для выхода): '))

#     #             if new_value == -1:
#     #                 break
#     #             new_list = []
#     #             numbers.append(new_value)
           
#     #         print(numbers)
#     # print('-------------------')

#     # if human_answer == 2:

#     if human_choose == 5:
#         human_answer = int(input('хотите изменить весь список -1.его отдельные значения -2. : '))
        

#         if human_answer == 1:
#             new_list = []

#             while True:
#                 new_value = int(input('введите новые значения для нового списка(-1 для выхода): '))

#                 if new_value == -1:
#                     break

#                 new_list.append(new_value)

#             numbers = new_list

#         print(numbers)

#     print('-------------------')

#     if human_choose == 5:
#         human_answer = int(input('хотите изменить весь список -1.его отдельные значения -2.3 возврат в меню: '))
#         if human_answer == 3:
#             continue

#         if human_answer == 1:
#             new_list = []

#             while True:
#                 new_value = int(input('введите новые значения для нового списка(-1 для выхода): '))

#                 if new_value == -1:
#                     break

#                 new_list.append(new_value)

#             numbers = new_list

#         print(numbers)

#     print('-------------------')


# -----------------------------------



class StackStrok:
    def __init__(self,size):
        self.stack=[]
        self.size = size
        self.top_index = -1
    def is_empty(self):
        return len(self.stack)==0
    
    def is_full(self):
        return len(self.stack) == self.size
    
    def push(self,value):
        if not self.is_full():
            self.top_index += 1
            self.stack.append(value)
            print(f'строка "{value}"помещена в стек [TOP: {self.stack[-1]}] ')
        else:
            print('стек заполнен!')
    def pop(self):
        if not self.is_empty():
            print(f'Строка "{self.stack.pop()}" вытащена из стека [TOP: {self.stack[-1]}]')
            self.top_index -= 1
        else:
            print('Стек пуст. Нечего вытаскивать.')

    def get_top(self):
        if not self.is_empty():
            print(f'Строка на вершине стека - [TOP: {self.stack[-1]}]')
        else:
            print('Стек пуст. Нечего смотреть.')

    def size(self):
        print(f'Размер стека - {len(self.stack)}')

    def clear(self):
        if not self.is_empty():
            self.stack.clear()
            self.top_index = -1
            print('Стек очищен.')
        else:
            print('Стек пуст. Нечего очищать.')

    def count(self):
        print(f'В стеке {len(self.stack)} строк')


if __name__ == '__main__':
    app_is_working = True
    s = StackStrok(3)

    while app_is_working:
        print('\nСтек строк:')
        print('1 - поместить строку в стек.')
        print('2 - вытащить строку из стека.')
        print('3 - посмотреть топ стека.')
        print('4 - очистить стек.')
        print('5 - количество строк в стеке.')
        print('6 - проверить пуст ли стек.')
        print('7 - проверить заполнен ли стек.')
        print('8 - выход из приложения.')

        user_input = input('Выберите нужную операцию: ')

        if user_input.isdigit():
            user_choice = int(user_input)

            if 1 <= user_choice <= 8:
                if user_choice == 1:
                    user_string = input('Введите строку: ')
                    s.push(user_string)

                elif user_choice == 2:
                    s.pop()

                elif user_choice == 3:
                    s.get_top()

                elif user_choice == 4:
                    s.clear()

                elif user_choice == 5:
                    s.count()

                elif user_choice == 6:
                    if s.is_empty():
                        print('Да, стек пуст.')
                    else:
                        print('Нет, стек не пуст.')

                elif user_choice == 7:
                    if s.is_full():
                        print('Да, стек заполнен.')
                    else:
                        print('Нет, стек не заполнен.')

                elif user_choice == 8:
                    app_is_working = False

            else:
                print('Неверный ввод.')

        else:
            print('Неверный ввод.')
