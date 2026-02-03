lst = [5,8,99,0,50,9,-5,7]


def sort_lst(lst): # Функция принимает список чисел lst и возвращает отсортированный список
    if len(lst) <= 1:#  если в списке всего один элемент то он считается отсортированным
        return lst
    else:
        opor_element = lst[-1] # берем последний элемент из списка
        do_opor_element = [i_num for i_num in lst if i_num < opor_element]# все элементы списка до базового
        centr_opor_element = [i_num for i_num in lst if i_num == opor_element]# все элементы списка = базовому
        posle_opor_element = [i_num for i_num in lst if i_num > opor_element] # все элементы списка после базового


        return (sort_lst(do_opor_element) +
            centr_opor_element +
            sort_lst(posle_opor_element)) # тут сортируем все элементы мень базового + базовые+ сортируем все элементы больше базового


print(sort_lst(lst))

test_dop_f = [5,8,99,0,50,9,-5,7] #   задаем лист для дополнительной функции

# дополнительная функция сортировки значений из листа
def dop_f(lst):
    opor_dop_f = lst[-1]   # берём последний элемент как опорный

    min_opor_dop_f = []
    ravno_opor_dop_f = []
    max_opor_dop_f = []

    for x in lst:
        if x < opor_dop_f:
            min_opor_dop_f.append(x) # тут append (x) - добавляет элемент в конец списка
        elif x == opor_dop_f:
            ravno_opor_dop_f.append(x)
        else:
            max_opor_dop_f.append(x)

    return min_opor_dop_f, ravno_opor_dop_f, max_opor_dop_f

print(dop_f(test_dop_f))






