greeting = {'New Zealand': 'Hongi',
            'Botswana': 'An elaborate handshake',
            'Greenland': 'Kunik',
            'Thailand' : 'Wai',
            'India' : 'Namaste',
            'Tibet' : 'Sticking your tongue out',
            'Russia' : 'A firm handshake',
            'The Philippines': 'Mano',
            'Argentina' : 'Kiss on the right cheek',
            'Japan' : 'A bow',
            'France' : 'Kiss on each cheek',
            'Ukraine' : 'A triple kiss',

}

print(greeting.values())
while(True):
    for key, val in greeting.items():
        ans = input('Guerss the greeting of' + key+':')
        if ans == greeting[key]:
            print('congrat')
        else:
            continue
