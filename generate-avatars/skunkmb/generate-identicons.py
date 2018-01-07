'''Generates a 50-50 PNG image using a SHA256. Any amount of inputs can be
used to generate the identicon. If more than 1 input is used, the inputs are
summed together and then hashed.
'''

import sys
import hashlib
from PIL import Image, ImageDraw, ImageFilter, ImageOps


'''The image's size (horizontal and vertical), in pixels.
'''
SIZE = 50

# This is currently set to 0, but could be changed to change the style.
'''The amount of pixels that a point can go outisde of the image's frame (so
that lines don't have to end inside the image).
'''
OUSIDE_SIZE = 0

'''The amount of shapes to include in the image.
'''
SHAPES_AMOUNT = 5

'''The amount of points/sides for each shape in an image.
'''
POINTS_AMOUNT = 12

# Multiply by 2 because there is both x and y, and 6 to the section size for
# the shape color.
'''The amount of characters in the hash needed for each shape.
'''
shape_hash_section_size = 6 + 2 * POINTS_AMOUNT

'''The assumed size of an individual hash's hex digest.
'''
ONE_HASH_SIZE = 64

'''The amount of hashes generated in total, since using only 1 would be too
small. Each hash after #1 is generated using the previous hash's hex digest.
'''
HASHES_AMOUNT = 5

'''The amount of characters in the combined hash.
'''
combo_hash_size = ONE_HASH_SIZE * HASHES_AMOUNT

# Add 6 to the total for the background color.
'''The required size of the combined hash.
'''
required_hash_size = 6 + SHAPES_AMOUNT * shape_hash_section_size


if combo_hash_size < required_hash_size:
    print((
        'Error: there is not enough space in the hash for those settings.\n\n'
        'Your settings would require a hash length of {} but only {} '
        'characters are available.'
    ).format(required_hash_size, combo_hash_size))
    sys.exit()

def sum_hashes(hashes):
    '''Sums together multiple hexadecimal hash digests and hashes the sum with
    SHA-256.

    Parameters:
     - hashes ([str]): The hash digests.

    Returns (int): The hashed sum.
    '''
    # Convert the hashes to `int`s.
    hash_ints = [int(hash_digest, 16) for hash_digest in hashes]

    combined = 0

    for hash_int in hash_ints:
        combined += hash_int

    # Hash the combined amount and return it.
    return hashlib.sha256(hex(combined).encode('utf8')).hexdigest()

def make_additional_hashes(amount, start_hash):
    '''Creates additional hashes based on a starting hash's hexadecimal digest.
    The starting hash is hashed again using SHA-256, then the result is
    hashed again, etc.

    Parameters:
     - amount (int): The number of hashes to make, including the starting hash.
     - start_hash (str): The hash digest to start with.

    Returns ([str]): The hashes' digests.
    '''
    additional_hashes = [start_hash]

    # Start at 1 because the `start_hash` is at index 0.
    for i in range(1, amount):
        last_hash = additional_hashes[-1]
        hash_of_last_hash = hashlib.sha256(last_hash.encode('utf8')).hexdigest()
        additional_hashes.append(hash_of_last_hash)

    return additional_hashes

def draw_shape(image_draw, hash_digest, shape_num):
    '''Draws a shape on an `ImageDraw`. The global variables
    `shape_hash_section_size`, `SIZE`, and `OUSIDE_SIZE` are used to calculate
    the number of points in the polygon and where they should go.

    Parameters:
     - image_draw (`ImageDraw`): The Pillow `ImageDraw` object.
     - hash_digest (str): The hexadecimal hash digest to use to make the shape.
     - shape_num (int): The number of the shape that's being made.
    '''
    # Add 6 because the first 6 characters are used for the background color.
    start_hash_index = 6 + shape_num * shape_hash_section_size
    end_hash_index = start_hash_index + shape_hash_section_size
    hash_section = hash_digest[start_hash_index:(end_hash_index + 1)]

    coordinates = []

    # Start at 6 because the first 6 characters are used for the shape color.
    for i in range(6, shape_hash_section_size, 2):
        # Multiply the outside size by 2 so that it is applied to both sides,
        # and then subtract the outside size to the location so that it is
        # "centered" based on the 2x applied before.
        coordinates.append((
            (int(hash_section[i], 16) / 16) * (SIZE + 2 * OUSIDE_SIZE) - OUSIDE_SIZE,
            (int(hash_section[i + 1], 16) / 16) * (SIZE + 2 * OUSIDE_SIZE) - OUSIDE_SIZE
        ))

    image_draw.polygon(coordinates, None, '#' + hash_section[0:6])

args = sys.argv[1:]
hashed_vals = [hashlib.sha256(arg.encode('utf8')).hexdigest() for arg in args]
hash_sum = sum_hashes(hashed_vals)

hashes_combo = ''.join(make_additional_hashes(HASHES_AMOUNT, hash_sum))

image = Image.new('RGB', (SIZE, SIZE), '#' + hashes_combo[0:6])
image_draw = ImageDraw.Draw(image)

for i in range(SHAPES_AMOUNT):
    draw_shape(image_draw, hashes_combo, i)

image = image.filter(ImageFilter.MedianFilter(9))
image = ImageOps.solarize(image, 100)

image.save('output.png', "PNG")
