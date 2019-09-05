from rules.xp_over_xp import XPOverXP
from nltk.parse import CoreNLPParser


def one_test(rule, parser, input, exp_output=None):
    if exp_output is None:
        exp_output = input

    input = list(parser.raw_parse(input))[0]

    terminals = rule.transform(input, None).leaves()
    output = " ".join(terminals).strip()
    print(output)
    assert output == exp_output


def run():
    rule = XPOverXP()
    parser = CoreNLPParser(url='http://localhost:9000')

    input = "De Blasio , a white man married to a black woman , also received a boost from a campaign ad featuring " \
            "their son ."
    exp_output = "De Blasio also received a boost from a campaign ad featuring their son ."
    one_test(rule, parser, input, exp_output)

    input = "Heavy trucks also ruin bridges more quickly and crumble prairie roads built for light farm traffic ."
    exp_output = "Heavy trucks also ruin bridges more quickly ."
    one_test(rule, parser, input, exp_output)

    input = "The pitch was effective ."
    one_test(rule, parser,  input)

    input = "Children were accosting adults , smoking marijuana , making sexual noises in class , the complaint said ."
    exp_output = "Children were accosting adults making sexual noises in class"
    one_test(rule, parser, input, exp_output)

    input = "A fire killed a firefighter who was fatally injured as he searched the house ."
    exp_output = "A fire killed a firefighter ."
    one_test(rule, parser, input, exp_output)
