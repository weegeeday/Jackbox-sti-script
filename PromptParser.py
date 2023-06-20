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
                

#Rewriting entire write method done!

    @staticmethod
    def newwrite(SPN,T):
        print("write time")
        if SPN == 1:
            PPRun.STIWrite(PMT=T)
        if SPN == 2:
            PPRun.STIJobWrite(PMT=T)
        if SPN == 3:
            PPRun.STIPhotoWrite(PMT=T)
        if SPN == 4:
            PPRun.STIStoreWrite(PMT=T)

    
    @staticmethod
    def STIWrite(PMT):
        print("STIWrite") #PMT = Prompt mod text
        print(PMT)
        PN = 0
        MPJC = None
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
            PFTD = open("./STIC.txt","r") #PFTD = Prompt file text dir
            PFD = str(PFTD.read()) #PFD = Prompt file dir
            OPF = open(str(PFD + "\STIPrompt.jet")) #OPF = Original prompt file
            OP = OPF.read()
            OPF.close()
            PFTD.close() 
            OPJ = json.loads(OP) #OPJ = Original prompts JSON OP = Original Prompts
            MPJ2 = OPJ #needed for making the new file
            OPJC = OPJ["content"] #OPJC = Original prompts json content
            OP = OPJC[PN] #PN = Prompt number OP = Original Pormpt
            #The read is cut, since we dont need the rest.
            PN = PN + 1
            time.sleep(0.02)            
            print(str(PN))
        #make new file
        PN = 0
        while PN != 187: #original version (down below) has a first write, might be needed.
            OP = OPJC[PN] #OPM = Original prompt
            MP = OP
            MPJC = OPJC
            OPP = OP["prompt"] #OPP = original prompt prompt
            OPPT = OPP["text"] #OPPT = original prompt prompt text
            print(OPPT)
            PPM = OPP
            try: 
                if PMT[PN] == None:
                    PMT[PN] = OPPT
                    print("On the fly none prompt!")
                PPM["text"] = {"text": str(PMT[PN])} #PPM = Prompt prompt mod
            except IndexError:
                PMT[PN] = OPPT
            print("PPM['text'] = " + str(PPM["text"]))
            MP["prompt"] = PPM["text"] #MP = Mod Prompt
            MPJC[PN] = MP #MPJC = Mod prompt json content
            MPJ2["content"] = MPJC #MPJ = Mod prompt json
            MPJC = MPJ2["content"]
            PN = PN + 1
            time.sleep(0.02)
            print(str(PN))
            print(PMT)
        json.dump(MPJ2,NPF)

    
    @staticmethod
    def STIJobWrite(PMT):
        print("STIJobWrite") #PMT = Prompt mod text
        print(PMT)
        PN = 0
        MPJC = None
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
            PFTD = open("./STIC.txt","r") #PFTD = Prompt file text dir
            PFD = str(PFTD.read()) #PFD = Prompt file dir
            OPF = open(str(PFD + "\STIJobPrompt.jet")) #OPF = Original prompt file
            OP = OPF.read()
            OPF.close()
            PFTD.close()             
            OPJ = json.loads(OP) #OPJ = Original prompts JSON OP = Original Prompts
            MPJ2 = OPJ #needed for making the new file
            OPJC = OPJ["content"] #OPJC = Original prompts json content
            OP = OPJC[PN] #PN = Prompt number OP = Original Pormpt
            #The read is cut, since we dont need the rest.
            PN = PN + 1
            time.sleep(0.02) 
            print(str(PN))
        #make new file
        while PN != 38: #original version (down below) has a first write, might be needed.
            OP = OPJC[PN] #OPM = Original prompt
            MP = OP
            MPJC = OPJC
            OPP = OP["prompt"] #OPP = original prompt prompt
            PPM = OPP
            OPPT = OPP["text"] #OPPT = original prompt prompt text
            print(OPPT)
            PPM = OPP
            try: 
                if PMT[PN] == None:
                    PMT[PN] = OPPT
                    print("On the fly none prompt!")
                PPM["text"] = {"text": str(PMT[PN])} #PPM = Prompt prompt mod
            except IndexError:
                PMT[PN] = OPPT
            print("PPM['text'] = " + str(PPM["text"]))
            MP["prompt"] = PPM["text"] #MP = Mod Prompt
            MPJC[PN] = MP #MPJC = Mod prompt json content
            MPJ2["content"] = MPJC #MPJ = Mod prompt json
            MPJC = MPJ2["content"]
            PN = PN + 1
            time.sleep(0.02)
            print(str(PN))
            print(PMT)
        json.dump(MPJ2,NPF)


    @staticmethod
    def STIPhotoWrite(PMT):
        print("STIPhotoWrite") #PMT = Prompt mod text
        print(PMT)
        PN = 0
        MPJC = None
        #read text file of new prompts
        NP = open("./PPE.txt","r")
        NP = NP.readlines()
        #create mod prompt file
        try:
            NPF = open("./STIContent to put in content/STIPhotoPrompt.jet","x")
        except FileExistsError:
            os.remove("./STIContent to put in content/STIPhotoPrompt.jet")
            time.sleep(2)
            NPF = open("./STIContent to put in content/STIPhotoPrompt.jet","x")
        #read original file
        while PN != 195:
            global OP
            PFTD = open("./STIC.txt","r") #PFTD = Prompt file text dir
            PFD = str(PFTD.read()) #PFD = Prompt file dir
            OPF = open(str(PFD + "\STIPhotoPrompt.jet")) #OPF = Original prompt file
            OP = OPF.read()
            OPF.close()
            PFTD.close()             
            OPJ = json.loads(OP) #OPJ = Original prompts JSON OP = Original Prompts
            MPJ2 = OPJ #needed for making the new file
            OPJC = OPJ["content"] #OPJC = Original prompts json content
            OP = OPJC[PN] #PN = Prompt number OP = Original Pormpt
            #The read is cut, since we dont need the rest.
            PN = PN + 1
            time.sleep(0.02) 
            print(str(PN))
        #make new file
        while PN != 195: #original version (down below) has a first write, might be needed.
            OP = OPJC[PN] #OPM = Original prompt
            MP = OP
            MPJC = OPJC
            OPP = OP["prompt"] #OPP = original prompt prompt
            PPM = OPP
            OPPT = OPP["text"] #OPPT = original prompt prompt text
            print(OPPT)
            PPM = OPP
            try: 
                if PMT[PN] == None:
                    PMT[PN] = OPPT
                    print("On the fly none prompt!")
                PPM["text"] = {"text": str(PMT[PN])} #PPM = Prompt prompt mod
            except IndexError:
                PMT[PN] = OPPT
            print("PPM['text'] = " + str(PPM["text"]))
            MP["prompt"] = PPM["text"] #MP = Mod Prompt
            MPJC[PN] = MP #MPJC = Mod prompt json content
            MPJ2["content"] = MPJC #MPJ = Mod prompt json
            MPJC = MPJ2["content"]
            PN = PN + 1
            time.sleep(0.02)
            print(str(PN))
            print(PMT)
        json.dump(MPJ2,NPF)
    
    @staticmethod
    def STIStoreWrite(PMT):
        print("STIStoreWrite") #PMT = Prompt mod text
        print(PMT)
        PN = 0
        MPJC = None
        #read text file of new prompts
        NP = open("./SPE.txt","r")
        NP = NP.readlines()
        #create mod prompt file
        try:
            NPF = open("./STIContent to put in content/STIStorePrompt.jet","x")
        except FileExistsError:
            os.remove("./STIContent to put in content/STIStorePrompt.jet")
            time.sleep(2)
            NPF = open("./STIContent to put in content/STIStorePrompt.jet","x")
        #read original file
        while PN != 58:
            global OP
            PFTD = open("./STIC.txt","r") #PFTD = Prompt file text dir
            PFD = str(PFTD.read()) #PFD = Prompt file dir
            OPF = open(str(PFD + "\STIStorePrompt.jet")) #OPF = Original prompt file
            OP = OPF.read()
            OPF.close()
            PFTD.close() 
            OPJ = json.loads(OP) #OPJ = Original prompts JSON OP = Original Prompts
            MPJ2 = OPJ #needed for making the new file
            OPJC = OPJ["content"] #OPJC = Original prompts json content
            OP = OPJC[PN] #PN = Prompt number OP = Original Pormpt
            #The read is cut, since we dont need the rest.
            PN = PN + 1
            time.sleep(0.02)            
            print(str(PN))
        #make new file
        PN = 0
        while PN != 58: #original version (down below) has a first write, might be needed.
            OP = OPJC[PN] #OPM = Original prompt
            MP = OP
            MPJC = OPJC
            OPP = OP["prompt"] #OPP = original prompt prompt
            PPM = OPP
            OPPT = OPP["text"] #OPPT = original prompt prompt text
            print(OPPT)
            PPM = OPP
            try: 
                if PMT[PN] == None:
                    PMT[PN] = OPPT
                    print("On the fly none prompt!")
                PPM["text"] = {"text": str(PMT[PN])} #PPM = Prompt prompt mod
            except IndexError:
                PMT[PN] = OPPT
            print("PPM['text'] = " + str(PPM["text"]))
            MP["prompt"] = PPM["text"] #MP = Mod Prompt
            MPJC[PN] = MP #MPJC = Mod prompt json content
            MPJ2["content"] = MPJC #MPJ = Mod prompt json
            MPJC = MPJ2["content"]
            PN = PN + 1
            time.sleep(0.02)
            print(str(PN))
            print(PMT)
        json.dump(MPJ2,NPF)   
PPRun = PromptParser()