#Дан список размера N, все элементы которого, кроме первого, упорядочены по
#возрастанию. Сделать список упорядоченным, переместив первый элемент на новую
#позицию.

def sort_list(lst):
    # Если список пустой или содержит только 1 элемент
    if len(lst) <= 1:
        return lst
    
    # Берем первый элемент
    first_element = lst[0]
    
    # Ищем, куда вставить первый элемент
    i = 1
    while i < len(lst) and lst[i] < first_element:
        i += 1
    
    # Вставляем элемент на нужную позицию
    lst.insert(i, first_element)
    
    # Убираем первую позицию 
    lst.pop(0)
    
    return lst

lst = [10, 15, 20, 30, 40] 
sorted_lst = sort_list(lst)
print(sorted_lst)
