inp = open("SongBook\\vse_akordy(1).txt", "r", encoding="UTF-8")
outp = open("SongBook\\outp.txt", "w", encoding="UTF-8")

inp = inp.read()
inp = inp.split("\"song\"")



reqested = ["songName", "songAuthor", "sectionName", "chordName", "text"]
toReplace = ["\"", "\n", "\t", "class="]

for i in inp[1:]:
    songs = {"songName": "",
             "songAuthor": "",
             "text": ""
             }
    for line in i.split("\n"):
        for rep in toReplace:
            line = line.replace(rep, "")
        for req in reqested:
            if line.find(req) != -1:
                
                line = line[line.find(">") + 1 : ]
                line = line[ : line.find("<")]

                if req in ["songName", "songAuthor"]:
                    songs[str(req)] = str(line)
                else:
                    songs["text"] += "[" + str(line) + "]" if req == "chordName" else "{" + str(line) + "}" if req == "chordName" else str(line)
                
    print(str(songs), file=outp)


"""file = file.replace("\t", "")

file = file.replace("<table>\n", "")
file = file.replace("</table>", "")

file = file.replace("<tr>\n", "")
file = file.replace("</tr>\n", "")

file = file.replace("<td class=\"chordName\">", "[")
file = file.replace("</td>\n<td>", "]\n<td>")

file = file.replace("<td>\n", "")
file = file.replace("</td>\n", "")
file = file.replace("<td>\n", "")

songs = file.split("</div><div class=\"song\">\n")

def getStr(base: str, fromString: str, toString: str) -> str:
    StringNotFoundError = "FromString or ToString not found"

    posOfStartString = base.find(fromString)
    posOfEndString = base[posOfStartString + len(fromString):].find(toString) + posOfStartString + len(fromString)
    posOfReturnString = 0

    if (posOfEndString == -1 or posOfEndString == -1):
        raise StringNotFoundError

    posOfReturnString = posOfStartString + len(fromString)
    
    outputString = base[posOfReturnString:posOfEndString]
    return outputString

#print(songs[len(songs)-1])
"""

"""songs = file.split("</div><div class=\"song\">\n")
for song in songs:
    print(song)

    songName = getStr(base = song, fromString = "songName\">", toString = "</div>")
    song = song[song.find("<div class=\"section\">"):]
    print(f"songName = {songName}", file=outp)
    for section in song.split("</div><div class=\"section\">\n"):
        sectionName = getStr(base = section, fromString = "sectionName\">", toString = "</div>")
        print(f"sectionName = {sectionName}", file=outp)
        print(section, file=outp)
        #print(section + "\n\n\n")

    break
    #print(f"songAuthor = {getStr(base = song, fromString = "songAuthor\">", toString = "</div>")}")
    #print(getStr(base = file, fromString = "sectionName\">", toString = "</div>"))
    #print(getStr(base = file, fromString = "<td class=\"chordName\">", toString = "</td>"))
    #print(getStr(base = file, fromString = "songName\">", toString = "songName\">"))"""