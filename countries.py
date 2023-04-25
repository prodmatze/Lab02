
def sortc():

    with open("europeancountrys.txt", "r") as file:

        contents = file.read()
        words = contents.split()
        # we noticed that countries consisting of more than one word get split as well.
        # So we removed them
        sorted_words = sorted(words)

    for word in sorted_words:
        print(word)

sortc()