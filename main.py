import re


def valid_parentheses(string):
    pattern = re.compile(r"^[()]{2,}$")
    temp_lst = []
    if re.search(pattern, string):
        for char in string:
            if (char == '('):
                temp_lst.append(char)
            else:
                if (len(temp_lst)):
                    temp_lst.pop()
                else:
                    return False
        return True
    else:
        return False
