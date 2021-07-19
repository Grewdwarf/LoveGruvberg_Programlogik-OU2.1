#coding=utf-8

# För att kunna använda sleep-funktionen (som jag kanske borde om ursäkt för nu i förväg),
# så måste jag importera som man ser i raderna (5 och 6) här under:
import sys
from time import sleep

intro = '    ________________________________________________________________________\n.: Mata in födelsetal/årtal för "kanditater" i valfri ålder mellan 21 och 87! :.\n'
for char in intro:
    sleep(0.003)
    sys.stderr.write(char)

sleep(0.5)
print('\tTänk på:')
sleep(0.7)
beAware = '\t– [ För att undvika att programmet lägger ned; använd endast siffror (ej bokstäver!) ]                          \n\t– [ För att avsluta; ange talet 0 ]\n\n\t  .:Varsågod att börja:.\n\t I\t Försök #1\tI\n'
for char in beAware:
    sleep(0.03)
    sys.stderr.write(char)

pp = int('2')   # En "försöksräknare" som jag döpte till 'pp' för att den senare – på rad 25 – 
# kommer att bli "Plus-Plus" (++), dvs. att den inkrementerar / adderar för varje försök som 
# användaren gör! 
    # Anledning till att det står en 2a här; är för att under körningen av programmet kommer själva 
    # räkningen egentligen att börja fr.o.m. det 2a försöket (spelar inte så stor roll
    # men det var mest för att testa runt och för att jag hade skrivit Försök #1 "manuellt"!)


while True:
    anno = raw_input("Årtal: ")     # anno –> Årtal (ish, på Latin)
    # "raw_input" menar att den registrerar användarens input, i detta fall tryck på tangentbordet.
    # Vad som skiljer input från raw_input vet jag inte riktigt förutom att jag har förstått 
    # att raw_input läses av "lite mer allmänt" och fungerar bättre (för mig iallafall!)
    
    ggr = str("\t I\t Försök #")+str(pp)+("\tI\n") # 'ggr' skriver ut vilket försök användaren är på.
    pp += int('1')      # Här blir pp –> Plus-Plus / ++ / += 1. Den ökar med +1 för varje angivelse.

    for char in ggr: # Här är en häftig "skrivareffekt" som jag älskar att använda när jag gör konsolprogram.
        sleep(0.05)  # Funktionen säger i princip: "för varje bokstav (char) som finns i meddelandet 'ggr', 
        sys.stderr.write(char) # vänta (sleep) i 50 millisekunder".

    if anno == '0':     # Om användaren anger 0, avsluta ('Tryck 0 för att avsluta').
        pp = pp-1   # Räkna ett steg bakåt (eftersom att försöksräknaren räknar avlutet som ett steg)
        ggr = str("försök #")+str(pp-1)+(" *\n")
        avslutar = "\a\t.:. :.: .:. :.: .:. :.: .:."    # Lite design :)
        for char in avslutar:
            sleep(0.05)
            sys.stderr.write(char)
        print ("\n    * Faktiskt avslut under "+ggr)
        break   # avslutar
    
    x = int(anno)   # här säger jag till 'x' att bli exakt det årtalet som användaren angav

    elli = str(-2021%x);    # "elli" får stå för ålder. (Långsökt anledning är att 'Elli' är ett 
                                # fornnordiskt namn som bl.a. symboliserar gammal ålder)
                            
        # procenttecknet (%) i funktionen kallas för modulos.
            # Kortfattat används '%' för att ta fram rest-summan av (i just det 
            # här fallet) '2021' kontra 'x' (x är angivet årtal 'anno')
            # alltså; om du exempelvis angav '1950' så räknar den '2021 % 1950' (= 71).
                # Här hade man lika gärna kunnat räkna '2021 minus 1950', 
                # som ju också hade blivit = 71. 
                    # Så lite onödigt kanske, Modulo (%) kan vara superanvändbart
                    # i massvis av andra tillfällen.
    if anno > '2021': 
        print ('\nOj! '+anno+' är ' + elli + ' år i in framtiden! (Nutid räknas som 2021)');

    if anno < '1934': 
        elli = str(1934%x);
        print ('.:::::!STOPP!:::::.\t\t|\n\t |\t\t\t|\nFödelsetalet ('+anno+') är ju ' + elli + ' år före än det äldsta dugliga årtalet.');

    if anno > '2000': 
        elli = str(-2000%x);
        print ('.:::::!STOPP!:::::.\t\t|\n\t |\t\t\t|\nFödelsetalet ('+anno+') är ju ' + elli + ' år efter den yngsta dugliga årtalet.');

    elli = str(2021%x);
    
    # yngsta är 21 år (föddes alltså år 2000)
    if anno == '2000': 
        print('Den som föddes år '+anno+' är ' + elli + ' år och den yngsta dugliga angivningsbara.')
    elli = str(x%2021);
    
    # äldsta är 87 år (föddes alltså 1934)
    if anno == '1934':
        elli = str(2021%x);
        print ('Den som föddes '+ anno+ ' är idag ' + elli + ' år och den äldsta dugliga angivningsbara.')
        
    
    # Medelåldern är 49 år (föddes alltså 1972)
    if anno == '1972':
        elli = str(2021%x);
        print ('Här är årtalet för ' + elli + '-åringen som befinner sig i medelåldern! +/–\n')

    # Love Gruvberg-åldern är 27 år (föddes alltså 1994)
    if anno == '1994': 
        elli = str(2021%x);
        print('Nämen! Love Gruvberg (som skrev det här programmet) föddes år '+anno+' och är idag hela ' + elli + ' år gammal.')

    # Om angiven tidsålder är mindre än '1934' – eller (or) – tidsåldern är högre än '2000', säg ifrån!
    if anno < '1934' or anno > '2000':
        #print ('Fel: Orimligt årtal. Försök igen.')
        print ("Det räknas alltså inte som ett rimligt årtal.\nFörsök igen!\n\t |\n\t V")