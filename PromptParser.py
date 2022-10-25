import json
import os

class PromptParser():
    @staticmethod
    def read():
        global PF
        global PP
        global P
        global PFJ
        global PFJ2       
        PN = 0
        OTLP = open("./PL.txt", "w")
        PFT = open("./STIC.txt","r")
        PFD = str(PFT.read())
        PF1 = open(str(PFD + "\STIPrompt.jet"))
        PF = PF1.read()
        PF1.close()
        while PN != 187:
            PFJ = json.loads(PF)
            PFJ2 = PFJ
            PFJ = PFJ["content"]
            P = PFJ[PN]
            PP = P["prompt"]
            PPT = PP["text"]           
            OTLP.write(str(PPT + "\n"))
            PN = PN + 1       
    @staticmethod
    def write(NPPT,PN):  
        NPF = open("./STIContent to put in content/STIPrompt.jet","x")
        PP["text"] = NPPT
        print("PP[]=" + str(PP["text"]) + "PP=" + str(PP))
        P["prompt"] = PP["text"]
        print("P[]=" + str(P["prompt"]) + "P=" + str(P))
        PFJ[PN] = P
        print("PFJ[]=" + str(PFJ[PN]) + "PFJ=" + str(PFJ))
        PFJ2["content"] = PFJ
        json.dump(PFJ2,NPF)

PPRun = PromptParser()