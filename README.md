# Ecom_Merci

## Configuração Dev

### Dependências
* python3
* [virtualenv](https://virtualenv.pypa.io/en/stable/)
* [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)


### Criando um VirtualEnv

```
mkvirtualenv -p python3 -a <project_path> -r requirements/requirements.txt <virtual_env_name>
```

Exemplo:
```
mkvirtualenv -p python3 -a Ecom_Merci -r requirements/requirements.txt eco
```

###Configurando seu Projeto
Crie um arquivo .env em ecom_merci/ecom_merci/ com as seguintes configurações:

```
SECRET_KEY=blablakey
DEBUG = True
```

#### Gerando sua SECRET_KEY

```
python manage.py generate_secret_key
```
Copie o output do comando para a linha SECRET_KEY do seu arquivo .env