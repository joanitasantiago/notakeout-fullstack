# notakeout-fullstack

Aplicação fullstack desenvolvida como parte do MVP da disciplina de Desenvolvimento Front-End Avançado da pós-graduação em Desenvolvimento Full Stack da PUC-Rio.

O sistema permite gerenciar alimentos, receitas, menus personalizados e gerar listas de compras, integrando uma API em Flask com um front-end moderno em React.

---

## Tecnologias Usadas

### Backend
- Python 3.11
- Flask
- Flask SQLAlchemy
- SQLite
- Flasgger (Swagger)
- ReportLab (PDF)
- UV (gerenciador de pacotes Python)

### Frontend
- React
- Vite
- React Router DOM
- LocalStorage API

---

## Estrutura do Projeto

```
notakeout-fullstack/
│
├── backend/                 # API Flask
│   ├── app.py
│   ├── routes/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── requirements.txt
│
├── frontend/                # SPA React
│   ├── index.html
│   └── src/
│       ├── main.jsx
│       ├── App.jsx
│       ├── components/
│       └── pages/
```

---

## Como rodar o projeto

### Backend

1. Acesse a pasta:

```bash
cd backend
```

2. Crie e ative o ambiente virtual com UV:

```bash
uv venv
.venv\Scripts\activate
```

3. Instale as dependências:

```bash
uv pip install -r requirements.txt
```

4. Inicie a aplicação:

```bash
python app.py
```

Acesse em `http://127.0.0.1:5000/`

---

### Frontend

1. Acesse a pasta:

```bash
cd frontend
```

2. Instale as dependências:

```bash
npm install
```

3. Inicie a aplicação:

```bash
npm run dev
```

Acesse em `http://127.0.0.1:5173/`

---

## API Pública Utilizada

- Nome: OpenFoodFacts API
- Licença: Open Database License (ODBL)
- API key: Não requerida
- Rotas utilizadas: busca de produtos por nome e código de barras

---

## Documentação Swagger

Disponível em:

```
http://127.0.0.1:5000/apidocs/
```

---

## Status do Projeto

- Estrutura organizada com separação de front e back
- SPA funcional com React Router
- Integração futura com Docker, PostgreSQL, testes automatizados e CI/CD

---

## Autoria

Desenvolvido por **Joanita Santiago** como parte do desafio final da disciplina de Desenvolvimento Front-end Avançado – Pós-graduação PUC-Rio Digital.