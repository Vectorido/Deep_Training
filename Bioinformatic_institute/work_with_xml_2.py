from xml.etree import ElementTree

tree = ElementTree.parse("example_modified.xml")
root = tree.getroot()

greg = root[0]

# certificate = greg[2]
# certificate.set("type", "with distinction")
#
# tree.write("example_modified.xml")

description = ElementTree.Element("description")
description.text = "Showed excellent skills during the course"
greg.append(description)
greg.remove(description)

tree.write("example_modified.xml")