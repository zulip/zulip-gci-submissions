Task B-generate identicons

========================
  1. Structure of icon 

Size of icons are 50 x 50px.
Each icon is made up of 100 tiles (10 x 10), where each tile is 5 x 5 px. The tiles are numbered 0-99 as shown below.

=======================================

  0   1   2   3   4   5   6   7   8   9   
 10  11  12  13  14  15  16  17  18  19  
 20  21  22  23  24  25  26  27  28  29  
 30  31  32  33  34  35  36  37  38  39  
 40  41  42  43  44  45  46  47  48  49  
 50  51  52  53  54  55  56  57  58  59  
 60  61  62  63  64  65  66  67  68  69  
 70  71  72  73  74  75  76  77  78  79  
 80  81  82  83  84  85  86  87  88  89  
 90  91  92  93  94  95  96  97  98  99  
 
=======================================

3. Each icon is symmetrical. Therefore, only half of the icon (columns 1 2 3 4 5) needs to be generated. 

==Generating the hash==

Firstly, using a few mathematical operations, a basic starting key is generated.
As the function loops through each char in the data input, the current char is represented by the value of 1.31 / ord(char) in binary form. 
1.31 is used since its the closest prime number that comes after 128. 
The purpose of using a prime number is to generate a 'random looking' and long decimal string. 
The binary string is then inverted so that even if the input data is a string like 'abcd', the binary value won't follow any sequence. 
Refer to the illustration below:


1.31 / 97 = 0.013505154639175258
1.31 / 98 = 0.013367346938775511
1.31 / 99 = 0.013232323232323233
1.31 / 100 = 0.0131

~inverting the results gives

852571936451505310.0
115577839643763310.0
332323232323232310.0
1310.0

~which follows no order


Next, the xor value of the starting key and the binary string becomes a new 'key'. 
The key then undergoes a circular shift to the left. 
The purpose of doing so is because if the data input is a string containing the exact same values, such as 'aaaaaa', the binary string of each char in the data input will always be the same. Therefore if the value of the key does not keep changing, the key will end up alternating between the same 2 values constantly. However, because of the circular shift, the hash value of any input data with a length that is a multiple of 64 will always be either the same as the starting key, or the xor value of the starting key. Therefore a word limit of 64 is placed. 

The xor value of the 'key' and the binary string of the next char in the data input then replaces the old 'key' to become a new 'key'
Loop continues until the entire data input string is exhausted

The final version of the key becomes a 64-bit hash value.

=======================================
  2.Translating the hash to a picture 

Half of the icon takes up half of 10 x 10 which equals to 5 x 10 tiles = 50 tiles
The first 50 bits of the hash value is used to determine where tiles are placed in the icon. 
To do this, a for loop runs through the 50 bits, and if the current bit is a '1', a tile is placed in the corresponding position in the left half of the square. 
It is then reflected to the other side of the square so the icon is complete.

As for the coloration of the tiles, a RGB value is generated based on the last 14-bits of the hash value.
Simply take modulo 3 of the denary value of the last 14-bits to determine which of the 3 colors R, G, or B is used

After the color is picked, the colored tiles are generated using the Python Imaging Library (PIL) to form an icon.

========================
  3.Running the script

Enter input data values into the file 'input_data.txt' according to the format below:

1) To input a data, write #<data>
Note: no spaces between # and <data>. # must be on the very first letter. Do not leave a space on the left of the hastag. Enter as many lines of data as you like, but do not exceed the 64 word limit.

2) To save the icon as <filename>, write @<filename> 
Note: Include file name extensions in the filename E.g. 'avatar-1.png'

3) Save the input_data.txt file and double click generate_identicons.py to generate the icons








