from xml.etree import ElementTree

tree = ElementTree.parse("XML_Example.xml")
root = tree.getroot()
# use root to parse from str

# print(root)
# print(root.tag, root.attrib)

# for child in root:
#     print(child.tag, child.attrib)

# for element in root.iter('scores'):
#     score_sum = 0
#     for child in element:
#         score_sum += float(child.text)
#     print(score_sum)

greg = root[0]
module1 = next(greg.iter('module1'))
print(module1, module1.text)
module1.text = str(float(module1.text) + 30)

tree.write("example_modified.xml")