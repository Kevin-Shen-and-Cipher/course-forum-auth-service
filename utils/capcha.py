import ddddocr


def identify_capcha(image):
    ocr = ddddocr.DdddOcr()
    return ocr.classification(image)
