from nltk import Tree
from rules.base_rule import BaseRule


class ProjectionPrinciple(BaseRule):
    """
    Gets the lowest leftmost S in the parse tree
    """

    def is_s_with_np_vp(self, node):
        is_s = isinstance(node, Tree) and node.label() == "S"
        return is_s and any([child.label() == "NP" for child in node]) and \
               any([child.label() == "VP" for child in node])

    def transform(self, node, new_tree):

        if isinstance(node, Tree):

            for child in node:
                new_tree = self.transform(child, new_tree)

                if self.is_s_with_np_vp(node) and new_tree is None:
                    new_tree = node

        return new_tree

