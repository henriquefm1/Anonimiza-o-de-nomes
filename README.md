#Anonimizador de Documentos Médicos

Este projeto nasceu de uma necessidade real: garantir a privacidade de dados sensíveis em laudos e exames médicos antes que fossem processados por modelos de Inteligência Artificial.

##Funcionalidades
- **Extração de Texto:** Lê arquivos PDF de forma automatizada.
- **Censura Flexível:** Utiliza **Expressões Regulares (Regex)** para identificar e remover nomes, CRMs e rodapés de hospitais, mesmo quando o PDF possui quebras de linha irregulares.
- **Interface Intuitiva:** Janela de seleção de arquivos (Tkinter) para facilitar o uso por pessoas não técnicas.
- **Conformidade com LGPD:** Ideal para preparar datasets que precisam de anonimização de dados pessoais.

##Tecnologias Utilizadas
- **Python 3.x**
- **PyPDF2**: Para manipulação e extração de dados de arquivos PDF.
- **Regex (re)**: Para busca e substituição padronizada de termos sensíveis.
- **Tkinter**: Para a interface de seleção de arquivos.
