stores = [
    {
        'name':'My wonderful store',
        'items': [
            {
                'name':'my item',
                'prices': 15.99
            }
        ]
    }
]

for bt in stores:
    print(bt['items'][0]['name'])

#estudiantes = [{'nombre': 'Memo Llano'}]
#nombre = 'akjnskdjhfksdf'
#el_nombre = {'nombre': nombre, 'edad': 23}
#estudiantes.append(el_nombre)
#print(estudiantes)
#estudiante = next(filter(lambda x: x['nombre'], estudiantes), None)
#print('estudiante', estudiante)

estudiantes = [{
    'nombre': 'Pedro Perez',
    'edad': 18
    #'materias': []
}]

mate = {
       'titulo':'matematicas'
        }
estudiantes[0]['materias'] = mate
print(estudiantes[0]['materias'])
print(estudiantes)
