# notakeout-api

API em Flask desenvolvida como parte do MVP da disciplina de Desenvolvimento Full-Stack básico da pós-graduação em Desenvolvimento Full Stack administrada pela PUC-Rio.

Este sistema tem como objetivo permitir o cadastro de alimentos e receitas, servir como base para criação de menus personalizados e gerar listas de compras em PDF.

--- 

## Tecnologias Usadas

- **Python 3.11**
- **Flask** – framework web para criação da API
- **Flask SQLAlchemy** – ORM para banco de dados
- **SQLite** – banco de dados leve e local
- **Flasgger** – geração automática de documentação Swagger
- **ReportLab** – geração de arquivos PDF (lista de compras)
- **UV** – gerenciador de pacotes python

---

## Estrutura do Projeto

```
notakeout-api/
│
├── app.py                 # Arquivo principal da aplicação
├── requirements.txt       # Lista de dependências do projeto
├── README.md              # Documentação do projeto
│
├── models/                # Modelos de dados com SQLAlchemy
├── routes/                # Rotas organizadas por blueprint
├── schemas/               # Serialização para resposta JSON
└── services/              # Lógica de negócio (lista de compras, PDF)
```

---

## Como rodar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/notakeout-api.git
cd notakeout-api
```

2. Crie e ative o ambiente virtual com UV:

```bash
uv venv
.venv\Scripts\Activate
```

3. Instale as dependências:

```bash
uv pip install -r requirements.txt
```

4. Inicie a aplicação:

```bash
python app.py
```

5. Acesse no navegador:

```
http://127.0.0.1:5000/

```

---

## Endpoints principais

### Alimentos `/foods`
- `GET /foods`
- `POST /foods`
- `GET /foods/{id}`
- `PUT /foods/{id}`
- `DELETE /foods/{id}`

### Receitas `/recipes`
- `POST /recipes`
- `GET /recipes`
- `GET /recipes/{id}`
- `PUT /recipes/{id}`

### Menus `/menus`
- `POST /menus`
- `GET /menus`
- `GET /menus/{id}`
- `DELETE /menus/{id}`

### Menus - Lista de Compras
- `GET /menus/{id}/shopping-list` – retorna a lista em JSON
- `GET /menus/{id}/pdf` – gera e baixa a lista em PDF

---

## Documentação Swagger

Disponível em:

```
http://127.0.0.1:5000/apidocs/
```

---

## Status do projeto

- Estrutura organizada em `routes/`, `models/`, `schemas/` e `services/`
- Próximo passo: desenvolvimento da interface front-end

---

## Autoria

Desenvolvido por **Joanita Santiago** como parte do desafio final da disciplina de Desenvolvimento Full Stack Básico – Pós-graduação PUC-Rio Digital.