
from entity.syntax import Syntax
from res.re.re_syntax_rules import RE_SYNTAX_RULES
from res.re.re_follow import RE_FOLLOW

RE_SYNTAX = Syntax(rules=RE_SYNTAX_RULES, follow_set_load=RE_FOLLOW)
