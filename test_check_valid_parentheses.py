from check_valid_pranteces import check_valid_parentheses



def test_valid_parentheses():
    exp = "{{{{{[[[[(((())))]]]]}}}}}"
    output = check_valid_parentheses(exp)
    assert output == True


def test_invalid_parentheses():
    exp = "[[{{{{{[[[[(((())))]]]]}}}}}"
    output = check_valid_parentheses(exp)
    assert output == False