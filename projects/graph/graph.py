"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        neighbors = set()
        for edge in self.vertices[vertex_id]:
            neighbors.add(edge)
        return neighbors

    def bft(self, starting_vertex):
        used = set() # Keep track of already used vertices
        q = Queue() # Make a Queue
        q.enqueue(starting_vertex)
        used.add(starting_vertex)
        while q.size() > 0:
            node_index = q.dequeue() # Get current node
            node_current = self.vertices[node_index]
            print(node_index)
            for neighbor in node_current:  # Go through all unused neighbors
                if neighbor not in used:
                    q.enqueue(neighbor) # Enqueue vertex
                    used.add(neighbor)

    def dft(self, starting_vertex):
        used = set() # Keep track of already used vertices
        st = Stack() # Make a Stack
        st.push(starting_vertex) # Push starting vertex
        used.add(starting_vertex)
        while st.size() > 0:
            node_index = st.pop() # Get current node
            node_current = self.vertices[node_index]
            print(node_index)
            for neighbor in node_current:  # Go through all unused neighbors
                if neighbor not in used:
                    st.push(neighbor) # Push vertex
                    used.add(neighbor)

    def dft_recursive(self, vertex_id, used=None):
        if used == None: # Make new used set if not one (initial call)
            used = set()
            used.add(vertex_id)
        node_current = self.vertices[vertex_id] # Get current node
        print(vertex_id)
        for neighbor in node_current:  # Go through all unused neighbors
            if neighbor not in used:
                used.add(neighbor)
                self.dft_recursive(neighbor, used) # Pass through used set

    def bfs(self, starting_vertex, destination_vertex):
        used = set() # Keep track of already used vertices
        q = Queue() # Make a Queue
        q.enqueue((starting_vertex, [])) # Enqueue vertex with list of path travelled
        used.add(starting_vertex)
        while q.size() > 0:
            node = q.dequeue() # Get current node
            node_index = node[0]
            node_path = node[1].copy()
            node_current = self.vertices[node_index] 
            node_path.append(node_index) # Add current vertex to path
            if node_index == destination_vertex: 
                return node_path
            for neighbor in node_current: # Go through all unused neighbors
                if neighbor not in used:
                    q.enqueue((neighbor, node_path)) # Enqueue vertex with list of path travelled
                    used.add(neighbor)
        return None

    def dfs(self, starting_vertex, destination_vertex):
        used = set() # Keep track of already used vertices with list of path travelled
        st = Stack() # Make a Stack
        st.push((starting_vertex, [])) # Push starting vertex
        used.add(starting_vertex)
        while st.size() > 0:
            node = st.pop() # Get current node
            node_index = node[0]
            node_path = node[1].copy()
            node_current = self.vertices[node_index] 
            node_path.append(node_index) # Add current vertex to path
            if node_index == destination_vertex: # Return if at destination
                return node_path
            for neighbor in node_current:  # Go through all unused neighbors
                if neighbor not in used:
                    st.push((neighbor, node_path)) # Push vertex with list of path travelled
                    used.add(neighbor)
        return None

    def dfs_recursive(self, vertex_id, destination_vertex, node_path_orig=[], used=None):
        if used == None: # Make new used set if not one (initial call)
            used = set()
            used.add(vertex_id)
        node_current = self.vertices[vertex_id] # Get current node
        node_path = node_path_orig.copy()
        node_path.append(vertex_id) # Add current vertex to path
        if vertex_id == destination_vertex: # Return if at destination
            return node_path
        for neighbor in node_current:  # Go through all unused neighbors
            if neighbor not in used:
                used.add(neighbor)
                node_path = self.dfs_recursive(neighbor, destination_vertex, node_path, used) # Pass through used set
                if node_path[-1] == destination_vertex: # Return list if found the solution
                    return node_path
        return node_path_orig # Default returning original list

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
