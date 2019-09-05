The project implements a set of deletion rules to simplify a sentence. The rules are taken from the paper - "Hedge Trimmer: A Parse-and-Trim Approach to Headline Generation"

To run the code, use the following format:
python main.py --complex <input file with complex sentences> --simple <out file with simplified sentences>

Please make sure you run the Stanford CoreNLP server on the port 9000, before you run the script. This is needed extract the constituency parse of the sentence.
