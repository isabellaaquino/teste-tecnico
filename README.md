# teste-tecnico

## O que é preciso ser feito para executar o projeto localmente:

- [ ] No shell de seu sistema, navegue até a pasta teste-tecnico-master e com o pip, instale o pipenv, o django e o numpy: <br><i> py (ou python, dependendo da sua versão do Python) -m pip install pipenv </i> <br> <i> py -m pip install django </i> <i> py -m pip install numpy </i>
- [ ] Após isso, ainda no diretório principal, inicialize o ambiente virtual através do comando = <i> py -m pipenv shell </i>
- [ ] Navegue para a pasta byne e rode os seguintes comandos: <i> py manage.py makemigrations </i> e depois <i> py manage.py migrate </i>
- [ ] Com o ambiente virtual inicializado, rode o servidor através do comando: <i> py manage.py runserver </i>
- [ ] O servidor estará hospedado em: http://127.0.0.1:8000/

## Observações:
- A pagina /profile tem um carregamento lento, devido a atualização do número atual com o processamento de dados;

## Autor
Feito por [Isabella Aquino](https://github.com/isabellaaquino).
