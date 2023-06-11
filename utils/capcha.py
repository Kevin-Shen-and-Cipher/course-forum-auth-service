import ddddocr


def identify_capcha(image):
    ocr = ddddocr.DdddOcr()
    try:
        capcha = ocr.classification(image)
    except Exception as error:
        print(error)
        capcha = ""
    return capcha
