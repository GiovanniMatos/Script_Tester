# pip install beautifulsoup4
######################################
from bs4 import BeautifulSoup
import re

def banner():
        print("""\033[1;31m
                   Script Tester \033[0;0m
          \033[31m    
          https://github.com/GiovanniMatos  \033[0;0m       

    """)

# Poderão ser usadas durante o processo        
linha_terminal = "\033[1;37m-\033[0;0m" * 70
estilo = ["color", "width", "height", "border", "align", "rgb", "red", "blue", "yellow", "black", "white", "px", "vh", "border"]

def compare_html_css_js(html_file, css_file, js_file):
    # Lê o arquivo HTML
    with open(html_file, 'r') as f:
        html_content = f.read()

    # Lê o arquivo CSS
    with open(css_file, 'r') as f:
        css_content = f.read()

    # Lê linhas do arquivo Javascript
    with open(js_file, 'r') as f:
        linhas_js = f.readlines()     

    with open(js_file, 'r') as f:
        javascript_code = f.read()

    # Extrai as tags do arquivo HTML
    html_soup = BeautifulSoup(html_content, 'html.parser')
    html_tags = set([tag.name for tag in html_soup.find_all()])

    # Extrai as tags do arquivo CSS
    css_tags = re.findall(r'\w+', css_content)

    # Verifica tags usadas no HTML
    tags_usadas = html_tags

    # Verifica se as tags do CSS estão presentes no HTML
    tags_sobra_css = [tag for tag in css_tags if tag in html_tags]

    # Exibe o resultado
    banner()

    # Tags usadas no HTML
    print("""\033[1;32mAs seguintes tags estão no arquivo HTML:\033[0;0m""")
    for tag in tags_usadas:
        print(tag)
    print()

    # Analise HTML - CSS
    print(linha_terminal)
    print("\033[1;32mTags HTML usadas no CSS:\033[0;0m \n")
    for tag in tags_sobra_css:
        print(tag)
    print()    
    if len(tags_sobra_css) == 0 and len(tags_usadas) == 0:
        print("""\033[1;32mO arquivo HTML e o arquivo CSS estão em sincronia.\033[0;0m""")
    elif len(css_tags) > len(tags_usadas):
        print("O arquivo CSS possui tags a Mais, que o não constam no HTML")
    elif len(css_tags) < len(html_tags):
        print("O arquivo CSS possui tags a Menos, que constam no HTML, não necessariamente um problema")
    print()
    
    # Mostra componentes de estilo no CSS 
    print(linha_terminal)    
    print("\033[1;32mComponente de estilo do CSS, não necessariamente tags inutilizadas no HTML:\033[0;0m")  
    for item in estilo:  
        if item not in estilo:
            print("[]")   
        elif item in css_content:
            print(f"{ {item} }")
    print()    

    # Encontrar todos os campos de entrada de texto
    print(linha_terminal)
    forms = html_soup.find_all("form")
    input_fields = html_soup.find_all("input")
    
    # Mostrar campos encontrados ou não
    print("\033[1;32mFormulários: \033[0;0m")
    if input_fields == []:
        print("\033[31mFormulários não encontrados\033[0;0m\n")
    else:    
        print("\033[37mFormulários encontrados:\033[0;0m\n")
        for form in forms:
            print("\n",form, "\n")
        for field in input_fields:
            print(field)

            # Mostra se o preenchimento do campo é obrigatorio
            if field.has_attr("required"):
                print("\033[34mCampo obrigatório\033[0;0m \n")
            else:
                print("\033[31mCampo não obrigatório\033[0;0m")
    print()

    # Verifica links no HTML
    print(linha_terminal)
    print("\033[1;32mLinks:\033[0;0m \n")
    teste_links = html_soup.find_all("a")
    for link in teste_links:
        links = link.get('href')
        print(links)
    print()
    print(linha_terminal)

    # Estrair do JS atraves de parametros para mostrar uso de elementos do html
    print("\033[1;32mElementos do HTML no Javascript:\033[0;0m\n")
    for linha in linhas_js:
        if re.search("document.get", linha):
            print(linha)
        elif re.search("ElementBy", linha):
            print(linha) 
        elif re.search("ElementsBy", linha):
            print(linha)
        
    # Exibe funções do Javascript
    print(linha_terminal)
    print("\033[1;32mFunções do Javascript\033[0;0m\n")
    for linha in linhas_js:
        if re.search("function", linha):    
            print(linha)
    print()        
    bloco_de_codigo = javascript_code
    resultado = re.search(r'{(.*)}', bloco_de_codigo, re.DOTALL).group(0)
    print(f"function {resultado}")

# trocar pelo arquivo que deseja testar
compare_html_css_js("index.html", "style.css", "script.js")