# @skunkmb's Identicon Project

## Approach

The following steps are followed when creating the identicon:

 1. Hash every argument provided to the file using `SHA-256`.
 2. Convert the hexadecimal digests to integers and sum the hashes together.
 3. Hash that combined sum to get a final hex digest to use throughout the rest
    of the program.
 4. Use the first `6` digits of the hash as the RGB color hex code for the
    background.
 5. Take the next `6` digits to find the color for the first shape.
 6. Use the next `24` digits to create `12` points on the image (each point
    using a digit for `x` and a digit for `y`), and outline that shape with the
    color from step 5.
 7. Repeat steps #5 and #6 4 more times for a total of `5` shapes.
 8. Use a `median` filter with a kernel size of `9` to make the image more
    aesthetically appealing.
 9. Finally, `solarize` the image with a threshold of `100`.

## Examples:

 - [avatar-1](avatar-1.png): `Zulip`
 - [avatar-2](avatar-2.png): `skunkmb`
 - [avatar-3](avatar-3.png): `someone@example.com`
 - [avatar-4](avatar-4.png): `Google Code-In`
 - [avatar-5](avatar-5.png): `🐙`
