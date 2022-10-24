import json
import os
PN = 1
OTLP = open("./PL.txt", "w")
PFT = open("./STIC.txt","r")
PFD = str(PFT.read())
PF1 = open(str(PFD + "\\STIPrompt.jet"))
PF = PF1.read()
PF1.close()
while PN != 188:
    PFJ = json.loads(PF)
    PFJ = PFJ["content"]
    P = PFJ[PN]
    PP = P["prompt"]
    PPT = PP["text"]
    OTLP.write(str(PPT + "\n"))
    PN = PN + 1
