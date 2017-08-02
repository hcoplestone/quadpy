# -*- coding: utf-8 -*-
#
import numpy


class Felippa(object):
    '''
    Carlos Felippa,
    A compendium of FEM integration formulas for symbolic work,
    Engineering Computation,
    Volume 21, Number 8, 2004, pages 867-890.

    <https://people.sc.fsu.edu/~jburkardt/datasets/quadrature_rules_wedge/quadrature_rules_wedge.html>
    '''
    def __init__(self, index):
        if index == 1:
            self.weights = [1.0]
            self.points = [[1.0/3.0, 1.0/3.0, 0.0]]
            self.degree = 1
        elif index == 2:
            self.weights = 6 * [1.0/6.0]
            self.points = _s21_z(1.0/6.0, numpy.sqrt(1.0/3.0))
            self.degree = 2
        elif index == 3:
            self.weights = 6 * [1.0/6.0]
            self.points = _s21_z(0.5, numpy.sqrt(1.0/3.0))
            self.degree = 2
        elif index == 4:
            self.weights = (
                6 * [0.6205044157722541E-01] +
                6 * [0.3054215101536719E-01] +
                3 * [0.9928070652356065E-01] +
                3 * [0.4886744162458750E-01]
                )
            self.points = (
                _s21_z(0.4459484909159649, 0.7745966692414834) +
                _s21_z(0.9157621350977074E-01, 0.7745966692414834) +
                _s21(0.4459484909159649) +
                _s21(0.9157621350977074E-01)
                )
            self.degree = 4
        elif index == 5:
            self.weights = (
                6 * [0.3498310570689643E-01] +
                6 * [0.3677615355236283E-01] +
                2 * [0.6250000000000000E-01] +
                3 * [0.5597296913103428E-01] +
                3 * [0.5884184568378053E-01] +
                1 * [1.0000000000000000E-01]
                )
            self.points = (
                _s21_z(0.1012865073234563, 0.7745966692414834) +
                _s21_z(0.4701420641051151, 0.7745966692414834) +
                _s3_z(0.7745966692414834) +
                _s21(0.1012865073234563) +
                _s21(0.4701420641051151) +
                _s3()
                )
            self.degree = 5
        else:
            assert index == 6
            self.weights = (
                6 * [0.8843323515718317E-02] +
                6 * [0.2031233592848984E-01] +
                12 * [0.1441007403935041E-01] +
                6 * [0.1657912966938509E-01] +
                6 * [0.3808080193469984E-01] +
                12 * [0.2701546376983638E-01]
                )
            self.points = (
                _s21_z(0.6308901449150223E-01, -0.8611363115940526) +
                _s21_z(0.2492867451709104, -0.8611363115940526) +
                _s111_z(
                    0.5314504984481695E-01,
                    0.3103524510337844,
                    0.8611363115940526
                    ) +
                _s21_z(0.6308901449150223E-01, 0.3399810435848563) +
                _s21_z(0.2492867451709104, 0.3399810435848563) +
                _s111_z(
                    0.5314504984481695E-01,
                    0.3103524510337844,
                    0.3399810435848563
                    )
                )
            self.degree = 6

        self.weights = numpy.array(self.weights)
        self.points = numpy.array(self.points)
        return


def _s3():
    return [
        [1.0/3.0, 1.0/3.0, 0.0],
        ]


def _s3_z(z):
    return [
        [1.0/3.0, 1.0/3.0, +z],
        [1.0/3.0, 1.0/3.0, -z],
        ]


def _s21(a):
    b = 1.0 - 2*a
    return [
        [a, b, 0.0],
        [b, a, 0.0],
        [a, a, 0.0],
        ]


def _s21_z(a, z):
    b = 1.0 - 2*a
    return [
        [a, b, +z],
        [b, a, +z],
        [a, a, +z],
        [a, b, -z],
        [b, a, -z],
        [a, a, -z],
        ]


def _s111_z(a, b, z):
    c = 1.0 - a - b
    return [
        [b, c, +z],
        [a, b, +z],
        [c, a, +z],
        [c, b, +z],
        [a, c, +z],
        [b, a, +z],
        [b, c, -z],
        [a, b, -z],
        [c, a, -z],
        [c, b, -z],
        [a, c, -z],
        [b, a, -z],
        ]