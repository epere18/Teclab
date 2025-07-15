#Listas

estudiantes = ['Oscar', 'Juan', 'Pedro', 'Ana', 'Maria']
print(estudiantes)

# Agregar un estudiante al final de la lista
estudiantes.append('Andres')
print(estudiantes)

#Tuplas
video_juegos = ('Mario', 'Zelda', 'Metroid', 'Pokemon')
print(video_juegos)

# Largo de la tupla
largo_tupla = len(video_juegos)
print(f'La lista tiene un largo de {largo_tupla} elementos.')


#Acceso a elementos de la tupla
acceso_elemento = video_juegos[2]
print(f'El tercer elemento de la tupla es: {acceso_elemento}')

#Indexación de la tupla
indexacion1_tupla = video_juegos[-1]
indexacion2_tupla = video_juegos[-2]
print(f'El último elemento de la tupla es: {indexacion1_tupla}')
print(f'El penultimo elemento de la tupla es: {indexacion2_tupla}')

#Rangos
rango_tupla = video_juegos[2:4]
print(f'Los elementos del rango son: {rango_tupla}')

#Cambiar un elemento de la tupla
# Las tuplas son inmutables, por lo que no se pueden cambiar sus elementos directamente
# Sin embargo, se puede convertir a lista, modificar y volver a convertir a tupla
video_juegos_lista = list(video_juegos)
video_juegos_lista[1] = 'Donkey Kong'
video_juegos = tuple(video_juegos_lista)
print(f'La tupla modificada es: {video_juegos}')

#Agregar un elemento a la tupla
# Las tuplas son inmutables, por lo que no se pueden agregar elementos directamente
# Sin embargo, se puede convertir a lista, agregar y volver a convertir a tupla
video_juegos_lista = list(video_juegos)
video_juegos_lista.append('Kirby')
video_juegos = tuple(video_juegos_lista)
print(f'La tupla modificada con un nuevo elemento es: {video_juegos}')

