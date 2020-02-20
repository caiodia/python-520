usuarios = [
    {
        'id': 1,
        'email': 'teste@gmail.com',
        'pagou_conta': False
    },
    {
        'id': 2,
        'email': 'teste@gmail.com',
        'pagou_conta': True
    },
    {
        'id': 3,
        'email': 'brualfa@gmail.com',
        'pagou_conta': False
    }   
]

def filtro(usuario):
    if usuario['pagou_conta']:
        return False
    return True
    
def filtar_usuarios(lista):
    return list(filter(filtro, lista))

lista = filtar_usuarios(usuarios)
print(lista)