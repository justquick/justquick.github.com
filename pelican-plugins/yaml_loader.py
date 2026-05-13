"""
Pelican plugin to load YAML data files into Jinja2 context.

This plugin loads info.yaml and work.yaml from the project root
and makes them available in templates as SITEDATA.info and SITEDATA.works
"""

from pelican import signals
import yaml
import os


def load_yaml_data(generator):
    """Load YAML files into Jinja2 context"""
    # Get the project root directory
    project_root = os.getcwd()

    # Load info.yaml
    info_path = os.path.join(project_root, 'info.yaml')
    with open(info_path, 'r') as f:
        info = yaml.safe_load(f)

    # Load work.yaml
    work_path = os.path.join(project_root, 'work.yaml')
    with open(work_path, 'r') as f:
        works = yaml.safe_load(f)

    # Add to generator context
    generator.context['SITEDATA'] = {
        'info': info,
        'works': works
    }


def register():
    """Register the plugin with Pelican"""
    signals.generator_init.connect(load_yaml_data)
