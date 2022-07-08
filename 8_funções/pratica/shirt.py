def make_shirt(height='grande',text='eu amo python'):
    print("\nA sua camiseta é " + height.title() + ".")
    print("O texto que irá ficar estampado na camiseta é >>>" 
    + text.title() + "<<<.")
make_shirt()
make_shirt('media')
make_shirt(height='pequena',text='codder')