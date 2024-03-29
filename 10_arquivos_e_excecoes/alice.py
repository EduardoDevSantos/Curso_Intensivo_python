filename = 'alice.txt'
directory = '10_arquivos_e_excecoes/'
try:
    with open(directory+filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = 'Sorry, the file ' + filename + " does not exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")