# notakeout-fullstack

Aplicação fullstack desenvolvida como parte do MVP da disciplina de Desenvolvimento Front-End Avançado da pós-graduação em Desenvolvimento Full Stack da PUC-Rio.

O sistema permite gerenciar alimentos, receitas, menus personalizados e gerar listas de compras, integrando uma API em Flask com um front-end moderno em React.

---

## Tecnologias Utilizadas

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

### DevOps
- Docker
- Docker Compose

---

## Estrutura do Projeto

```
notakeout-fullstack/
├── backend/              # Aplicação Flask
│   ├── app.py
│   ├── routes/
│   ├── services/
│   ├── schemas/
│   ├── models/
│   ├── tests/
│   └── requirements.txt
├── frontend/             # Aplicação React
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.jsx
│   └── vite.config.js
├── docker-compose.yml
└── README.md
```

---

## Como rodar o projeto

### Opção 1: Com Docker

#### 1. Instale Docker e Docker Compose

- Baixe o [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Após instalar, verifique se tudo está funcionando:

```bash
docker --version
docker compose version
```

#### 2. Clone o repositório

```bash
git clone https://github.com/joanitasantiago/notakeout-fullstack.git
cd notakeout-fullstack
```

#### 3. Suba os serviços com Docker Compose

```bash
docker compose up --build
```

#### 4. Acesse a aplicação

- Front-end: [http://localhost:5173](http://localhost:5173) (modo desenvolvimento) ou [http://localhost:80](http://localhost:80) (produção)
- Back-end (API): [http://localhost:5000](http://localhost:5000)

> **Atenção:**  
> Durante o desenvolvimento, o projeto utiliza `docker-compose.override.yml` para habilitar hot reload tanto no Flask quanto no React.  
> Lembre-se de configurar as variáveis de ambiente copiando `.env.example` para `.env` em cada serviço.

---

### Opção 2: Sem Docker

#### 1. Rodando o Backend (Flask)

**Pré-requisitos:**
- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (ou venv/pip)

**Passos:**
```bash
cd backend
uv venv
uv pip install -r requirements.txt
cp .env.example .env
python app.py
```
A API estará disponível em: [http://localhost:5000](http://localhost:5000)

---

#### 2. Rodando o Frontend (React + Vite)

**Pré-requisitos:**
- Node.js 18+
- npm ou [pnpm](https://pnpm.io/)

**Passos:**
```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```
A aplicação estará disponível em: [http://localhost:5173](http://localhost:5173)

---


## Integração com Open-Meteo (Sugestão de comida pelo clima)

O frontend agora conta com integração à API [Open-Meteo](https://open-meteo.com/) para sugerir pratos de acordo com a temperatura local. Veja o serviço em `frontend/src/services/weather.js`:

- Busca a temperatura atual via coordenadas (latitude/longitude)
- Gera uma sugestão de comida personalizada para o usuário
- Em caso de erro de rede, exibe uma sugestão genérica


## Ambiente de desenvolvimento com Dev Container

Para facilitar o desenvolvimento no VS Code, o projeto inclui suporte a [Dev Containers](https://containers.dev/):

- Arquivo `.devcontainer/devcontainer.json` já configurado para abrir o projeto no container Docker
- Basta instalar a extensão "Remote - Containers" no VS Code e abrir o projeto usando "Reopen in Container"
- O VS Code irá reconhecer automaticamente os pacotes Python do backend e Node do frontend

## Documentação Swagger

A documentação da API está disponível em:

[http://127.0.0.1:5000/apidocs/](http://127.0.0.1:5000/apidocs/)

---

## Em breve

- **Frontend:** Menus, Lista de Compras, testes
- **Backend:** Migração para PostgreSQL, testes
- **DevOps:** GitHub Actions com CI/CD

---

## Autoria

Desenvolvido por **Joanita Santiago** como parte do desafio final da disciplina de Desenvolvimento Front-end Avançado – Pós-graduação PUC-Rio Digital.
