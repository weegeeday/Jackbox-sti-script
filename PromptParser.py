import json
import os
import time
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
        OTLPE = open("./PLE.txt", "w")
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
            OTLPE.write(str(PPT + "\n"))
            PN = PN + 1       
    
    @staticmethod
    def write():
        global PF
        global PP
        global P
        global PFJ
        global PFJ2
        PN = 0  
        PELF = open("./PLE.txt","r")
        PEL = PELF.readlines()
        try:
            NPF = open("./STIContent to put in content/STIPrompt.jet","x")
        except FileExistsError:
            os.remove("./STIContent to put in content/STIPrompt.jet")
            time.sleep(2)
            NPF = open("./STIContent to put in content/STIPrompt.jet","x")
        P = PFJ[PN]
        PP = P["prompt"]
        PPT = str(PEL[PN]).rstrip("\n")
        PP["text"] = {"text": str(PPT)}
        print("PP['text'] = " + str(PP["text"]))
        P["prompt"] = PP["text"]
        PFJ[PN] = P
        PFJ2["content"] = PFJ
        PFJ = PFJ2["content"]
        #loop after first time writing a prompt
        PN = PN + 1
        while PN != 187:
            P = PFJ[PN]
            PP = P["prompt"]
            PPT = str(PEL[PN]).rstrip("\n")
            PP["text"] = {"text": str(PPT)}
            print("PP['text'] = " + str(PP["text"]))
            P["prompt"] = PP["text"]
            PFJ[PN] = P
            PFJ2["content"] = PFJ
            PFJ = PFJ2["content"]
            PN = PN + 1
        #write finished file
        json.dump(PFJ2,NPF)
        
PPRun = PromptParser()