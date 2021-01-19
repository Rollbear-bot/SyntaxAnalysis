letter = [chr(i) for i in list(range(ord("A"), ord("Z") + 1))
          + list(range(ord("a"), ord("z") + 1))]
digit = [chr(i) for i in range(ord("0"), ord("9") + 1)]

RE_FOLLOW = {
    "re": {"EOF"},
    "stmt": {"EOF"},
    "branch_stmt": {"EOF", "(", *letter, *digit},
    "seq_stmt": {"EOF", "(", "|", *letter, *digit},
    "repeat_stmt": {"EOF", "(", "|", *letter, *digit},
    "prime_stmt": {"EOF", "(", "|", "*", *letter, *digit},
    "simple_char": {"EOF", "(", "|", "*", *letter, *digit},
    "| seq_stmt": {"EOF", "(", "|", *letter, *digit}
}
