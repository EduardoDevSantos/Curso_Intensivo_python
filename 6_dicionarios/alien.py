alien_0 = {'color':'green','points':5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}
print(alien_0)
alien_0['color'] = 'green'
alien_0['points'] = '5'
print(alien_0)

alien_0 = {'color':'green'}
print("\nThe alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print("\nOriginal x-position: " + str(alien_0['x_position']))
# move o alienígena para a direita
# determina a distância que o alienígena deve se deslocar de acordo com sua velocidade atual
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Este deve ser um alienigena rápido
    x_increment = 3
# A nova posição é a posição antiga somada ao incremento
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: "+str(alien_0['x_position'])) 

alien_0 = {'color':'green','points':5}
print(alien_0)
del alien_0['points']
print(alien_0)