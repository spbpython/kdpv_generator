# coding: utf-8

import os
import pytest
from core.elements import Ellipse, Rectangle, RoundImage
from test.helper import get_image_diff_percentage
from PIL import Image, ImageDraw

IMAGES_PATH = 'test/images/'


def test_ellipse():
    """Test Ellipse element"""
    position = (25, 25)
    size = (50, 50)
    color = '#334455'
    canvas_size = (100, 100)
    canvas_color = '#ffffff'

    # draw Ellipse element
    image = Image.new('RGB', canvas_size, canvas_color)
    ellipse = Ellipse(position, size, color)
    ellipse.draw(image)

    # load expected image with Ellipse element
    expected_image = Image.open(os.path.join(IMAGES_PATH, 'ellipse_50x50.png'))

    # compute the difference between images
    diff = get_image_diff_percentage(image, expected_image)
    # use a threshold
    max_threshold = 0
    if diff > max_threshold:
        raise Exception(
            'Ellipse element check failed! The difference between result and expected image is {}%!'.format(diff))


def test_rectangle():
    """Test Rectangle element"""
    position = (10, 10)
    size = (80, 20)
    color = '#456789'
    canvas_size = (100, 40)
    canvas_color = '#000000'

    # draw Rectangle element
    image = Image.new('RGB', canvas_size, canvas_color)
    rectangle = Rectangle(size, color, position=position)
    rectangle.draw(image)

    # load expected image with Rectangle element
    expected_image = Image.open(os.path.join(IMAGES_PATH, 'rectangle_80x20.png'))

    # N.B.: the second point is just outside the drawn rectangle, so rect in expected image is 81x21.
    # (see: http://pillow.readthedocs.io/en/latest/reference/ImageDraw.html)

    # compute the difference between images
    diff = get_image_diff_percentage(image, expected_image)
    if diff > 0:
        raise Exception(
            'Rectangle element check failed! The difference between result and reference image is {}%!'.format(diff))


def test_round_image():
    """Test RoundImage element"""
    canvas_size = (100, 100)
    canvas_color = '#000000'

    # draw RoundImage element
    # crop image in a circle shape (incircle on test image)
    # test image has a circle (100x100) inscribed in rectangle (100x100)
    # therefore use 98x98 crop size to avoid the outer circle grip
    src = None
    filename = os.path.join(IMAGES_PATH, 'test_image.png')
    size = (100, 100)
    crop = (1, 1, 99, 99)
    position = (1, 1)
    image = Image.new('RGBA', canvas_size, canvas_color)
    round_image = RoundImage(src, filename, size, crop, position=position)
    round_image.draw(image)

    # load expected image with RoundImage element
    expected_image = Image.open(os.path.join(IMAGES_PATH, 'round_image_98x98.png'))

    # compute the difference between images
    diff = get_image_diff_percentage(image, expected_image)
    if diff > 0:
        raise Exception(
            'RoundImage element check failed! The difference between result and reference image is {}%!'.format(diff))
