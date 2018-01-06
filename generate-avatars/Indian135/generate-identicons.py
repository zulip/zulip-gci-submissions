from PIL import Image,ImageDraw
import sys
import hashlib

def draw_shape(x,y,hexa_num,image,color):
    # type: (int,int,str,Image,(int,int,int)) -> None
    num = int(hexa_num,16)
    draw = ImageDraw.Draw(image)
    if num == 0:
        draw.line([x+0,y+0,x+4,y+0],color)
        draw.line([x+4,y+0,x+4,y+9],color)
        draw.line([x+4,y+9,x+0,y+9],color)
        draw.line([x+0,y+9,x+0,y+0],color)
        draw.line([x+1,y+1,x+3,y+1],color)
        draw.line([x+3,y+1,x+3,y+8],color)
        draw.line([x+3,y+8,x+1,y+8],color)
        draw.line([x+1,y+8,x+1,y+1],color)
    elif num == 1:
        draw.line([x+2,y+2,x+2,y+7],color)
    elif num == 2:
        draw.polygon([x,y,x+4,y+4,x+4,y+9,x,y+9],color)
    elif num == 3:
        draw.polygon([x,y+4,x+4,y,x+4,y+9,x,y+9],color)
    elif num == 4:
        draw.polygon([x,y,x+4,y,x+4,y+5,x,y+9],color)
    elif num == 5:
        draw.polygon([x,y,x+4,y,x+4,y+9,x,y+5],color)
    elif num == 6:
        draw.polygon([x,y,x+4,y,x+4,y+2,x,y+2],color)
        draw.polygon([x,y+7,x+4,y+7,x+4,y+9,x,y+9],color)
    elif num == 7:
        draw.polygon([x,y+3,x+4,y+3,x+4,y+6,x,y+6],color)
    elif num == 8:
        draw.line([x+0,y+0,x+0,y+9],color)
        draw.line([x+1,y+0,x+1,y+9],color)
        draw.line([x+3,y+0,x+3,y+9],color)
        draw.line([x+4,y+0,x+4,y+9],color)
    elif num == 9:
        draw.line([x+2,y,x+2,y+9],color)
    elif num == 10:
        draw.polygon([x,y+2,x+4,y+6,x,y+6],color)
    elif num == 11:
        draw.polygon([x+4,y+2,x+4,y+6,x,y+6],color)
    elif num == 12:
        draw.polygon([x,y+2,x+4,y+2,x,y+6],color)
    elif num == 13:
        draw.polygon([x,y+2,x+4,y+2,x+4,y+6],color)
    elif num == 14:
        draw.line([x+0,y+0,x+0,y+9],color)
        draw.line([x+2,y+0,x+2,y+9],color)
        draw.line([x+4,y+0,x+4,y+9],color)
    elif num == 15:
        draw.polygon([x+0,y+0,x+4,y+0,x+4,y+1,x+0,y+1],color)
        draw.polygon([x+0,y+4,x+4,y+4,x+4,y+5,x+0,y+5],color)
        draw.polygon([x+0,y+8,x+4,y+8,x+4,y+9,x+0,y+9],color)

def get_identicon(email_address):
    # (str) -> None
    md5 = hashlib.md5()
    md5.update(email_address.encode('ascii','ignore'))
    hash_code = md5.hexdigest()
    
    bg_color_code = hash_code[:3]
    line_color_code = hash_code[3:6]
    point_code = hash_code[6]
    
    bg_color = (int(bg_color_code[0]+'0',16)+8,int(bg_color_code[1]+'0',16)+8,int(bg_color_code[2]+'0',16)+8)
    fg_color = (255-bg_color[0],255-bg_color[1],255-bg_color[2])
    line_color = (int(line_color_code[0]+'0',16)+8,int(line_color_code[1]+'0',16)+8,int(line_color_code[2]+'0',16)+8)
    identicon = Image.new('RGBA',(50,50),bg_color)
    draw = ImageDraw.Draw(identicon)
    
    x,y = 0,0
    for i in range(7,32,1):
        draw_shape(x,y,hash_code[i],identicon,fg_color)
        x = x + 5
        if x >= 25:
            x = 0
            y = y + 10
    copy = identicon.crop((0,0,25,50))
    identicon.paste(copy.transpose(Image.FLIP_LEFT_RIGHT),(25,0))
    point = int(point_code,16)
    y = 3*point
    draw.point([24,y,25,y,25,y+1,24,y+1],'white')
    draw.line([0,0,49,0,49,0,49,49,49,49,0,49,0,49,0,0,1,1,48,1,48,1,48,48,48,48,1,48,1,48,1,1],line_color)
    identicon.save(email_address + '.png')

get_identicon(sys.argv[1])
