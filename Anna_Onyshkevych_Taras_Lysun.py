"""
member1: Anna Onyshkevych
member2: Taras Lysun
"""
from typing import List, Dict
import csv


def read_csv(file_name: str) -> Dict[int, List[int]]:
    """
    read graph represented as matrix in .csv file and return it
    as dictionary where each key represents a vertex, while the value
    represent the list of matrices adjacent to the key
    :rtype: dict(key=int, value=list(int))
    :param file_name: string
    :return: graph
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            graph = {}
            fild = [row for row in reader]
            for ind, row in enumerate(fild):
                for index, value in enumerate(row):
                    if value != '0':
                        row[index] = row.index(value)
                graph[ind]=[x for x in row if x != '0']
            return graph
    except FileNotFoundError:
        return {}


def bfs(graph: Dict[int, List[int]]) -> List[int]:
    """
    perform bfs on the graph and store its result
    in the list of vertices(integers that represent vertices)
    :rtype: list(int)
    :param graph: dict(key=int, value=list(int))
    :return: bfs-result
    """
    res = []
    queue = []
    try:
        key = list(graph.keys())[0]
        res.append(key)
        for val in graph[key]:
            res.append(val)
            queue.append(val)
        while queue:
            for val in graph[queue[0]]:
                if val not in res:
                    res.append(val)
                    queue.append(val)
            queue.pop(0)
    except IndexError:
        return []
    return res


def dfs(graph: Dict[int, List[int]]) -> List[int]:
    """
    perform dfs on the graph and store its result
    in the list of vertices(integers that represent vertices)
    :rtype: list(int)
    :param graph:  dict(key=int, value=list(int))
    :return: dfs-result
    """
    res = []
    queue = []
    try:
        key = list(graph.keys())[0]
        res.append(key)
        for val in graph[key]:
            queue.append(val)
        while queue:
            if queue[0] not in res:
                res.append(queue[0])
            ind = queue.pop(0)
            for val in reversed(graph[ind]):
                if val not in res:
                    queue.insert(0, val)
    except IndexError:
        return []
    return res


def calc_pow(graph: Dict[int, List[int]]) -> Dict[int, int]:
    """
    calculate power of every vertex of your graph(i.e. number adjacent edges)
    :rtype: dict(key=int, value=int)
    :param graph: dict(key=int, value=list(int))
    :return: vertices and their powers
    """
    dct = {}
    for key, value in graph.items():
        dct[key] = len(value)
    return dct


def find_path(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    """
    here is another way of representing a graph:
    edges - is a list of edges of a graph,
    where each edge is also a list of two integers,
    which represent 2 adjacent vertices
    find if there is a way from the source vertex to the destination one
    :rtype: bool
    :param n: int
    :param edges: list(list(int))
    :param source: int
    :param destination: int
    :return:
    """
    vortexes = set()
    for edge in edges:
        for vortex in edge:
            if vortex >= n:
                return False
            vortexes.add(vortex)

    res = list(vortexes)
    res.insert(0,res.pop(source))

    graph = {}
    for vortex in res:
        vtx = set()
        for edge in edges:
            if vortex in edge:
                for v in edge:
                    vtx.add(v)
        vtx.discard(vortex)
        graph[vortex] = list(vtx)

    return destination in dfs(graph)
