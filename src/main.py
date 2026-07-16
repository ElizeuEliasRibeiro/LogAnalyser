import os
cont = 0
quantidade_totalBF = 0
path = os.path.join("Logs", "auth.log")

with open(path, "r", encoding="utf-8", errors="ignore") as arquivo:
    tentativas = {}
    linhas = arquivo.readlines()

print('')
print('Lendo o arquivo')
print("="*30)
print('')

for linha in linhas:    
    palavra = linha.split()

    '''if (palavra[5] + " " + palavra[6]  == "Failed password"):
        print("Tentativa de senha falhou")
        print("Usuário: " + palavra[8] + "\nIP da máquina: " + palavra[10])
        print("================================")
        cont += 1'''

    if "Failed" in palavra and "password" in palavra:
        print("Tentativa de senha falhou")
        cont +=1
        for_index = palavra.index("for")

        if (palavra[for_index + 1]) == "invalid":
            user = palavra[for_index + 3]
            print(f"Usuário: {user}")
            print("="*20)
            print('')
        
        else:
            user = palavra[for_index + 1]
            print(f"Usuário: {user}")
            print("="*20)
            print('')

        from_index = palavra.index("from")
        ip = palavra[from_index + 1]
        
        if ip in tentativas:
            tentativas[ip] += 1
        else:
            tentativas[ip] = 1 

for ip, quantidade in tentativas.items():
    if quantidade >= 5:
        print('')
        print("="*20)

        print("ALERTA DE BRUTE FORCE")
        print("IP:", ip)
        print("Tentativas:", quantidade)
        print(f"Status: Suspeito")
        print("="*20)
        print('')
        quantidade_totalBF += 1
    else:
        print("IP:", ip)
        print("Tentativas:", quantidade)
        print(f"Status: Normal")


with open("relátorio.txt", "w", encoding="utf-8") as relatorio:

    relatorio.write('')
    relatorio.write('='*30 + "\n\n")
    relatorio.write('Relatório das análises de LOG'+ "\n\n")
    relatorio.write('')
    relatorio.write(f"total de tentativas falhas: {cont}\n")
    relatorio.write(f"Quantidade de IPs analisados: {len(tentativas)}\n")
    relatorio.write(f"Possíveis ataques de força bruta: {quantidade_totalBF}\n")
    relatorio.write('')
    relatorio.write('='*30)
    relatorio.write("=" * 30 + "\n\n")

print("Relatório gerado com sucesso!")
