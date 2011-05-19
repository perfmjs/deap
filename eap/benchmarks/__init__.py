#    This file is part of EAP.
#
#    EAP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    EAP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with EAP. If not, see <http://www.gnu.org/licenses/>.


"""
Regroup typical EC benchmarks functions to import easily and benchmark
examples.
"""

__author__ = "Francois-Michel De Rainville and Felix-Antoine Fortin"
__version__ = "0.7"
__revision__ = "0.7.0+"

import random
from math import sin, cos, pi, exp, e, sqrt
from operator import mul
from functools import reduce

# Unimodal
def rand(individual):
    """Random test objective function."""
    return random.random(),
    
def plane(individual):
    """Plane test objective function."""
    return individual[0],

def sphere(individual):
    """Sphere test objective function."""
    return sum(gene * gene for gene in individual),

def cigar(individual):
    """Cigar test objective function."""
    return individual[0]**2 + 1e6 * sum(gene * gene for gene in individual),

def rosenbrock(individual):  
    """Rosenbrock test objective function."""
    return sum(100 * (x * x - y)**2 + (1. - x)**2 \
                   for x, y in zip(individual[:-1], individual[1:])),

# Multimodal
def ackley(individual):
    """Ackley test objective function."""
    N = len(individual)
    return 20 - 20 * exp(-0.2*sqrt(1.0/N * sum(x**2 for x in individual))) \
            + e - exp(1.0/N * sum(cos(2*pi*x) for x in individual)),
            
def bohachevsky(individual):
    return sum(x**2 + 2*x1**2 - 0.3*cos(3*pi*x) - 0.4*cos(4*pi*x1) + 0.7 
                for x, x1 in zip(individual[:-1], individual[1:])),

def griewank(individual):
    return 1.0/4000.0 * sum(x**2 for x in individual) - \
        reduce(mul, (cos(x/sqrt(i+1.0)) for i, x in enumerate(individual)), 1) + 1,
            
def rastrigin(individual):
    """Rastrigin test objective function. Consider using ``lambda_ = 20 * N`` 
    for this test function.
    """     
    return 10 * len(individual) + sum(gene * gene - 10 * \
                        cos(2 * pi * gene) for gene in individual),

def rastrigin_scaled(individual):
    N = len(individual)
    return 10*N + sum((10**(i/(N-1))*x)**2 - 
                      10*cos(2*pi*10**(i/(N-1))*x) for x in individual),

def rastrigin_skew(individual):
    N = len(individual)
    return 10*N + sum((10*x if x > 0 else x)**2 
                    - 10*cos(2*pi*(10*x if x > 0 else x)) for x in individual),
def schaffer(individual):
    return sum((x**2+x1**2)**0.25 * ((sin(50*(x**2+x1**2)**0.1))**2+1.0) 
                for x, x1 in zip(individual[:-1], individual[1:])),

def schwefel(individual):
    N = len(individual)
    return 418.9828872724339*N-sum(x*sin(sqrt(abs(x))) for x in individual),
    
