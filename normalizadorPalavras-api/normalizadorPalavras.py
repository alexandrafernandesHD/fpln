from lxml import etree

f = open( 'testamento.xml',"r", encoding="utf-8")
tree = etree.parse(f)

#for folha in tree.findall("//orig"):
  #  folha.tag = "sub"
for folha in tree.findall("//reg"):
    folha.tag = "sup"

tree.write("out.html", method="html", encoding="utf-8")

#with open ("out.html", "w",encoding="utf8") as out:
  #  print(etree.)

#print(a.text)

#print(tree)
#print(tree.find("//orig").text)
#print(tree.find("//orig").tag)
#a= tree.find("//orig")
#a.tag = "batatas"
#print(a.tag)
