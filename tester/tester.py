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
    if len(missing_tags) == 0 and len(unnecessary_tags) == 0:
        print("O arquivo HTML e o arquivo CSS estão em sincronia.")
    else:
        if len(missing_tags) > 0:
            print("As seguintes tags estão presentes no arquivo CSS, mas não estão no arquivo HTML:")
            print(missing_tags)
        if len(unnecessary_tags) > 0:
            print("As seguintes tags estão presentes no arquivo HTML, mas não estão no arquivo CSS:")
            print(unnecessary_tags)

# Exemplo de uso do script
compare_html_css("index.html", "style.css")