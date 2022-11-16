import json
import os
import time
class PromptParser():
    @staticmethod
    def read():      
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
        PN = 0  
        PELF = open("./PLE.txt","r")
        PEL = PELF.readlines()
        try:
            NPF = open("./STIContent to put in content/STIPrompt.jet","x")
        except FileExistsError:
            os.remove("./STIContent to put in content/STIPrompt.jet")
            time.sleep(2)
            NPF = open("./STIContent to put in content/STIPrompt.jet","x")        
        NPFJ = NPF.read() #not readable error here
        PFJ = json.loads(NPFJ)    
        PFJ2 = PFJ
        PFJ = PFJ["content"]
        P = PFJ[PN]
        PP = P["prompt"]
        PP["text"] = PEL[PN]
        P["prompt"] = PP["text"]
        PFJ[PN] = P
        PFJ2["content"] = PFJ
        #loop after first time writing a prompt
        while PN != 187:
            PFJ = PFJ2 #instead of loading original prompt file, load new one made before and edit it again.
            PFJ = PFJ["content"]
            P = PFJ[PN]
            PP = P["prompt"]
            PP["text"] = PEL[PN]
            P["prompt"] = PP["text"]
            PFJ[PN] = P
            PFJ2["content"] = PFJ
        #write finished file
        json.dump(PFJ2,NPF)
        
PPRun = PromptParser()
#REWRITE ENTIRE WRITE METHOD
#use a system of having all the new prompts in a text file
#read text file and based on line number transplant into STIPrompt.jet
#listbox and ui redone needed too
#as of now, only writing one prompt works.
#after that errors with str and such happen.