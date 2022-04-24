import argparse
import cv2


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("image", help="path to the image to be converted")
    return parser


def main(args):
    image = cv2.imread(args.image, cv2.IMREAD_GRAYSCALE)



if __name__ == "__main__":
    args = make_parser().parse_args()
    main(args)
