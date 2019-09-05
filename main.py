# -*- coding: utf-8 -*-

import argparse
from nltk.parse import CoreNLPParser

from rules.xp_over_xp import XPOverXP
from rules.time_expressions import TimeExpressions
from rules.preposed_adjuncts import PreposedAdjuncts
from rules.projection_principle import ProjectionPrinciple

THRESHOLD = 0

# TODO: Iterative shortening
# TODO: Tune the threshold
# TODO: PPs and SBARs shortening


def simplify(text, parser, rules):
    tree = list(parser.raw_parse(text))[0]
    threshold = THRESHOLD

    # TODO: Reformat the rule pipeline
    for rule in [rules[0], rules[1]]:
        new_tree = rule.transform(tree, None)
        if new_tree is None:
            new_tree = tree

        text = " ".join(new_tree.leaves())
        tree = new_tree

    for rule in [rules[2], rules[3]]:
        new_tree = rule.transform(tree, None)
        if new_tree is None or len(new_tree.leaves()) < threshold:
            new_tree = tree

        text = " ".join(new_tree.leaves())
        tree = new_tree

    return text


def main(args):

    parser = CoreNLPParser(url='http://localhost:9000')
    rules_pipeline = [ProjectionPrinciple(), TimeExpressions(), XPOverXP(), PreposedAdjuncts()]
    
    fp = open(args.simple, "w")

    for i, line in enumerate(open(args.complex)):
        print(line.strip())
        simplified_text = simplify(line.strip(), parser, rules_pipeline)
        print(i, simplified_text)
        fp.write(simplified_text + "\n")

    fp.close()

    """    
    input = "According to a now finalized blueprint described by U.S. officials and other sources, " \
            "the Bush administration plans to take complete, unilateral control of a post-Saddam Hussein Iraq."
    print(simplify(input, parser, rules_pipeline))

    input = "Gaunt , with a patchy beard and a wooden cross hanging from his neck , Medina says he hopes that his fast " \
            "will pressure House Republicans , who have held up action on an immigration overhaul ."
    print(simplify(input, parser, rules_pipeline))
    """


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--simple')
    parser.add_argument('--complex')
    args = parser.parse_args()
    main(args)
