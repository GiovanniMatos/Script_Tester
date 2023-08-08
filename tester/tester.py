from bs4 import BeautifulSoup

def banner():
        print("""\033[1;31m
                   Script Tester \033[0;0m
          \033[1;32m    
          https://github.com/GiovanniMatos  \033[0;0m       

    """)

# Poderão ser usadas durante o processo        
linha = "\033[1;32m-\033[0;0m" * 70
estilo = ["color", "width", "height"]

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
    css_tags = set([tag.strip() for tag in css_content.split('{')])

    # Encontra tags no Javascript
    js_soup = BeautifulSoup(js_content, 'html.parser')
    js_tags = set([tag.strip() for tag in js_content.split('{')])

    # Verifica tags usadas no HTML
    tags_usadas = html_tags

    # Verifica se as tags do CSS estão presentes no HTML
    tags_sobra_css = css_tags - html_tags

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
    if len(tags_sobra_css) == 0 and len(tags_usadas) == 0:
        print("""\033[1;32mO arquivo HTML e o arquivo CSS estão em sincronia.\033[0;0m""")
    elif len(tags_sobra_css) > 0:
        print("""\033[31mAs seguintes tags estão presentes no arquivo CSS, mas não estão no arquivo HTML:\033[0;0m""")
        for tag in tags_sobra_css:
            print(tag)
            print()

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
    input_fields = html_soup.find_all("input")
    
    # Mostrar campos encontrados ou não
    requisitos = ["required","maxlength"]
    print("\033[1;32mFormulários: \033[0;0m")
    if input_fields == []:
        print("\033[31mFormulários não encontrados\033[0;0m\n")
    else:
        for field in input_fields:
            print("Formulários encontrados:\n\n", field)

        # Valida campo obrigatório e maxima capacidade de caracteres        
        for requisito in requisitos:
            if requisito == "required":
                print("\033[32mCampo obrigatorio\033[0;0m")
            elif requisito == "maxlength":
                print("\033[32mCapacidade máxima de caracteres definida\033[0;0m")
    print()
# trocar pelo arquivo que deseja testar
compare_html_css_js("index.html", "style.css", "script.js")
