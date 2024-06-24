# WHOIS to JSON Converter

Este projeto fornece um script Python para converter dados brutos do WHOIS em formato JSON. O script pode ler dados de um arquivo ou diretamente da entrada padrão (stdin).

## Pré-requisitos

- Python 3.x

## Instalação

1. Clone o repositório ou baixe o script `whois-to-json.py` diretamente.

    ```sh
    git clone https://github.com/seu-usuario/whois-json.git
    cd whois-json
    ```

2. Torne o script executável.

    ```sh
    chmod +x whois-to-json.py
    ```

## Uso

Você pode usar o script de duas maneiras: passando um arquivo de entrada ou usando a entrada padrão.

### Passando um arquivo de entrada

1. Execute o comando `whois` para obter os dados brutos e salve-os em um arquivo.

    ```sh
    whois example.com > whois_raw.txt
    ```

2. Execute o script Python fornecendo o arquivo de entrada e o arquivo de saída.

    ```sh
    ./whois-to-json.py -f whois_raw.txt -o whois_output.json
    ```

### Usando a entrada padrão

1. Execute o comando `whois` e passe a saída diretamente para o script.

    ```sh
    whois example.com | ./whois-to-json.py -o whois_output.json
    ```

## Exemplo de Saída

A saída do script será um arquivo JSON formatado contendo as informações do WHOIS. Também será impresso na tela. Exemplo de conteúdo do arquivo `whois_output.json`:

```json
{
    "Domain Name": "example.com",
    "Registrar": "Example Registrar, Inc.",
    "Updated Date": "2023-01-01T00:00:00Z",
    "Creation Date": "1995-08-14T04:00:00Z",
    "Registry Expiry Date": "2024-08-13T04:00:00Z",
    "Registrar WHOIS Server": "whois.example-registrar.com",
    "Registrar URL": "http://www.example-registrar.com",
    "Name Server": "NS1.EXAMPLE.COM",
    "Name Server": "NS2.EXAMPLE.COM",
    "Status": "clientTransferProhibited",
    "DNSSEC": "unsigned"
}
