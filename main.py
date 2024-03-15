# -*- coding: utf-8 -*-
"""You can torch.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u9mI2Cy_8JxMjsF3rOGEQwYGDhhY5xkZ
"""

import autograd.numpy as np
import torch

# Simulation parameters
N         = 1       # Number of particles
Nx        = 10      # Number of mesh cells
t         = 0       # current time of the simulation
tEnd      = 50      # time at which simulation ends
dt        = 1       # timestep
boxsize   = 1.0      # periodic domain [0,boxsize]
n0        = 1       # electron number density
vb        = 3       # beam velocity
vth       = 1       # beam width
A         = 0.1     # perturbation
plotRealTime = True # switch on for plotting as the simulation goes along

# Generate Initial Conditions
#np.random.seed(42)            # set the random number generator seed
# construct 2 opposite-moving Guassian beams
#pos  = torch.rand(N) * boxsize
pos  = torch.tensor([0.2,0.8])
pos.requires_grad = True

import sys
def denst(Pos,Nx,boxsize,n0):
    dx = boxsize/Nx
    n= torch.zeros(Nx)
    for pos in Pos:
        j = torch.floor(pos / dx).int()
        jp1 = j + 1
        weight_j=(jp1 * dx - pos) / dx
        weight_jp1 = (pos - j * dx) / dx
        jp1 = torch.remainder(jp1, Nx)
        n[j] += weight_j
        n[jp1] += weight_jp1
    return n


n = denst(pos,Nx,boxsize,n0)
qq = 0




import matplotlib.pyplot as plt
plt.plot(n)

