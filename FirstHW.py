import math #включаем библиотеку math, чтобы производить мат. операции
import numpy #включаем библиотеку numpy, чтобы генерировать числа
import matplotlib.pyplot as mpp #включаем библиотеку для построения графиков, задавая ее краткое имя как "mpp"

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__': #не до конца понял, по какому принципу выполняется эта операция (откуда взялась переменная __name__ и почему она по умолчанию равна '__main__')
    arguments = numpy.arange(0, 200, 0.1) #здесь ясно: библиотека "numpy" может задавать последовательность от 0 до 200 с шагом 0.1 (переменная arguments хранит эти значения, видимо, как массив)
    mpp.plot(       #начинаем задавать параметры графика
        arguments,     #строчка определяет значения по оси x
        [math.cos(a*2) * math.cos(a/2.0)* math.sin(a/2.0)*(-a) for a in arguments] #здесь идет задание точек в соответствии с числами из arguments, иначе говоря: определяется функция в зависимости от x из arguments
    )
    mpp.show() #команда отображения функции в виде графика
    #новая строка для проверки коммитов на Гите