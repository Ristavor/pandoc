import sys
from panflute import *

headers = {}


def filtering(element, document):
    if type(element) == Header:
        elem_as_str = stringify(element)
        if elem_as_str in headers.keys() and headers.get(elem_as_str)[0] == element.level:
            headers.get(elem_as_str)[1] += 1
            if headers.get(elem_as_str)[1] == 2:  # сообщение о повторе только 1 раз
                sys.stderr.write("This element is repeated. Level: " + str(element.level) + ", header: \"" +
                                 stringify(element) + "\"\n")

        else:
            headers[elem_as_str] = [element.level, 1]

        if element.level <= 3:
            return Header(Str(elem_as_str.upper()), level=element.level)

    if type(element) == Str and str(element.text).lower() == "bold":
        return Strong(Str(element.text))


def main(document=None):
    return run_filter(filtering, doc=document)


if __name__ == '__main__':
    main()
