#Dicionário
loja={
        "prodt1": {"nome":"caderno", "preço": 4.20, "quantidade":50},
        "prodt2": {"nome":"caneta", "preço":0.80, "quantidade":150}
    }


def print_loja():
    print("----------------------------------------")
    for chave, valor in loja.items():
        print(chave, valor)

def funcoes_loja():
    print_loja()
    novo_prodt = {"nome":"tesoura", "preço":2.50, "quantidade":75}
    loja["prodt3"] = novo_prodt
    print_loja()




funcoes_loja()
