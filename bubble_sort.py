class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f'[Node with value {self.value}]'


def sort(head):
    change = True
    while change:
        cur, change, l = head, False, []
        l.append(head)
        while cur.next is not None:
            next = cur.next
            l.append(next)
            if cur.value > next.value:
                cur.value, next.value = next.value, cur.value
                change = True
            cur = cur.next

        l.append(None)
        for i in range(len(l) - 1):
            l[i].next = l[i + 1]
        head = l[0]

    return head


def main():
    h, a, b, c, d, e = Node(2), Node(4), Node(1), Node(1), Node(2), Node(0)
    h.next = a
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = None

    nodes = []
    cur = h
    while cur is not None:
        nodes.append(cur)
        cur = cur.next

    print(f'[{", ".join([str(n.value) for n in nodes])}]')
    print('---')
    h = sort(h)
    print(f'[{", ".join([str(n.value) for n in nodes])}]')


if __name__ == '__main__':
    main()
