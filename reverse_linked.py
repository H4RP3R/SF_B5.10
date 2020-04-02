# Напишите функцию (пусть она будет называться reverse_linked_list), которая разворачивает
# связный список. На вход она принимает головную ноду, а на выход отдает хвостовую ноду
# исходного списка, которая становится головной.


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


def reverse_linked_list(head):
    prev = head
    cur = prev.next
    prev.next = None

    while True:
        try:
            n = Node(cur.value)
            n.next = prev
            prev = cur
            cur = cur.next
            prev = n
        except:
            return prev


def main():
    h, a, b, c, d = Node(1), Node(2), Node(3), Node("Внезапно"), Node(5)
    h.next = a
    a.next = b
    b.next = c
    c.next = d

    print_linked_list(h)
    print('---')
    h = reverse_linked_list(h)
    print_linked_list(h)


if __name__ == '__main__':
    main()

# [Node with value 1]
# [Node with value 2]
# [Node with value 3]
# [Node with value Внезапно]
# [Node with value 5]
# ---
# [Node with value 5]
# [Node with value Внезапно]
# [Node with value 3]
# [Node with value 2]
# [Node with value 1]
