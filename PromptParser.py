import json
import os
import time 
class PromptParser:

    @staticmethod
    def read():      
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
                PFJ = PFJ["content"]
                P = PFJ[PN]
                PP = P["prompt"]
                PPT = PP["text"]           
                OTLPE.write(str(PPT + "\n"))
                PN = PN + 1
                PFC = PFC + 1
                print("PFC=" + str(PFC))
            PN = 0
            while PN != 38:
                global P2
                PFJ = json.loads(PF3)
                PFJ = PFJ["content"]
                P2 = PFJ[PN]
                PP = P2["prompt"]
                PPT = PP["text"]           
                JPE.write(str(PPT + "\n"))
                PN = PN + 1
                PFC = PFC + 1
                print("PFC=" + str(PFC))
            PN = 0
            while PN != 195:
                global P3
                PFJ = json.loads(PF5)
                PFJ = PFJ["content"]
                P3 = PFJ[PN]
                PP = P3["prompt"]
                PPT = PP["text"]           
                PPE.write(str(PPT + "\n"))
                PN = PN + 1
                PFC = PFC + 1
                print("PFC=" + str(PFC))
            PN = 0
            while PN != 58:
                global P4
                PFJ = json.loads(PF7)
                PFJ = PFJ["content"]
                P4 = PFJ[PN]
                PP = P4["prompt"]
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
    def newwrite(SPN):
        print("write time")
        if SPN == 1:
            PPRun.STIWrite()
        if SPN == 2:
            PPRun.STIJobWrite()
        if SPN == 3:
            PPRun.STIPhotoWrite()
        if SPN == 4:
            PPRun.STIStoreWrite()

    
    @staticmethod
    def STIWrite():
        print("STIWrite")
        PN = 0
        PPM = None
        MP = None
        MPJC = None
        MPJ = None
        #read text file of new prompts
        NP = open("./PLE.txt","r")
        NP = NP.readlines()
        #create mod prompt file
        try:
            NPF = open("./STIContent to put in content/STIPrompt.jet","x")
        except FileExistsError:
            os.remove("./STIContent to put in content/STIPrompt.jet")
            time.sleep(2)
            NPF = open("./STIContent to put in content/STIPrompt.jet","x")
        #read original file
        while PN != 187:
            global OP
            OPJ = json.loads(OP) #OPJ = Original prompts JSON OP = Original Prompts
            MPJ2 = OPJ #needed for making the new file
            OPJC = OPJ["content"] #OPJC = Original prompts json content
            OP = OPJC[PN] #PN = Prompt number OP = Original Pormpt
            #The read is cut, since we dont need the rest.
            print(str(PN))
        #make new file
        while PN != 187: #original version (down below) has a first write, might be needed.
            OP = OPJC[PN] #OPM = Original prompt
            OPP = OP["prompt"] #OPP = original prompt prompt
            PMT = str(NP[PN]).rstrip("\n") #PMT = Prompt mod text
            PPM = OPP
            PPM["text"] = {"text": str(PMT)} #PPM = Prompt prompt mod
            print("PPM['text'] = " + str(PPM["text"]))
            MP["prompt"] = PPM["text"] #MP = Mod Prompt
            MPJC[PN] = MP #MPJC = Mod prompt json content
            MPJ2["content"] = MPJC #MPJ = Mod prompt json
            MPJC = MPJ2["content"]
            PN = PN + 1
            time.sleep(0.3)
            print(str(PN))
        json.dumps(MPJ2,NPF)

    
    @staticmethod
    def STIJobWrite():
        print("STIJobWrite")
        PN = 0
        PPM = None
        MP = None
        MPJC = None
        MPJ = None
        #read text file of new prompts
        NP = open("./JPE.txt","r")
        NP = NP.readlines()
        #create mod prompt file
        try:
            NPF = open("./STIContent to put in content/STIJobPrompt.jet","x")
        except FileExistsError:
            os.remove("./STIContent to put in content/STIJobPrompt.jet")
            time.sleep(2)
            NPF = open("./STIContent to put in content/STIJobPrompt.jet","x")
        #read original file
        while PN != 38:
            global OP
            OPJ = json.loads(OP) #OPJ = Original prompts JSON OP = Original Prompts
            MPJ2 = OPJ #needed for making the new file
            OPJC = OPJ["content"] #OPJC = Original prompts json content
            OP = OPJC[PN] #PN = Prompt number OP = Original Pormpt
            #The read is cut, since we dont need the rest.
            print(str(PN))
        #make new file
        while PN != 38: #original version (down below) has a first write, might be needed.
            OP = OPJC[PN] #OPM = Original prompt
            OPP = OP["prompt"] #OPP = original prompt prompt
            PMT = str(NP[PN]).rstrip("\n") #PMT = Prompt mod text
            PPM = OPP
            PPM["text"] = {"text": str(PMT)} #PPM = Prompt prompt mod
            print("PPM['text'] = " + str(PPM["text"]))
            MP["prompt"] = PPM["text"] #MP = Mod Prompt
            MPJC[PN] = MP #MPJC = Mod prompt json content
            MPJ2["content"] = MPJC #MPJ = Mod prompt json
            MPJC = MPJ2["content"]
            PN = PN + 1
            time.sleep(0.3)
            print(str(PN))
        json.dumps(MPJ2,NPF)
    
    
    
    
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