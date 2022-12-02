def try_iter(code_string, byline=True, except_case="pass"):

    old_string = code_string
    new_string = ''

    if byline:

        on = 'try'
        first = True
        nexttry = False

        for c in old_string:
            if c != '\n' and not first and not nexttry:
                new_string += c
            else:
                if on == 'try':
                    if first:
                        string_value = 'try:\n\t' + c
                    else:
                        string_value = '\ntry:\n\t' + c
                    new_string += string_value
                    on = 'except'
                    nexttry = False
                else:
                    new_string += '\nexcept:\n\t' + except_case
                    on = 'try'
                    nexttry = True

                first = False

        new_string += '\nexcept:\n\t' + except_case

    else:
        tabbed = False
        for c in old_string:
            if c != '%' and c != '^':
                new_string += c
                if tabbed and c == '\n':
                    new_string += '\t'
            elif c == '%':
                new_string += 'try:\n\t'
                tabbed = True
            elif c == '^':
                new_string += '\nexcept:\n\t' + except_case
                tabbed = False
    return new_string