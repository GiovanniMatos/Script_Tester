from bs4 import BeautifulSoup

def compare_html_css(html_file, css_file):
    # Lê o arquivo HTML
    with open(html_file, 'r') as f:
        html_content = f.read()

    # Lê o arquivo CSS
    with open(css_file, 'r') as f:
        css_content = f.read()

    # Extrai as tags do arquivo HTML
    html_soup = BeautifulSoup(html_content, 'html.parser')
    html_tags = set([tag.name for tag in html_soup.find_all()])

    # Extrai as tags do arquivo CSS
    css_tags = set([tag.strip() for tag in css_content.split('{')])

    # Verifica se as tags do CSS estão presentes no HTML
    missing_tags = css_tags - html_tags

    # Verifica se há tags desnecessárias no HTML
    unnecessary_tags = html_tags - css_tags

    # Exibe o resultado
    print("""\033[1;31m
        ________           _____             
        ___  __/_____________  /_____________
        __  /  _  _ \_  ___/  __/  _ \_  ___/
        _  /   /  __/(__  )/ /_ /  __/  /    
        /_/    \___//____/ \__/ \___//_/ 
        \033[0;0m  \033[1;32m    
          https://github.com/GiovanniMatos  \033[0;0m       
    """)
    if len(missing_tags) == 0 and len(unnecessary_tags) == 0:
        print("\033[1;32mO arquivo HTML e o arquivo CSS estão em sincronia.\033[0;0m")
    else:
        if len(missing_tags) > 0:
            print("\033[31mAs seguintes tags estão presentes no arquivo CSS, mas não estão no arquivo HTML:\033[0;0m")
            print(missing_tags)
            print()
        if len(unnecessary_tags) > 0:
            print("\033[1;32mAs seguintes tags estão no arquivo HTML:\033[0;0m")
            print(unnecessary_tags)
            print()

# Exemplo de uso do script
compare_html_css("index.html", "style.css")