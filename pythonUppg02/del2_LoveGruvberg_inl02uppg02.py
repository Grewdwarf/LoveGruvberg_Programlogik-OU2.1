#coding=utf-8

import math
import sys
import webbrowser
from time import sleep

upp1Rad = '\x1b[1A'     ### '\x1b[1A' <- placerar skrivmarkören 
                        ### en rad ovanför befintlig rad 
                        ### (typ som '\n' fast uppåt).
linje = str('____________________________________________________________\n') # Skriver ut ett avskiljande streck.
nySida = str('\r'+upp1Rad*13)

huvudMeny = True            # Allt under loopen 'huvudMeny' återvänder tillbaka 
                            ## till alternativen så länge huvudMeny == True
while huvudMeny == True:
    print('.:Menu:.\n'
    +'\t1. Convert dec number to binary form.\n\n'
    +'\t2. Convert binary number to decimal form.\n\n'
    +'\t3. EXIT \n\n\t4. "I dunno..."\n'+linje+'\r')    # Här skrivs alternativen ut.

    val = int(input('\r\nYour answer: '))  ## Alternativväljare -> 'val' <- tar emot int-värden från användaren.
    
    # ALTERNATIV 1      (dvs., om användaren anger '1')
    if val == 1:    # Decimaltal till binär form
        print(upp1Rad + "\t-> Convert decimal number to binary form.")
        inDec = int(input("\nSubmit a decimal number: "))
        def dec2Bin(deNum):       ### Här börjar funktion för binärtal
            biNum = 0           # (hittills) tomma variablar
            pwr = 0             # ( -||- )
            while deNum > 0:        ### Medan decimalTalet är större än 0
                biNum += 10 ** pwr * (deNum % 2)    
                    # 'biNum += '10'' [binärtalet inkrementeras med 10] 
                    #   ** [exponentiering] power (potens) 
                    #       * [ggr] decimaltalet % 2 [modulär aritmetik eller rest.].
                        ## Med '%' (modulär aritmetik) får vi fram talens rest vid division. 
                        ## Denna 'rest' avgör förövrigt huruvida vi får ut en etta eller en nolla!
                deNum //= 2     
                # '//' kallas i Python för "Floor division", vad är det? (Jag vet typ, se exempel nedan) 
                # Exempel på 'floor division':
                    # "Normal division" kan exempelvis se ut såhär:     -> 10/4 = 2,5 
                    # medan 'Floor division' (kan ej svensk benämning) kan se ut: -> 10//4 = 2.
                    # Så med floor division får vi ut 2 som naturligt tal 
                    # (dvs., '2,5' blir det positiva heltalet '2').
                pwr += 1    # potensen är 1++ (inkrementeras med 1 (dvs. är alltid + 1)).
            return biNum 
            # Du kan använda 'return' för att få koden att skicka/hoppa 
            # tillbaka programmet till 'caller'-koden (dvs. till början av kodblocket). 
        decSvar = str(dec2Bin(inDec))
        print(inDec)    # användarens input printas ut.
        decResultat = str(upp1Rad + str(inDec) + "\t\t <- has the binary number: "+ decSvar)
        for char in decResultat:    # Min skrivmaskinseffekt.
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        
        sleep(2)                    # Konstpaus.
        print('\033c\n\n'+decResultat+'\n'+linje)   
            # ['\033c'] rensar skärmdata 
            ## + ['decResultat'] som skriver ut resultatet en gång till
            ### + återvänder till while-loopens start (menyn)

    ## ALTERNATIV 2      (om användaren anger '2')
    if val == 2:    ## Val 2 - binär till decimalform   (fungerar som dec2Bin, men åt andra hållet!)
        print(upp1Rad + "\t-> Convert binary to decimal form.")
        inBin = int(input("\nSubmit a binary number: "))
        
        def bin2Dec(biNum):       ### Här börjar funktion för binärtal
            decNum = 0
            pwr = 0
            while biNum > 0:
                decNum += 2 ** pwr * (biNum % 10)
                biNum //= 10        ## Floor division
                pwr += 1
            return decNum
        binSvar = str(bin2Dec(inBin))
        
        print(inBin)    # användarens input printas ut.
        binResultat = str(upp1Rad + str(inBin) + "\t\t <- has the decimal number: "+ binSvar)
        for char in binResultat:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        # print("\n"+linje+"\n")
        sleep(2)                    # Konstpaus
        print('\033c\n\n'+binResultat+'\n'+linje)

    ### ALTERNATIV 3      (om användaren anger '3')
    if val == 3:
        avslut = 'false'
        while avslut == 'false':
            sys.stdout.write('\rAvslutar\t  |')
            sleep(0.09)
            sys.stdout.write('\raVslutar\t  /')
            sleep(0.09)
            sys.stdout.write('\ravSlutar\t  -')
            sleep(0.09)
            sys.stdout.write('\ravsLutar\t  \\')
            sleep(0.09)
            sys.stdout.write('\ravslUtar\t  |')
            sleep(0.09)
            sys.stdout.write('\ravsluTar\t  /')
            sleep(0.09)
            sys.stdout.write('\ravslutAr\t  -')
            sleep(0.09)
            sys.stdout.write('\ravslutaR\t  \\')
            sleep(0.09)
            sys.stdout.write('\ravslutAr\t  |')
            sleep(0.09)
            sys.stdout.write('\ravsluTar\t  /')
            sleep(0.09)
            sys.stdout.write('\ravslUtar\t  -')
            sleep(0.09)
            sys.stdout.write('\ravsLutar\t! | !')
            sleep(0.09)
            sys.stdout.write('\ravSlutar       !! / !!')
            sleep(0.09)
            sys.stdout.write('\raVslutar      !!! - !!!')
            sleep(0.09)
            sys.stdout.write('\rAvslutar     !!!! \\ !!!!')
            sleep(0.5)
            sys.stdout.write('\rAvslutat     ____ _ ____\n\n')
            break
        avslut = 'true'
        huvudMeny = False

    #### ALTERNATIV 4 (bonusval för den som inte vet vad den vill)
    if val == 4:
        print(linje+"\n\n"
        + "\t[ Press 'ctrl + c' when you've thought this through ]\n"
        +linje+"\n")
        webbrowser.open('https://www.youtube.com/watch?v=lP85TIFdMD4')
        while True:
            try:
                tankeEffekt = str("\r [:..] \t\t.:.Tänk.:.   \t?! \t __Bin_?_Dec__\t\t[..:]"
                +"\r [::.] \t\t .:Thnk:.    \t??| \t _?Bin?__Dec_?\t\t[.::]"
                +"\r [:::] \t\t  .Denk.     \t???| \t _?Dec?__Bin_?\t\t[:::]"
                +"\r [.::] \t\t ..Tänk..    \t???? \t __Dec_?_Bin__\t\t[::.]"
                +"\r [..:] \t\t...Thnk...   \t???| \t ?_Dec__?Bin?_\t\t[:..]"
                +"\r [...] \t\t:..Denk..:   \t??| \t ?_Bin__?Dec?_\t\t[...]"+"\r")
                for char in tankeEffekt:
                    sleep(.004)
                    sys.stderr.write(char)
                    sys.stdout.flush()
            except KeyboardInterrupt:
                break
                sleep(.1)
