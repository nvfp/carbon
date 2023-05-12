

def interpolate_color(color1: str, color2: str, x: float) -> str:
    """
    Interpolates between two colors based on the given ratio `x`.

    ---

    ## Params
        - `color1`: The first color in hexadecimal format (e.g., '#RRGGBB').
        - `color2`: The second color in hexadecimal format (e.g., '#RRGGBB').
        - `x`: The ratio determining the interpolation between the two colors. Should be between 0 and 1.

    ## Returns
        - The interpolated color as a hexadecimal string.

    ## Demo
        >>> interpolate_color('#ff0000', '#0000ff', 0.0)
        '#ff0000'
        >>> interpolate_color('#ff0000', '#0000ff', 0.5)
        '#7f007f'
        >>> interpolate_color('#ff0000', '#0000ff', 1.0)
        '#0000ff'
    """
    ## convert color strings to RGB values
    r1, g1, b1 = int(color1[1:3], 16), int(color1[3:5], 16), int(color1[5:7], 16)
    r2, g2, b2 = int(color2[1:3], 16), int(color2[3:5], 16), int(color2[5:7], 16)

    ## interpolate RGB values based on x
    r = int(r1 + (r2 - r1)*x)
    g = int(g1 + (g2 - g1)*x)
    b = int(b1 + (b2 - b1)*x)

    ## convert interpolated RGB values to hexadecimal color string
    interpolated_color = f'#{r:02x}{g:02x}{b:02x}'
    return interpolated_color