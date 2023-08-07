from bs4 import BeautifulSoup

def compare_html_css_js(html_file, css_file, js_file):
    # Lê o arquivo HTML
    with open(html_file, 'r') as f:
        html_content = f.read()

    # Lê o arquivo CSS
    with open(css_file, 'r') as f:
        css_content = f.read()

    # Lê arquivo Javascript
    with open(js_file, 'r') as file:
        js_content = file.read()

    # Extrai as tags do arquivo HTML
    html_soup = BeautifulSoup(html_content, 'html.parser')
    html_tags = set([tag.name for tag in html_soup.find_all()])

    # Extrai as tags do arquivo CSS
    css_tags = set([tag.strip() for tag in css_content.split('{')])

    # Encontra tags no Javascript
    js_soup = BeautifulSoup(js_content, 'html.parser')
    js_tags = set([tag.strip() for tag in js_content.split('{')])

    # Verifica se as tags do CSS estão presentes no HTML
    tags_sobra = css_tags - html_tags

    # Verifica se há tags desnecessárias no HTML
    tags_usadas = html_tags - css_tags

    tags_sobra_js = js_tags - html_tags

    tags_usadas_js = html_tags - js_tags

    # Verificar se as tags do JavaScript estão presentes no HTML
    tags_presentes_js = []
    tags_ausentes_js = []

    # Exibe o resultado
    print("""\033[1;31m
                   Script Tester \033[0;0m
          \033[1;32m    
          https://github.com/GiovanniMatos  \033[0;0m       
    """)
    if len(tags_sobra) == 0 and len(tags_usadas) == 0:
        print("\033[1;32mO arquivo HTML e o arquivo CSS estão em sincronia.\033[0;0m")
    else:
        if len(tags_sobra) > 0:
            print("\033[31mAs seguintes tags estão presentes no arquivo CSS, mas não estão no arquivo HTML:\033[0;0m")
            print(tags_sobra)
            print()
        if len(tags_usadas) > 0:
            print("\033[1;32mAs seguintes tags estão no arquivo HTML:\033[0;0m")
            print(tags_usadas)
            print()


    if len(tags_sobra_js) == 0 and len(tags_usadas_js) == 0:
        print("\033[1;32mO arquivo HTML e o arquivo CSS estão em sincronia.\033[0;0m")
    else:
        if len(tags_sobra_js) > 0:
            print("\033[31mAs seguintes tags estão presentes no arquivo Javascript, mas não estão no arquivo HTML:\033[0;0m")
            print(tags_sobra_js)
            print()
        if len(tags_usadas_js) > 0:
            print("\033[1;32mAs seguintes tags estão no arquivo HTML:\033[0;0m")
            print(tags_usadas_js)
            print()
          

# Exemplo de uso do script
compare_html_css_js("index.html", "style.css", "script.js")
