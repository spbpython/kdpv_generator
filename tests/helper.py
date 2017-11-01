# coding: utf-8


def get_image_diff_percentage(image1, image2):
    """Get the percentage difference between two images"""
    if image1.size != image2.size:
        raise Exception('image1.size {} != image2.size {}'.format(image1.size, image2.size))
    pixels1 = image1.load()
    pixels2 = image2.load()
    diff_pixels = 0
    for y in range(image1.size[1]):
        for x in range(image1.size[0]):
            if pixels1[x, y] != pixels2[x, y]:
                diff_pixels += 1
    percentage = diff_pixels / float(image1.size[0] * image1.size[1])
    return percentage * 100
