#!/usr/bin/python
from jinja2 import Environment, FileSystemLoader
from map import OT, NT, title, imgs


environment = Environment(loader=FileSystemLoader('.'))


def render(template, ctx):
    return environment.get_template(template).render(ctx)


content = render('index.tmpl', {
    'OT': OT, 'NT': NT, 'title': title, 'imgs': imgs
})
with open('index.html', 'w') as f:
    f.write(content)


for book in OT + NT:
    content = render('book.tmpl', {'book': book, 'title': title})
    with open(book + '.html', 'w') as f:
        f.write(content)
