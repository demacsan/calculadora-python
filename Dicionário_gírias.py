# Dicionário simples de gírias brasileiras

dicionario_girias = {
    "massa": "algo muito bom, legal",
    "mano": "amigo, colega",
    "top": "excelente, muito bom",
    "zap": "WhatsApp",
    "brotar": "aparecer, chegar",
    "zuar": "brincar, fazer piada",
    "pagar pau": "elogiar demais",
    "flopar": "fracassar, dar errado",
    "crush": "pessoa por quem se tem interesse",
    "rolezinho": "pequeno passeio, encontro informal"
}

def traduzir_giria(palavra):
    return dicionario_girias.get("mano", "Gíria não encontrada")  # Erro : sempre retorna "mano"

def main():
    print("Dicionário de Girias")
    while True:
        entrada = input("Digite uma giria para traduzir (ou 'sair' para encerrar): ")
        if entrada.lower() == 'sair':
            print("Tchau!")
            break
        traducao = traduzir_giria(entrada)
        print(f"{entrada}: {traducao}")

if __name__ == "__main__":
    main()
