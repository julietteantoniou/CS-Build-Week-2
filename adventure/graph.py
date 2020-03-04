"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.visited = set()

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id in self.vertices:
            print('vertex already exists')
        else:
            self.vertices[vertex_id] = {}

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('vertex does not exist')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue
        queue = Queue()
        # Add the starting vetex_id to the queue
        queue.enqueue(starting_vertex)
        # Create an empty set to store visited nodes
        visited = set()
        #while the queue is not empty-
        while queue.size() > 0:
            #Dequeue the first vertex
            first_vert = queue.dequeue()
            # Check if it's been visited
            # If it has NOT been visted-
            if not first_vert in visited:
                # Mark it as visited
                print(first_vert)
                visited.add(first_vert)
                # Then add all neighbors to the back of the queue
                for neighbor in self.get_neighbors(first_vert):
                    queue.enqueue(neighbor)
        return visited


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack
        stack = Stack()
        # Push the starting vetex_id to the top of the stack
        stack.push(starting_vertex)
        # Create an empty set to store visited nodes
        visited = set()
        #while the stack is not empty-
        while stack.size() > 0:
            #Pop the first vertex
            first_vert = stack.pop()
            # Check if it's been visited
            # If it has NOT been visted-
            if not first_vert in visited:
                # Mark it as visited
                print(first_vert)
                visited.add(first_vert)
                # Then push all neighbors to the top of the stack
                for neighbor in self.get_neighbors(first_vert):
                    stack.push(neighbor)

    def dft_shortest(self, starting_vertex):
                # Create an empty stack
        stack = Stack()
        # Push the starting vetex_id to the top of the stack
        stack.push([starting_vertex])
        # Create an empty set to store visited nodes
        visited = set()
        longest = 600
        direction_list = [[]]
        final_path= []
        end_node = 0
        final_directions = []
        #while the stack is not empty-
        while stack.size() > 0:
            current_path = stack.pop()
            current_node = current_path[-1]
            
            current_moves = direction_list.pop()
            #last_move = current_moves[-1]

            if not current_node in visited:
                visited.add(current_node)
                neighbors = self.get_neighbors(current_node)
                # print('neighbors', neighbors)
                for node in self.get_neighbors(current_node):
                    # print("*****",node)
                    # print(neighbors[node])
                    direction_dup = list(current_moves)
                    direction_dup.append(node)
                    direction_list.append(direction_dup)
                    path_dup = list(current_path)
                    path_dup.append(neighbors[node])
                    stack.push(path_dup)

                    # print('dup', path_dup, direction_dup)
                    if len(path_dup) < longest and path_dup[-1] not in self.visited and path_dup[-1] not in path_dup[:-1]:
                        longest = len(path_dup)
                        end_node = path_dup[-1]
                        final_path = path_dup
                        final_directions = direction_dup
        print(final_path, '******')
        for room in final_path:
            self.visited.add(room)
            # print('visited', self.visited)
        return (end_node, final_path, final_directions)


    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        print(starting_vertex)

        visited.add(starting_vertex)
        edges = self.get_neighbors(starting_vertex)
    
        if len(edges) == 0:
            return

        for edge in edges:
            if edge not in visited:
                self.dft_recursive(edge, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        queue.enqueue([starting_vertex])
        visited = set()
        direction_list = Queue()
        direction_list.enqueue([])
        final_list=[]
        while queue.size() > 0:
            current_path = queue.dequeue()
            current_node = current_path[-1]
            current_moves = direction_list.dequeue()
            if current_node == destination_vertex:
                for i in range(len(current_moves)):
                    final_list.append([current_moves[i], str(current_path[i + 1])])
                return final_list
            elif not current_node in visited:
                visited.add(current_node)
                neighbors = self.get_neighbors(current_node)
                for v in self.get_neighbors(current_node):
                    path_dup = list(current_path)
                    path_dup.append(neighbors[v])
                    direction_dup = list(current_moves)
                    direction_dup.append(v)
                    direction_list.enqueue(direction_dup)
                    queue.enqueue(path_dup)



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        stack.push([starting_vertex])
        visited=set()
        direction_list = [[]]
        final_list=[]
        while stack.size() > 0:
            current_path = stack.pop()
            current_node = current_path[-1]
            current_moves = direction_list.pop()
            if current_node == destination_vertex:
                for i in range(len(current_moves)):
                    final_list.append([current_moves[i], str(current_path[i + 1])])
                return final_list
            elif not current_node in visited:
                visited.add(current_node)
                neighbors = self.get_neighbors(current_node)
                for node in self.get_neighbors(current_node):
                    direction_dup = list(current_moves)
                    direction_dup.append(node)
                    direction_list.append(direction_dup)
                    path_dup = list(current_path)
                    path_dup.append(neighbors[node])
                    stack.push(path_dup)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path= None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        edges = self.get_neighbors(starting_vertex)
        if path == None:
            path = []
        path = path + [starting_vertex]
        print(path)
      
        if starting_vertex == destination_vertex:
            return path
        if not starting_vertex in visited:
            visited.add(starting_vertex)
            for vertex in edges:
                final_path = self.dfs_recursive(vertex, destination_vertex, visited, path)
                if final_path:
                    return final_path

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
    #graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    #graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    #print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    #print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
