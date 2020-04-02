# Напишите функцию, которая получает на вход голову связного списка и число k,
# а возвращает узел, соответствующий k-му узлу с конца списка.


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


def give_kth_last(head, k):
    l = []
    cur = head
    i = 0
    while cur is not None:
        l.append(cur)
        cur = cur.next
    return l[-k]


def main():
    h, a, b, c, d, e, f, g = Node(3), Node(1), Node(2), Node(7), Node(5), Node(4), Node(0),\
        Node(9)
    h.next = a
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    f.next = g
    g.next = None

    print_linked_list(h)
    n = give_kth_last(h, 3)
    print('---')
    print(n)


if __name__ == '__main__':
    main()


# [Node with value 3]
# [Node with value 1]
# [Node with value 2]
# [Node with value 7]
# [Node with value 5]
# [Node with value 4]
# [Node with value 0]
# [Node with value 9]
# ---
# [Node with value 4]
