#coding=utf-8 
#import datetime

print ('\n.: Dags att mata in födelsetal! :.\n\n\t[ För att avsluta, ange talet 0 ]\n');
while True:
    anno = input("Årtal: ")     # Anno –> Årtal







    if anno == '0': break   # Funktionen: 'tryck 0 för att avsluta'
    
    x = int(anno)
    #x = int(nutid)

    elli = str(-2021%x);
    if anno > '2021': 
        print ('\n.:Födelsetalet ('+anno+') är ' + elli + ' år i in framtiden:.');

    if anno < '1934': 
        elli = str(1934%x);
        print ('\nFödelsetalet ('+anno+') är ju ' + elli + ' år före än den äldsta kanditaten.');

    if anno > '2000': 
        elli = str(-2000%x);
        print ('\nFödelsetalet ('+anno+') är ju ' + elli + ' år efter den yngsta kandidaten.');

    elli = str(2021%x);
    
    # yngsta är 21 år 
    if anno == '2000': 
        print('Du är ' + elli + ' år och yngst.')
    elli = str(x%2021);
    
    # äldsta är 87 år.
    if anno == '1934':
        elli = str(2021%x);
        print ('Du är ' + elli + ' år, i sina redigaste år och äldst.')
        
    
    # Medelåldern är 49 år. 
    if anno == '1972':
        elli = str(2021%x);
        print ('\nI ' + elli + '-åringen som befinner sig i medelåldern! +/–\n')

    if anno < '1934' or anno > '2000':
        #print ('Fel: Orimligt årtal. Försök igen.')
        print ("Det räknas alltså inte som ett rimligt årtal.\nFörsök igen!\n")
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