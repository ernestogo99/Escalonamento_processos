## Como rodar o projeto

1. crie uma virtual env:
   ```sh
   python -m venv venv
   ```
2. inicie o ambiente virtual,Execute o comando abaixo quando estiver na pasta do projeto:

   ```sh
   ./venv/Scripts/Activate
   ```

3. Instale os requisitos:

   ```sh
   pip intall -r requirements.txt
   ```

4. Rode o Projeto:

   ```sh
   python manage.py runserver
   ```

5. Para ver a documentação com o swagger, vá para:
   ```sh
    http://127.0.0.1:8000/api/docs
   ```

## Estrutura do projeto

BACKEND/
├── manage.py
├── core/ -- Arquivo principal do Django
│ ├── init.py
│ ├── api.py -- Arquivo principal para chamar a api do django ninja
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py -- Arquivo para configurar Rotas
│ ├── wsgi.py
├── task_scheduling/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── api.py -- Arquivo onde faremos a lógica e os endpoints
│ ├── models.py (Opcional - modelo para garantir persistência e enviar ao banco de dados)
│ ├── schemas.py (Montar os schemas dos algoritmos e tipar)
│ ├── algorithms/
│ │ ├── init.py
│ │ ├── fcfs.py
│ │ ├── sjf.py
│ │ ├── srtf.py
│ │ ├── priority.py
│ │ ├── rr.py
│ │ └── rr_priority_aging.py
│
│
│
├── venv/
├── requirements.txt
└── readme.md
