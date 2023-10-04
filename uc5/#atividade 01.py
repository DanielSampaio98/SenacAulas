#atividade 01
contatos = {
    'samuel': {'telefone': '987-654-3210', 'email': 'samuel@email.com'},
    'eloiza': {'telefone': '123-456-7890', 'email': 'eloiza@email.com'}
}

# 01. Acessar as informações de contato de uma pessoa específica a partir do dicionário "contatos".

contato_usuario = 'eloiza'
if contato_usuario in contatos:
    contato_eloiza = contatos[contato_usuario]
    telefone_eloiza = contato_eloiza['telefone']
    email_eloiza = contato_eloiza['email']
    print(f"Telefone de {contato_usuario}: {telefone_eloiza}")
    print(f"Email de {contato_usuario}: {email_eloiza}")


#passo 2

#anexando um conatato
contatos["thiago"]={'telefone': '123-654-3210', 'email': 'thiago@email.com'}
print(contatos['thiago'])

#passo 3

#nova modificação email

novoemail_samuel = 'samuel20@email.com'
contatos['samuel']['email'] = novoemail_samuel
print(contatos)


#passo 4 eliminar um contato, da tabela contato

if 'Samuel' in contatos:
    del contatos['Samuel']
    print(f"Contato de Samuel foi removido.")
