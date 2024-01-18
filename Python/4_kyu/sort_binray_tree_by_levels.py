from collections import deque as dq

def tree_by_levels(node):
    if not node:
        return []

    queue = dq([node])
    result = []

    while queue:
        current = queue.popleft()
        result.append(current.value)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return result
