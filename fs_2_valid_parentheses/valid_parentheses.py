def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    str_to_list = list(parens)
    # If we have an odd number of parens we can exit immediately
    if len(str_to_list) % 2 != 0:
        return False

    tested_indices = []
    for i, char in enumerate(str_to_list):
        # We check the opening parentheses
        if char == '(':
            try:
                # If it is closed right away, it's valid
                if str_to_list[i + 1] == ')':
                    tested_indices.append((i, i + 1))
                    continue
                elif str_to_list[-1] == ')':
                    # If it is closed at the end of the list, it's valid
                    tested_indices.append((i, len(str_to_list) - 1))
                    continue
                else:
                    # If we didn't find a closing parens, it's invalid
                    return False
            except IndexError:
                pass
        else:
            # We check the closing parentheses
            processed = False
            # Did we process it already when we were going through the opening parens?
            for idx in tested_indices:
                if i not in idx:
                    # Didn't find it yet, keep looking
                    continue
                else:
                    # Found it, so it's valid
                    processed = True

            # If we went through all the processed parens and did not find it it's a floating closing parens
            # it's invalid
            if processed is False:
                return False

    # We processed the list without issues, it's valid
    return True
