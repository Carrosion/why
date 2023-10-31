
# Задача 1 (Односвязный список)

class Node:
    def __init__(self, data): ##ячейка списка. из них будет состоять весь наш список. Всё работает по принципу паровоза.
        # ноды - вагоны, которые содержат информацию. Сам список - только ссылки на первый и последний нод и их количество
        self.head = data #содержимое ячейки
        self.next = None #ссылка на следующую ячейку. по умолчанию она пустая

class LinkedList:
    def __init__(self, *args):
        '''
        У объекта класса есть три атрибута - первый узел, последний узел и длина списка. Данные атрибуты можно использовать только внутри класса
        '''
        ##параметры с двойным подчёркиванием спереди, чтобы их можно было использовать только внутри класса
        #*args это список аргументов, из которых надо сделать список
        self.__first = None
        self.__last = None
        self.__len = 0 
        #создаём пустой список длины 0 и поочерёдно добавляем него новые ноды
        for i in args:
            self.add_back(i)


    def add_forward(self, el):
        '''
        Добавляет элемент в начало списка со сложностью O(1)

        >>> l1 = LinkedList(1,2,3)
        >>> l1.add_forward(0)
        >>> print(l1)
        (0 -> 1 -> 2 -> 3)

        >>> l2 = LinkedList(l1, LinkedList(4,5, LinkedList(6,7)), 1)
        >>> print(l2)
        ((0 -> 1 -> 2 -> 3) -> (4 -> 5 -> (6 -> 7)) -> 1)
        >>> l2.add_forward(LinkedList(-2, -1))
        >>> print(l2)
        ((-2 -> -1) -> (0 -> 1 -> 2 -> 3) -> (4 -> 5 -> (6 -> 7)) -> 1)
        '''
        self.__len += 1 #увеличиваем длину на 1
        if self.__len == 1: #если длина = 1, т.е. список до этого был пустой:
            self.__first = Node(el) #создаём первую ячейку списка
            self.__last = self.__first #она же становится последней, т.к. в списке всего 1 ячейка
            return 
        #иначе (когда список был не пустой)
        newfirst = Node(el) #создаём нод, который надо добавить в начало
        newfirst.next = self.__first #цепляем к нему первый нод
        self.__first = newfirst #назначаем новый нод первым нодом в списке
        

    def add_back(self, el):
        '''
        Добавляет элемент в конец списка со сложностью O(1)

        >>> l1 = LinkedList(1,2,3)
        >>> l1.add_back(4)
        >>> print(l1)
        (1 -> 2 -> 3 -> 4)

        >>> l2 = LinkedList(l1, LinkedList(5,6, LinkedList(7,8)), 9)
        >>> print(l2)
        ((1 -> 2 -> 3 -> 4) -> (5 -> 6 -> (7 -> 8)) -> 9)
        >>> l2.add_back(LinkedList(10, 11))
        >>> print(l2)
        ((1 -> 2 -> 3 -> 4) -> (5 -> 6 -> (7 -> 8)) -> 9 -> (10 -> 11))
        '''

        #аналогично предыдущей функции
        self.__len += 1
        if self.__len == 1:
            self.__first = Node(el)
            self.__last = self.__first
            return
        
        self.__last.next = Node(el) 
        self.__last = self.__last.next 

    def pop(self, index=0):
        '''
        Удаляет элемент списка на позиции index с конца и с начала cо сложностью O(1), а произвольный элемент списка за O(n),
        и возвращает значение удаленного элемента.

        >>> l1 = LinkedList(1, 2, 3, 4)
        >>> print(l1)
        (1 -> 2 -> 3 -> 4)
        >>> l1.pop()
        1
        >>> print(l1)
        (2 -> 3 -> 4)
        >>> l1.pop(1)
        3
        >>> print(l1)
        (2 -> 4)

        >>> l1.pop(10)
        Traceback (most recent call last):
            ...
        IndexError: pop index out of range
        '''
        if index >= self.__len: #если индекс больше или равен длине, сообщаем об ошибке
            raise IndexError(f"pop index out of range") 
        self.__len -= 1 #уменьшаем длину на 1
        if index == 0: #если индекс нулевой, проще поступить так:
            answer = self.__first.head #забираем содержимое первого нода
            self.__first = self.__first.next #назначаем первым нод, который следует за первым сейчас
            return answer
        i = self.__first 
        pos = 0
        while pos < index - 1:
            i = i.next
        answer = i.next.head
        i.next = i.next.next
        return answer
                


    def __add__(self, other):
        '''
        other - только LinkedList обьект, в противном случае - ошибка

        >>> l1 = LinkedList(1, 2, 3)
        >>> l2 = LinkedList(4, 5)
        >>> l3 = l1 + l2
        >>> print(l3)
        (1 -> 2 -> 3 -> 4 -> 5)
        >>> print(l3 + [1, 2])
        Traceback (most recent call last):
            ...
        TypeError: can only concatenate LinkedList (not "list") to LinkedList
        >>> print(l3 + 1)
        Traceback (most recent call last):
            ...
        TypeError: can only concatenate LinkedList (not "int") to LinkedList
        '''
        if isinstance(other, LinkedList):
            answer = LinkedList()
            for i in range(len(self)):
                answer.add_back(self[i])
            for j in range(len(other)):
                answer.add_back(other[j])
            return answer
        raise TypeError(f'can only concatenate LinkedList (not "{type(other).__name__}") to LinkedList')
        

    def __getitem__(self, index):
        '''
        Этот метод позволяет доступаться до элементов списка по индексу и возвращать значение элемента (сложность O(n)), например:

        >>> l1 = LinkedList(1,2,3)
        >>> l1[1]
        2
        >>> l1[0]
        1

        >>> l1[10]
        Traceback (most recent call last):
            ...
        IndexError: list index out of range
        '''
        if index >= self.__len:
            raise IndexError(f"list index out of range")
        pos = 0
        i = self.__first
        while pos < index:
            i = i.next
            pos += 1
        return i.head


    def __setitem__(self, key, value):
        '''
        Этот метод позволяет присваивать значение элементу списка найденному по индексу (сложность O(n)), например:

        >>> l1 = LinkedList(1,2,3)
        >>> l1[1] = 5
        >>> l1
        LinkedList(1, 5, 3)
        >>> l1[10]
        Traceback (most recent call last):
            ...
        IndexError: list index out of range
        '''
        if key >= self.__len:
            raise IndexError(f"list index out of range")
        pos = 0
        i = self.__first
        while pos < key:
            i = i.next
            pos += 1
        i.head = value

    def __len__(self):
        '''
        Вызывается при передаче экземпляра класса LinkedList в встроенную функцию len() -> возвращается длина связанного списка

        >>> l1 = LinkedList(1,2,3)
        >>> len(l1)
        3
        '''
        return self.__len #просто возвращаем длину

    def __str__(self):
        answer = '('
        i = self.__first
        while i != None:
            answer += str(i.head)
            answer += ' -> '
            i = i.next
        return answer[:-4] + ')'
            

    def __repr__(self):
        answer = 'LinkedList('
        i = self.__first
        while i != None:
            answer += str(i.head)
            answer += ', '
            i = i.next
        return answer[:-2] + ')'


# Следующие две алгоритмические задачи требуется решать исключительно собственным созданным списком LinkedList
# без использования встроенных структур данных: list, tuple, set, dict, и т.д.

#Задача 2 (Подмена)

def swap_values(link_list, k):
    '''
    Учитывая связанный список, меняет местами k-ый элемент с самого начала с k-ым элементом с конца.  
    >>> l1 = LinkedList(1,2,3,4,5)
    >>> swap_values(l1, 2)
    >>> l1
    (1 -> 4 -> 3 -> 2 -> 5)
    '''

    link_list[k-1], link_list[len(link_list) - k] = link_list[len(link_list) - k], link_list[k-1]



# Задача 3 (Передел)

def alternating_split(link_list):
    '''
    Разбивает связанный список на два списка, содержащих чередующиеся элементы из исходного и возвращает эти списки
    
    >>> alternating_split(LinkedList(1,2,3,4,5))
    (LinkedList(1, 3, 5), LinkedList(2, 4))

    '''
    x, y = LinkedList(), LinkedList()
    for i in range(len(link_list)):
        if i % 2 == 0:
            x.add_back(link_list[i])
        else:
            y.add_back(link_list[i])
    return x, y
    