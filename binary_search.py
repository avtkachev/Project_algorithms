'''Бинарный поиск - это алгоритм; на входе он получает отсортированный
список элементов. Если элемент, который вы ищете, присутствует в списке,
то бинарный поиск возвращает ту позицию, в которой он был найден. В противном
случае бинарный поиск возвращает null.
Пример, при входе в соц. сеть нужно проверить зарегистрирован ли такой пользователь
в сети, т.е. сходить в БД и найти имя пользователя'''

def binary_search(list, item):
    low = 0 # нажняя граница поиска
    high = len(list)-1 # верхняя граница поиска

    while low <= high: # пока список не сократится до одного элемента
        mid = (low + high) // 2 # проверяем средний элемент
        guess = list[mid]
        if guess == item: # Значение найдено
            return mid
        if guess > item: # Много
            high = mid - 1
        else: # Мало
            low = mid + 1
    return None # значение не существует

my_list = [1, 3, 5, 7, 9]
print(my_list)

print(binary_search(my_list, 3))

print('Дружим Cit и pycharm')