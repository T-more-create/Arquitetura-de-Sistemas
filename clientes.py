from util import calcular_media

def ler_dados_arquivo(nome_arquivo):
    """Lê os dados do arquivo e retorna listas de idades e rendas mensais."""
    idades = []
    rendas = []
    try:
        with open(nome_arquivo, "r") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(";")  
                idades.append(int(partes[2]))     
                rendas.append(float(partes[3]))   
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
    except ValueError:
        print("Erro: Dados mal formatados no arquivo.")
    return idades, rendas

def main():
    nome_arquivo = "clientes.txt"
    idades, rendas = ler_dados_arquivo(nome_arquivo)

    if idades and rendas:  
        media_idade = calcular_media(idades)
        media_renda = calcular_media(rendas)

        print(f"Média de idade: {media_idade:.2f} anos")
        print(f"Média de renda mensal: R$ {media_renda:.2f}")
    else:
        print("Não foi possível calcular as médias.")

if __name__ == "__main__":
    main()
