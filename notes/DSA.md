# Data Structures and Algorithms

## Data Structures

### Contiguous Memory Data Structures

Data structures that allocate a continuous block of memory for their elements.

- **Array**: Basic contiguous memory structure.
  - **Static Array**: Fixed-size array determined at compile time.
  - **Dynamic Array**: Array that can dynamically grow in size.
  - **Matrix**: Two-dimensional array.
  - **N-dimensional Array (ND-array)**: An array with more than two dimensions, used to represent higher-dimensional data structures such as tensors in computational mathematics, data science, and engineering.
  - **Bit Array (Bit Vector)**: Compact array storing bits.

- **String**: Sequence of characters stored contiguously in memory.
  - **Immutable String**: A string that cannot be modified after creation, common in many programming languages.
  - **Mutable String**: A string-like data structure that allows in-place modifications.
  - **C-style String**: A string represented as an array of characters terminated by a null character `\0`.
  - **Unicode String**: A string that supports Unicode characters, allowing representation of a wide range of characters beyond ASCII.
  - **Rope**: A data structure for efficiently storing and manipulating very large strings by breaking them into smaller chunks.
  - **Packed String**: A specialized string representation that compresses or packs characters to save memory or improve performance in specific applications.

- **Circular Buffer**: Fixed-size buffer wrapping around when full.
  - **Circular Queue**: A data structure that follows FIFO (First In, First Out) principle with a fixed size, where elements are added at the rear and removed from the front.
  - **Circular Buffer with Overwrite**: A circular buffer that overwrites the oldest data when it reaches capacity and new data is added.

#### Non-Contiguous Memory Data Structures

Non-contiguous memory data structures do not store elements in contiguous blocks of memory.

- **Linked List**: A linear collection of data elements, where each element points to the next one, allowing for efficient insertion and deletion operations.
  - **Singly Linked List**: Each node contains a data element and a reference (link) to the next node in the sequence.
  - **Doubly Linked List**: Each node contains a data element and references (links) to both the next and previous nodes in the sequence.
  - **Circular Linked List**: A linked list where the last node points back to the first node instead of terminating at `None`.
  - **Skip List**: A probabilistic data structure that allows for faster search times than a simple linked list by maintaining multiple layers of linked lists with skip pointers.

- **Graph**: A collection of nodes (vertices) and edges that connect pairs of nodes, representing relationships between objects.
  - **Undirected Graph**: A graph where edges have no direction, and any edge between nodes $A$ and $B$ is bidirectional.
  - **Directed Graph (Digraph)**: A graph where edges have a direction, meaning there is an ordered pair of nodes $(A,B)$ such that there is a directed edge from $A$ to $B$ but not necessarily from $B$ to $A$.
  - **Directed Acyclic Graph (DAG)**: A directed graph with no cycles, where each edge has a direction.
  - **Weighted Graph**: A graph where edges have weights or costs associated with them, influencing algorithms like shortest path or minimum spanning tree calculations.
  - **Sparse Graph**: A graph where the number of edges is much less than the number of possible edges, often represented using adjacency lists for efficient memory usage.
  - **Dense Graph**: A graph where the number of edges is close to the maximum number of edges, typically represented using adjacency matrices for efficient edge lookup.
  - **Tree**: A special type of graph with a hierarchical structure, where each node has a parent-child relationship and there are no cycles.

#### Algorithm-Based Data Structures

Data structures optimized with specific algorithms.

- **Hashmap (Hash Table)**: Key-value store using hashing for fast access.
  - **Linked Hash Map**: Preserves insertion order.
  - **Identity Hash Map**: Uses object reference equality for keys.
  - **Concurrent Hash Map**: Supports concurrent access.
  - **Weak Hash Map**: Allows keys to be garbage collected.

- **Set**: Collection of unique elements using hashing or other structures like trees.
  - **TreeSet**: Implements a set using a self-balancing binary search tree (like AVL tree or Red-Black tree), ensuring elements are stored in sorted order, allowing for efficient range queries and ordered traversal.
  - **HashSet**: Implements a set using a hashmap where elements are stored as keys, ensuring uniqueness and allowing for fast insertion, deletion, and lookup operations.
  - **LinkedHashSet**: Maintains a doubly linked list running through all of its entries, used to maintain order.

