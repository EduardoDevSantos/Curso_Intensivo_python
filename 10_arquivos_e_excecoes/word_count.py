from itertools import count


def count_words(filename):
    """Conta o número aproximado de palavras em um arquivo."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) 
        + " words.")
filenames = ['alice.txt','little_women.txt','moby_dick.txt','siddhartha.txt']
for filename in filenames:
    count_words(filename)

