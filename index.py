from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from yaml import safe_load as load

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())


def do_template(tpl):
    template = env.get_template(tpl)
    template.stream(works=load(open("work.yaml")), info=load(open("info.yaml"))).dump(
        tpl.name.replace(".tpl.", "")
    )


for tpl in Path("templates").glob("*.tpl.*"):
    do_template(tpl)
