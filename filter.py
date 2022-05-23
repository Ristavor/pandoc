import sys
from panflute import *


def filtering(element, document):
    headers = {}
    if type(element) == Header:
        elem_as_str = stringify(element)
        if elem_as_str in headers.keys():
            if headers.get(elem_as_str) == element.level:
                sys.stderr.write("This element is repeated. Level: " + str(element.level) + ", header: \"" +
                                 stringify(element) + "\"\n")
        else:
            headers[elem_as_str] = element.level

        if element.level <= 3:
            return Header(Str(elem_as_str.upper()), level=element.level)

    if type(element) == Str and str(element.text).lower() == "bold":
        return Strong(Str(element.text))


def main(document=None):
    return run_filter(filtering, doc=document)


if __name__ == '__main__':
    main()
