# dic2 = {j: [j for j in input().split()] for i in range(int(input()))}

# print(dic2)
#
# graph = {'A': ['B', 'C'],
#          'B': ['C', 'D'],
#          'C': ['D'],
#          'D': ['C'],
#          'E': ['F'],
#          'F': ['C']}
#
#
# def find_path(graph, start, end, path=None):
#     if path is None:
#         path = []
#     path = path + [start]
#     if start == end:
#         return path
#     if start not in graph:
#         return None
#     for node in graph[start]:
#         if node not in path:
#             newpath = find_path(graph, node, end, path)
#             if newpath:
#                 return newpath
#     return on

class ExtendedStack(list):

    def sum(self):
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 + top2)

    def sub(self):
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 - top2)

    def mul(self):
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 * top2)

    def div(self):
        top1 = self.pop()
        top2 = self.pop()
        self.append(top1 // top2)

ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
ex_stack.div()
assert ex_stack.pop() == 2
ex_stack.sub()