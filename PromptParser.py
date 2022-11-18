import json
import os
import time
class PromptParser():
    @staticmethod
    def read():      
        global PF
        global PP
        global P
        global P2
        global P3
        global P4
        global PFJ
        global PFJ2 
        PN = 0
        PFC = 0
        JPE = open("./JPE.txt", "w")
        PPE = open("./PPE.txt","w")
        SPE = open("./SPE.txt", "w")
        OTLPE = open("./PLE.txt", "w")
        PFT = open("./STIC.txt","r")
        PFD = str(PFT.read())
        PF1 = open(str(PFD + "\STIPrompt.jet"))
        PF = PF1.read()
        PF1.close()
        PF2 = open(str(PFD + "\STIJobPrompt.jet"))
        PF3 = PF2.read()
        PF2.close()
        PF4 = open(str(PFD + "\STIPhotoPrompt.jet"))
        PF5 = PF4.read()
        PF4.close()
        PF6 = open(str(PFD + "\STIStorePrompt.jet"))
        PF7 = PF6.read()
        PF6.close()
        while PFC != 3:  
            while PN != 187:
                PFJ = json.loads(PF)
                PFJ2 = PFJ
                PFJ = PFJ["content"]
                P = PFJ[PN]
                PP = P["prompt"]
                PPT = PP["text"]           
                OTLPE.write(str(PPT + "\n"))
                PN = PN + 1
                PFC = PFC + 1
            PN = 0
            while PN != 38:
                PFJ = json.loads(PF3)
                PFJ2 = PFJ
                PFJ = PFJ["content"]
                P2 = PFJ[PN]
                PP = P2["prompt"]
                PPT = PP["text"]           
                JPE.write(str(PPT + "\n"))
                PN = PN + 1
                PFC = PFC + 1
            PN = 0
            while PN != 195:
                PFJ = json.loads(PF5)
                PFJ2 = PFJ
                PFJ = PFJ["content"]
                P3 = PFJ[PN]
                PP = P3["prompt"]
                PPT = PP["text"]           
                PPE.write(str(PPT + "\n"))
                PN = PN + 1
                PFC = PFC + 1
            PN = 0
            while PN != 58:
                PFJ = json.loads(PF7)
                PFJ2 = PFJ
                PFJ = PFJ["content"]
                P4 = PFJ[PN]
                PP = P4["prompt"]
                PPT = PP["text"]           
                SPE.write(str(PPT + "\n"))
                PN = PN + 1
                PFC = PFC + 1

    
    @staticmethod
    def write(SPN):
        global PF
        global PP
        global P
        global P2
        global P3
        global P4
        global PFJ
        global PFJ2
        global SPNS
        if SPN == 1:
            SPNS = P
        if SPN == 2:
            SPNS = P2
        if SPN == 3:
            SPNS = P3
        if SPN == 4:
            SPNS = P4
        PN = 0  
        PELF = open("./PLE.txt","r")
        PEL = PELF.readlines()
        try:
            NPF = open("./STIContent to put in content/STIPrompt.jet","x")
        except FileExistsError:
            os.remove("./STIContent to put in content/STIPrompt.jet")
            time.sleep(2)
            NPF = open("./STIContent to put in content/STIPrompt.jet","x")
        SPNS = PFJ[PN]
        PP = SPNS["prompt"]
        PPT = str(PEL[PN]).rstrip("\n")
        PP["text"] = {"text": str(PPT)}
        print("PP['text'] = " + str(PP["text"]))
        SPNS["prompt"] = PP["text"]
        PFJ[PN] = SPNS
        PFJ2["content"] = PFJ
        PFJ = PFJ2["content"]
        #loop after first time writing a prompt
        PN = PN + 1
        while PN != 187:
            SPNS = PFJ[PN]
            PP = SPNS["prompt"]
            PPT = str(PEL[PN]).rstrip("\n")
            PP["text"] = {"text": str(PPT)}
            print("PP['text'] = " + str(PP["text"]))
            SPNS["prompt"] = PP["text"]
            PFJ[PN] = SPNS
            PFJ2["content"] = PFJ
            PFJ = PFJ2["content"]
            PN = PN + 1
        #write finished file
        json.dump(PFJ2,NPF)
        
PPRun = PromptParser()