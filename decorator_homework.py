def repeat(n_func:int) -> int: 
    """Главная функция"""
    def true_decorator(origin):
        """Создаем декоратор"""
        def subfunction(args):
            """Тайная функция, в которой происходит реализация дочерней функции и вывод значений"""
            for k in range(n_func):
                args=origin(args)
            result=args
            return result
        return subfunction 
    return true_decorator

@repeat(2)
def plus_1(x_par):
    return x_par + 1
@repeat(0)
def mul_2(x_par):
    return x_par * 2
print(plus_1(3))  # должно выдать 5
print(mul_2(4))  # должно выдать 4
