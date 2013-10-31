Python Django Bootstrap
=======================

![screenshot](https://lh5.googleusercontent.com/-WjFWSHA3MjY/UnJX9Qm1AiI/AAAAAAAAD0A/9JsWq6kKUa4/w959-h859-no/temp.jpg)


Instalacion:
------------

```bash
git clone https://github.com/martinovic/mysite.git && cd mysite

sudo pip install -r requirements.txt

./manage.py syncdb

./manage.py runserver
```

Guia de Estilo de Codigo:
-------------------------

- Lint, debe pasar sin Error.
- PEP8, debe pasar sin Error.
- No Tabs, tampoco en .html, .css, .js
- No Trailing Whitespaces, tampoco en .html, .css, .js
- No print() en los .py, borrarlos antes de subirlos.
- No console.log() en los .js, borrarlos antes de subirlos.
- No codigo Python comentado, Borrar codigo muerto viejo.
- UTF-8 Encoding Declaration en los .py        # -*- coding: utf-8 -*-
- __ init __.py Vacios siempre que sea posible, previene import circular


Debug:
------

Para hacer Debug se incluye wdb y se puede usar agregando temporalmente esta linea en el codigo

```python
import wdb; wdb.set_trace()
```

La ejecucion se cortara y se lanzara el Debugger con una Session Interactiva para investigar el error

_(Si sabes usar otro debugger puedes usarlo, pero siempre borra el settrace() antes de subir el codigo)_
