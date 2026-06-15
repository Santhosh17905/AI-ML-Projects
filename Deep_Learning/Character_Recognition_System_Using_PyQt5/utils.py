import cv2
import numpy as np


def preprocess_character(image_path):

    img = cv2.imread(
        image_path,
        cv2.IMREAD_GRAYSCALE
    )

    if img is None:
        raise ValueError(
            "Unable to load image."
        )

    _, thresh = cv2.threshold(
        img,
        30,
        255,
        cv2.THRESH_BINARY
    )

    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if len(contours) == 0:

        img = cv2.resize(
            thresh,
            (28, 28)
        )

    else:

        contour = max(
            contours,
            key=cv2.contourArea
        )

        x, y, w, h = cv2.boundingRect(
            contour
        )

        roi = thresh[
            y:y+h,
            x:x+w
        ]

        canvas = np.zeros(
            (28, 28),
            dtype=np.uint8
        )

        roi = cv2.resize(
            roi,
            (20, 20)
        )

        canvas[
            4:24,
            4:24
        ] = roi

        img = canvas

    img = np.rot90(img)
    img = np.fliplr(img)

    img = img.astype(
        "float32"
    ) / 255.0

    img = img.reshape(
        1,
        28,
        28,
        1
    )

    return img