import json

arquivo_cadastros = "cadastros.json"

def exibir_menu():
    print("\n ---- MENU CADASTRO ----")
    print("1 - Cadastra pessoa")
    print("2 - Ver CadastroS")
    print("3 - Sair") 
    print("-----------------------------------") 

def salvar_cadastros (cadastros):
    with open (arquivo_cadastros, "w", encoding="utf-8") as arquivo:
        json.dump(cadastros, arquivo, indent=4, ensure_ascii=False)

def carregar_cadastros():
    try:
        with open (arquivo_cadastros, "r", encoding="utf-8") as arquivo:
             return json.load(arquivo)     
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def cadastrar_pessoa(cadastros):    
    nome = input ("Nome:")
    idade = input ("Idade:")
    turma = input ("Turma:")
    curso = input ("Curso:")
    cadastros.append({ "Nome": nome, "Idade": idade, "Turma": turma, "Curso": curso})
    salvar_cadastros(cadastros)
    print("Cadastro realizado com sucesso!")
     