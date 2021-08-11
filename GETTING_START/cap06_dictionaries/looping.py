#using everythinh
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
 }

for key, value in user_0.items():
     print("\nKey: " + key)
     print("Value: " + value)
    
print(user_0.items())

#using keys
favorite_languages = {
     'jen': 'python',
     'sarah': 'c',
     'edward': 'ruby',
     'phil': 'python',
 }

for name in favorite_languages.keys():
     print(name.title())

##outra aplicação

favorite_languages = {
     'jen': 'python',
     'sarah': 'c',
     'edward': 'ruby',
     'phil': 'python',
}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
     print(name.title())
     if name in friends:
          print(" Hi " + name.title() + ", I see your favorite language is " + 
          favorite_languages[name].title() + "!")

#looping sobre os valores
print("The following languages have been mentioned:")
for language in favorite_languages.values():
     print(language.title())

