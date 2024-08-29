# ifl-reflex-python-front
MoureDev tutorial Curso de PYTHON para WEB desde cero.

## Comando útiles
Crear entorno virtual (dentro de la carpeta del proyecto ```/link_bio```):
```console
foo@bar:~$ python3.13 -m venv venv
```
**NOTA**: el comando ```python3.13``` puede diferir de su versión de pyhton. Podría ser ```python```, ```python3``` o ```python3.x```. Asegúrese que utiliza el comando correcto.

Activar el entorno virtual:
```bash
foo@bar:~$ source venv/bin/activate
```

Desactivar el entorno virtual:
```bash
(venv) foo@bar:~$ deactivate
```

Instalar reflex (dentro del entorno virtual):
```bash
(venv) foo@bar:~$ pip install reflex
```

Ejecutar reflex:
```bash
(venv) foo@bar:~$ reflex run
```

Ejecutar reflex (modo debug):
```bash
(venv) foo@bar:~$ reflex run --loglevel debug
```

Esto nos creará dos urls:

Frontend: http://localhost:3000
Backend: http://localhost:8000

Hacer ping al backend: http://localhost:8000/ping

## Enlaces útiles

- [Videotutorial MoureDev](https://www.youtube.com/watch?v=n2YrGsXJC6Y)
- [Canal de MoureDev](https://www.youtube.com/@mouredev)
- [Reflex](https://reflex.dev)
- [Reflex Docs](https://reflex.dev/docs/getting-started/introduction/)
- [Reflex CLI](https://reflex.dev/docs/api-reference/cli)
