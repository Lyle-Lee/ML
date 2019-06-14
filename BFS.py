#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def divide_subgraph(graph,n):
    subgraph = []
    node = []
    for i in range(len(graph)):
        local = []
        if i not in node:
            node.append(i)
            local.append(i)
            link = [i]
            while link:
                v = link.pop()
                for j in range(len(graph[i])):
                    if graph[v][j] == 1 and j not in node:
                        node.append(j)
                        local.append(j)
                        link.append(j)
            subgraph.append(local)
    return subgraph

def count_dis(con_mat,a,b):
    '''
    计算邻接矩阵中任意两点的距离
    返回-1代表两点间无通路连接
    采用广度优先搜索(Breadth First Search)
    '''
    to_search = [a]
    finish_search = []
    dis = 0
    flag = -1
    while to_search:
        tmp = []
        for node in to_search:
            finish_search.append(node)
            cur = con_mat[node]
            for i in range(len(cur)):
                if cur[i] == 1:
                    if i == b:
                        dis += 1
                        return dis
                    if i not in finish_search and i not in to_search:
                        tmp.append(i)
        dis += 1
        to_search = tmp
    return flag

def diameter(con_mat,subgraph):
    d = 0
    for i in range(len(subgraph)):
        for j in range(i+1,len(subgraph)):
            d = max(d,count_dis(con_mat,subgraph[i],subgraph[j]))
    return d

with open('/users/lyle/downloads/graph2.txt', 'r') as f:
    s = f.read()
    g = s.split()
    n = int(len(g)**0.5)
    gra = []
    for i in range(n):
        gra.append([int(x) for x in g[n*i:n*(i+1)]])
    subg = divide_subgraph(gra,n)
    if 1 not in subg[0]:
        print('can not transmit')
    else:
        at = {x:-1 for x in subg[0][1:]}
        link1 = [0]
        link2 = []
        t = 1
        a = 0
        while -1 in at.values(): #无权无向图找最短路径(传输时间),v0为原点
            if a == 0:
                v = link1.pop()
                for i in subg[0][1:]:
                    if gra[v][i] == 1 and at[i] == -1:
                        at[i] = t
                        link2.append(i)
                if len(link1) == 0:
                    t += 1
                    a = 1
            else:
                v = link2.pop()
                for i in subg[0][1:]:
                    if gra[v][i] == 1 and at[i] == -1:
                        at[i] = t
                        link1.append(i)
                if len(link2) == 0:
                    t += 1
                    a = 0
        print('the least time to transmit from v0 to v1 is %d' %at[1])
    if count_dis(gra,0,1) == -1:
        print('can not transmit')
    else:
        print(count_dis(gra,0,1))