# -*- coding: utf-8 -*-
#
import os
import json

from ..helpers import untangle2


class VioreanuRokhlin(object):
    """
    B. Vioreanu and V. Rokhlin,
    Spectra of Multiplication Operators as a Numerical Tool,
    Methods and Algorithms for Scientific Computing,
    2014,
    SIAM J. Sci. Comput., 36(1), A267–A288,
    <https://doi.org/10.1137/110860082>,
    <http://www.cs.yale.edu/publications/techreports/tr1443.pdf>.

    Data adapted from modepy
    <https://github.com/inducer/modepy/blob/master/modepy/quadrature/vr_quad_data_tet.py>.
    """

    def __init__(self, index):
        self.name = "VioreanuRokhlin({})".format(index)

        this_dir = os.path.dirname(os.path.realpath(__file__))
        filename = "vr{:02d}.json".format(index)
        with open(os.path.join(this_dir, filename), "r") as f:
            data = json.load(f)

        self.degree = data.pop("degree")

        self.bary, self.weights = untangle2(data)
        self.points = self.bary[:, 1:]
        self.weights *= 3.0 / 4.0
        return
