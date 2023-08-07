from bs4 import BeautifulSoup

def banner():
        print("""\033[1;31m
                   Script Tester \033[0;0m
          \033[1;32m    
          https://github.com/GiovanniMatos  \033[0;0m       

    """)

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
    if len(tags_sobra_css) == 0 and len(tags_usadas) == 0:
        print("""\033[1;32mO arquivo HTML e o arquivo CSS estão em sincronia.\033[0;0m""")
    elif len(tags_sobra_css) > 0:
        print("""\033[31mAs seguintes tags estão presentes no arquivo CSS, mas não estão no arquivo HTML:\033[0;0m""")
        for tag in tags_sobra_css:
            print(tag)
            print()
        
    # Analise HTML - JS
    if len(tags_sobra_js) == 0 and len(tags_usadas) == 0:
        print("""\""033[1;32mO arquivo HTML e o arquivo CSS estão em sincronia.\033[0;0m""")
    else:
        if len(tags_sobra_js) > 0:
            print("""\033[31mAs seguintes tags estão presentes no arquivo Javascript, mas não estão no arquivo HTML:\033[0;0m""")
            print(tags_sobra_js)
            for tag in tags_sobra_js:
                print(tag)
            print()

# trocar pelo arquivo que deseja testar
compare_html_css_js("index.html", "style.css", "script.js")
