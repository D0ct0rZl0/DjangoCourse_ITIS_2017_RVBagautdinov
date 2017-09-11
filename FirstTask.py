def sorter(filename):

    with open(filename, 'r') as file:
        words = list(filter(None, file.read().replace("\n", " ").lower().split(" ")))
        out = []
        for word in words:
            if word not in out:
                out.append(word)

        for word in out:
            print(word)

sorter('words.txt')
