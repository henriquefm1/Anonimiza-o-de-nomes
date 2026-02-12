import PyPDF2
import re
import os
from tkinter import filedialog, Tk

def limpar_documento(texto, termos_para_remover):
    texto_normalizado = " ".join(texto.split())
    
    lista_termos = [t.strip() for t in termos_para_remover.split(",") if t.strip()]
    
    for termo in lista_termos:
        termo_limpo = " ".join(termo.split())
        
        padrao_flexivel = re.escape(termo_limpo).replace(r'\ ', r'\s+')
        
        padrao = re.compile(padrao_flexivel, re.IGNORECASE)
        texto_normalizado = padrao.sub("", texto_normalizado)
    
    return texto_normalizado

print("=== ANONIMIZADOR DE EXAMES MÉDICOS ===")

root = Tk()
root.withdraw()
root.attributes("-topmost", True) 

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
        with open(caminho_pdf, "rb") as f:
            leitor = PyPDF2.PdfReader(f)
            texto_original = ""
            for pagina in leitor.pages:
                texto_original += pagina.extract_text() + "\n"
        
        print("\nProcessando limpeza do texto...")
        texto_final = limpar_documento(texto_original, termos)
        
        pasta_do_arquivo = os.path.dirname(caminho_pdf)
        nome_saida = "exame_anonimizado_PRONTO.txt"
        caminho_saida = os.path.join(pasta_do_arquivo, nome_saida)

        with open(caminho_saida, "w", encoding="utf-8") as f:
            f.write(texto_final)
            
        print("\n" + "="*60)
        print(f"SUCESSO! O arquivo limpo foi gerado.")
        print(f"PASTA: {pasta_do_arquivo}")
        print(f"ARQUIVO: {nome_saida}")
        print("="*60)

    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")

print("\n" + "-"*30)

input("Pressione ENTER para fechar esta janela...")
