[![Travis CI Build Status](https://travis-ci.org/Desenho-2-2017/Ecom_merci.svg?branch=master)](https://travis-ci.org/Desenho-2-2017/Ecom_merci)
[![Maintainability](https://api.codeclimate.com/v1/badges/66c7eec706fdc129d8dd/maintainability)](https://codeclimate.com/github/Desenho-2-2017/Ecom_merci/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/66c7eec706fdc129d8dd/test_coverage)](https://codeclimate.com/github/Desenho-2-2017/Ecom_merci/test_coverage)
# Ecom_Merci

## Configuração Dev

### Dependências
* python3
* [virtualenv](https://virtualenv.pypa.io/en/stable/)
* [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)

### Configurando o VirtualEnv
Tenha as Dependências citadas acima instaladas na sua máquina.

Siga as instruções de instalação do virtualenvwrapper [(neste link)](https://virtualenvwrapper.readthedocs.io/en/latest/).

#### Configurando o seu ambiente
Adicione as seguintes linhas no arquivo ~/.bashrc
```
export WORKON_HOME=$HOME/.virtualenvs
mkdir -p $WORKON_HOME
source /usr/local/bin/virtualenvwrapper.sh

export PROJECT_HOME=$HOME/workspace
mkdir -p $PROJECT_HOME
```

#### Clonando o Repositório
Clone o repositório na pasta ```$PROJECT_HOME```

```
cd $PROJECT_HOME
git clone git@github.com:Desenho-2-2017/Ecom_merci.git
```

#### Criando um VirtualEnv
```
mkvirtualenv -p python3 -a <project_path> -r requirements/requirements.txt <virtual_env_name>
```

Exemplo:
```
mkvirtualenv -p python3 -a Ecom_merci -r requirements/requirements.txt eco
```

### Configurando seu Projeto
Crie um arquivo .env em Ecom_merci/ecom_merci/ com as seguintes configurações:

```
SECRET_KEY=blablakey
DEBUG = True
```

#### Gerando sua SECRET_KEY

```
python manage.py generate_secret_key
```
Copie o output do comando para a linha SECRET_KEY do seu arquivo .env

#### Suba o sistema
```
python manage.py runserver
```

### Verificação de Commits
O projeto possui integração continua com o [travis](https://travis-ci.org/Desenho-2-2017/Ecom_merci) e executa ao menos 2 verificações:
- pytest
- flake8

para evitar falhas no build, você pode executa-los manualmente ou "instalar" o pre-commit hook através do script:
```
./scripts/git_hooks/install_pre_commit.sh
```
