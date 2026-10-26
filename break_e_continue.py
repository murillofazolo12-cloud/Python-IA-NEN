while True :
    cmd = input('Comando:').strip().lower()
    if cmd == 'sair':
        break                   # encerra o laço 
    if cmd == '' : 
        continue                # volta ao inicio 
    print(f'Executando {cmd}')
