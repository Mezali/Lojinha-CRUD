import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='banco'
)
cursor = conn.cursor()


def create(nome=False, valor=False):
    if nome == False and valor == False:
        n = input("Insira o nome do produto: ")
        v = input("Insira o valor do produto: R$")
        cursor.execute(f'INSERT INTO loja (nome, valor) VALUES ("{n}", {v})')
        print(10 * "----")
        read(None, True)
        print(10 * "----")
    else:
        cursor.execute(f'INSERT INTO loja (nome, valor) VALUES ("{nome}", {valor})')
        print(10 * "----")
        read(None, True)
        print(10 * "----")

    conn.commit()


def read(consulta=None, tudo=True):
    if not consulta and not tudo:
        prod = input("Qual produto para consulta? ")
    else:
        prod = consulta

    if not tudo:
        cursor.execute(f'SELECT id, nome, valor FROM loja WHERE nome="{prod}"')
    else:
        cursor.execute(f'SELECT * FROM loja')
    result = cursor.fetchall()

    if not result: print("NÃO FOI ACHADO O PRODUTO!")

    for ID, nome, valor in result:
        print("|id: {} | Produto {} R${:.2f}".format(ID, nome, valor))


def update():
    print(10 * "----")
    read(None, True)
    print(10 * "----")

    ID = input("Insira o ID do produto para alterar-lo: ")
    cursor.execute(f'SELECT id, nome, valor FROM loja WHERE id="{ID}"')
    result = cursor.fetchall()

    for id, nome, valor in result:
        print(10 * "----")
        print("PRODUTO SELECIONADO:")
        print("|{}| R${:.2f}".format(nome, valor))
        print(10 * "----")

    while True:

        resp = input('O que gostaria de alterar? [NOME, VALOR] ')

        if resp == "NOME":
            nome = input("Insira o nome para substitui-lo: ")
            cursor.execute(f'UPDATE loja SET nome="{nome}" WHERE id={ID}')
            conn.commit()
            print(10 * "----")
            read(None, True)
            print(10 * "----")
            break
        elif resp == "VALOR":
            valor = input("Insira o valor para substitui-lo: R$")
            cursor.execute(f'UPDATE loja SET valor="{valor}" WHERE id={ID}')
            conn.commit()
            print(10 * "----")
            read(None, True)
            print(10 * "----")
            break
        else:
            print("INSIRA: 'NOME' OU 'VALOR'!")


def delete():
    print(10 * "----")
    read(None, True)
    print(10 * "----")

    resp = input("Insira o ID do produto para deleta-lo: ")
    cursor.execute(f'DELETE FROM loja WHERE id = {resp}')
    conn.commit()

    print(10 * "----")
    read(None, True)
    print(10 * "----")


if __name__ == '__main__':

    while True:
        print("________________________")
        print("|    Mercadinho CRUD   |")
        print("|----------------------|")
        print("| 1. Criar produto     |")
        print("| 2. Lista produtos    |")
        print("| 3. Atualizar produto |")
        print("| 4. Apagar Produto    |")
        print("| 5. Sair do programa  |")
        print("|----------------------|")

        resp = int(input("SELECIONE: "))
        if resp == 1:
            create()
        elif resp == 2:
            read()
        elif resp == 3:
            update()
        elif resp == 4:
            delete()
        else:
            break
