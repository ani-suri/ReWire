import xml.etree.ElementTree as ET

tree = ET.parse('/Users/anirudh/Downloads/testarticles-xml/TestArticles-2023-Quarter1/testarticles-2023-quarter1.xml')
root = tree.getroot()

for element in root.iter('toxic'):
    # Process and use the element data as needed
    value = element.text
    print(value)

