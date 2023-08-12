import json
import os

path = "../../../iw4x/zonetool/font_test/fonts"


for font in os.listdir(path):
    with open(f"{path}/{font}") as file_2:
        font_json = json.load(file_2)

    for glyph in font_json["glyphs"]:
        if glyph["letter"] > 127:
            try:
                glyph["letter"] = int.from_bytes(chr(glyph["letter"]).encode('gb2312'), "big")
            except:
                print("out of range")
    font_json["glyphCount"] = len(font_json["glyphs"])
    font_json["glyphs"] = sorted(font_json["glyphs"], key=lambda d: d['letter'])
    file_2.close()
    with open(f"{path}/{font}", "w") as file_3:
        json.dump(font_json, file_3, indent=4)