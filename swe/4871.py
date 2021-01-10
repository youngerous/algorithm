## 4871 - 그래프 경로
### ref: https://taejin0527.github.io/[object%20Object]/sw-stack1/


def make_graph(v, e):
    # key means vertex / set() means related node
    graph = {key + 1: set() for key in range(V)}

    # construct directed graph
    # ex) {1: {3,4,6}, 2:{3}, 3:set()}
    for _ in range(e):
        key, val = map(int, input().split())
        graph[key].add(val)
    return graph


def DFS(graph, v, e):
    visited, stack = [], []  # set path tracker
    stack.append(v)  # push start node
    is_path = False

    while stack:
        node = stack.pop()
        if node == e:  # arrived
            is_path = True
            break

        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return is_path


T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    graph = make_graph(V, E)

    start, end = map(int, input().split())
    exist = DFS(graph, start, end)
    print(f"#{test_case} {int(exist)}")
