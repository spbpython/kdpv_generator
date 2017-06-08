# -*- coding: utf-8 -*-

from urllib.request import urlopen

from PIL import Image as PILImage
from PIL import ImageFont as PILImageFont
from PIL import ImageDraw as PILImageDraw


__all__ = (
    'ElementType',
    'Line',
    'Rectangle',
    'Text',
    'Image',
)


class ElementType:
    LINE = 1
    RECTANGLE = 2
    TEXT = 3
    IMAGE = 4


class Element:
    TYPE = None

    def __init__(self, position: tuple):
        self.position = position

    @staticmethod
    def _get_image_draw(image: PILImage.Image):
        return PILImageDraw.Draw(image)

    def draw(self, image: PILImage.Image):
        raise NotImplementedError


class Line(Element):
    TYPE = ElementType.LINE

    def __init__(self, end_position: tuple, color: str, width: int, **kwargs):
        self.end_position = end_position
        self.color = color
        self.width = width
        super(Line, self).__init__(**kwargs)

    def draw(self, image: PILImage.Image):
        draw = self._get_image_draw(image)
        draw.line((self.position, self.end_position), self.color, self.width)


class Rectangle(Element):

    def __init__(self, size: tuple, color: str, outline: str = None, **kwargs):
        self.size = size
        self.color = color
        self.outline = outline
        super(Rectangle, self).__init__(**kwargs)

    def draw(self, image: PILImage.Image):
        draw = self._get_image_draw(image)

        x, y = self.position
        w, h = self.size

        draw.rectangle((x, y, x + w, y + h), fill=self.color, outline=self.outline)


class Text(Element):
    TYPE = ElementType.TEXT

    def __init__(self, text: str, color: str, font: str, font_size: int, **kwargs):
        self.text = text
        self.color = color
        self.font = font
        self.font_size = font_size
        super(Text, self).__init__(**kwargs)

    def _load_font(self):
        return PILImageFont.truetype(self.font, size=self.font_size)

    def draw(self, image: PILImage.Image):
        draw = self._get_image_draw(image)
        draw.text(self.position, self.text, fill=self.color, font=self._load_font())


class Image(Element):
    TYPE = ElementType.IMAGE

    def __init__(self, src: str = None, file: str = None, size: tuple = None, size_percent: tuple = None, **kwargs):
        self.src = src
        self.file = file
        self.size = size
        self.size_percent = size_percent
        super(Image, self).__init__(**kwargs)

    def _download_image(self):
        return urlopen(self.src)

    def _load_image(self):
        if self.src:
            im = self._download_image()
        elif self.file:
            im = self.file
        else:
            raise ValueError('Image: src or file required')

        return PILImage.open(im)

    def _resize_image(self, image: PILImage.Image):
        new_size = None

        if self.size:
            new_size = self.size

        elif self.size_percent:
            w, h = image.size
            rw, rh = self.size_percent
            new_size = (w * rw, h * rh)

        if new_size:
            image.thumbnail(new_size, PILImage.LANCZOS)

        return image

    def draw(self, image: PILImage.Image):
        im = self._load_image()
        im = self._resize_image(im)

        if im.mode == 'RGBA':
            im2 = PILImage.new('RGBA', image.size, (0, 0, 0, 0))
            im2.paste(im, self.position)
            im2 = PILImage.alpha_composite(image, im2)
            image.paste(im2, (0, 0))

        else:
            image.paste(im, self.position)


