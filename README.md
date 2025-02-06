# API-CardBrandChecker

## Leia com Atencão
Esta API foi desenvolvida para uma atividade acadêmica de certificação, onde o principal objetivo era usar o GitHub Copilot como assistente de escrita de código para acelerar o desenvolvimento e aumentar a produtividade, portanto grande parte do código foi gerado pelo GitHub Copilot, e meu trabalho como desenvolvedor e aluno foi revisar e ajustar o código gerado para que ele atendesse aos requisitos do projeto. Desta forma deixo claro que possíveis bugs ou instabilidades podem ocorrer, e que o código pode não estar 100% otimizado, mas que o principal objetivo foi alcançado, que era o de aprender a usar o GitHub Copilot e entender como ele pode ser útil no desenvolvimento de software.

## Descrição do Projeto

O projeto **API-CardBrandChecker** é uma aplicação web desenvolvida em Python utilizando o framework Flask. A principal funcionalidade deste projeto é verificar e identificar a bandeira de cartões de crédito com base em seus prefixos e comprimentos. O algoritmo implementado é chamado de ***Alogiritmo de Luhn*** e é um algoritmo realmente usado para verificar a validade de números de cartões de crédito. O banco de dados implementado em SQLITE3 foi usado apenas para guardar informações sobre os prefixos de cada bandeira, os possíveis comprimentos e o nome da bandeira, logo não há nenhuma informação sensível armazenada no banco de dados. A escolha desta opção foi por questões de simplicidade e facilidade de implementação.



## Funcionalidades

- **Rota home**: A aplicação Flask define uma rota principal que renderiza uma página HTML usando o template `index.html` no qual temos uma página frontend que apresenta exemplos de uso e outras informações sobre a API.
- **Consultas de Bandeiras**: O projeto permite a busca e recuperação de informações sobre bandeiras de cartões armazenadas no banco de dados.
- **verificação de números de cartão**: A aplicação verifica se um número de cartão de crédito é válido e, se for, identifica a bandeira do cartão, o algoritmo de Luhn é utilizado para verificar a validade do número do cartão. O número do cartão não é salvo em lugar nenhum.


    | Bandeira         | Prefixos                                                                 | Comprimentos                  |
    |------------------|--------------------------------------------------------------------------|-------------------------------|
    | Visa             | 4                                                                        | 13, 16, 19                    |
    | MasterCard       | 51-55, 2221-2720                                                         | 16                            |
    | American Express | 34, 37                                                                   | 15                            |
    | Discover         | 6011, 622126-622925, 644-649, 65                                         | 16                            |
    | Diners Club      | 300-305, 36, 38                                                          | 14, 16, 19                    |
    | JCB              | 3528-3589                                                                | 16                            |
    | Hipercard        | 38, 6062                                                                 | 13, 16, 19                    |
    | Elo              | 4011, 4312, 4387, 4576, 6277, 6362                                       | 16                            |
    | Aura             | 50                                                                       | 16                            |
    | Sodexo           | 606282                                                                   | 13, 16                        |
    | Enroute          | 2014, 2149                                                               | 15                            |
    | Voyager          | 8699                                                                     | 15                            |
    | Visa Electron    | 4026, 4175, 4508, 4844, 4913, 4917                                       | 13, 14, 15, 16, 17, 18, 19    |


### Estrutura do Projeto

```
.
├── app.py
├── db
│   ├── database.py
│   ├── db.sqlite3
│   └── __pycache__/
├── .gitignore
├── json/
├── routes/
├── static
│   ├── images/
└── templates/
```

### Como Executar

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/devLink13/API-CardBrandChecker.git
    ```
2. **Navegue até o diretório do projeto**:
    ```bash
    cd API-CardBrandChecker
    ```
3. **Crie um ambiente virtual**:
    ```bash
    python -m venv env
    ```
4. **Ative o ambiente virtual**:
    - No Windows:
      ```bash
      .\env\Scripts\activate
      ```
    - No Linux/Mac:
      ```bash
      source env/bin/activate
      ```
5. **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```
6. **Execute a aplicação**:
    ```bash
    python app.py
    ```
7. **Acesse a aplicação**: Abra um navegador web e vá para a [página home](https://api-cardbrandchecker.onrender.com/) da API.

### Exemplo de uso com Python

Você pode usar a API para verificar a bandeira de um cartão de crédito com base em seu número. Abaixo está um exemplo de uso da API com Python:
```python
import requests

url = "https://api-cardbrandchecker.onrender.com/checkCard/5527 1928 3463 4931"

response = requests.post(url)

if response.status_code == 200:
    result = response.json()
    print(result)
```
A resposta será assim se o número do cartão for válido:
```json
{
    "card_number": "5527 1928 3463 4931",
    "is_valid": true,
    "flag": "MasterCard"
}
```

Se o número do cartão for inválido, a resposta será assim:
```json
{
    "card_number": "5527 1928 3463 4931",
    "is_valid": false
}
```
Se a bandeira não for encontrada:
```json
{
    "card_number": "5527 1928 3463 4931",
    "is_valid": true,
    "flag": "not found"
}
```

### Exemplos de possíveis usos para a API

* Integrar com um sistema de pagamento para verificar a bandeira de um cartão de crédito.
* Verificar a bandeira de um cartão de crédito em um aplicativo de e-commerce.
* Validar números de cartões de crédito em um aplicativo de gerenciamento financeiro.

**Nota**: Este projeto foi desenvolvido para fins educacionais e não deve ser usado em produção sem uma revisão completa do código.


### Requisitos

- Python 3.x
- Flask
- SQLite

### Autor

devLink13

### Licença

Este projeto está licenciado sob os termos da licença MIT.

### Contribuições

Contribuições são bem-vindas! Se você tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

### Erros Comuns

- **Erro de Conexão com o Banco de Dados**: Verifique se o arquivo `db.sqlite3` está presente no diretório `db` e se você possui permissões para lê-lo e escrevê-lo.
- **Problemas com Dependências**: Certifique-se de que todas as dependências estão instaladas corretamente executando `pip install -r requirements.txt`.

### Contato

Para mais informações ou suporte, entre em contato pelo GitHub.