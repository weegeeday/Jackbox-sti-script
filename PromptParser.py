import json
import os
import time 
class PromptParser:
    
    def __init__(self):
        self.P = None
        self.P2 = None
        self.P3 = None
        self.P4 = None

    @staticmethod
    def read():      
        global PF
        global PP
        global PFJ
        global PFJ2
        print("read timePE")
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
                global P
                PFJ = json.loads(PF)
                PFJ2 = PFJ
                PFJ = PFJ["content"]
                PPRun.P = PFJ[PN]
                PP = PPRun.P["prompt"]
                PPT = PP["text"]           
                OTLPE.write(str(PPT + "\n"))
                PN = PN + 1
                PFC = PFC + 1
                print("PFC=" + str(PFC))
            PN = 0
            while PN != 38:
                global P2
                PFJ = json.loads(PF3)
                PFJ2 = PFJ
                PFJ = PFJ["content"]
                PPRun.P2 = PFJ[PN]
                PP = PPRun.P2["prompt"]
                PPT = PP["text"]           
                JPE.write(str(PPT + "\n"))
                PN = PN + 1
                PFC = PFC + 1
                print("PFC=" + str(PFC))
            PN = 0
            while PN != 195:
                global P3
                PFJ = json.loads(PF5)
                PFJ2 = PFJ
                PFJ = PFJ["content"]
                PPRun.P3 = PFJ[PN]
                PP = PPRun.P3["prompt"]
                PPT = PP["text"]           
                PPE.write(str(PPT + "\n"))
                PN = PN + 1
                PFC = PFC + 1
                print("PFC=" + str(PFC))
            PN = 0
            while PN != 58:
                global P4
                PFJ = json.loads(PF7)
                PFJ2 = PFJ
                PFJ = PFJ["content"]
                PPRun.P4 = PFJ[PN]
                PP = PPRun.P4["prompt"]
                PPT = PP["text"]           
                SPE.write(str(PPT + "\n"))
                PN = PN + 1
                PFC = PFC + 1
                print("PFC=" + str(PFC))                
            break
                

    #REWRITE WHOLE WRITE FUNCTION!
    #1. add support for the diffrent jet files
    #2. fix isssue with SPNS = PFJ[PN] using the P4 read (since its the last one) and attach correct read per jet file
    #3. try to make it more efficant and shit
    @staticmethod
    def write(SPN):
        print("write timePE")
        global PF
        global PP
        global PFJ
        global PFJ2
        global SPNS
        if SPN == 1:
            SPNS = PPRun.P
        if SPN == 2:
            SPNS = PPRun.P2
        if SPN == 3:
            SPNS = PPRun.P3
        if SPN == 4:
            SPNS = PPRun.P4
        PN = 0  
        PELF = open("./PLE.txt","r")
        PEL = PELF.readlines()
        try:
            NPF = open("./STIContent to put in content/STIPrompt.jet","x")
        except FileExistsError:
            os.remove("./STIContent to put in content/STIPrompt.jet")
            time.sleep(2)
            NPF = open("./STIContent to put in content/STIPrompt.jet","x")
        print(str(SPNS))
        SPNS = PFJ[PN]
        print(str(SPNS))
        PP = SPNS["prompt"]
        PPT = str(PEL[PN]).rstrip("\n")
        PP["text"] = {"text": str(PPT)}
        print("PP['text'] = " + str(PP["text"]))
        SPNS["prompt"] = PP["text"]
        print(str(SPNS))
        PFJ[PN] = SPNS
        PFJ2["content"] = PFJ
        PFJ = PFJ2["content"]
        #loop after first time writing a prompt
        print(str(PN))
        PN = PN + 1
        print(str(PN))
        print(str(SPNS))
        while PN != 187:
            print(str(PN))
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
            print(str(PN))
        #write finished file
        json.dump(PFJ2,NPF)
        
PPRun = PromptParser()