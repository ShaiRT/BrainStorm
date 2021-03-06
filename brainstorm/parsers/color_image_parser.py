"""A snapshot color image parser
"""
import PIL.Image


def parse_color_image(snapshot):
    '''saves parsed color image
    to the same directory of the unparsed information

    **assumes snapshot has a color image, a user and datetime

    Args:
        snapshot (dict): snapshot with a color image

    Returns:
        dict -- parsed color image information
    '''
    image_info = snapshot['color_image']
    image_size = image_info['width'], image_info['height']
    image_path = image_info['path'] + '.png'

    with open(image_info['path'], 'rb') as f:
        image = PIL.Image.frombytes('RGB', image_size, f.read())
    image.save(image_path)

    image_info['path'] = image_path
    parsed_info = dict()
    parsed_info['user'] = snapshot['user']
    parsed_info['datetime'] = snapshot['datetime']
    parsed_info['color_image'] = image_info
    return parsed_info
