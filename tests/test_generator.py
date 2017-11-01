# coding: utf-8

import os
from core.generator import KDPVGenerator

CONFIGS_PATH = 'tests/configs/'


def test_generator_from_yml():
    kdpv_generator = KDPVGenerator.from_yml(os.path.join(CONFIGS_PATH, 'test_config_1.yml'))
    assert kdpv_generator.width == 800
    assert kdpv_generator.height == 300
    assert kdpv_generator.filename == 'test_image.png'

    assert len(kdpv_generator.fonts) == 4
    assert kdpv_generator.fonts.get('default', 'assets/fonts/BebasNeue Regular.ttf')
    assert kdpv_generator.fonts.get('default_bold', 'assets/fonts/BebasNeue Bold.ttf')
    assert kdpv_generator.fonts.get('default_italic', 'assets/fonts/CaviarDreams_Italic.ttf')
    assert kdpv_generator.fonts.get('default_bold_italic', 'assets/fonts/CaviarDreams_BoldItalic.ttf')

    assert len(kdpv_generator.elements) == 2
    assert kdpv_generator.elements[0].get('type') == 'rectangle'
    assert kdpv_generator.elements[0].get('color') == '#B1392B'
    assert kdpv_generator.elements[0].get('position') == [0, 0]
    assert kdpv_generator.elements[0].get('size') == [800, 300]

    assert kdpv_generator.elements[1].get('type') == 'text'
    assert kdpv_generator.elements[1].get('text') == 'Test Line 1\nTest Line 2\n'
    assert kdpv_generator.elements[1].get('position') == [20, 15]
    assert kdpv_generator.elements[1].get('font') == 'default'
    assert kdpv_generator.elements[1].get('font_size') == 69
    assert kdpv_generator.elements[1].get('color') == '#E1E0DD'

    assert kdpv_generator.canvas
    assert kdpv_generator.canvas.width == 800
    assert kdpv_generator.canvas.height == 300
