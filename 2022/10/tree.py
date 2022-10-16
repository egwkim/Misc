"""
Tree data type with Python
"""


class Node:
    def __init__(self, data=None) -> None:
        self.parent: Node = None
        self.data = data
        self.children:list[Node] = []

    def __str__(self) -> str:
        s = ''
        s += '*' + str(self.data) + '\n'
        for child in self.children:
            s += '\t' + child.__str__().replace('\n', '\n\t')[:-1]
        return s

    def append(self, *nodes) -> None:
        """
        Append children to a node.

        Args:
            nodes (Node): Child nodes

        Raises TypeError if node is not an instance of Node.
        """
        for node in nodes:
            if not isinstance(node, Node):
                raise TypeError
            if node in self.children:
                return

            self.children.append(node)
            node.parent = self

    def remove(self) -> None:
        """
        Remove a node and its children recursively.
        """
        for node in self.children:
            node.remove()
        self.parent.children.remove(self)
        del self


class Tree:
    def __init__(self, root: Node = None) -> None:
        if root:
            self.set_root(root)

    def __str__(self) -> str:
        return root.__str__()

    def set_root(self, root: Node) -> None:
        if not isinstance(root, Node):
            raise TypeError
        if root.parent != None:
            raise ValueError("Root node cannot have parent.")
        self.root = root


if __name__ == '__main__':
    root = Node('root')
    tree = Tree(root)
    root.append(Node('1'))
    root.children[0].append(Node('2'))
    root.children[0].append(Node('3'))
    root.children[0].append(Node('4'))
    root.append(Node('5'))
    root.children[1].append(Node('6'))
    print(tree)
