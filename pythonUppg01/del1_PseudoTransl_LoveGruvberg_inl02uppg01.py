#coding=utf-8
### Inlämningsuppgift 02 - Deluppgift 01. [Direkt-översatt pseudo - Love Gruvberg]

### Notering till Per:
### Antagligen har jag gjort någonting lite galet - då jag inte har lyckats 
### rätta till skönhetsfelet (dvs. meddelandet 'orimligt årtal') som tyvärr 
### kan poppa upp lite som det vill, särskilt om användarens 'första angivna årtal' har 
### ett högre värde än 'nästa angivna årtal'. 
    ### Exempel: 
    ### om du i den första inmatningen anger årtalet '1977' och i den andra inmatningen anger 
    ### '1957' -> så får du meddelandet 'orimligt årtal'. 
    ### Det fungerar däremot bättre om du skriver (tidigare årtalet) '1957' först och 
    ### (senare årtalet) '1977' i den andra, av någon anledning!
    ### Deluppgift
### [Slut på notering]

antal_ar = int(0)       ### Startvärde (har inte börjat räkna ännu)
summa_ar = int(0)       ### Startvärde (har inte börjat räkna ännu)
max_ar = int(0)         ### Ingen högsta ålder ännu
min_ar = int(110)       ### Väl tilltaget minvärde (ålder) att starta med

inmatat_ar = int(-1)    ### Bara som startvarde för loopstartens skull!

### Loop start!
while inmatat_ar != 0:
    print("\nMata in (förslagsvis 3 st) födelseårtal! Avsluta med talet 0.")
    inmatat_ar = int(input("Årtal: ")) ### 'input' för att registrera indata från användaren | 'int(input)' för att specificera att det inmatade värdet ska lagras som typen 'int'.
    nuvAr = int(2021)   ### Med 'nuVar' (nuvarande årtalet 2021) som en variabel - vars värde ju går 
                        ### att ändra från int(2021) till något annat -> blir det ganska tacksamt om jag 
                        ### exempelvis vill köra detta program igen nästa år, eftersom att jag slipper 
                        ### fylla i '2022' överallt! 
                        ### Det räcker alltså att jag ändrar variabelns värde här på rad '25'.
    alder = (nuvAr - inmatat_ar)

    if alder < 0 or alder > min_ar and alder != nuvAr:
        print("Orimligt årtal. Försök igen.")
    else:
        if inmatat_ar > 0:
            antal_ar += 1
            summa_ar = summa_ar + alder
            if alder < min_ar:
                min_ar = alder     ### Ny lägsta ålder funnen
            if alder > max_ar:
                max_ar = alder     ### Ny högsta ålder funnen
        
                    ### Om det inmatatde talet var noll trillar vi ur loopen
        else:       ### <- om inmatat_ar är lika med 0:
            break   ### Break:a loopen.

### Nu är det bara att skriva ut medelvärdet samt yngsta och äldsta    
print("\nResultat:\n\t- Medelåldern är", int(summa_ar/antal_ar), "år.")              # skriv_ut "Medelaldern är ", summa_år / antal_år, "år."
print("\n\t- Den yngsta är", min_ar, "\n\n\t- Den äldsta är hela", max_ar,"år.\n")  # skriv_ut "Den yngsta är ", min_år, " och den aldsta är ", max_år