# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():
    print("Hi, user.\nThank u for using Fahrettin's app :3")

def EncriptorDecript():
    print("what would you want from that code?")
    print("would you wanna encript or decript?")
    print("or did you just miss click it? type 'OUT' for leaving this code")
    while 1:
        value = input("Type 1 for encript, 2 for decript (encript şifreleme, decript şifrelemeyi açma): ")
        if value == "1":
            with open('encripting.py', 'r', encoding='utf-8') as f:
                exec(f.read())
                return

        elif value == "2":
            with open('decripting.py', 'r', encoding='utf-8') as f:
                exec(f.read())
                return
        elif value == "OUT" or value =="out":
            print("have a good days")
            return
        else:
            print("You wrote something wrong, try it again.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()
    EncriptorDecript()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
