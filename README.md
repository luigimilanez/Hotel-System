# Hotel-System
O projeto foi um trabalho de faculdade o qual visava criar um sistema de gerenciamento de reservas utilizando apenas a linguagem `Python`. O armazenamento de dados seria por meio de um arquivo .txt porém optei por utilizar o `MySQL`.

# Requisitos do projeto
<b>O código deverá possuir:</b> 

- `Funções`
- `Controle de fluxo`
- `Laços de repetição`
- `Comentários`

<br>

<b>O sistema deverá possuir:</b>

- `Menu Principal`
- `Cadastro de Reservas`
- `Entrada do Cliente (Check-in)`
- `Saída do Cliente (Check-out)`
- `Alteração de Reserva`
- `Relatório de Reservas`

# Banco de Dados
Como dito anteriormente, utilizei o `MySQL` num servidor local via [`WSL2`](https://learn.microsoft.com/pt-br/windows/wsl/about), mas você pode optar por outra linguagem de banco e IDEs diferentes. Como estava utilizando uma VM, resolvi optar pelo próprio `SQL Command Line`. Deixo aqui para download duas grandes IDEs.
- [MySQL Workbench](https://dev.mysql.com/downloads/workbench/)
- [SQL Server Management Studio (SSMS)](https://learn.microsoft.com/pt-BR/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16)

<br>

<b>Passo a passo para a criação de tabelas e inserts de dados:</b>

Após a abertura de um servidor local, basta executar este código LINK DA PASTA em seu IDE ou salvar o arquivo em formato `.sql` e executar no Prompt do SQL como fiz na imagem abaixo!
```
$ create database NOMEDOBANCO; use NOMEDOBANCO; source NOMEDOARQUIVO; select * from NOMEDATABELA;
```
![fetchdemo](https://user-images.githubusercontent.com/89088603/217149133-1949e3df-f84f-4c34-bde7-e2b91b49e2c5.png)
.
# Dependências
Caso você não tenha as bibliotecas instaladas em sua máquina, baixe-as utilizando o seguinte comando via terminal:
```bash
$ pip install -r requirements.txt
```
[`Python V3.0 > Higher`](https://www.python.org/downloads/)
