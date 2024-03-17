"""simplified_markdown_editor"""
import functions as f


available_formatters = ["plain", "bold", "italic", "inline-code", "link",
                        "header", "unordered-list", "ordered-list", "new-line"]
users_text = ""
while True:
    user_inp = input("Choose a formatter: >")
    if user_inp == "!help":
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
        print("Special commands: !help !done")
    elif user_inp == "plain":
        users_text += f.make_text_plain()

    elif user_inp == "bold":
        users_text += f.make_text_bold()

    elif user_inp == "italic":
        users_text += f.make_text_bold()

    elif user_inp == "inline-code":
        users_text += f.make_inline_code()

    elif user_inp == "link":
        users_text += f.add_link()

    elif user_inp == "header":
        users_text += f.make_text_header()

    elif user_inp == "unordered-list":
        users_text += f.add_list()

    elif user_inp == "ordered-list":
        users_text += f.add_list(1)

    elif user_inp == "new-line":
        users_text += f.add_new_line()

    elif user_inp == "!done":
        with open("output.md", "w", encoding="utf-8") as result_file:
            result_file.write(users_text)
        break
    else:
        print("Unknown formatting type or command")
    print(users_text)



