from wand.color import Color
from wand.drawing import Drawing
from wand.image import Image


class KDPVGenerator:
    DESIRED_WIDTH = 800
    DESIRED_HEIGHT = 300
    BACKGROUND_COLOR = '#2ca5e0'

    def __init__(
            self,
            speaker_image_link: str,
            talk: str,
            speaker: str,
            when: str,
            where: str
    ):
        self.speaker_image_link = speaker_image_link
        self.talk = talk
        self.speaker = speaker
        self.when = when
        self.where = where

        self.filename = '{}.png'.format(self.speaker)
        self.kdpv = None

    def generate(self):
        with Drawing() as context:
            context.stroke_color = Color('black')
            context.stroke_width = 0.1
            with Image(width=self.DESIRED_WIDTH,
                       height=self.DESIRED_HEIGHT,
                       background=Color(self.BACKGROUND_COLOR)) as img:

                context.font_size = 50
                context.text(25, 50, 'SPb Python Meetup')

                context.font_size = 20
                context.text(25, 100, self.talk)

                context.font_size = 20
                context.text(25, 150, self.speaker)

                context.draw(img)
                img.save(filename=self.filename)
