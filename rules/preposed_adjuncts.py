from nltk import Tree
from rules.base_rule import BaseRule


class PreposedAdjuncts(BaseRule):
    """
    Removes preposed adjuncts
    """

    def is_s_with_np_vp(self, node):
        is_s = isinstance(node, Tree) and node.label() == "S"
        return is_s and any([child.label() == "NP" for child in node]) and \
               any([child.label() == "VP" for child in node])

    def transform(self, node, new_tree):
        if isinstance(node, Tree):
            new_node = None

            if self.is_s_with_np_vp(node):
                children = []
                first_NP = False

                for child in node:
                    if child.label() == "NP" and not first_NP:
                        first_NP = True

                    if first_NP:
                        children.append(child)

                node = Tree(node.label, children)

            new_children = []
            for child in node:
                new_child = self.transform(child, new_tree)
                new_children.append(new_child)
                new_node = Tree(node.label(), new_children)

            return new_node

        return node
