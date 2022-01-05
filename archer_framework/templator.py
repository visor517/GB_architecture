from jinja2 import Environment, FileSystemLoader, select_autoescape


def render(template_name, folder='templates', **kwargs):

    env = Environment(
        loader=FileSystemLoader(folder),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template(template_name)

    return template.render(**kwargs)
