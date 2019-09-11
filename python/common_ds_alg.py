"""
This is templates for common data structures and algorithms.
Frequently used in my leetcode practices.
"""


"""
Basic built-in types & libs
"""
list, dict, set, tuple


from collections import Counter
from collections import defaultdict

# call basic operators as functions
from operator import truediv, mul, add, sub

sorted(iterable, key=lambda x: x, reversed=True)

"""
Binary search
"""

nums, target
left, right = 0, len(nums) - 1

while left + 1 < right:
    mid = (left + right) // 2

    # might need modification to fit the problem.
    if nums[mid] < target:
        left = mid
    elif nums[mid] > target:
        right = mid

"""
Two-pointer
"""




"""
quick select
"""
# for kth smallest item.

def quick_select(nums, begin, end, k):
    # find the k+1th smallest element, whose idx == k.
    if begin == end:
        return nums[begin]

    pivot_idx = partition(nums, begin, end)
    if k == pivot_idx:
        return nums[k]

    if k < pivot_idx: # find in left side
        return quick_select(nums, begin, pivot_idx - 1, k)

    return quick_select(nums, pivot_idx + 1, end, k)


def partition(nums, begin, end):
    # could choose any pivot, even with randomness
    pivot_idx = (begin + end) // 2 
    
    pivot_val = nums[pivot_idx]
    nums[pivot_idx], nums[end] = nums[end], nums[pivot_idx]
    
    # scan from `begin` to `end`-1, only leave elements smaller
    # than `pivot_val` on the left side.
    write_pos = begin
    for i in range(begin, end):
        if nums[i] < pivot_val:
            nums[i], nums[write_pos] = nums[write_pos], nums[i]
            write_pos += 1
    
    # move the pivot back to where it should be.
    nums[write_pos], nums[end] = nums[end], nums[write_pos]

    return write_pos


"""
BST iterator
"""


"""
Represent a Graph (with built-in types)
"""



"""
BFS
"""

from collections import deque

visited = set()
queue = deque()
queue.append(root)
visited.add(root)
while len(queue) > 0:
    node = queue.popleft()
    print(node)

    for ne in node.neighbors:
        if ne not in visited:
            queue.append(ne)

"""
DFS, preorder, inorder postorder
"""

def inorder(node, order):
    if node is None:
        return 

    order.append(node.val)
    inorder(node.left)
    inorder(node.right)

order = []
inorder(root, order)

# This is a common trick to collect results with recursion.
# list are mutable in python, so all recusion calls will 
# operate on the same instance of list.

"""
  Combinations & Permutation

usually works when the problem asks for every solution.
"""
# iterators for combinations, permuations, ...
from itertools import product, permutations

# combination
def search(nums, pos, combo, solutions):
    # termination condition
    if done:
        solutions.append()
        return

    while pos < len(nums):
        combo.append(nums[pos])
        search(nums, pos+1, combo, solutions)
        combo.pop()
        pos += 1


# permutation
def search(nums, visited, perm, solutions):
    # termination condition
    if done:
        solutions.append()
        return

    for i in range(len(nums)):
        if i in visited:
            continue
        visited.add(i)
        perm.append(nums[i])
        search(nums, visited, perm, solutions)
        visited.remove(i)
        perm.pop()


""" 
  Heap / Priority Queue

- insert(H, x): O(log n)
- extract_min(H): O(1) amortized
- decrease_key(H, x, k): O(log n)
- meld(H1, H2): O(n)
- find_min(H, x): O(1)
- delete(H, x): O(log n)
"""
import heapq
# default is min heap. to use a max heap, invert the numbers.
# we could also use a tuple to store objects. first element of 
# tuple will be used for comparison.

# obtain heap from existing iterable.
unordered_list = [6,3,9,4,2]
heapq.heapify(unordered_list)

# built heaps
heap = []

heapq.heappush(heap, 3)
heapq.heappush(heap, 9)
heapq.heappush(heap, 6)
heapq.heappop(heap)

heapq.nsmallest(list, )


"""
Union Find

- make_set(x): O(1)
- find(x): m O(log* n) (where m: total # of operations, n: # of elements)
- union(x, y): same as find(x, y) 
"""
class Node:
    def __init__(self, val):
        self.val = val

class UnionFind:
    def __init__(self):
        self.node_2_parent = {}
        self.node_2_rank = {}

    def make_set(x):
        self.node_to_parent[x] = x
        self.node_to_rank[x] = 0

    def find(x):
        if self.node_2_parent[x] != x:
            self.node_2_parent[x] = self.find(self.node_2_parent[x])
        return self.node_2_parent[x]

    def union(x, y):
        x_repr, y_repr = self.find(x), self.find(y)
        if x_repr == y_repr:
            return 

        x_rank, y_rank = self.node_2_rank[x_repr], self.node_2_rank[y_repr]
        if x_rank > y_rank:
            self.node_2_parent[y_repr] = x_repr
        elif x_rank < y_rank:
            self.node_2_parent[x_repr] = y_repr
        else:
            self.node_2_parent[y_repr] = x_repr
            self.node_2_rank[x_repr] += 1

uf = UnionFind()
uf.make_set(1)            
uf.make_set(2)
uf.make_set(3)
uf.make_set(4)
uf.union(1,3)
print(uf.find(2) == uf.find(4))
print(uf.find(1) == uf.find(3))
 

"""
Trie
"""




