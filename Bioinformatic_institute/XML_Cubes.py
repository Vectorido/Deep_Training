from xml.etree import ElementTree as ET


class MaxDepth:
    color_list = [0, 0, 0]
    maxDepth = 0
    depth = 0

    def start(self, tag, attrib):
        self.depth += 1
        if self.depth > self.maxDepth:
            self.maxDepth = self.depth
        if attrib['color'] == 'red':
            MaxDepth.color_list[0] += (1 * self.depth)
        elif attrib['color'] == 'green':
            MaxDepth.color_list[1] += (1 * self.depth)
        else:
            MaxDepth.color_list[2] += (1 * self.depth)

    def end(self, tag):
        self.depth -= 1

    def data(self, data):
        pass

    def close(self):
        return MaxDepth.color_list


parser = ET.XMLParser(target=MaxDepth())

parser.feed(input())
print(*parser.close())
