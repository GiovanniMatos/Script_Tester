from bs4 import BeautifulSoup
import re

def banner():
        print("""\033[1;31m
                   Script Tester \033[0;0m
          \033[1;32m    
          https://github.com/GiovanniMatos  \033[0;0m       

    """)

# Poderão ser usadas durante o processo        
linha = "\033[1;32m-\033[0;0m" * 70
estilo = ["color", "width", "height", "border", "align", "rgb", "red", "blue", "yellow", "black", "white", "px", "vh", "border"]

def compare_html_css_js(html_file, css_file, js_file):
    # Lê o arquivo HTML
    with open(html_file, 'r') as f:
        html_content = f.read()

    # Lê o arquivo CSS
    with open(css_file, 'r') as f:
        css_content = f.read()

    # Lê arquivo Javascript
    with open(js_file, 'r') as f:
        js_content = f.read()

    # Extrai as tags do arquivo HTML
    html_soup = BeautifulSoup(html_content, 'html.parser')
    html_tags = set([tag.name for tag in html_soup.find_all()])

    # Extrai as tags do arquivo CSS
    css_tags = re.findall(r'\w+', css_content)

    # Encontra tags no Javascript
    js_soup = BeautifulSoup(js_content, 'html.parser')
    js_tags = set([tag.strip() for tag in js_content.split('{')])

    # Verifica tags usadas no HTML
    tags_usadas = html_tags

    # Verifica se as tags do CSS estão presentes no HTML
    tags_sobra_css = [tag for tag in css_tags if tag in html_tags]

    # Verifica se as tags do JS estão presentes no HTML
    tags_sobra_js = js_tags - html_tags

    # Exibe o resultado
    banner()

    # Tags usadas no HTML
    print("""\033[1;32mAs seguintes tags estão no arquivo HTML:\033[0;0m""")
    for tag in tags_usadas:
        print(tag)
    print()

    # Analise HTML - CSS
    print(linha)
    print("\033[1;32mTags HTML usadas no CSS:\033[0;0m \n")
    for tag in tags_sobra_css:
        print(tag)
    print()
    for tag in css_tags:
        if tag not in tags_usadas and tag not in estilo:
            print(f"\033[31mArquivo HTML e CSS Não possuem tag em comum ->\033[0;0m  {tag}")    

    print()
    if len(tags_sobra_css) == 0 and len(tags_usadas) == 0:
        print("""\033[1;32mO arquivo HTML e o arquivo CSS estão em sincronia.\033[0;0m""")
    elif len(css_tags) > len(tags_usadas):
        print("O arquivo CSS possui tags a Mais, que o não constam no HTML")
    elif len(css_tags) < len(html_tags):
        print("O arquivo CSS possui tags a Menos, que constam no HTML, não necessariamente um problema")
    print()
    
    # Mostra componentes de estilo no CSS 
    print(linha)    
    print("\033[34mComponente de estilo do CSS, não necessariamente tags inutilizadas no HTML:\033[0;0m")  
    for item in estilo:  
        if item not in estilo:
            print("[]")   
        elif item in css_content:
            print(f"{ {item} }")
    print()    

    # Encontrar todos os campos de entrada de texto
    print(linha)
    forms = html_soup.find_all("form")
    input_fields = html_soup.find_all("input")
    
    # Mostrar campos encontrados ou não
    print("\033[1;32mFormulários: \033[0;0m")
    if input_fields == []:
        print("\033[31mFormulários não encontrados\033[0;0m\n")
    else:    
        print("\033[33mFormulários encontrados:\033[0;0m\n")
        for form in forms:
            print("\n",form, "\n")
        for field in input_fields:
            print(field)

            # Mostra se o preenchimento do campo é obrigatorio
            if field.has_attr("required"):
                print("\033[34mCampo obrigatório\033[0;0m \n")
            else:
                print("\033[31mCampo não obrigatório\033[0;0m \n")
    print()

# trocar pelo arquivo que deseja testar
compare_html_css_js("index.html", "style.css", "script.js")