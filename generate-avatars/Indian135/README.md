# Process

This file takes an email address as an input and processes it.

The email address is hashed using the MD5 hash function. It 
outputs a hexadecimal number of 32 digits. 

The first 3 digits are used to determine the background color 
and the next 3 are used to determine the margin's color. The 
7th digit is used to determine the position of a white colored 
point. The foreground color is always the inverse of 
the background color.

Each digit of the remaining 25 digits decide the shapes to 
be filled in 5x10px blocks which are arranged in the left 
half of the 50x50px image. The left half is then copied, 
flipped and pasted on the right half to complete the image.

The list of shapes is in the 'draw_shape' function, the 
point is drawn in lines 82 to 84, and the margin is drawn in 
line 85. The Pillow library is used to draw the shapes and 
perform functions on images.

# List of inputs and avatars produced:

avatar-1: example@domain.com
avatar-2: arushi@hotmail.com
avatar-3: tankix@yahoo.com
avatar-4: iago@zulip.org
avatar-5: tbnkix@yahoo.com