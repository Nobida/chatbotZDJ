# -*- coding: utf-8 -*-

import requests
from py2neo import Graph
import re


def py2neodb():
    test_graph = Graph(
    'http://59.110.243.182:7474',
    username='xxxxx',
    password='xxxxxxx'
    )
    return test_graph


def keywords(keywords):
    test_graph = py2neodb()
    find_node  = test_graph.run(
        "match(n) where n.name =~'%s.*' return \
        n.name,n.uuid limit 5"%(keywords))
    if find_node:
        return list(find_node) 


def path(entity1,entity2):
    test_graph = py2neodb()
    find_path = test_graph.run(
        'MATCH (p1{name:"%s"}),(p2{name:"%s"}),\
        p=shortestpath((p1)-[r*..10]-(p2)) \
        return r,p1.uuid,p2.uuid'%(entity1,entity2))
    if find_path:
        return list(find_path)

def net(entity,limit_num):
    limit_num = str(limit_num)
    test_graph = py2neodb()
    find_path = test_graph.run(
        'MATCH (p1{ name:"%s"})<-[r]->(p2) \
        RETURN r,p1.uuid,p2.uuid limit %s'%(entity,limit_num))
    if find_path:
        return list(find_path)

if __name__ == '__main__':
    print(net('罗马帝国',3)) 