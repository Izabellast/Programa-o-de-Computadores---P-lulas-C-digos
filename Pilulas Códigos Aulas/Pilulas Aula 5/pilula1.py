def validarSenha(s):
    if len(s) < 8:
        return 'Senha inválida, muito curta.'
    
    temNumero = False
    temMaiuscula = False
    Simbolos = '!@#$%*'
    temSimbolo = False
    
    for c  in s:
        if c == ' ':
            return 'Senha inválida, não pode ter espaços' 
        if c >= '0' and c<= '9':
            temNumero = True
        if c >= 'A' and c <='Z':
            temMaiuscula = True
        if c in Simbolos:
            temSimbolo = True
            
    
    if not temNumero:
        return 'Senha inválida, precisa de um num. pelo menos'
    if not temMaiuscula:
        return 'Senha inválida, precisa de uma letra maiuscula'
    if not temSimbolo:
        return 'Senha inválida, precisa de um simbolo'
    return 'Senha valida'
            
#main
senha= input ('Digite sua senha:')
r = validarSenha(senha)
print(r)