from urllib.request import urlopen

from wand.color import Color
from wand.drawing import Drawing
from wand.font import Font
from wand.image import Image


class KDPVGenerator:
    MAX_WIDTH = 800
    MAX_HEIGHT = 300

    BACKGROUND_COLOR = Color('#08327d')
    FONT_COLOR = Color('#e1e0dd')

    FONT = 'static/CaviarDreams.ttf'
    FONT_BOLD = 'static/CaviarDreams_Bold.ttf'
    FONT_ITALIC = 'static/CaviarDreams_Italic.ttf'
    FONT_BOLD_ITALIC = 'static/CaviarDreams_BoldItalic.ttf'

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
        left_margin = 20

        with Drawing() as context:
            context.stroke_color = self.FONT_COLOR
            context.stroke_width = 0.1
            context.font_family = 'monospace'

            with Image(width=self.MAX_WIDTH,
                       height=self.MAX_HEIGHT,
                       background=self.BACKGROUND_COLOR) as img:
                vertical_offset = top_margin

                font = Font(path=self.FONT, size=50, color=self.FONT_COLOR)
                img.caption('SPb Python\nMeetup', left=left_margin, top=vertical_offset,
                            width=self.MAX_WIDTH,
                            height=self.MAX_HEIGHT,
                            gravity=None, font=font)

                vertical_offset += 150

                font = Font(path=self.FONT_BOLD, size=21, color=self.FONT_COLOR)
                img.caption(self.talk, left=left_margin, top=vertical_offset,
                            width=self.MAX_WIDTH,
                            height=self.MAX_HEIGHT,
                            gravity=None, font=font)

                vertical_offset += 50

                font = Font(path=self.FONT_BOLD_ITALIC, size=17, color=self.FONT_COLOR)
                img.caption(self.speaker, left=left_margin, top=vertical_offset,
                            width=self.MAX_WIDTH,
                            height=self.MAX_HEIGHT,
                            gravity=None, font=font)

                with Image(filename='static/logo.png') as logo_img:
                    context.composite(operator='atop', left=300, top=top_margin-20,
                                      width=logo_img.width / 3, height=logo_img.height / 3, image=logo_img)

                with Image(file=speaker_image) as speaker_img:
                    speaker_width = 200
                    context.composite(operator='atop', left=self.MAX_WIDTH - speaker_width, top=top_margin,
                                      width=0.9 * speaker_width, height=0.9 * self.MAX_HEIGHT, image=speaker_img)

                context.draw(img)
                img.save(filename=self.filename)
