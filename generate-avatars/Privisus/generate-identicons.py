'''Generates a unique 50px * 50px .png file from user name

Usage: generate-identicons.py username <useremail>

Keyword arguments:
    username -- User's username in string
    useremail (optional) -- User's email

Returns: void
'''

import sys
import hashlib
import png
from math import sin, cos, tan

#Return the sum of the list with this pattern: + * - //
def unique_sum(val_list):
    sum = 0
    for k, ascii_value in enumerate(val_list):
        if k % 4 == 0:
            sum += ascii_value
        elif k % 4 == 1:
            sum *= ascii_value
        elif k % 4 == 2:
            sum -= ascii_value
        elif k % 4 == 3:
            sum //= ascii_value

    return sum

#create sha-1 instance
sha1 = hashlib.sha1()

#create encoded, utf-8 string from the second argument passed by the user
username_encoded = sys.argv[1].encode('utf-8')

#check if the user supplied more than or equal to three arguments
if len(sys.argv) >= 3:
    #if it does, set the encoded user-email
    useremail_encoded = sys.argv[2].encode('utf-8')
else:
    #if not, use the default encoded user-email
    useremail_encoded = "DEFAULT".encode('utf-8')

#create sha-1 of username
sha1.update(username_encoded)
username_sha1 = sha1.hexdigest()

#create sha-1 of useremail
sha1.update(useremail_encoded) #dependent on the username
useremail_sha1 = sha1.hexdigest()

#convert each character in each string to ASCII value, 
#and summing it with this pattern: + * - //

username_val_list = [ord(character) for character in username_sha1]
useremail_val_list = [ord(character) for character in useremail_sha1]

username_sum = unique_sum(username_val_list)
useremail_sum = unique_sum(useremail_val_list)

#figure out the trig values for the half of the icon
if useremail_sum % 3 == 0:
    trig_values = [sin((useremail_sum**2+1)*x+useremail_sum) for x in range(0,2500//4)]
elif useremail_sum % 3 == 1:
    trig_values = [cos((useremail_sum**2+1)*x+useremail_sum) for x in range(0,2500//4)]
elif useremail_sum % 3 == 2:
    trig_values = [tan((useremail_sum**2+1)*x+useremail_sum) for x in range(0,2500//4)]

grid_locations = []

#This can be simplified with list comprehension, but I decided to left it this way for readability
for trig_value in trig_values:
    q1 = round(255 * sin(username_sum * (useremail_sum * trig_value)))
    q2 = round(255 * sin(useremail_sum))
    
    if q1 == 0:
        q1 = 1

    if q2 == 0:
        q2 = 1

    k = round(q1) % round(q2)

    if k >= 25 and k < 100:
        k = 100
        
    if k >= 100 and k < 200:
        k = 200
        
    if k > 200:
        k = 100
    
    grid_locations.append(k)

#check if the list is generally dull, if it is, contrast it
if sum(grid_locations) < 25*25*100:
    average_light = 255 * sum(grid_locations) // (25*25*100)
    
    grid_fix_dull = []
    
    for color in grid_locations:
        if color < average_light:
            grid_fix_dull.append(255-average_light)
        else:
            grid_fix_dull.append((color*2) % 256)
    
    grid_locations = grid_fix_dull

if sum(grid_locations) < 25*25*100:
    grid_locations = [255-color for color in grid_locations]

#split the list into chunk of 25 ints, which will be mirrored in the next steps
grid_squared = [grid_locations[x:x+25] for x in range(0, len(grid_locations),25)]

grid_rgb = []

color_decide = (username_sum+useremail_sum) % 3

for row in grid_squared:
    rgb_row = []
    for light in row:
        if color_decide == 0:
            rgb_row.extend([light, light//2, light//3])
        elif color_decide == 1:
            rgb_row.extend([light//2, light , light//3])
        elif color_decide == 2:
            rgb_row.extend([light//2, light//3, light])
    grid_rgb.append(rgb_row)

#for each list, add a mirror list so it is symetrical with the respect to y axis
grid_rgb = [grid+grid[::-1] for grid in grid_rgb]

#for each list, add a mirror list so it is symetrical with the respect to x axis
grid_rgb = grid_rgb + grid_rgb[::-1]

#put the image and save it
png.from_array(grid_rgb, 'RGB').save(sys.argv[1] + ".png")

