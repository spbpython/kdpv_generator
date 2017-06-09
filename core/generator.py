import yaml
from PIL import Image as PILImage

from .elements import Line, Rectangle, Text, Image


class KDPVGenerator:
    def __init__(
            self, width: int, height: int, fonts: dict, elements: list,
            background: str = None, filename: str = 'kdpb.png'
    ):
        self.width = width
        self.height = height
        self.filename = filename

        self.fonts = fonts
        self.elements = elements

        self.canvas = PILImage.new('RGBA', (self.width, self.height), background)

    @classmethod
    def from_yml(cls, path: str):
        with open(path, 'r') as config_file:
            config = yaml.load(config_file)
            return cls(**config)

    def _resolve_font(self, font):
        return self.fonts.get(font, font)

    @staticmethod
    def _get_element_cls(element_type: str):
        return {
            'line': Line,
            'rectangle': Rectangle,
            'text': Text,
            'image': Image,
        }.get(element_type)

    def _make_element(self, element_config: dict):
        el_cls = self._get_element_cls(element_config.pop('type'))

        if not el_cls:
            raise ValueError('unsupported element {}'.format(element_config))

        if 'font' in element_config:
            element_config['font'] = self._resolve_font(element_config['font'])

        return el_cls(**element_config)

    def _draw_element(self, element_config: dict):
        element = self._make_element(element_config)
        element.draw(self.canvas)

    def _save(self):
        self.canvas.save(self.filename)

    def generate(self):
        for element_config in self.elements:
            self._draw_element(element_config)

        self._save()
