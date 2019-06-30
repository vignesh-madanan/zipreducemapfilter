
####################MAP##################
def string_edit(text):
    return text.lower().replace('the','')


string_list=[
    'The best apps download superpowers to your smartphone.',
    ' The Verge covers the new and noteworthy Android apps, iPhone apps, and games', 
    'Highlighting great design, impressive utility, and novel features.',
     'If it belongs on your phone, youll find it on The Verge.'
]

x=list(map(string_edit,string_list))
print(x)
[' best apps download superpowers to your smartphone.', '  verge covers  new and noteworthy android apps, iphone apps, and games', 'highlighting great design, impressive utility, and novel features.', 'if it belongs on your phone, youll find it on  verge.']

##################FILTER#################
div3=list(filter(lambda n: n%5 == 0,range(20)))
print(div3)



########REDUCE##########
from functools import reduce

reduce(lambda x, y: x+y, range(100))

#################ZIP#############

animals=['Cat', 'Dog', 'Mouse', 'Elephant', 'Hamster']
number_of_animals=[3,4,6,1,5]
print(list(zip(animals,number_of_animals)))
