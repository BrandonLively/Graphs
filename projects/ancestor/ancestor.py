def earliest_ancestor(ancestors, starting_node):
    children = [starting_node]
    result = -1
    while True:
        children = get_parents(ancestors, children)
        if len(get_parents(ancestors, children)) == 0:
            if len(children) > 0:
                result = children[0]
            return result



def get_parents(ancestors, children):
    parents = []
    for child in children:
        for parent in ancestors:
            if parent[1] == child:
                parents.append(parent[0])
    return parents
