import argparse
import cv2
import math


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("image", help="path to the image to be converted")
    parser.add_argument("ratio", type=int, help="x = one character for each block of x by x pixels")
    return parser


def main(args):
    array = [32, 46, 44, 39, 96, 34, 45, 126, 58, 95, 59, 43, 124, 94, 47, 92, 105, 114, 118, 121, 61, 106, 33, 40, 41,
             108, 60, 62, 84, 116, 73, 76, 89, 91, 93, 99, 102, 110, 74, 120, 122, 123, 125, 55, 117, 49, 63, 115, 37,
             42, 86, 88, 111, 107, 104, 119, 67, 70, 101, 112, 113, 35, 38, 65, 90, 109, 85, 97, 79, 36, 52, 80, 98,
             100, 72, 75, 103, 71, 68, 69, 81, 83, 87, 50, 51, 54, 57, 78, 53, 77, 82, 48, 56, 66, 64]
    img = cv2.imread(args.image, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"unable to find : {args.image}")
        return
    f = open("res.txt", "w")
    if f is None:
        print(f"unable to create : res.txt")
        return
    width = int(img.shape[1] / args.ratio)
    height = int(img.shape[0] / args.ratio)
    print(f"(width, height) : ({width}, {height})")
    img_resized = cv2.resize(img, (width, height))
    for i in range(height):
        for j in range(width):
            lower_bound = 0
            upper_bound = 1 / 95
            for k in range(95):
                if lower_bound < 1 - img_resized[i][j] / 255 <= upper_bound:
                    f.write(chr(array[k]))
                    break
                lower_bound = upper_bound
                upper_bound += 1/95
        f.write('\n')


if __name__ == "__main__":
    args = make_parser().parse_args()
    main(args)
