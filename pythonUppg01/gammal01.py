#coding=utf-8

import sys
from time import sleep

intro = '\n.: Mata in födelsetal/årtal för "kanditater" i valfri ålder mellan 21 och 87! :.\n\t [ För att avsluta, ange talet 0 ]\n\n\t |\t Försök #1\t|\n'
for char in intro:
    sleep(0.02)
    sys.stderr.write(char)

pp = int('2')   # En "försöksräknare" som jag döpte till 'pp' för att den senare (på rad 23) 
# kommer att bli "Plus-Plus". Räkningen kommer egentligen att börja på 
# 2a försöket (då jag redan har skrivit Försök #1 "för hand")


while True:
    anno = raw_input("Årtal: ")     # anno –> Årtal 
    # "raw_input" menar att den registrerar användarens input (keyboard-tryck i detta fall) 
    # Vad skillnaden mellan input och raw_input är vet jag inte riktigt, 
    # mer än att raw_input är "mer allmän" och fungerar bättre (för mig iallafall!)
    
    ggr = str("\t |\t Försök #")+str(pp)+("\t|\n")
    pp += int('1')  # Här blir pp –> Plus-Plus / ++ / += 1

    for char in ggr:
        sleep(0.05)
        sys.stderr.write(char)

    if anno == '0':     # 'Tryck 0 för att avsluta' 
        pp = pp-1
        ggr = str("försök #")+str(pp-1)+(" *\n")
        avslutar = "\a\t.:. :.: .:. :.: .:. :.: .:."
        for char in avslutar:
            sleep(0.03)
            sys.stderr.write(char)
        print ("\n    * Faktiskt avslut efter "+ggr)
        break   # avslutar
    
    x = int(anno)
    #x = int(nutid)

    elli = str(-2021%x);
    if anno > '2021': 
        print ('\n'+anno+' är ' + elli + ' år i in framtiden!');

    if anno < '1934': 
        elli = str(1934%x);
        print ('::::::::::.\nFödelsetalet ('+anno+') är ju ' + elli + ' år före än den äldsta kanditaten.');

    if anno > '2000': 
        elli = str(-2000%x);
        print ('::::::::::.\nFödelsetalet ('+anno+') är ju ' + elli + ' år efter den yngsta kandidaten.');

    elli = str(2021%x);
    
    # yngsta är 21 år 
    if anno == '2000': 
        print('Den som föddes '+anno+' är ' + elli + ' år och yngst.')
    elli = str(x%2021);
    
    # äldsta är 87 år.
    if anno == '1934':
        elli = str(2021%x);
        print ('Denna "kandidat" är ' + elli + ' år och äldst.')
        
    
    # Medelåldern är 49 år.
    if anno == '1972':
        elli = str(2021%x);
        print ('Här är årtalet för ' + elli + '-åringen som befinner sig i medelåldern! +/–\n')

    if anno < '1934' or anno > '2000':
        #print ('Fel: Orimligt årtal. Försök igen.')
        print ("Det räknas alltså inte som ett rimligt årtal.\nFörsök igen!\n\t |\n\t V")
        elli = str(x%2021);

# elli = str(-2021%x);
#     if anno == '2019' or '2020' or '2021':      # Året nu
#         elli = str(x%2021);    # Elli –> Ålder
#         print (anno+' är man en '+'coronabebis på knappt '+ elli +' år.\n')
            

#elli = str(2021%anno);
        

#    elif anno <= '2021':
#       print ('Året '+ anno +' ')
    #print(anno)



#     datum = datetime.datetime.now()
# date = datum.date()
# nutid = date.strftime("%Y")
#print('Året är -> ') + nutid;
#elli = str(x%2021);