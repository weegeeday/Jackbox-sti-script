import json
import os
import time
class PromptParser():
    global firstWriteD
    firstWriteD = False
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
    def write(NPPT,PN,loop):  
        global firstWriteD
        global PF
        global PP
        global P
        global PFJ
        global PFJ2
        if firstWriteD == False and loop == False:
            try:
                NPF = open("./STIContent to put in content/STIPrompt.jet","x")
            except FileExistsError:
                os.remove("./STIContent to put in content/STIPrompt.jet")
                time.sleep(2)
                NPF = open("./STIContent to put in content/STIPrompt.jet","x")
            PP["text"] = NPPT
            print("PP[]=" + str(PP["text"]) + "PP=" + str(PP))
            P["prompt"] = PP["text"]
            print("P[]=" + str(P["prompt"]) + "P=" + str(P))
            PFJ[PN] = P
            print("PFJ[]=" + str(PFJ[PN]) + "PFJ=" + str(PFJ))
            PFJ2["content"] = PFJ
            json.dump(PFJ2,NPF)
            firstWriteD = True
            return
        if firstWriteD == True and loop == False:
            NPF = open("./STIContent to put in content/STIPrompt.jet","r")
            NPFJ = NPF.read()
            PFJ = json.loads(NPFJ)
            PFJ2 = PFJ
            PFJ = PFJ["content"]
            P = PFJ[PN]
            PP = P["prompt"]
            NPF.close()
            NPF = open("./STIContent to put in content/STIPrompt.jet","w")
            PP["text"] = str(NPPT)
            print("PP[]=" + str(PP["text"]) + "PP=" + str(PP))
            P["prompt"] = PP["text"]
            print("P[]=" + str(P["prompt"]) + "P=" + str(P))
            PFJ[PN] = P
            print("PFJ[]=" + str(PFJ[PN]) + "PFJ=" + str(PFJ))
            PFJ2["content"] = PFJ
            json.dump(PFJ2,NPF)
            PN = PN + 1
            return
        if firstWriteD == True & loop == True:
            while PN != 187:
                NPF = open("./STIContent to put in content/STIPrompt.jet","r")
                NPFJ = NPF.read()
                PFJ = json.loads(NPFJ)
                PFJ2 = PFJ
                PFJ = PFJ["content"]
                P = PFJ[PN]
                PP = P["prompt"]
                NPF.close()
                NPF = open("./STIContent to put in content/STIPrompt.jet","w")
                PP["text"] = str(NPPT)
                print("PP[]=" + str(PP["text"]) + "PP=" + str(PP))
                P["prompt"] = PP["text"]
                print("P[]=" + str(P["prompt"]) + "P=" + str(P))
                PFJ[PN] = P
                print("PFJ[]=" + str(PFJ[PN]) + "PFJ=" + str(PFJ))
                PFJ2["content"] = PFJ
                json.dump(PFJ2,NPF)
                PN = PN + 1 
                raise
PPRun = PromptParser()