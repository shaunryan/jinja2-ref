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

