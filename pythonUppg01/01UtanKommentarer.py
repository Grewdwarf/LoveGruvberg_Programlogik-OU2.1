#coding=utf-8

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

pp = int('2')

while True:
    anno = raw_input("Årtal: ")     

    ggr = str("\t I\t Försök #")+str(pp)+("\tI\n")
    pp += int('1')

    for char in ggr: 
        sleep(0.05)  
        sys.stderr.write(char)

    if anno == '0':
        pp = pp-1  
        ggr = str("försök #")+str(pp-1)+(" *\n")
        avslutar = "\a\t.:. :.: .:. :.: .:. :.: .:."
        for char in avslutar:
            sleep(0.05)
            sys.stderr.write(char)
        print ("\n    * Faktiskt avslut under "+ggr)
        break  
    
    x = int(anno)
    elli = str(-2021%x);

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

    if anno < '1934' or anno > '2000':
        print ("Det räknas alltså inte som ett rimligt årtal.\nFörsök igen!\n\t |\n\t V")