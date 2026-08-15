import csv

def gerar_csv(tipo, quartos, garagem, filhos, aluguel, contrato, parcelas):
    with open("orcamento.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow(["ORCAMENTO IMOBILIARIA"])
        escritor.writerow([])

        escritor.writerow(["Tipo de imovel", tipo])
        escritor.writerow(["Quantidade de quartos", quartos])
        escritor.writerow(["Garagem", garagem])
        escritor.writerow(["Possui filhos", filhos])
        escritor.writerow(["Valor do aluguel", f"R$ {aluguel:.2f}"])
        escritor.writerow(["Contrato imobiliario", f"R$ {contrato:.2f}"])
        escritor.writerow(["Parcelas", f"5x de R$ {parcelas:.2f}"])

def calcular():

    contrato = 2000

    print("=" * 40)
    print("     ORÇAMENTO IMOBILIARIA")
    print("=" * 40)

    print("\nEscolha o tipo de imovel")
    print("1 - Apartamento")
    print("2 - Casa")
    print("3 - Estudio")

    opcao = input("Opcao: ")

    quartos = 0
    garagem = "Nao"
    filhos = "Nao"

    if opcao == "1":
        tipo = "Apartamento"
        aluguel = 1500

        quartos = int(input("Quantidade de quartos: "))
        aluguel += quartos * 200

        resposta = input("Deseja garagem? (S/N): ").upper()

        if resposta == "S":
            aluguel += 150
            garagem = "Sim"

        filhos = input("Possui filhos? (S/N): ").upper()

        if filhos == "N":
            aluguel *= 0.95
            filhos = "Nao"
        else:
            filhos = "Sim"

    elif opcao == "2":
        tipo = "Casa"
        aluguel = 2200

        quartos = int(input("Quantidade de quartos: "))
        aluguel += quartos * 250

        resposta = input("Deseja garagem? (S/N): ").upper()

        if resposta == "S":
            aluguel += 200
            garagem = "Sim"

        filhos = "-"

    elif opcao == "3":
        tipo = "Estudio"
        aluguel = 1200

        vagas = int(input("Quantidade de vagas de estacionamento: "))
        aluguel += vagas * 100

        quartos = 1
        garagem = f"{vagas} vaga(s)"
        filhos = "-"

    else:
        print("Opcao invalida.")
        return

    parcelas = contrato / 5

    print("\n")
    print("=" * 40)
    print("ORCAMENTO FINAL")
    print("=" * 40)

    print(f"Tipo de imovel: {tipo}")
    print(f"Quartos: {quartos}")
    print(f"Garagem: {garagem}")
    print(f"Possui filhos: {filhos}")
    print(f"Valor do aluguel: R$ {aluguel:.2f}")
    print(f"Contrato imobiliario: R$ {contrato:.2f}")
    print(f"Parcelamento do contrato: 5x de R$ {parcelas:.2f}")

    gerar_csv(
        tipo,
        quartos,
        garagem,
        filhos,
        aluguel,
        contrato,
        parcelas
    )

    print("\nArquivo 'orcamento.csv' gerado com sucesso!")

calcular()