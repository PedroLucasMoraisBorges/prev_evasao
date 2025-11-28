# Sistema de Predição — Django + XGBoost

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-316192?style=for-the-badge&logo=postgresql&logoColor=white)

---

## 📜 Descrição do Projeto

Este projeto entrega uma interface web dedicada à execução do modelo preditivo desenvolvido no TCC, permitindo que usuários processem arquivos CSV e obtenham inferências de forma ágil e intuitiva.
A solução foi estruturada para oferecer uma experiência simples, objetiva e orientada a resultados, eliminando fricções no uso do modelo treinado.

A máquina preditiva integrada é capaz de identificar alunos com o perfil de evasão, classificando se um aluno apresenta ou não perfil compatível com tendência à evasão. Essa camada de inteligência oferece suporte decisório, permitindo antecipação de casos críticos e atuação estratégica baseada em dados. 

---

## 📑 Índice

* [Stack de Tecnologias](#-stack-de-tecnologias)
* [Estrutura de Apps Django](#-estrutura-de-apps-django)
* [Iniciando o Projeto (Primeira Vez)](#-iniciando-o-projeto-primeira-vez)

---

## 🚀 Stack de Tecnologias

* **Backend:** Python 3.13, Django 5.2
* **Banco de Dados:** PostgreSQL 17

---

## 📦 Estrutura de Apps Django

| App         | Descrição                                                                      |
| ----------- | ------------------------------------------------------------------------------ |
| `prev_evasao`      | App principal que contém as configurações do projeto, URLs e arquivos de base. |
| `pages`     | Responsvável pela configuração da página e funções existentes                   |

---

## ✨ Iniciando o Projeto (Primeira Vez)

Siga estes passos para configurar e executar o ambiente de desenvolvimento pela primeira vez.


### ⚙️ Passos para Instalação

**1. Clone o Repositório**

```bash
git clone "https://github.com/PedroLucasMoraisBorges/prev_evasao"
cd "prev_evasao"
```

### **2. Instale o ambiente virtual e os requisitos do projeto**

Instale o ambiente virtual do python e ative-o

```bash
python -m virtualenv venv
venv\Scripts\activate
```

Instale as dependências do projeto

```bash
pip install -r requirements.txt
```

### **3. Configure o Ambiente e Aplique as Migrações**

Execute as migrações iniciais para preparar o banco de dados:

```bash
python manage.py makemigrations
python manage.py migrate
```

Crie um superusário para ter acesso ao gerenciador de banco de dados

```bash
python manage.py createsuperuser
```

### **4. Rode o projeto localmente**

```bash
python manage.py runserver
```

A aplicação estará acessível em http://127.0.0.1:8000/.