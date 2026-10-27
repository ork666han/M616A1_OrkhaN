class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# İki düyün yaradırıq
d1 = Node(10)
d2 = Node(20)

# Bir-birinə bağlayırıq
d1.next = d2
d2.prev = d1

# Yoxlayırıq
print(d1.next.data)  # 20 (d1-in sonrakı düyünü)
print(d2.prev.data)  # 10 (d2-nin əvvəlki düyünü)