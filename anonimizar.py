import PyPDF2
import re
import os
from tkinter import filedialog, Tk

def limpar_documento(texto, termos_para_remover):
    # 1. Normaliza o texto: remove espaços duplos e quebras de linha estranhas
    # Isso ajuda a encontrar termos que o PDF "quebrou" em várias linhas (comum em rodapés)
    texto_normalizado = " ".join(texto.split())
    
    # Dividimos a entrada do usuário por vírgulas e limpamos espaços extras
    lista_termos = [t.strip() for t in termos_para_remover.split(",") if t.strip()]
    
    for termo in lista_termos:
        # Criamos uma versão do termo também sem espaços extras para garantir a correspondência
        termo_limpo = " ".join(termo.split())
        
        # O padrão abaixo aceita qualquer quantidade de espaços entre as palavras do termo
        # Isso resolve o problema de rodapés que o Python lê com espaços aleatórios
        padrao_flexivel = re.escape(termo_limpo).replace(r'\ ', r'\s+')
        
        # Aplica a substituição ignorando maiúsculas/minúsculas
        padrao = re.compile(padrao_flexivel, re.IGNORECASE)
        texto_normalizado = padrao.sub("", texto_normalizado)
    
    return texto_normalizado

# --- Início do Programa ---
print("=== ANONIMIZADOR DE EXAMES MÉDICOS ===")

# Configuração da janela de seleção de arquivo
root = Tk()
root.withdraw()
root.attributes("-topmost", True) # Garante que a janela apareça na frente de outros apps

print("\nSelecione o arquivo PDF na janela que abriu...")
caminho_pdf = filedialog.askopenfilename(
    title="Selecione o PDF do exame",
    filetypes=[("Arquivos PDF", "*.pdf")]
)

if not caminho_pdf:
    print("Nenhum arquivo selecionado. Encerrando...")
else:
    print(f"Arquivo selecionado: {os.path.basename(caminho_pdf)}")
    
    print("\n--- CONFIGURAÇÃO DE PRIVACIDADE ---")
    print("Digite nomes, CRMs, Rodapés ou Hospitais separados por vírgula.")
    termos = input("Conteúdos para remover: ")

    try:
        # 1. Extração do texto do PDF
        with open(caminho_pdf, "rb") as f:
            leitor = PyPDF2.PdfReader(f)
            texto_original = ""
            for pagina in leitor.pages:
                texto_original += pagina.extract_text() + "\n"
        
        # 2. Execução da limpeza (com a nova lógica flexível)
        print("\nProcessando limpeza do texto...")
        texto_final = limpar_documento(texto_original, termos)
        
        # 3. Define o local de saída (mesma pasta do PDF original)
        pasta_do_arquivo = os.path.dirname(caminho_pdf)
        nome_saida = "exame_anonimizado_PRONTO.txt"
        caminho_saida = os.path.join(pasta_do_arquivo, nome_saida)

        # 4. Gravação do arquivo de texto final
        with open(caminho_saida, "w", encoding="utf-8") as f:
            f.write(texto_final)
            
        print("\n" + "="*60)
        print(f"SUCESSO! O arquivo limpo foi gerado.")
        print(f"PASTA: {pasta_do_arquivo}")
        print(f"ARQUIVO: {nome_saida}")
        print("="*60)

    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")

# Pausa para o usuário ver o resultado se estiver rodando fora do VS Code
print("\n" + "-"*30)
input("Pressione ENTER para fechar esta janela...")