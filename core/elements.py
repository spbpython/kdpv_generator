from typing import Tuple
from urllib.request import urlopen

from PIL import Image as PILImage
from PIL import ImageDraw as PILImageDraw
from PIL import ImageFont as PILImageFont

__all__ = (
    'Line',
    'Rectangle',
    'Ellipse',
    'Text',
    'Image',
    'RoundImage',
)


class Element:
    def __init__(self, position: Tuple[int, int]):
        self.position = position

    @staticmethod
    def _get_image_draw(image: PILImage.Image):
        return PILImageDraw.Draw(image)

    def draw(self, image: PILImage.Image):
        raise NotImplementedError


class Line(Element):
    def __init__(self, end_position: Tuple[int, int], color: str, width: int, **kwargs):
        self.end_position = end_position
        self.color = color
        self.width = width
        super(Line, self).__init__(**kwargs)

    def draw(self, image: PILImage.Image):
        draw = self._get_image_draw(image)
        draw.line((self.position, self.end_position), self.color, self.width)


class Rectangle(Element):
    def __init__(self, size: Tuple[int, int], color: str, outline: str = None, **kwargs):
        self.size = size
        self.color = color
        self.outline = outline
        super(Rectangle, self).__init__(**kwargs)

    def draw(self, image: PILImage.Image):
        draw = self._get_image_draw(image)

        x, y = self.position
        w, h = self.size

        draw.rectangle((x, y, x + w, y + h), fill=self.color, outline=self.outline)


class Ellipse(Element):
    ANTIALIAS_RATIO = 5

    def __init__(
            self,
            position: Tuple[int, int],
            size: Tuple[int, int],
            color: str = None,
            **kwargs
    ):
        self.position = position
        self.size = size
        self.color = color
        super(Ellipse, self).__init__(position, **kwargs)

    def _draw_ellipse(self, image: PILImage.Image):
        x, y = self.position
        w, h = self.size
        # create mask in higher resolution for antialias effect
        mask_size = image.size[0] * self.ANTIALIAS_RATIO, image.size[1] * self.ANTIALIAS_RATIO
        mask = PILImage.new('L', mask_size, color='black')
        mask_draw = PILImageDraw.Draw(mask)
        left, top = x * self.ANTIALIAS_RATIO, y * self.ANTIALIAS_RATIO
        right, bottom = left + w * self.ANTIALIAS_RATIO, top + h * self.ANTIALIAS_RATIO
        # draw ellipse and then downscale from higher resolution for antialias effect
        mask_draw.ellipse((left, top, right, bottom), fill='white')
        mask = mask.resize(image.size, PILImage.LANCZOS)
        image.paste(self.color, mask=mask)
        return image

    def draw(self, image: PILImage.Image):
        self._draw_ellipse(image)


class Text(Element):
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
    def __init__(
            self,
            src: str = None,
            file: str = None,
            size: Tuple[int, int] = None,
            crop: Tuple[int, int, int, int] = None,
            **kwargs
    ):
        self.src = src
        self.file = file
        self.size = size
        self.crop = crop
        super(Image, self).__init__(**kwargs)

    def _download_image(self):
        return urlopen(self.src)

    def _load_image(self) -> PILImage.Image:
        if self.src:
            im = self._download_image()
        elif self.file:
            im = self.file
        else:
            raise ValueError('Image: src or file required')

        return PILImage.open(im)

    def _resize_image(self, image: PILImage.Image) -> PILImage.Image:
        if self.size:
            image = image.resize(self.size, PILImage.LANCZOS)

        return image

    def _crop_image(self, image: PILImage.Image) -> PILImage.Image:
        if self.crop:
            return image.crop(self.crop)

        return image

    def _draw_image_with_alpha(self, image: PILImage.Image, image2: PILImage.Image):
        im2 = PILImage.new('RGBA', image.size, (0, 0, 0, 0))
        im2.paste(image2, self.position)
        im2 = PILImage.alpha_composite(image, im2)
        image.paste(im2, (0, 0))

    def _draw_image(self, image: PILImage.Image, image2: PILImage.Image):
        if image2.mode == 'RGBA':
            self._draw_image_with_alpha(image, image2)

        else:
            image.paste(image2, self.position)

    def draw(self, image: PILImage.Image):
        im = self._load_image()
        im = self._resize_image(im)
        im = self._crop_image(im)
        self._draw_image(image, im)


class RoundImage(Image):
    ANTIALIAS_RATIO = 5

    @classmethod
    def _round_image(cls, image: PILImage.Image):

        if image.mode != 'RGBA':
            image = image.convert('RGBA')

        mask_size = image.size[0] * cls.ANTIALIAS_RATIO, image.size[1] * cls.ANTIALIAS_RATIO
        mask = PILImage.new('L', mask_size, color=0)
        mask_draw = cls._get_image_draw(mask)
        mask_draw.ellipse(((0, 0), mask.size), fill=255)

        mask = mask.resize(image.size, PILImage.LANCZOS)

        canvas = PILImage.new('RGBA', image.size, color=(0, 0, 0, 0))
        canvas.paste(image, mask=mask)

        return canvas

    def draw(self, image: PILImage.Image):
        im = self._load_image()
        im = self._resize_image(im)
        im = self._crop_image(im)
        im = self._round_image(im)
        self._draw_image(image, im)
