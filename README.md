# Teste tecnico - Leitor de CNAB

---

## 1. Resumo

Essa API foi estruturada no intuito de facilitar a manipulação de arquivos de texto CNAB.

Leitor de CNAB é uma aplicação que faz a leitura de um arquivo de texto CNAB, <br/>
guarda suas informações em um banco de dados e as renderiza em uma página html

A aplicação possui duas tabelas:

- **Transactions**
- **Types**

Tecnologias usadas nesse projeto:

- [DJango](https://www.djangoproject.com/)
- [DJango Rest Framework](https://www.django-rest-framework.org/)
- [Black](https://pypi.org/project/black/)
- [IPython](https://pypi.org/project/ipython/)
- [IPDB](https://pypi.org/project/ipdb/)

---

## 2. Preparativos

### 2.1. Instalando Dependências

Clone o projeto em sua máquina local e crie o ambiente virtual VENV:

```shell
python -m venv venv
```

### 2.2. Entrando no ambiente virtual

Entre no ambiente virtual com o comando:

**Windows**

```shell
source venv/Scripts/activate
```

**Linux**

```shell
source venv/bin/activate
```

### 2.3. Instale as dependências

Dependências necessárias para rodar o projeto:

```shell
pip install -r requirements.txt
```

### 2.4. Execute as migrações para realizar a persistência de dados

```shell
python manage.py migrate
```

### 2.5. Execute a população da tabela de tipos

```shell
python manage.py create_types
```

### 2.6. Execute a aplicação

```shell
python manage.py runserver
```

---

## 3. Rotas

A aplicação possui uma rota e dois verbos HTTP:

`GET api/upload/`

Renderiza uma página html mostrando todas as transações guardadas no banco de dados, <br/> juntamente com um campo para envio de arquivos, não precisa de autorização

`POST api/upload/`

É feito assim que houver um click no botão enviar do formulário da página, <br/>
faz a leitura do arquivo enviado e quarda suas informações em um banco de dados, <br/>
se houver qualquer tipo de erro no envio ou nos dados do arquivo será renderizada uma lista de erros, não precisa de autorização

---

## 4. Formatação do arquivo

### 4.1. Regras do arquivo

Para o envio correto do arquivo de texto CNAB deve ser seguido uma série de passos:

- Todas as linhas do arquivo devem ter exatamente 80 caracteres
- Todas as informações devem ser passadas juntas, sem nenhum tipo de separação (ex: "," , "-" , "/" e etc...)
- As informações devem seguir a ordem da tabela

  ![Formatação cnab](formatacao-cnab.png)

<br/>

### 4.2. Tipos dos Campos

- Tipo: inteiro de 1 a 9
- Data: uma data válida (AAAAMMDD)
- Valor: um inteiro (em centavos)
- CPF: um cpf válido
- Cartão: um cartão válido
- Hora: uma horário válido (HHMMSS)
- Dono da loja: um nome qualquer
- Nome da loja: um nome qualquer

<br/>

### 4.3. Tabela de tipos

![Formatação tipos](formatacao-tipos.png)

<br/>

### 4.4. Exemplo

[Arquivo exemplo](cnab-example.txt)
