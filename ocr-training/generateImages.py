from PIL import Image, ImageFont, ImageDraw
import os
import typing


def imageFromText(
    text: list[str],
    lineHeight: int,
    textSize: int,
    shape: tuple[int, int] = (200, 200),
    origin: tuple[int, int] = (10, 10),
) -> None:
    """Creates training images for a certain font.

    Args:
        text (list[str]): List of text strings
        lineHeight (int): pt height of each line
        textSize (int): pt size of text
        shape (tuple[int, int], optional): Canvas Shape. Defaults to (200, 200).
        origin (tuple[int, int], optional): Position of top left corner of text box. Defaults to (10, 10).
    """

    img = Image.new("RGB", shape, color="black")
    font = ImageFont.truetype("../assets/supercell-magic/supercell-magic.ttf", textSize)
    d = ImageDraw.Draw(img)

    for i, txt in enumerate(text):
        d.text(
            (origin[0], (origin[1] + (i * lineHeight))),
            txt,
            font=font,
            fill=(255, 255, 255),
        )

    img.show()


if __name__ == "__main__":
    text = ["1 104 305", "4 775", "1 748 963", "None", "Attack!"]
    lineHeight = 36
    textSize = 36
    shape = (200, 200)
    origin = (20, 10)

    imageFromText(text, lineHeight, textSize, shape, origin)
