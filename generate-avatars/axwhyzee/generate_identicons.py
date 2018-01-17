from PIL import Image

###################
## Picture class ##
###################

class Picture(object):
    def __init__(self):
        self._mode = 'RGB'
        self._size = (50,50)
        self._background_color = 'white'
        self._img = Image.new(self._mode, self._size, self._background_color)

    # change the color of a specified block of pixels
    def make_tile(self, color, index):
        
        # tiles are numbered from 0 to 50
        def coord(index):
            
            # wrap around to next row of tiles
            return ((index * 5) % 50, ((index * 5) // 50) * 5) 

        # coordinates of upper left pixel of the tile is found using coord() function
        upper_left = coord(index) 
        #since we are making a 50 X 50px icon, and there are 5 tiles, each tile will be 5 X 5px
        for y in range(5):
            for x in range(5):
                self._img.putpixel((upper_left[0] + x, upper_left[1] + y), color) #putpixel(coordinate(x,y), color(R,G,B))

    def show(self):
        self._img.show()

    def save(self, name):
        self._img.save(name)
        
#############
## Hashing ##
#############

# inverts a string
def invert(string):
    output = ''
    for char in string:
        output = char + output
    return output

# generates a denary int value
def to_denary(num, base):
    output = 0
    count = - len(num)
    while count < 0:      
        output += int(num[count]) * (base ** abs(count + 1))
        count += 1

    return int(output)

# generates an inverted binary string with leading '0's behind to make it 64-bit long
def to_inverted_binary(num):
    output = ''
    while num > 0:
        remainder = num % 2
        num = num // 2 
        output += str(remainder)

    return "{:0<64}".format(output)

# generates a 64-bit hash 
def get_hash(data):
    # start key needs to be 64-bits long so value must not exceed the max value of a 64-bit string
    start_key = len(data) 
    while start_key < 2**16 - len(data):
        
        start_key = (start_key)**2 + len(data)
           
    key = to_inverted_binary(start_key)[:32] + invert(to_inverted_binary(start_key)[:32])

    for char in data:        
        # 131 is chosen since it is the smallest prime number after 128, the max value of ASCII code
        # by using 1.31, a 'random looking', long and unique decimal string can be generated
        # since all float values of 1.31 / ord(char) always starts with 0.0XXX, the 0.0 is removed since it becomes insignicant
        # binary value of 1.31 / ord(char) is inverted so that it no longer follows a sequence even if the characters are ordered in sequence, E.g. abcdefg or 12345
        new_char = to_inverted_binary(int(str(1.31 / ord(char))[3:]))
        temp_key = ''
        
        # invert the digits of the key with new_char
        for index in range(len(new_char)):
            if key[index] == '1':
                if new_char[index] == '1':
                    temp_key += '0'
                else:
                    temp_key += '1'
            else:
                temp_key += new_char[index]
                
        # key needs to keep changing on its own
        # because if the input is made up of the same exact character,
        # then new_char for each loop will always be the same.
        # This causes the key to keep alternating between 2 constant values
        key = temp_key[-1] + temp_key[:63] 

    return key

#########################
## Translation of hash ##
#########################

def translate_hash_to_pic(hash_val, file_name = None):
    p1 = Picture()
    flip_tile = hash_val[:50]
    color = to_denary(hash_val[50:], 2)

    color = color % 3
    RGB = ()
    for i in range(3):
        if i == color:
            RGB += (250,)
        else:
            RGB += (0,)

    row = 0
    column = 0
    for count in range(len(flip_tile)):
        index = (row * 10) + (column % 5)
        if flip_tile[count] == '1':
            # make tile on left side of square
            p1.make_tile(RGB, index)

            # reflect to other side of square
            p1.make_tile(RGB, (9 - column) + (10 * row))

        row += (column + 1) // 5
        column = (column + 1) % 5 

    #p1.show()

    if file_name:
        p1.save(file_name)

def read_file():
    data = ''
    file_name = None
    with open('input_data.txt','r') as f:
        line = True
        while line:
            line = f.readline()
            if len(line) > 0 and line[0] == '#':
                data += line[1:-1]
            elif len(line) > 0 and line[0] == '@':
                file_name = line[1:-1].strip()
                
                # word count limit = 64
                if 0 < len(data) < 64:
                    hash_value = get_hash(data)
                    translate_hash_to_pic(hash_value, file_name)
                    data = ''
                    file_name = None

read_file()

