from abc import ABC, abstractmethod
import numpy as np
from numpy import array as vec
import numpy.linalg
import matplotlib.pyplot as plt
import itertools
import math

MODEL_G = 0.5  # гравитационная постоянная
COLLISION_DISTANCE = 5.0
COLLISION_COEFFICIENT = 50
MODEL_DELTA_T = 0.1
TIME_TO_MODEL = 50

# ABC это не алфавит, а AbstractBaseClass. Не даст создать экземпляр, пока не переопределишь все методы-заглушки
class Universe(ABC):
    """Невнятная вселенная, основа всех миров"""

    def __init__(self):
        self.bodies = []

    @abstractmethod
    def gravity_flow_dencity_per_1_1(self, dist):
        """
        Плотность потока гравитационного поля между двумя
        единичными массами на заданном расстоянии
        """
        ...

    def model_step(self):
        """Итерация решения задачи Коши. Конечно не присуща вселенной, но тут на своём месте"""
        for b1, b2 in itertools.product(self.bodies, self.bodies):
            if b1 != b2:
                b1.apply_force(b1.force_induced_by_other(b2))
        for b in self.bodies:
            b.advance()

    def add_body(self, body):
        self.bodies.append(body)


class MaterialPoint:
    """Материальная точка, движущаяся по двумерной плоскости"""
    
    def __init__(self, universe, mass, position, velocity):
        self.universe = universe
        self.mass = mass
        self.position = position
        self.velocity = velocity
        universe.add_body(self)

        self.ptrace = [self.position.copy()]
        self.vtrace = [self.velocity.copy()]
    
    def force_induced_by_other(self, other):
        """Сила, с которой другое тело действует на данное"""
        delta_p = other.position - self.position
        distance = numpy.linalg.norm(delta_p)  # Евклидова норма (по теореме Пифагора)
        force_direction = delta_p / distance
        force = force_direction * self.mass * other.mass * self.universe.gravity_flow_dencity_per_1_1(distance)
        return force

    def advance(self):
        """Перемещаем тело, исходя из его скорости"""
        self.position += self.velocity * MODEL_DELTA_T
        self.ptrace.append(self.position.copy())
        self.vtrace.append(self.velocity.copy())

    def apply_force(self, force):
        """Изменяем скорость, исходя из силы, действующей на тело"""
        self.velocity += force * MODEL_DELTA_T / self.mass

class Universe2D(Universe):
    def __init__(self,G,k,collision_distance):
        super().__init__()
        self.G = G
        self.k = k                                  # коэффициент при упругом соударении
        self.collision_distance = collision_distance

    def gravity_flow_dencity_per_1_1(self, dist):
        # будем считать, что отскакивают точки друг от друга резко

        if dist > self.collision_distance:
            # Ситуация с обычным потоком поля — просто притяжение
            return self.G / dist
        else:
            # Отталкивание при соударении (притяжение убираем).
            return -self.k / dist

u2d = Universe2D(MODEL_G, COLLISION_COEFFICIENT, COLLISION_DISTANCE)

bodies = [
    MaterialPoint(u2d, 2000., vec([  0.,   0.]), vec([ 0.,   0.])),
    MaterialPoint(u2d,     10., vec([100.,   0.]), vec([ 0., -15.])),
    MaterialPoint(u2d,     10., vec([  0., 100.]), vec([15.,   0.]))
]

steps = int(TIME_TO_MODEL / MODEL_DELTA_T)
for stepn in range(steps):
    u2d.model_step()


plt.gca().set_aspect('equal')

def plt_kepler(same_fig=False):
    b=bodies[1]
    v=b.vtrace
    p=b.ptrace
    v_x=[a[0] for a in v]
    v_y=[a[1] for a in v]
    r_x=[k[0] for k in p]
    r_y=[k[1] for k in p]
    print(r_y)
    for i in range(steps):
        r_momentary=[r_x[i],r_y[i]]
        v_momentary=[v_x[i]*MODEL_DELTA_T,v_y[i]*MODEL_DELTA_T]
        # print(r_momentary)
        # print(v_momentary)
        s=abs(np.cross(r_momentary,v_momentary, axisa=0, axisb=0))
        plt.plot(s,MODEL_DELTA_T)
    if not same_fig: # По картинке на тело
        plt.show()
    if same_fig: # Одна картинка на всех
        plt.show()

plt_kepler()