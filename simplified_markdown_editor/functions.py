"""simplified_markdown_editor"""
def make_text_plain():

    """
    asks user for text and return it
    Returns: str: bold text
    """
    users_text = input("enter your text: >")
    return users_text + ' '


def make_text_bold():

    """
    asks user for text and transforms it to bold text
    Returns: str: bold text
    """
    users_text = input("Text: > ")
    return f"**{users_text}** "


def make_text_italic():
    """
    asks user for text and transforms it to italic text
    Returns: str: italic text
    """
    users_text = input("Text: > ")
    return f"*{users_text}* "


def make_inline_code():

    """
    asks user for text and transforms it to inline code text
    Returns: str: inline code
    """
    users_text = input("Text: > ")
    return f"`{users_text}` "


def get_level():

    """
    Gets the header level from the user
    Returns: int: level from 1 to 6
    """
    possible_values = [i for i in range(1, 7)]

    while True:
        try:
            user_choice = int(input("Level: > "))
            if user_choice in possible_values:
                return user_choice
            print("The level should be within the range of 1 to 6")

        except ValueError:
            print("The value must be numeric")


def make_text_header():

    """Gets the level and some text from the user and transforms it to header text
    Returns: str: header text
    """
    level = get_level()
    users_text = input("Text: > ")
    return f"{'#' * level} {users_text} "
    # return f"<h{level}>{users_text}</h{level}>"


def add_new_line():

    """
    Creates new line
    Returns: str: new line symbol
    """
    return "\n"


def add_link():

    """
    Gets label and URL from the user and transforms it to link with label
    Returns: str: link with label
    """
    label = input("Label: > ")
    url = input("URL: > ")
    return f"[{label}]({url}) "


def get_rows_count():

    """
    Get the number of rows for a list
    Returns: int: number of rows
    """
    while True:
        try:
            rows_count = int(input("Number of rows: > "))
            if rows_count > 0:
                return rows_count
            print("The number of rows should be greater than zero")

        except ValueError:
            print("The value must be numeric")


def add_list(is_ordered=False):

    """
    Gets number of rows and some text from the user and transforms it to ordered or unordered list
    Args: is_ordered (boolean): True for ordered list, False for unordered list
    Returns: str: ordered/unordered list
    """
    result = ""
    rows_count = get_rows_count()

    for i in range(rows_count):
        element = input(f"Row #{i+1}: > ")
        result += f"{i+1}. {element} \n" if is_ordered else f"* {element} \n"
    return result
