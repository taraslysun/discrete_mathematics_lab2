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
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        graph = {}
        fild = [row for row in reader]
        for row in fild:
            for index, value in enumerate(row):
                if value != '0':
                    row[index] = row.index(value)
            graph[fild.index(row)]=[x for x in row if x != '0']
        return graph
print(read_csv('graph.csv'))

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

bfs({0: [2, 5, 7],
    1: [2, 6, 7],
    2: [0, 1, 4, 5, 6, 7],
    3: [6, 7],
    4: [2, 5, 7],
    5: [0, 2, 4, 7],
    6: [1, 2, 3, 7],
    7: [0, 1, 2, 3, 4, 5, 6]})
# [0, 2, 5, 7, 1, 4, 6, 3]


def dfs(graph: Dict[int, List[int]]) -> List[int]:
    """
    perform dfs on the graph and store its result
    in the list of vertices(integers that represent vertices)
    :rtype: list(int)
    :param graph:  dict(key=int, value=list(int))
    :return: dfs-result
    """
    pass
dfs(graph={
    0:[1,2],
    1:[0,5,6],
    2:[0,3,4,9],
    3:[9,10],
    4:[2],
    5:[1],
    6:[1,7,8],
    7:[6,8],
    8:[6,7],
    9:[2,3,10],
    10:[3,9]
})
# [0, 1, 5, 6, 7, 8, 2, 3, 9, 10, 4]

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

print(calc_pow(read_csv('graph.csv')))

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
    # Your code goes here(delete "pass" keyword)
    pass
