from entity.analyzer import Analyzer

from res.re.re_tokenizer import RETokenizer
from res.re.re_syntax import RE_SYNTAX


def main():
    i = input("?")
    tokenizer = RETokenizer(doc=i)
    analyzer = Analyzer(syntax=RE_SYNTAX,
                        tokenizer=tokenizer,
                        debug=True)
    print(analyzer.get_syntax_tree_str())
    print()
    print(analyzer.syntax.rules_info())
    print()
    print(analyzer.analyze_log)


if __name__ == '__main__':
    main()
