from tkinter import Place


favorite_places =  {
    'eduardo':['canadá','santa catarina','rio grande do sul'],
    'paulo':['florianopólis','estados unidos','inglaterra'],
    'ana':['fortaleza','dubai','espanha']    
}
for name,place in favorite_places.items():
    print("Os lugares favoritos de " + name.title() + " são:")
    for item in place:
        print("\t" + item.title())
    