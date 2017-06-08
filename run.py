import yaml

from core import KDPVGenerator

with open('data.yaml', 'r') as f:
    data = yaml.load(f)

generator = KDPVGenerator(**data)

generator.generate()
