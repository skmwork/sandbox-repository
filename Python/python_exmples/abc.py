import abc

class Tombola(abc.ABC):
    
    @abc.abstractmethod
    def load(self, iterable):
        """Добавить эелементы из итерируемого объекта"""
        
    @abc.abstractmethod
    def pick(self):
        """Извлечь случайный элемент и вернуть его
            Этот метод должен возбуждать LookupError
            если объект пуст"""
        
    def loaded(self):
        """Вернуть true если есть хоть один элемент"""
        return bool(self.inspect())
    
    
    def inspect(self):
        """вернуть отсортированный кортеж содержащий элементы контейнера"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))


import random

class BingoCage(Tombola):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)
        
    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)
        
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')
        
    def __call__(self):
        self.pick()
        
class LotteryBlower(Tombola):
    def __init__(self, iterable):
        self._balls = list(iterable)
        
    def load(self, iterable):
        self._balls.extend(iterable)
        
    def pick(self):
        print(self._balls)
        
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty BingoCage')
        return self._balls.pop(position)
    
    def loaded(self):
        return bool(self._balls)
    
    def inspect(self):
        return tuple(sorted(self._balls))
    
@Tombola.register
class TomboList(list):
    def pick(self):
        if self:
            position = random.randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')
 
    load = list.extend
    
    def loaded(self):
        return bool(self)
    
    def inspect(self):
        return tuple(sorted(self))
class Fake(Tombola):
    def pick(self):
        return 13
    
a = TomboList([1,2,3])
print(a.pick())
print(a.inspect())