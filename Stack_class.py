




class Stack:
    stack =[]
    def __init__(self, *numbers):
        for number in numbers:
            Stack.stack.append(number)

    def isEmpty(self):
        '''проверка стека на пустоту. Метод возвращает True или False.'''
        if len(Stack.stack) > 0:
            print(f'Стэк не пустой')
            print(Stack.stack) # Как вывести содержимое?
            return False
        else:
            print('Стэк пустой')
            return True

    def push (self, *elements):
        '''добавляет новый элемент на вершину стека. Метод ничего не возвращает.'''
        Stack.stack.extend(elements)
        print(Stack.stack)

    def pop(self):
        ''' удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека'''
        pop_elem = Stack.stack.pop()
        print(f'Удален верхний элемент стэка {pop_elem}')
        return pop_elem

    def peek(self):
        '''возвращает верхний элемент стека, но не удаляет его. Стек не меняется.'''
        print('Верхний элемент стека: ', Stack.stack[-1])
        return Stack.stack[-1]

    def size(self):
        '''возвращает количество элементов в стеке'''
        print('Количество элементов в стеке: ', len(Stack.stack))
        return len(Stack.stack)
#
MySampleStack = Stack()
MySampleStack.isEmpty()

MySampleStack = Stack(6, [1231, 23423, 234], 10, {2234: {2342: {234234: [12312, 41321, 1241]}}},15,-5)
MySampleStack.isEmpty()
MySampleStack.push(7, 15, {1000: {12312: [123, 123, 123]}})
MySampleStack.pop()
MySampleStack.peek()
MySampleStack.size()

'''TASK 2'''

# def check_string_balance(string):
#     pass
round_pair = {'(': ')'}
square_pair = {'[': ']'}
figure_pair = {'{': '}'}
pairs = {'(': ')', '[': ']', '{': '}', ')': '(', ']': '[', '}': '{'}
'''
Условия:
элементов д.б. четное кол-во
кол-во открывающих элементов д.б равно кол-ву закрывающих
Как учесть порядок элеменов????????
'''
string = '(((([{}]))))'
ext_string = '(((([{)]})))'
# string = '[([])((([[[]]])))]{()}'

print(string)
reversed_string = list(reversed(string))
print(reversed_string)
if len(string) % 2 == 0:
    print('Проверку на четность скобок прошли')
else:
    print('Проверку на четность скобок НЕ прошли')

if string.count('(') == string.count(')') and \
    string.count('[') == string.count(']') and \
    string.count('{') == string.count('}'):
    print('Проверку на одинаковое кол-во открывашек и закрывашек прошли')
else:
    print('Проверку на одинаковое кол-во открывашек и закрывашек НЕ прошли')

i=0
for symbol in string:
    if pairs[string[i]] == reversed_string[i]:
        # print(pairs[string[i]], '==> OK', i, reversed_string[i])
        i+=1
    else:
        print('Проверку на соответствие откр/закр скобок НЕ прошли')
        break
    print('Проверяю на соответствие откр/закр скобок')


'''

'''


# print(round_pair[string[0]])
# i = 0
# j =-1
# for symbol in string:
#     if round_pair[string[i]] == string[j]:
#         print(round_pair[string[i]],'OK', string[j])
#         i+=1
#         j-=1
#     else:
#         if square_pair[string[i]] == string[j]:
#             print(square_pair[string[i]],'OK', string[j])
#             i+=1
#             j-=1
#         else:
#             if figure_pair[string[i]] == string[j]:
#                 print(figure_pair[string[i]],'OK', string[j])
#                 i+=1
#                 j-=1







# else:
#     print('Строка несбалансирована')
# [([])((([[[]]])))]{()}
# ')(', '][', '}{', ']{', '){', '}['
