from gingerit.gingerit import GingerIt

text = "I is Happy"
parser = GingerIt()
print(parser.parse(text)["result"])