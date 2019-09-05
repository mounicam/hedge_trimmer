from nltk.parse import CoreNLPParser
from rules.time_expressions import TimeExpressions


def one_test(rule, parser, input, exp_output=None):
    if exp_output is None:
        exp_output = input

    input = list(parser.raw_parse(input))[0]

    terminals = rule.transform(input, None).leaves()
    output = " ".join(terminals).strip()
    print(output)
    assert output == exp_output


def run():
    rule = TimeExpressions()
    parser = CoreNLPParser(url='http://localhost:9000')

    input = "They will play against a team of North Koreans on Wednesday , which is believed to be Kim 's birthday ."
    exp_output = "They will play against a team of North Koreans ."
    one_test(rule, parser, input, exp_output)

    input = "The pitch was effective ."
    one_test(rule, parser, input)

    input = "Patti Davis , a former first daughter , wrote a public letter to Malia and Sasha on Sunday ."
    exp_output = "Patti Davis , a former first daughter , wrote a public letter to Malia and Sasha ."
    one_test(rule, parser, input, exp_output)
