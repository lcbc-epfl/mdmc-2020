#!/usr/bin/env python3

import math

def put_in_box(box, resnr, coords):
    N      = len(coords)
    cgcm   = []
    old    = -1
    invres = []
    for i in range(N):
        if (resnr[i] != old):
            cgcm.append([ 0.0, 0.0, 0.0 ])
            invres.append([])
            old = resnr[i]
        for m in range(3):
            cgcm[len(cgcm)-1][m] += coords[i][m]
        invres[len(invres)-1].append(i)
    N = len(cgcm)
    for i in range(N):
        for m in range(3):
            cgcm[i][m] /= len(invres[i])
    for i in range(N):
        for m in range(3):
            if (cgcm[i][m] > box[m]):
                for k in invres[i]:
                    coords[k][m] -= box[m]
            if (cgcm[i][m] <= 0):
                for k in invres[i]:
                    coords[k][m] += box[m]
    

def compute_lambda_T(T, T_reference, time_step, tau_T):
    if (T == 0 or tau_T == 0):
        return 1
    return math.sqrt(1 + (time_step/tau_T)*(T_reference/T - 1))

