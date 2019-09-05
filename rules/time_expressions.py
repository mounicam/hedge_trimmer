from nltk import Tree
from rules.base_rule import BaseRule


class TimeExpressions(BaseRule):
    """
    Removes time expression in parse tree.
    """

    time_expressions = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'january',
                        'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
                        'november', 'december', 'year', 'day', 'week', 'month', 'today', 'yesterday', 'tomorrow',
                        'tonight', 'tonite', 'before', 'after', 'earlier', 'later', 'ago', 'afternoon', 'evening',
                        'morning'}

    def is_pp_with_time_expression(self, node):
        if node.label() == "PP":
            terminals = set([t.lower() for t in node.leaves()])
            return len(terminals.intersection(self.time_expressions)) > 0
        return False

    def is_np_with_time_expression(self, node):
        if node.label() == "NP" and len(node) == 1 and not isinstance(node[0], Tree):
            terminals = set([leaf.lower() for leaf in node.leaves()])
            return len(terminals.intersection(self.time_expressions)) > 0
        return False

    def transform(self, node, new_tree):
        if isinstance(node, Tree):
            new_node = None

            if not self.is_np_with_time_expression(node) and not self.is_pp_with_time_expression(node):
                new_children = []
                for child in node:
                    new_child = self.transform(child, new_tree)
                    if new_child is not None:
                        new_children.append(new_child)
                new_node = Tree(node.label(), new_children)

            return new_node

        return node