#### Abstract Data Types (ADTs)

- **Stack**: Stack data structures, which follow the Last In, First Out (LIFO) principle.
  - **Array-based Stack**: Uses a static or dynamic array to implement stack operations.
  - **Linked List-based Stack**: Uses nodes with pointers to implement stack operations efficiently.
  - **Dynamic Stack**: A stack that can grow and shrink dynamically based on the number of elements.
  - **Bounded Stack**: A stack with a fixed maximum capacity.

- **Queue**: Queue data structures, which follow the First In, First Out (FIFO) principle.
  - **Deque (Double-Ended Queue)**: Supports insertion and deletion at both ends.
  - **Priority Queue**: Supports efficient retrieval of highest (or lowest) priority elements.

- **List**: List data structures that store collections of elements.
  - **Array list**: Uses an array to store elements with dynamic resizing.
  - **Multiset (Bag)**: Allows multiple occurrences of the same element.

- **Dictionary**: Associative array data structures that store key-value pairs.
  - **Tree Map**: Stores keys in a sorted tree structure.
  - **Linked Tree Map**: Combines linked list and tree map features.
  - **Bimap**: Supports bidirectional mapping between keys and values.
  - **Hash Array Mapped Trie**: Efficiently stores key-value pairs using a trie structure with hash codes.

#### Tree

A hierarchical structure with a root node and child nodes, where each node may have a parent and multiple children.

- **Binary Tree**: Each node has at most two children.
  - **Full Binary Tree**: Every node other than the leaves has two children.
  - **Complete Binary Tree**: Every level, except possibly the last, is completely filled, and all nodes are as far left as possible.
  - **Perfect Binary Tree**: A binary tree in which all interior nodes have two children and all leaves have the same depth.
- **Binary Search Tree (BST)**: A binary tree where the left child of a node contains only nodes with keys less than the node's key and the right child contains only nodes with keys greater than the node's key.
- **Self-Balancing Tree**: Automatically maintains balance in a binary search tree to ensure O(log n) time complexity for insert, delete, and search operations.
  - **AVL Tree**: A self-balancing binary search tree where the difference between heights of left and right subtrees cannot be more than one for all nodes.
  - **Red-Black Tree**: A self-balancing binary search tree with each node colored red or black, ensuring no two red nodes are adjacent.
- **Multiway Trees**: Trees where nodes can have more than two children.
  - **B-Tree**: A self-balancing tree data structure that maintains sorted data and allows searches, sequential access, insertions, and deletions in logarithmic time.
  - **B+ Tree**: A variant of B-tree where only the leaf nodes hold pointers to data and all leaf nodes are linked together in a linked list.
- **Heap**: A specialized tree-based data structure that satisfies the heap property.
  - **Binary Heap**: A binary tree with two additional properties: shape property (a complete binary tree) and heap property (parent nodes are greater than or equal to child nodes).
  - **Fibonacci Heap**: A type of heap data structure consisting of a collection of trees that are min-heap ordered.
- **Trie (Prefix Tree)**: A tree-like data structure used to store a dynamic set of strings where each node represents a common prefix.
- **Suffix Tree**: A compressed trie containing all the suffixes of the given text as their keys and positions in the text as their values.
- **Segment Tree**: A tree data structure used for storing intervals or segments, with the ability to merge and query intervals efficiently.
- **Fenwick Tree (Binary Indexed Tree)**: A data structure that supports efficient updates and prefix sum queries in logarithmic time.
- **Quad Tree**: A tree data structure in which each internal node has exactly four children.
- **Octree**: A tree data structure in which each internal node has exactly eight children, commonly used for spatial partitioning in three-dimensional space.
- **Aho-Corasick Automaton**: An efficient multiple-pattern matching algorithm that constructs a finite state machine representing a set of patterns.

### Operations

#### Object Operations

- **Initialize:** Create and set up a new object.
- **Clone:** Create an exact copy of the object.
- **Destroy:** Remove the object from memory.

#### Data Operations

- **Insert:** Add new data elements.
- **Update:** Modify existing data elements.
- **Delete:** Remove data elements.
- **Traverse:** Visit all elements systematically.

