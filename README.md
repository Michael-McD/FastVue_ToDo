# ToDo App
### Using 
- Python 3.12.0
- Conda environments
- Poetry package dependency manager
- FastAPI Python API framework
- Vue JavaScript framework for web user interfaces
- Postgres SQL database
- Tortoise Python ORM (Object Relation Mapper)

### Setup
1. Initialize the Poetry manager
   > FYI: Install Poetry using [pipx](https://python-poetry.org/docs/#installing-with-pipx)
   

   Configure Poetry to use Conda Virtual Environments
   ```
   $ poetry config virtualenvs.path $CONDA_ENV_PATH
   $ poetry config virtualenvs.create false
   ```

   Create Poetry project
   ```
   $ poetry new ToDo
   $ cd ToDo

   Which creates the followinf folder structure: 
   ToDo
   ├── pyproject.toml
   ├── README.md
   ├── ToDo
   │   └── __init__.py
   └── tests
      └── __init__.py
   ```

2. Update Conda, create and activate Conda environment
   
   ```
      $ sudo conda update -n base -c defaults conda 
      $ conda -n ToDo python=3.12.0
      $ conda activate ToDo
   ```
  
3. Add FastAPI and Tortoise ORM Python packages
   ```
   $ poetry add "fastapi[all]"
   $ poetry add "tortoise-orm[asyncpg]"
   ```