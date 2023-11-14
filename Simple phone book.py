PhoneBook = {
    'Nimesh': {
        'Address':'Pokhara',
        'Phone': ('1234', '5678', '6523'),
        'Email': ('shreekrishna@', 'nimesh@123'),

                    },
    'Purna': {
        'Address': 'Achham',
        'Phone' : ('974633', '986843', '985842'),
        'Email' : ('purnasaud3@', 'ps0243@'),
    },
    'susil' : {
        'Address': 'Kailali',
        'Phone' : ('986534', '98763', '718317'),
        'Email': ('dikka@', 'susil@541'),

    },

}

def findingValue (number):
       for keys, value in PhoneBook.items():
              for additional in value:
               print(additional)
           # for details, values in value.items():
            #      print(details, values)
             #     if number in values:
              #       return keys
               #   else:
                #     return 'Name Not Found'

value = input('Enter your phone Number: ')
x =  findingValue(value)
print("{} ".format(x))





