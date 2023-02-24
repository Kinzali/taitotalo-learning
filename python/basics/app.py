# ask user to enter a any number. if number is > 10 then print 'number is verified'. 
# otherwaise print 'number is not verifide.
# number = int(input('please neter any number:\n'))
# # int(input('please neter any number:\n'))
# if number > 10:
#     print(f'{number} is verified')
# elif number == 10:
#     print(f'{number} is so so')    
# else:
#     print(f'{number} is not verified')
    
    
machine_off = input('Enter True or False')

if machine_off == True:
    print('Go home machine is off')
else:
    print('kam kro')      
    
      

# tarkista, etä olet oikeassa kansiossa ja aja terminaalissa python ehtolauseet.py 
# tai visual studio codessa oikealla ylhäällä olevalla kolmiolla ja sen alla Run Python File
    
    sana = input('anna sana: ')
    if len(sana) > 1:
        kirjaimia = len(sana)
        print(f'sanassa {sana} on {kirjaimia} kirjainta/merkkiä')
        print('kiitos!')