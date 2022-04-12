alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

alien_0 = {'color':'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color']+ ".")

alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print("Original x-position: "+str(alien_0['x_position']))

# Move o alienigena para a direita
# Determine a distância que o alienigina deve se deslocar de acordo com sua velocidade atual
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] ==  'medium':
    x_increment = 2
else:
    # Este deve ser um alienigena rapido
    x_increment = 3

# A nova posição é a posição antiga somada ao incremento
alien_0['x_position']+=x_increment

print("New x-position: "+str(alien_0['x_position']))

alien_0 = {'color':'green','points':5}
del alien_0['points']
print(alien_0)