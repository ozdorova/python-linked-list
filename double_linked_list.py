import time
from typing import Any
from functools import singledispatchmethod

class Node:
    __slots__ = ('value', 'next', 'prev')

    def __init__(self, value: Any):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"{self.__class__.__name__}({str(self.value)})"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.value == other.value
        return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)


class DoubleLinkedList:
    __slots__ = ('head',)
    
    @singledispatchmethod
    def __init__(self, value=None, *args):
        # добавить возможность добавление сразу нескольких Node
        self.head = Node(value)
        if args:
            for item in args:
                self.append(item)
    
    @__init__.register
    def _(self, array: list | tuple):
        self.head = Node(array[0])
        for item in array[1:]:
            self.append(item)
    

    def __iter__(self):
        yield from self._node_generator()

    def _node_generator(self, value_return=True):
        current = self.head
        while current:
            yield current.value if value_return else current
            current = current.next

    def __str__(self) -> str:
        return f"[{', '.join(str(n) for n in self)}]"

    def __repr__(self) -> str:
        node_name = self.head.__class__.__name__
        return f"{self.__class__.__name__}[{', '.join( (f'{node_name}({n})' for n in self))}]"

    def __len__(self) -> int:
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length

    def __getitem__(self, item: int) -> Node:
        """Вовзращает объект Node"""
        if item < 0:
            item = len(self) + item
        for i, v in enumerate(self._node_generator(value_return=False)):
            if i == item:
                return v
        raise IndexError("Index out of range")

    def __setitem__(self, key: int, value: Any) -> None:
        current = self.head
        while current:
            if self[key] is current:
                current.value = value
                return
            current = current.next
        raise IndexError("Index out of range")

    def __delitem__(self, key):
        pass

    def index(self, value: Any) -> int:
        """Возвращает индекс объекта Node"""
        for i, v in enumerate(self):
            if v == value:
                return i
        return -1

    def append(self, value: Any) -> None:
        """Добавление объекта Node в конец списка"""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def append_left(self, data) -> None:
        """Добавление объекта Node в начало списка"""
        new_node = Node(data)
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node

    def insert(self, position: int, value: Any) -> None:
        """Добавление объекта Node в указанную позицию"""
        new_node = Node(value)
        if position == 0:
            self.append_left(value)
            return

        current = self.head
        count = 0
        while current and count < position:
            current = current.next
            count += 1

        if current:
            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.prev = new_node

    def sort(self) -> None:
        """Сортировка списка DoubleLinkedList"""
        swapped = True
        while swapped:
            current = self.head
            swapped = False
            while current and current.next:
                if current.value > current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                    swapped = True
                current = current.next

    def print(self) -> None:
        current = self.head
        while current:
            print(current.value, end=' ')
            current = current.next

    def reverse_list(self) -> None:
        current = self.head
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp:
            self.head = temp.prev

    def delete(self, value) -> None:
        "Удаление элемента списка по значению"
        current = self.head
        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev

                return
            current = current.next

    def remove_duplicates(self) -> None:
        """Удаление дублирующихся объектов Node"""
        if not self.head:
            return

        current = self.head
        seen = set()
        while current:
            if current.value in seen:
                current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
            else:
                seen.add(current.value)
            current = current.next

    def rotate(self, k: int) -> None:
        """Поворот списка на определенное количество шаго как в deque"""
        if not self.head or not self.head.next:
            return

        current = self.head
        length = 1
        while current.next:
            current = current.next
            length += 1

        k = k % length  # Нормализуем k, если он больше длины списка

        if k == 0:
            return

        current.next = self.head
        self.head.prev = current

        count = length - k
        current = self.head

        for _ in range(count - 1):
            current = current.next

        new_head = current.next
        current.next = None
        new_head.prev = None
        self.head = new_head


if __name__ == "__main__":
    lst = DoubleLinkedList(1, 2, 3, 4, 5, 6)
    print(lst)

    lst.append(5)
    lst.insert(1, -8)
    lst.insert(6, 11)
    lst.insert(0, -1)
    lst.insert(2, 155)
    lst.append_left(0)
    lst.append(2)
    print(lst)


