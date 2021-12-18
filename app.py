import json 
import GUI
guion = {}
index = 1
json_object = json.dumps(guion, indent = 4) 
# print(guion)
# print(json_object)
def addElement(diccionario,number,voice,pitch,text):
    diccionario[str(number)]={
        "voice":voice,
        "pitch":int(pitch),
        "text":text
    }
def save():
    with open("sample.json", "w") as outfile:
        json.dump(guion, outfile)

def main():
    GUI.initWindow()
if __name__ == "__main__" : 
    main()
