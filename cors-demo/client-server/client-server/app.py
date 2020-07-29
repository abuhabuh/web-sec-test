import os

from jinja2 import Environment, FileSystemLoader, select_autoescape

from apis import bootstrap 


jinja_env = Environment(
    loader=FileSystemLoader(
        os.path.join(
            os.path.dirname(__file__), 
            'templates'
        )
    ),
    autoescape=select_autoescape(['html', 'xml'])
)
app = bootstrap.bootstrap_app(jinja_env)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5001)
