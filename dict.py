# Dicionário
loja = {
    "prodt1": {"nome": "caderno", "preço": 4.20, "quantidade": 50},
    "prodt2": {"nome": "caneta", "preço": 0.80, "quantidade": 150}
}

def print_loja():
    print("----------------------------------------")
    for chave, valor in loja.items():
        print(chave, valor)

def add_prod(cod_prod, nome, preco, quant):
    novo_prodt = {"nome": nome, "preço": preco, "quantidade": quant}
    loja[cod_prod] = novo_prodt

def remover_prod(cod_prod):
    if cod_prod in loja:
        del loja[cod_prod]  # Remover da loja


def calc_qtd():
    total = 0
    for prod in loja.values():
        quant = prod


def funcoes_loja():
    print_loja()
    add_prod("prodt3", "tesoura", 2.50, 75)
    add_prod("prodt4", "afia", 1, 10)
    remover_prod("prodt1")
    print_loja()
    remover_prod("prodt4")
    print_loja()
    calc_qtd()


funcoes_loja()
