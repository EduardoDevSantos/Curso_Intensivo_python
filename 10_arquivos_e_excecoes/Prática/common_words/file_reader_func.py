class FileReader():
    """Ler um arquivo e conta palavras especificas em um arquivo de texto."""
    def __init__(self,*filenames):
        """Ler arquivos de textos"""
        for filename in filenames:
            try:
                with open(filename, encoding='utf8') as f_obj:
                    self.text = f_obj.read()
                    print(self.text)
            except FileNotFoundError:
                pass
    def count_word(self,word):
        words = self.text.lower().count(word.lower())
        print(words)
