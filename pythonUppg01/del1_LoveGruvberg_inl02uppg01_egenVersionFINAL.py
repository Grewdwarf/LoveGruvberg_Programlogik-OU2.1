#coding=utf-8
### Inlämningsuppgift 02 - Deluppgift 01. [Egen (aningen spejsad) version av PythonUppgift 1 - Love Gruvberg]

### Notering till Per:
### Jag gjorde den här fritolkade versionen av Årtalsuppgiften först, då jag till en början ej tyckte att jag
### hade greppat vilket det förväntade resultatet skulle vara (av 'PythonUppgift 1')!
    ### Även om denna egna/fritolkade version riskerar att flaxa vilt utanför uppgiftens
    ### faktiska scope -> så väljer jag ändå att inkludera den, särskilt då; 
    ### att slutföra denna gav mig ett bättre grepp om vad som behövde göras i 'uppgift 1' (hoppas jag iallafall!).
### [Slut på notering]


### Angående '#coding=utf-8' på rad 1: "UTF-8" står för: 'Unicode Transformation Format – 8-bit'. 
### Angående 'utf-8' har jag skrivit mer ingående om i medföljande .txt-fil -> "angUTF-8.txt".

### För att kunna använda sleep-funktionen (som kanske borde bes om ursäkt för i förväg) så
### måste jag importera den (som man ser i raderna 11 och 12 här under)
import sys
from time import sleep
import webbrowser

intro = """\n____________________________________________________________________________________________________\n
\033[1m.: Uppgift 01: Mata in födelsetal/årtal för ''kanditater'' i valfri ålder mellan 21 och 87! :.\033[0m
____________________________________________________________________________________________________\n\n"""

# Här (rad 28 - 31) är en häftig "skrivareffekt" som jag tycker är väldigt kul 
# (kan dock uppfattas som väldigt störig ...Men så ball!) 
# Funktionen säger i princip: 
for char in str(intro):     # <- *för varje tecken (char) som finns i string-meddelandet 'ggr'*...
    sleep(0.005)             # <- ...*'vänta' (sleep) i 3 millisekunder*...
    sys.stdout.write(char)  # <- *Spottar ur sig bokstäverna* ('stdout' kan även skrivas som 'stderr', men out:ar då ut hela rader(?))
    sys.stdout.flush()      # <- svårt för mig att förklara 'flush' på ett koncist sätt, men det handlar i princip om att 
                                # .flush() tvingar skrivareffekten att "spola" buffern, det innebär tydligen att allt i buffern skrivs 
                                # till terminalen och det verkar vara lite av en bra praxis/säkerhetsåtgärd. 
                                # Kan läsas mer om här -> https://stackoverflow.com/questions/10019456/usage-of-sys-stdout-flush-method
# Skrivareffekten hade egentligen kunnat göras till en funktion som gått att återkalla varje gång den 
# ska användas, men så långt har jag inte kommit än (så det serveras spagettikod här...).
sleep(.5)
print("\x1B[3mTänk på följande: ")
sleep(.5)

beAware = str("\n\t– [ Använd siffror! Om du envisas med att bokstavera så blir \n\t\tprogrammet lite ilsket... (Men för all del, PRØVA) ]                                                   "
+"\n\n\t- [ Använd årtal (ej ålder!) ]                                              \n"
+"\n\t– [ För att avsluta; ange '0' ]                                                    \033[0m\n")
for char in beAware:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()

pp = int(2)     # En "försöksräknare" som jag döpte till 'pp' för att den senare – på rad '83' – 
                # kommer att bli "Plus-Plus" (++), dvs. att den inkrementerar / adderar 
                # för varje nytt försök som användaren gör! 
    # Anledning till att det står int(2) här; är för att räkningen egentligen kommer att börja fr.o.m. 
    # det 2a försöket (vilket nog egentligen inte spelar någon relativt stor roll här, det var något som fick bli kvar efter att ha testat runt)
sleep(0.5)
print("____________________________________________________________________________________________________\n"
+"\n")
nuKorVi = str("\t\033[93m .:!\033[0mVarsågod att börja\033[93m!:.\033[0m\n")    ### Ett textmeddelande (str = string)
for char in nuKorVi:
    sleep(0.02)
    sys.stdout.write(char)
    sys.stdout.flush()

