
class Stack:

    def __init__(self):
        self.stacklist = []

    def isEmpty(self):
        '''проверка стека на пустоту. Метод возвращает True или False.'''
        return self.stacklist == []

    def push (self, element):
        '''добавляет новый элемент на вершину стека. Метод ничего не возвращает.'''
        self.stacklist.append(element)

    def pop(self):
        ''' удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека'''
        if not self.isEmpty():
            return self.stacklist.pop()

    def peek(self):
        '''возвращает верхний элемент стека, но не удаляет его. Стек не меняется.'''
        if not self.isEmpty():
            return self.stacklist[len(self.stacklist)-1]

    def size(self):
        '''возвращает количество элементов в стеке'''
        return len(self.stacklist)

def check_string_balance(string):
    pairs = {')': '(', ']': '[', '}': '{'}
    brackets = ['{', '}', '[', ']', '(', ')']
    my_sample_stack = Stack()
    for symbol in string:
        if symbol in brackets:
            if symbol in pairs.values():
                my_sample_stack.push(symbol)
            else:
                if pairs[symbol] != my_sample_stack.peek():
                    return 'Строка несбалансирована'
                else:
                    my_sample_stack.pop()
    if my_sample_stack.isEmpty():
        return "Строка сбалансирована"
    else:
        return "Строка несбаланрирована"


print(check_string_balance('[([])((([[[]]])))]{()}'))
print(check_string_balance('(((([{}]))))'))
print()
print(check_string_balance('}{}'))
print(check_string_balance('{{[(])]}}'))
print(check_string_balance('[[{())}]'))