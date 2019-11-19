import sys


def show_output(choice):
    if choice == "hello":
        print("Hello to you too!")
    elif choice == "goodbye":
        print("I wish you goodbye!")
    else:
        print("I don't know what to make of that")


if __name__ == "__main__":
    show_output(sys.argv[1])
