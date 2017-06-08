from urllib.request import urlopen

from wand.color import Color
from wand.drawing import Drawing
from wand.image import Image


class KDPVGenerator:
    MAX_WIDTH = 800
    MAX_HEIGHT = 300
    BACKGROUND_COLOR = '#37bbe4'
    FONT_FILL_COLOR = '#35342f'
    FONT_NAME = 'Lucida Console'

    def __init__(
            self,
            speaker_image_url: str,
            talk: str,
            speaker: str,
            when: str,
            where: str
    ):
        self.speaker_image_url = speaker_image_url
        self.talk = talk
        self.speaker = speaker
        self.when = when
        self.where = where

        self.filename = '{}.png'.format(self.speaker)
        self.kdpv = None

    def generate(self):
        speaker_image = urlopen(self.speaker_image_url)

        top_margin = 15

        with Drawing() as context:
            context.fill_color = Color(self.FONT_FILL_COLOR)
            context.stroke_width = 0.1
            context.font = self.FONT_NAME
            with Image(width=self.MAX_WIDTH,
                       height=self.MAX_HEIGHT,
                       background=Color(self.BACKGROUND_COLOR)) as img:
                context.font_size = 50
                context.text(top_margin, 60, 'SPb Python\nMeetup')

                context.font_size = 20
                context.text(top_margin, 200, self.talk)

                context.font_size = 20
                context.font_style = 'italic'
                context.text(top_margin, 250, self.speaker)

                with Image(filename='static/logo.png') as logo_img:
                    context.composite(operator='atop', left=300, top=top_margin,
                                      width=logo_img.width / 3, height=logo_img.height / 3, image=logo_img)

                with Image(file=speaker_image) as speaker_img:
                    speaker_width = 200
                    context.composite(operator='atop', left=self.MAX_WIDTH - speaker_width, top=top_margin,
                                      width=0.9 * speaker_width, height=0.9 * self.MAX_HEIGHT, image=speaker_img)

                context.draw(img)
                img.save(filename=self.filename)
