




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

MySampleStack = Stack()
MySampleStack.isEmpty()

MySampleStack = Stack(6,10,15,-5)
MySampleStack.isEmpty()
MySampleStack.push(7, 15, 1000)
MySampleStack.pop()
MySampleStack.peek()
MySampleStack.size()