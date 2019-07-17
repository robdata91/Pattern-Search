import re

#Paragraph provided for search and replace

lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

#Searching for non-alphanumeric characters
pattern = re.compile("[^0-9a-zA-Z\d]")


#Searching for occurances 
results = re.findall("[^0-9a-zA-Z\d]",lorem_ipsum)
print(len(results))

#Printing numbers for sit amet
occurance_sit_amet = re.findall(r'sit[-:]amet', lorem_ipsum)
print(len(occurance_sit_amet))

#Assigning string to replace_results
replace_results=re.sub(r'sit[-:]amet', 'sit amet', 'lorem_ipsum')


#Finding special chars. inside sit amet
regex='sit[\s]amet'


#Taking the new paragraph for the phrase sit amet
occurance_sit_amet=re.findall(regex,replace_results)
print(len(occurance_sit_amet))

print(occurance_sit_amet)







