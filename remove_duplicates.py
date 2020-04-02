# Напишите функцию, которая на вход получает голову связного списка и удаляет из него все
# неуникальные (по значению) элементы. Предположите, что все элементы, которые будут вам
# встречаться, — числа.


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f'[Node with value {self.value}]'


def print_linked_list(head):
    cur = head
    while cur is not None:
        print(cur)
        cur = cur.next


def remove_duplicates(head):
    cur = head
    val_list = []
    while cur is not None:
        val_list.append(cur.value)
        cur = cur.next

    unique = [x for x in val_list if val_list.count(x) == 1]
    cur = head
    nodes = []
    while cur is not None:
        if cur.value in unique:
            nodes.append(Node(cur.value))
        cur = cur.next
    for i, n in enumerate(nodes):
        try:
            n.next = nodes[i + 1]
        except:
            n.next = None
    return nodes[0]


def main():
    h, a, b, c, d, e, f, g, i = Node(1), Node(1), Node(3), Node(2), Node(4), Node(4), Node(5),\
        Node(4), Node(5)
    h.next = a
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g
    g.next = i
    i.next = None

    print_linked_list(h)
    print('---')
    h = remove_duplicates(h)
    print_linked_list(h)


if __name__ == '__main__':
    main()

# [Node with value 1]
# [Node with value 1]
# [Node with value 3]
# [Node with value 2]
# [Node with value 4]
# [Node with value 4]
# [Node with value 5]
# [Node with value 4]
# [Node with value 5]
# ---
# [Node with value 3]
# [Node with value 2]
