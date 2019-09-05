from nltk import Tree
from rules.base_rule import BaseRule


class XPOverXP(BaseRule):
    """
    Removes XP over XP phrases.
    """

    def is_x_over_x(self, node):
        return (node.label() == "NP" and node[0].label() == "NP") or \
               (node.label() == "VP" and node[0].label() == "VP") or \
               (node.label() == "S" and node[0].label() == "S")

    def transform(self, node, new_tree):
        if isinstance(node, Tree):
            new_node = None

            if self.is_x_over_x(node):
                node = Tree(node.label, [node[0]])

            new_children = []
            for child in node:
                new_child = self.transform(child, new_tree)
                new_children.append(new_child)
                new_node = Tree(node.label(), new_children)

            return new_node

        return node