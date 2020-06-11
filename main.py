import sys
from typing import List
try:
    from PyPDF2 import PdfFileReader
    from PyPDF2.generic import Field
except ImportError:
    print("Please install PyPDF2 e.g. `pip3 install PyPDF2`")
    exit(1)


def readable_type(field: Field) -> str:
    if field.fieldType == "/Tx":
        return "Text"
    elif field.fieldType == "/Ch":
        return "Combo box"
    elif field.fieldType == "/Btn":
        return "Check or Radio box"
    elif field.fieldType == "/Sig":
        return "Signature bx"
    else:
        return "Unknown"


def get_value(field: Field) -> str:
    if field.value is None:
        return ""
    else:
        return field.value


def main(args: List[str]) -> int:
    filename = args[1]
    reader = PdfFileReader(filename)
    fields = reader.getFields()
    for f in fields.keys():
        print(f"Name: '{f}', "
              f"Type: '{readable_type(fields[f])}', "
              f"Value: {get_value(fields[f])}")
    return 0


if __name__ == "__main__":
    exit(main(sys.argv))