while True:     ### Och här börjar loopen!
    ggr = str("\t \033[93m:\t\t\t:\n\t :\033[0m\t \033[94mFörsök #")+str(pp-1)+("\033[0m\t\033[93m:\033[0m\n")     # Försöksräknaren + text!
    for char in ggr:
        sleep(0.02)
        sys.stdout.write(char)
        sys.stdout.flush()
    #print(ggr)                          # 'ggr' (försöksräknaren + text) –> skriver ut vilket försök användaren är på.
    try:
        anno = int(input(".:Årtal: "))      # anno ≈ Årtal (på Latin)
    # En "input" registrerar användarens input (indata) och med "int(input)" specificerar man att användaren
    # kommer att angiva int (siffertyp).
    except ValueError:
        nuDu = str("\t \033[91mx\033[0m\t  !NÄ NU!\t\033[91mx\n\t X\033[0m  .:::::\033[91m!STOPP!\033[0m:::::. \033[91mX\n"
        +"\t x\t\t\tx\033[0m\nAnvänd \033[1m\033[4mendast siffror\033[0m!\033[0m (Ej bokstäver) \033[94mFörsök igen\033[0m :(\n\t :\t\t\t:\n")
        for char in nuDu:
            sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()
        continue

    pp += int(1)    # Här blir pp –> Plus-Plus (aka '++', 'inkrement' eller -> som i python '+= 1'. 
                    # Den ökar med +1 för varje angivelse.

    if anno == 0:       # Om användaren anger 0, avsluta ('Tryck 0 för att avsluta').
        pp = pp-1       # Räkna ett steg bakåt (eftersom att försöksräknaren räknar avlutet som ett steg)
        ggr = str("\033[93mförsök #")+str(pp-1)+(" *\n")
        avslutar = str("\033[93m::.\t !   Tack för titten!   !\a\n::::.\t.!.A:.:V.:.S::L.:.U:.:T.!."
        +"\n::::::.:::.::H::E::J::.::D::Å::.:::.\033[0m \n\n\x1B[3mMed vänliga hälsningar,"
        +" \033[96mLove Gruvberg\033[0m\x1B[0m\n\n")    # Lite design :)
        for char in avslutar:
            sleep(0.04)
            sys.stdout.write(char)
            sys.stdout.flush()
        break   # avslutar
    
    x = anno   # här säger jag till 'x' att bli exakt det årtalet som användaren angav

    elli = (-2021%x);   # "elli" får stå för ålder. (fornnordiskt namn - symboliserar gammal ålder)
    aldersBrief = str("\033[93mOm du föddes år '" + str(anno) + "' så firar du (förhoppningsvis) din "+ str(2021%x)+"-årsdag i år!\033[0m\n")
    for char in aldersBrief:
            sleep(0.01)
            sys.stdout.write(char)
            sys.stdout.flush()
                            
        # Procenttecknet (%) i '2021 % x' kallas för modulos.
            # Kortfattat används '%' för att ta fram rest-summan av (i just det 
            # här fallet) '2021' kontra 'x' (x är angivet årtal 'anno')
            # Alltså; om du exempelvis angav '1950' så räknar den '2021 % 1950' (= 71).
                # Här hade man lika gärna kunnat räkna '2021 minus 1950', 
                # som ju också hade blivit = 71. 
                    # Så lite onödigt kanske, Modulo (%) kan vara superanvändbart
                    # i massvis av andra tillfällen.
    if anno > 2021: 
        print("\n\033[91mOj!\033[0m " + str(anno) + " är " + str(elli) + " år i in framtiden! (Nutid räknas som 2021)");

    if anno < 1934: 
        elli = str(1934%x);
        print("\033[91m.:::::!STOPP!:::::.\t\t:\n\t :\t\t\t:\nFödelsetalet ('" + str(anno) + "') är ju '" + str(elli) + "' år innan det äldst dugliga årtalet.\033[0m")

    if anno > 2000: 
        elli = str(-2000%x);
        print("\033[91m.:::::!STOPP!:::::.\t\t:\n\t :\t\t\t:\nFödelsetalet ('" + str(anno) + "') är ju '" + str(elli) + "' år efter det yngsta dugliga årtalet.\033[0m")

    elli = str(2021%x);
    
    # yngsta är 21 år (föddes alltså år 2000)
    if anno == 2000: 
        print("\033[92mDen som föddes år '" + str(anno) + "' är '" + str(elli) + "' år och den yngsta dugliga angivningsbara.\033[0m\n")
    elli = str(x%2021);
    
    # äldsta är 87 år (föddes alltså 1934)
    if anno == 1934:
        elli = str(2021%x);
        print('\n\033[92mDen som föddes ' + str(anno) + ' är idag ' + str(elli) + ' år och den äldsta dugliga angivningsbara.\033[0m\n')
        
    if anno == 1990: 
        webbrowser.open('https://www.youtube.com/watch?v=sPZPiZWqfwE')

    # Medelåldern är 49 år (föddes alltså 1972)
    if anno == 1972:
        elli = str(2021%x);
        print("\033[92mHär är årtalet för '" + str(elli) + "'-åringen som befinner sig i medelåldern! +\033[0m/\033[91m-\033[0m")
        sleep(3)
        print("Japp!")
        sleep(2)

    # Love Gruvberg-åldern är 27 år (föddes alltså 1994)
    if anno == 1994: 
        elli = str(2021%x);
        print("\n\tNämen! :')")
        sleep(.5)
        
        wow = str("Visste du: att \033[4mLove Gruvberg\033[0m (som skrev det här programmet) föddes året "
        + str(anno) + " och är idag hela '" + str(elli) + "' år gammal?!\n")
        for char in wow:
            sleep(0.04)
            sys.stdout.write(char)
            sys.stdout.flush()
        sleep(1.5)
        
        ow = str("...Dessutom, \x1B[3mRest in Peace Kurt Cobain.\x1B[0m\n")
        for char in ow:
            sleep(0.08)
            sys.stdout.write(char)
            sys.stdout.flush()
        print("\t\033[95m    [Show must go on!] \n\t :\t\t\t:\033[0m")

    # 'Om angiven tidsålder' 'är mindre än '1934' – eller (or) – tidsåldern är högre än '2000', säg ifrån!
    if anno < 1934 or anno > 2000:      # Printar ett meddelande som följer upp andra felmeddelanden
        print("\033[93mDet räknas alltså inte som ett rimligt årtal.\nFörsök igen!\n\t |\n\t V\033[0m")