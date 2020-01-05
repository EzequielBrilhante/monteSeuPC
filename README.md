# monteSeuPC

Uma aplicação feita com uma api em Django e Django Rest Framework.

Para rodar o backend o comando é **python manage.py runserver**, na *raiz do projeto.*

A aplicação irá abrir na URL **localhost:8000**, onde pode-se consultar a API colocando **/api** no final.

Caso seja necessário carregar os dados dos itens, na raiz do projeto tem que carregar o arquivo **fixture.json**, onde ja está pre-populado com os dados.
Então execute **python manage.py loaddata fixture.json**
