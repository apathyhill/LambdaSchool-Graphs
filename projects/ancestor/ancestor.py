def earliest_ancestor(ancestors, starting_node):
    q = [] # Make a Queue
    q.append((starting_node, 0)) # Enqueue starting node with distance of 0
    distances = {} # Keep track of all node's distances from starting node
    while len(q) > 0:
        node = q.pop(0) # Get current node
        node_index = node[0]
        node_dist = node[1]
        found_parent = False # Check if any parents found
        for i in ancestors: # Loop through all other elements (there's probably a faster way to this)
            if i[1] == node_index: # If it is a parent of the current node
                q.append((i[0], node_dist+1)) # Enqueue parent node with current distance + 1
                found_parent = True
        if not found_parent: # If this node has no parents
            if node_index == starting_node: # If it is the starting node, return -1
                return -1
            distances[node_index] = node_dist # Otherwise, set distance of node from starting node
    return max(distances.items(), key=lambda x: (x[1], -x[0]))[0] # Return index with most distance, and also least index value