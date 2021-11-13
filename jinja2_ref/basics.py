from jinja2 import (
    Environment, 
    PackageLoader, 
    select_autoescape, 
    Template
)
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def templateDemo():
    template = Template('Hello {{ name }}!')
    logger.info(f"Basic String Template:")
    logger.info(template.render(name='John Doe'))

def environmentDemo1():
    """
        This will create a template environment with a loader that 
        looks up templates in the templates folder inside the yourapp 
        Python package (or next to the yourapp.py Python module). 
        It also enables autoescaping for HTML files. This loader only 
        requires that yourapp is importable, it figures out the absolute 
        path to the folder for you.
    """
    logger.info(f"Basic Environment Package Loader, printing template list:")
    env = Environment(  
        loader=PackageLoader("jinja2_ref"),
        autoescape=select_autoescape()
    )
    str_list = "\n\t".join(env.list_templates())
    logger.info(f"\n\t{str_list}")

    logger.info(f"Load up and render the project.yml template:")
    template = env.get_template("jaffle_shop/project.yml")
    logger.info(f"Rendering the template {template.name}:")
    params = {
        "project": "basic_project",
        "layer": "basic_layer"

    }
    rendered_template = template.render(**params)
    logger.info(f"\n{rendered_template}")


