# Desafio de Modelagem de Dados

Este projeto envolve a modelagem e manipulação de dados de filmes, com o objetivo de criar um banco de dados relacional, importar dados de um arquivo CSV e realizar consultas SQL para extrair informações relevantes.

## Requisitos

- Python 3.x
- SQLite
- Pandas
- unidecode
- venv (ambiente virtual)

## Estrutura do Projeto

O projeto contém os seguintes arquivos e pastas:

- `src/`:
  - `create_tables.py`: Script para criar as tabelas no banco de dados SQLite usando o esquema definido em `schema.sql`.
  - `insert_data.py`: Script para inserir dados do arquivo CSV `IMDB-Movie-Data-Processed.csv` nas tabelas `Movies`, `Actors` e `MovieActors`.
  - `process_accent.py`: Script para remover acentos dos nomes dos atores.
  - `queries.py`: Script para executar as consultas SQL e gerar arquivos de resultados separados para cada consulta.

- `data/`:
  - `IMDB-Movie-Data.csv`: Arquivo CSV contendo dados sobre filmes.
  - `IMDB-Movie-Data-Processed.csv`: Contendo as informações formatadas.

- `sql/`:
  - `schema.sql`: Arquivo SQL contendo a definição das tabelas no banco de dados.
  - `queries.sql`: Arquivo SQL contendo as consultas que serão executadas.

## Instalação

1. **Clone o repositório**:

   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DIRETORIO>

2. **Crie e ative o ambiente virtual**:
     - Para ativar: python -m venv venv
     - No Linux use `source venv/bin/activate` 
     - No Windows use `venv\Scripts\activate` ou `.\venv\Scripts\activate`

3. **Instale as dependências**:

    pip install requirements.txt

4. **Execuções**:

     - Se quiser verificar a efetividade do programa, exclua os arquivos .txt referentes às consultas e também o movies.db.
     - Logo após execute estes scripts no terminal:
        - python src/create_tables.py Para criar as tabelas no banco de dados;
        - python src/insert_data.py Para Inserir os dados;
        - python src/queries.py Para realizar as consultas

