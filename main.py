import argparse
import cv2
import numpy as np


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("image", help="path to the image to be converted")
    return parser


def main(args):
    img = cv2.imread(args.image, cv2.IMREAD_GRAYSCALE)
    if img is None:
        return
    new_height = img.shape[1]
    new_width = int(img.shape[1] * 8 / 6)
    img_resized = cv2.resize(img, (new_height, new_height))
    for i in range(new_height):
        for j in range(new_width):
            pxl_val = img_resized[i][j]
            pxl_val = pxl_val / 256
            if 0.0 <= pxl_val < 0.1:
                print('.', end='')
            elif 0.1 <= pxl_val < 0.2:
                print(',', end='')
            elif 0.2 <= pxl_val < 0.3:
                print(';', end='')
            elif 0.3 <= pxl_val < 0.4:
                print('!', end='')
            elif 0.4 <= pxl_val < 0.5:
                print('v', end='')
            elif 0.5 <= pxl_val < 0.6:
                print('l', end='')
            elif 0.6 <= pxl_val < 0.7:
                print('L', end='')
            elif 0.7 <= pxl_val < 0.8:
                print('F', end='')
            elif 0.8 <= pxl_val < 0.9:
                print('E', end='')
            else:
                print('$', end='')
        print('')


if __name__ == "__main__":
    args = make_parser().parse_args()
    main(args)
