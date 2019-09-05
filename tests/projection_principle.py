from nltk.parse import CoreNLPParser
from rules.projection_principle import ProjectionPrinciple


def one_test(rule, parser, input, exp_output=None):
    if exp_output is None:
        exp_output = input

    input = list(parser.raw_parse(input))[0]
    print(input)

    out_tree = rule.transform(input, None)
    out_tree = input if out_tree is None else out_tree
    terminals = out_tree.leaves()
    output = " ".join(terminals).strip()
    print(output)
    assert output == exp_output


def run():
    rule = ProjectionPrinciple()
    parser = CoreNLPParser(url='http://localhost:9000')

    input = "The study is centered on 159 students at Dartmouth College in Hanover ,  this is truth."
    exp_output = "The study is centered on 159 students at Dartmouth College in Hanover"
    one_test(rule, parser, input, exp_output)

    input = "The pitch was effective ."
    one_test(rule, parser, input)

    input = "Pebble Partnership CEO John Shively said afterward that he told McCarthy the company has good intentions ."
    one_test(rule, parser, input)

    input = "In addition to her Ph.D. work on the intersection in digital spaces of copyright law and technology , " \
            "Fiesler said she has a law degree from Vanderbilt ."
    one_test(rule, parser, input)

    input = "Among the readers on hand was Mohammed Baghdadi , 32 , a manager at the Ministry of Trade ."
    one_test(rule, parser, input)
