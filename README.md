# **Django Vagas Website**

*Desenvolvido usando Django*

## Descrição

Aplicação web de um site de vagas com múltiplas permissões.

>## Como instalar localmente (supondo que você tenha git e python >= 3.11 instalado):

>clone o repositório e instale instale as dependencias que estão em "requirements.txt".
>
>Com o ambiente virtual ativo:

```console
git clone https://github.com/Ricardo-Jackson-Ferrari/djvagas.git
cd djvagas
cp env .env
python -m pip install poetry
poetry install
```

**OBS. Não se esqueça de alterar o arquivo .env que foi gerado a partida da cópia de exemplo "env" que vem na raíz do projeto.**

>Para total funcionamento da aplicação ainda é necessário fazer as migrações para gerar o esquema de banco de dados: 

```console
python manage.py migrate
``` 

>Criando um usuário com acesso ao admin:

```console
python manage.py createsuperuser
```

>## Ativando a aplicação (localmente)
>Para executar o servidor localmente (Com o ambiente virtual ativo):

```console
python manager.py runserver
```

Agora é possível acessar a aplicação em http://localhost:8000

>## Para executar os testes (localmente)
>Para executar o servidor localmente (Com o ambiente virtual ativo):

```console
pytest
```

>Caso queira ter acesso a cobertura de testes:

```console
coverage run -m pytest
coverage html
python -m http.server 9000 --directory htmlcov
```

Agora é possível acessar a cobertura de testes em http://localhost:9000