import re  # Regular Expression
with open ('D:\Knowledge\Programming Language\Exercise\Tw_text.txt', 'a+') as f:
    # Read lines of file through iteration
    def word():
        for line in f:
            print(line, end = "")

    # word()

    # Read lines of file through read method
    def read_file():
        text = f.read()
        print(text)

    # read_file()

    # Splitting words of all three lines
    def split_it():
        for line in f:
            print(line.split())

    # split_it()

    # Adding something in the file
    def adding():
        about = "My name is Nishant Nayan."
        f.write(about)
    
    adding()