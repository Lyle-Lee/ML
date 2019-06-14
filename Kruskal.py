#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def find(mat,a,b):
    to_search = [a]
    finish_search = []
    flag = 0
    while to_search:
        tmp = []
        for node in to_search:
            finish_search.append(node)
            cur = mat[node]
            for i in range(len(cur)):
                if cur[i] != 0:
                    if i == b:
                        flag = 1
                        return flag
                    if i not in finish_search and i not in to_search:
                        tmp.append(i)
        to_search = tmp
    return flag

def kruskal(con_mat):
    newmat = [[0 for j in range(len(con_mat[0]))] for i in range(len(con_mat))]
    weight = []
    p = 1
    while p < len(con_mat):
        q = 0
        while q < p:
            if con_mat[p][q] != 0 and con_mat[p][q] not in weight:
                weight.append(con_mat[p][q])
            q += 1
        p += 1
    weight = sorted(weight,reverse=True)
    while weight:
        w = weight.pop()
        p = 1
        while p < len(con_mat):
            q = 0
            while q < p:
                if con_mat[p][q] == w and find(newmat,p,q) == 0:
                    newmat[p][q] = con_mat[p][q]
                    newmat[q][p] = con_mat[p][q]
                q += 1
            p += 1
    return newmat

with open('/users/lyle/downloads/weighted_graph.txt', 'r') as f:
    s = f.read()
    g = s.split()
    n = int(len(g)**0.5)
    gra = []
    for i in range(n):
        gra.append([int(x) for x in g[n*i:n*(i+1)]])
    ltree = kruskal(gra)
    print(ltree)