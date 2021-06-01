import re  # Regular Expression
with open ('D:\Knowledge\Programming Language\Exercise\Tw_text.txt', 'r+') as f:
    # Read lines of file through iteration
    def word():
        for line in f:
            print(line, end = "")

    # word()

    # Read lines of file through read method
    def read_file():
        read = f.read()
        print(read)

    # read_file()

    # Splitting words of all three lines
    def find():
        for line in f:
            print(line.split())

    # find()