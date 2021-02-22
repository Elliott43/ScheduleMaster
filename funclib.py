def get_int(message="> ", limit=False):
    try:
        x = int(input(message))
        if limit:
            if x not in limit:
                print(f"Provided integer was not between: {limit[0]-1}, {limit[-1]}")
                raise ValueError

    except ValueError:
        print("Pleases provide a valid integer.")
        return get_int(message, limit)

    return x


def query(message="", questions=[], newline=True, get_num=False):
    # get_num can be a range or a bool
    assert not (questions and get_num)

    if message:
        print(message)

    if newline:
        print()

    if questions:
        for i,j in enumerate(questions):
            print(f"\t{i}) {j}")

        return questions[get_int(limit=range(len(questions)))]

    elif get_num:
        if isinstance(get_num, range):
            return get_int(limit=get_num)

        else:
            return get_int()

    else:
        return input("> ")



