import io
from lxml import etree


def parse(text_or_bytes):
    if isinstance(text_or_bytes, str):
        text_or_bytes = text_or_bytes.encode("utf-8")

    parser = etree.XMLParser(encoding="UTF-8")
    return etree.parse(io.BytesIO(text_or_bytes), parser)


# Main

sample_xml = """<?xml version="1.0"?>
<root>
    <child>Hello, World!</child>
</root>"""

tree = parse(sample_xml)
root = tree.getroot()
print(etree.tostring(root, pretty_print=True).decode("utf-8"))
