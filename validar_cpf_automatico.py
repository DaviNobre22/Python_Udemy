import random
for _ in range(100):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0,9))

    contador_regressivo = 10
    soma_cpf = 0
    for digito in nove_digitos:
        soma_cpf += int(digito) * contador_regressivo
        contador_regressivo -= 1
    def validar_primeiro_digito(a):
        etapa = (a * 10) % 11
        return etapa if etapa <= 9 else 0
    primeiro_digito = validar_primeiro_digito(soma_cpf)

    descobrir_segundo_digito = nove_digitos + str(primeiro_digito)
    contagem_segundo_digito = 11
    soma_segundo_digito = 0
    for digito in descobrir_segundo_digito:
        soma_segundo_digito += int(digito) * contagem_segundo_digito
        contagem_segundo_digito -= 1
    def validar_segundo_digito(a):
        etapa = (a * 10) % 11
        return etapa if etapa <= 9 else 0
    segundo_digito = validar_segundo_digito(soma_segundo_digito)
    cpf_usuario = f"{nove_digitos}{primeiro_digito}{segundo_digito}"

    print(cpf_usuario)



