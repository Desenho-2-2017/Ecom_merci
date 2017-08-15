# Ecom_Merci

## Configuração Dev

### Dependências
* python3
* [virtualenv](https://virtualenv.pypa.io/en/stable/)
* [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)

### Configurando o VirtualEnv
Tenha as Dependências citadas acima instaladas na sua máquina.
Siga as instruções de instalação do virtualenvwrapper [link](https://virtualenvwrapper.readthedocs.io/en/latest/).

#### Configurando o seu ambiente
Adicione as seguintes linhas no arquivo ~/.bachrc
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
cd PROJECT_HOME
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

###Configurando seu Projeto
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