def main():
    s = input()
    if is_valid(s):
        return True
    else:
        return False


def is_valid(s):
    # Verify that the input has no punct and is correct length
    if s.isalnum() and 2 <= len(s) <= 6:
        # Verify that it starts with at least two letters
        if s[0].isalpha() and s[1].isalpha():
            # Verify that there are no letters after a number
            if s.isalpha():
                return True
            elif s.isalnum():
                # Verify that 0 is not the first number
                zero_test = s.split("0")
                if zero_test[0].isalpha():
                    return False
                else:
                    # Verify that there are no letters following a number
                    i = None
                    for n in s:
                        if n.isnumeric():
                            i = n
                            break
                    s_list = list(s.split(i, maxsplit=1))
                    if s_list[1].isnumeric():
                        return True
                    else:
                        return False
            else:
                return False
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