#### Query Operations

- **Map:** Apply a function to each element.
- **Reduce:** Aggregate elements into a single result using a function.
- **Fold:** Similar to reduce, but more general used in functional programming contexts.
- **Filter:** Extract elements that meet certain criteria.
- **Search:** Find elements that match a specific value.
- **Locate:** Identify the position of an element.
- **Count:** Determine the number of elements.

#### Modification Operations

- **Sort:** Arrange elements in a specified order.
- **Reverse:** Invert the order of elements.
- **Shuffle:** Randomly reorder the elements.
- **Rotate:** Move elements circularly.
- **Clear:** Remove all elements.
- **Resize:** Change the size of the data structure.
- **Truncate:** Reduce the size by removing elements.
- **Group:** Organize elements into groups based on a key.
- **Partition:** Divide elements into distinct subsets based on a criterion.

#### Multi-Object Operations

- **Merge:** Combine elements from multiple objects.
- **Append:** Add elements from one object to another.
- **Intersect:** Find common elements between objects.
- **Difference:** Find elements in one object but not another.
- **Union:** Combine elements from multiple objects without duplication.

#### Explanation

##### Filter vs. Search vs. Locate

- **Filter:**
  - **Description:** Extract elements that meet certain criteria.
  - **Example:** From a list of numbers, extract all even numbers.`
  - **Use Case:** Often used to create a subset of elements that satisfy specific conditions.
- **Search:**
  - **Description:** Find elements that match a criterion.
  - **Example:** From a list of numbers, find all occurrences of the number 5.
  - **Use Case:** Used to identify elements that match a particular value or set of values.
- **Locate:**
  - **Description:** Identify the position of an element.
  - **Example:** Find the index of the number 5 in a list of numbers.
  - **Use Case:** Used when the position or index of an element within a collection is needed.

##### Fold vs. Reduce

- **Fold:**
  - **Description:** Similar to reduce, but often used in functional programming contexts. It generally refers to a more general or flexible way of combining elements.
  - **Example:** Summing a list of numbers, where the initial value can be specified, and the function can be applied from either direction (left fold or right fold).
  - **Use Case:** Often used in functional programming languages to process collections in a flexible manner, supporting both left and right associativity.
- **Reduce:**
  - **Description:** Aggregate elements using a function to produce a single cumulative result.
  - **Example:** Summing a list of numbers.
  - **Use Case:** Used to combine all elements of a collection into a single result using an associative operation.

##### Group vs. Partition

- **Group:**
  - **Description:** Organize elements into groups based on a key.
  - **Example:** Grouping a list of students by their grade level.
  - **Use Case:** Used to categorize elements into multiple sets where each set shares a common key.
- **Partition:**
  - **Description:** Divide elements into distinct subsets based on a criterion.
  - **Example:** Partitioning a list of numbers into two subsets: one with even numbers and one with odd numbers.
  - **Use Case:** Used to split a collection into two or more subsets based on a boolean condition or similar criterion.

## Algorithms

### Pattern Matching

- **Knuth-Morris-Pratt (KMP)**: Efficiently searches for occurrences of a "word" W within main "text" T.
- **Boyer-Moore**: Uses character comparisons to skip sections of the text, making it efficient for large texts.
- **Rabin-Karp**: Uses hashing to find any one of a set of pattern strings in a text.

### Sorting

- **Bubble Sort**: Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
- **Insertion Sort**: Builds the sorted array one item at a time, inserting each new element into its correct position.
- **Radix Sort**: Sorts numbers by processing individual digits.
- **Address Sort**: Sorts data by first digit of the keys.

### Searching

- **Linear Search**: Iterates through a list to find a target value.
- **Binary Search**: Finds the position of a target value within a sorted array.
- **Jump Search**: Searches sorted arrays by jumping ahead by fixed steps and then linearly searching backwards to find the exact location.
- **Interpolation Search**: Improves performance of Binary Search for uniformly distributed data.

### Graph Algorithms

- **Depth-First Search (DFS)**: Explores as far as possible along each branch before backtracking.
- **Breadth-First Search (BFS)**: Explores all nodes at the present depth level before moving on to nodes at the next depth level.
- **Dijkstra's Algorithm**: Finds the shortest path between nodes in a graph with non-negative edge weights.
- **Prim's Algorithm**: Finds a minimum spanning tree for a weighted undirected graph.
- **Kruskal's Algorithm**: Constructs a minimum spanning tree for a connected weighted graph.

### Dynamic Programming

- **Fibonacci Sequence**: Computes Fibonacci numbers efficiently using dynamic programming.
- **Longest Common Subsequence (LCS)**: Finds the longest subsequence common to all sequences in a set of sequences.

### Miscellaneous

- **Greedy Algorithms**: Makes locally optimal choices at each stage with the hope of finding a global optimum.
- **Backtracking**: Searches for all possible solutions recursively and prunes paths that lead to dead-ends.
- **Segment Tree**: A data structure for efficient range queries and updates.

## Concepts

- **Abstract Data Types (ADT)**: A theoretical model for data structures that defines the data and operations without specifying the implementation details.
- **Recursion**: A method where a function calls itself to solve a problem by breaking it down into smaller sub-problems.

### Hash Map Concepts

- **Open Addressing**: A technique where all elements are stored directly in the hash table array itself, typically used for resolving collisions by probing.
  - **Linear Probing**: A method of open addressing where if the slot at the hashed index is already occupied, the next slot in the array is tried, and so on.
  - **Quadratic Probing**: A variation of linear probing where the interval between probes is increased quadratically.
  - **Double Hashing**: A method where a second hash function determines the probe interval, aiming to avoid clustering.
- **Separate Chaining**: A technique where each bucket in the hash table points to a linked list of elements that hashed to the same index, used for resolving collisions.
- **Robin Hood Hashing**: An open-addressing scheme where elements are displaced along with their distance to their ideal position, aiming to reduce the maximum search time.
- **Cuckoo Hashing**: A hashing technique that resolves collisions using multiple hash functions and displacing existing elements to alternative locations.

### Graph Concepts

- **Adjacency List**: A way of representing a graph as a collection of lists or arrays, one for each vertex, containing the vertices adjacent to it.
- **Adjacency Matrix**: A way of representing a graph as a 2D array, where the element at row i and column j is true if there is an edge from vertex i to vertex j.
- **Incidence Matrix**: A way of representing a graph as a 2D array, where rows represent vertices and columns represent edges, with entries indicating the incidence of vertices on edges.
- **Graph Traversal**: Techniques to visit all vertices of a graph.
  - **Depth-First Search (DFS)**: Explores as far as possible along each branch before backtracking.
  - **Breadth-First Search (BFS)**: Explores all nodes at the present depth level before moving on to nodes at the next depth level.

### Tree Concepts

- **Binary Tree**: A tree data structure in which each node has at most two children.
  - **Binary Search Tree (BST)**: A binary tree in which each node's value is greater than all values in its left subtree and less than those in its right subtree.
  - **Self-Balancing Trees**: Trees that automatically maintain a balanced height to ensure efficient operations.
    - **AVL Tree**: A self-balancing binary search tree where the difference in heights between the left and right subtrees is at most one for every node.
    - **Red-Black Tree**: A self-balancing binary search tree with an additional property of node coloring that helps in balancing the tree.
  - **Heap**: A complete binary tree used to implement priority queues, where each node is greater (max-heap) or lesser (min-heap) than its children.
    - **Binary Heap**: A type of heap where each node has at most two children.
    - **Fibonacci Heap**: A heap data structure consisting of a collection of trees, which allows for more efficient merging of heaps.

### Dynamic Programming Concepts

- **Memoization**: Storing the results of expensive function calls and reusing the cached result when the same inputs occur again.
- **Tabulation**: Building a table in a bottom-up manner and filling the table based on previously computed results.

### Complexity Analysis

- **Time Complexity**: The computational complexity that describes the amount of time it takes to run an algorithm.
- **Space Complexity**: The computational complexity that describes the amount of memory space required by an algorithm.

This list includes key concepts in data structures and algorithms, covering a wide range of fundamental ideas and advanced techniques.

## Techniques

- **Two Pointers Technique**: Utilizes two pointers to solve problems efficiently in linear time.
- **Sliding Window Technique**: Maintains a subset of a data structure over a contiguous subarray of the data.
- **Greedy Technique**: Makes locally optimal choices at each stage with the hope of finding a global optimum.
- **Divide and Conquer**: Breaks down a problem into smaller subproblems, solves each subproblem recursively, and then combines the solutions.
- **Dynamic Programming (DP)**: Solves problems by breaking them down into overlapping subproblems and using stored results of subproblems to avoid re-computation.
- **Backtracking**: Searches for all possible solutions recursively and prunes paths that lead to dead-ends.
- **Depth-First Search (DFS)**: Explores as far as possible along each branch before backtracking.
- **Breadth-First Search (BFS)**: Explores all nodes at the present depth level before moving on to nodes at the next depth level.
- **Hashing**: Maps data to an array of indices using a hash function to accelerate data retrieval.

## Patterns

- **Prefix Sum**: Optimizes multiple subarray sum queries from `O(n*m)` to `O(1)` by precomputing sums of all subarrays.
  - Store sums of all subarrays in a 2D array.
  - Use the 2D array to calculate sums of any subarray in `O(1)` time.
- **Two Pointers**: Reduces time complexity by moving pointers toward or away from each other for problems like palindrome checking.
  - Set up two pointers, one at the start and one at the end of the array.
  - Move the pointers toward or away from each other based on the condition.
- **Sliding Window**: Optimizes subarray problems by maintaining a window that slides across the array, reducing time complexity.
  - Set up a window of size k.
  - Slide the window one element to the right and recompute the result.
- **Fast and Slow Pointers**: Detects cycles in linked lists or finds the middle of a list in one pass using two pointers.
  - Set up two pointers, one moving twice as fast as the other.
  - If the two pointers meet, there is a cycle.
  - If not, the fast pointer will reach the end of the list.
- **Linked List In-Place Reversal**: Rearranges linked list nodes without extra space by using three pointers.
  - Set up three pointers, one at the start, one at the middle, and one at the end.
  - Swap the start and end pointers, and move the middle pointer one step to the right.
  - Repeat until the middle pointer reaches the end of the list.
- **Monotonic Stack**: Finds the next greater or smaller element in `O(n)` time, using a stack.
  - Set up a stack of elements.
  - Iterate through the array and push or pop elements based on the condition.
- **Top K Elements**: Efficiently finds K largest/smallest elements using a min/max heap.
  - Set up a min/max heap.
  - Iterate through the array and push or pop elements based on the condition.
- **Overlapping Intervals**: Solves problems involving merging or intersecting intervals by sorting and iterating through them.
  - Sort the intervals by their start time.
  - Iterate through the intervals and merge or intersect them as needed.
- **Modified Binary Search**: Extends binary search to non-perfectly sorted arrays, such as rotated sorted arrays.
  - Set up two pointers, one at the start and one at the end of the array.
  - Move the pointers toward or away from each other based on the condition.
- **Binary Tree Traversal**: Includes pre-order, in-order, post-order, and level-order traversal, each used for different problem types.
  - Recursively traverse the tree in pre-order, in-order, post-order, or level-order.
- **Depth-First Search (DFS)**: Explores all paths in graphs or trees and is useful for problems involving cycles or connected components.
  - Set up a stack of nodes to visit.
  - Visit each node in the stack and push its neighbors to the stack.
- **Breadth-First Search (BFS)**: Traverses graphs level-by-level and is ideal for finding shortest paths or connected components.
  - Set up a queue of nodes to visit.
  - Visit each node in the queue and push its neighbors to the queue.
- **Matrix Traversal**: Uses graph techniques like DFS and BFS to explore 2D arrays, with applications like island counting.
  - Set up a 2D array of nodes to visit.
  - Visit each node in the array and push its neighbors to the stack or queue.
- **Backtracking**: Explores all possible solutions and backtracks when paths are invalid, useful for puzzles like Sudoku.
  - Set up a stack of nodes to visit.
  - Visit each node in the stack and push its neighbors to the stack.
  - If the node is invalid, pop it from the stack and backtrack.
- **Dynamic Programming**: Solves optimization problems by breaking them down into subproblems and avoiding redundant work.
  - Set up a 2D array of subproblems to solve.
  - Iterate through the array and solve each subproblem.
