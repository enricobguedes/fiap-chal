Para subir o projeto:


-> docker build -t fiap-chal-2 .

-> docker run --name fiap -p8882:8882 -d -t fiap-chal-2

-> docker exec -it fiap /bin/sh -c "/startDBService.sh"

-> docker exec -it fiap /bin/sh -c "python3 /backend/startServer.py"


DUVIDAS:
falar com enrico bardella guedes