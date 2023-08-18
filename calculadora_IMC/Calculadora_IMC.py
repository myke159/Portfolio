"IMC = PESO(KG) / ALTURA(M²)"

def main():
    """Funcao MAIN,
    Coleta informacoes como: nome, peso e altura,
    calcula o IMC, faz sua classificacao e o registra
    no arquivo .txt"""
    try:
        print("** Calculadora de IMC **")
        nome = str(input("Digite o nome do avaliado: ")).title()
        peso = convert_str_float("Digite o peso em Quilos (ex:70.8): ")
        altura = convert_str_float("Digite a altura em Metros (ex:1.7): ")
        imc =  round(peso / altura**2, 2) 
        classificacao = classificacao_peso(imc)
        registro_imc(nome, imc, peso, altura, classificacao)
        print("")
        print(f"[SUCESSO] Ao registrar o IMC!")
        print("")
        print(f"Resultado do IMC: {imc}kg/m2 | {classificacao}")
        print("")
    except:
        print("[ERROR] Ao tentar calcular IMC!")


def convert_str_float(mensagem):
    """
    Funcao usada em main(),
    Criada para evitar uma digitacao
    errada, como ',' ao inves de '.'
    """
    try:
        opc = str(input(f"{mensagem}")).replace(",", ".")
        return float(opc)
    except:
        print("[ERROR] Ao tentar converter de string para float")

def classificacao_peso(imc):
    # Endereco da tabela: "https://www.drrogermoura.com.br/images/artigos/tabela-imc.png"
    """
    Funcao usada em main(), 
    intuido de fazer a classificacao de peso
    e retornar a clasfficacao dele
    """
    if imc <= 18.5:
            resultado = "Abaixo do peso"
    elif 18.6 <= imc <=24.9:
            resultado = "Pesoal ideal"
    elif 25 <= imc <= 29.9:
            resultado = "Levemente acima do peso"
    elif 30 <= imc <= 34.9:
            resultado = "Obesidade grau I"
    elif 35 <= imc <= 39.9:
            resultado = "Obesidade grau II"
    else:
            resultado = "Obesidade grau III (Mórbida)"
    return resultado
    
def verif_arqui_result():
    """
    Funcao usada em registro_imc(),
    Tenta se conectar ao resultados_IMC.txt, caso falhe,
    cria esse arquivo com o cabecalho em formato csv
    """
    try: 
        with open("resultados_IMC.txt", "r") as arquivo:
            return True
    except IOError:
        with open("resultados_IMC.txt", "a") as arquivo:
            arquivo.write("nome,imc,peso,altura,classificacao\n")

def registro_imc(nome="Anonimo",imc=0,peso=0,altura=0,classificacao=None):
    """
    Funcao usada em main(),
    pega as informacoes como: nome, imc, peso, altura e classificacao e
    as registra no arquivo .txt
    """
    try:
        verif_arqui_result()
        with open("resultados_IMC.txt", "a") as arquivo:
            arquivo.write(f"{nome},{imc},{peso},{altura},{classificacao}\n")
    except IOError:
        print("[ERROR] Ao tentar registrar os dados (IMC) no arquivo 'resultados_IMC.txt' !")

if __name__ == "__main__":
    main()
        