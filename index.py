from jinja2 import Environment, FileSystemLoader, select_autoescape
from yaml import safe_load as load
env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape()
)
for tpl in ('index','resume','pe'):
    template = env.get_template(f"{tpl}.tpl.html")
    template.stream(
        works=load(open('work.yaml')),
        info=load(open('info.yaml'))
    ).dump(f'{tpl}.html')
