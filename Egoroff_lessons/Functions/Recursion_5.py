# Метод быстрой сортировки

# функция quick_sort должна выполнить сортировку
def quick_sort(s):
    if len(s) <= 1:
        return s
    elem = s[0]
    left = list(filter(lambda x: x < elem, s))
    center = [_ for _ in s if _ == elem]
    right = list(filter(lambda x: x > elem, s))
    return quick_sort(left) + center + quick_sort(right)

print(quick_sort([0,5,8,2,1,9,0]))