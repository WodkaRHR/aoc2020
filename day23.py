from tqdm import tqdm

order = list(map(int, '872495136'))
# order = list(map(int, '389125467'))

class Node:

    def __init__(self, key):
        self.next = None
        self.key = key

    def insert(self, other):
        other.next = self.next
        self.next = other
    
    def remove_next(self):
        node = self.next
        self.next = node.next
        node.next = None
        return node

    def __repr__(self):
        if self.next is not None:
            return f'N{self.key} -> {self.next.key}'
        else:
            return f'T{self.key}'

def play(nodes, current, num_rounds):
    n = len(nodes)
    for i in tqdm(range(num_rounds)):
        picked_up = [current.remove_next() for _ in range(3)]
        picked_up_keys = set(n.key for n in picked_up)
        destination_key = current.key
        while True:
            destination_key = ((destination_key - 2) % n) + 1 # Subtract 1, wrap arround [1-N]
            if destination_key not in picked_up_keys:
                break
        destination = nodes[destination_key]
        for node in picked_up:
            destination.insert(node)
            destination = node
        current = current.next

nodes = {i : Node(i) for i in order}
for idx in range(len(order)):
    nodes[order[idx]].next = nodes[order[(idx + 1) % len(nodes)]]
play(nodes, nodes[order[0]], 100)
result = ''
node = nodes[1]
for _ in range(8):
    node = node.next 
    result += str(node.key)
print(result)

# Reset the node configuration
nodes = {i : Node(i) for i in order}
for idx in range(len(order)):
    nodes[order[idx]].next = nodes[order[(idx + 1) % len(nodes)]]

# Insert 1000000 - 9 more nodes
tail = nodes[order[-1]]
for key in range(10, 1000000 + 1):
    nodes[key] = Node(key)
    tail.insert(nodes[key])
    tail = nodes[key]

play(nodes, nodes[order[0]], 10000000)
result = nodes[1].next.key * nodes[1].next.next.key
print(result)


