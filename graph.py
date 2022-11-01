class Node:
    def __init__(self, val, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Graph:
    def __init__(self, head):
        self.head = head
    
    def bfs(self, val, start = None):
        start = start or self.head
        queue = [start]
        steps = 0

        while True:
            if len(queue) == 0:
                return f'{val} not found starting from {start.val}'

            currNode = queue[0] 

            if currNode.val == val:
                return f'{currNode.val} found in {steps} steps from the head!'

            queue = queue[1:] + currNode.neighbors
            steps += 1

node1 = Node(1)
node2 = Node(2, [node1])
node3 = Node(3, [node2])
node4 = Node(4, [node3])
node5 = Node(5, [node4])

graph = Graph(node5)

print(graph.bfs(10))