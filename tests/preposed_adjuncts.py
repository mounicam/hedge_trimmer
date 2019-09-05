from nltk.parse import CoreNLPParser
from rules.preposed_adjuncts import PreposedAdjuncts


def one_test(rule, parser, input, exp_output=None):
    if exp_output is None:
        exp_output = input

    input = list(parser.raw_parse(input))[0]

    terminals = rule.transform(input, None).leaves()
    output = " ".join(terminals).strip()
    print(output)
    assert output == exp_output


def run():
    rule = PreposedAdjuncts()
    parser = CoreNLPParser(url='http://localhost:9000')

    input = "The pitch was effective ."
    one_test(rule, parser, input)

    input = "According to a now finalized blueprint described by U.S. officials and other sources, " \
           "the Bush administration plans to take complete, unilateral control of a post-Saddam Hussein Iraq."
    exp_output = "the Bush administration plans to take complete , unilateral control of a post-Saddam Hussein Iraq ."
    one_test(rule, parser, input, exp_output)

    input = "While never forgetting her Chinese roots , Yee has grown to love America over the years ."
    exp_output = "Yee has grown to love America over the years ."
    one_test(rule, parser, input, exp_output)
