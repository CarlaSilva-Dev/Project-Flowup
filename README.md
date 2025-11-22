📘 Sistema de Tarefas – CRUD em Django

Este projeto é um sistema CRUD desenvolvido em Django, criado como trabalho avaliativo para uma disciplina, com o objetivo de aplicar conceitos fundamentais do desenvolvimento web.
Ele permite criar, visualizar, editar e excluir tarefas, servindo como base para quaisquer aplicações que utilizem manipulação de dados.

🚀 Propósito do Projeto
✔️ Facilitar o gerenciamento de informações

O sistema permite que usuários ou administradores:

Cadastrem novas tarefas

Visualizem listas de tarefas

Editem registros existentes

Excluam itens não necessários

✔️ Servir como base para diversas aplicações

A lógica CRUD é usada em praticamente todo tipo de sistema:

Redes sociais

E-commerce

Blogs

ERPs e sistemas corporativos

Aplicativos de cadastro

✔️ Aplicação de fundamentos essenciais

Durante o desenvolvimento, são aplicados conceitos como:

Estruturação e modelagem de banco de dados

Criação de rotas (URLs) e views

Manipulação de formulários

Integração entre backend e frontend

Funcionamento do servidor e arquitetura MVT (Model–View–Template)

✔️ Garantir controle e organização

As operações CRUD permitem manter os dados organizados, atualizados e seguros conforme o estado real do sistema.

⚙️ Funcionamento do Sistema

O sistema funciona como um gerenciador simples de tarefas, permitindo:

📝 Criar uma tarefa — ex: "Estudar Django"

🧾 Definir uma descrição

🔄 Acompanhar o status de cada tarefa

✏️ Editar qualquer informação da tarefa

🗑️ Remover tarefas que não são mais necessárias

🛠️ Tecnologias Utilizadas

Python 3

Django

HTML / CSS

SQLite (banco padrão do Django)

▶️ Como Executar o Projeto

Clone o repositório

git clone https://github.com/CarlaSilva-Dev/Project-Flowup.git


Acesse a pasta

cd Project-Flowup


Crie um ambiente virtual (opcional mas recomendado)

python -m venv venv


Ative o ambiente

Windows:

venv\Scripts\activate


Linux/Mac:

source venv/bin/activate


Instale as dependências

pip install -r requirements.txt


Execute as migrações

python manage.py migrate


Execute o servidor

python manage.py runserver


Acesse no navegador:

http://127.0.0.1:8000/

📜 Licença

Projeto desenvolvido exclusivamente para fins acadêmicos.