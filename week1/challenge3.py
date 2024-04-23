import requests
import json

def get_astronaut_squirrel(name,n=2000):

    squirrel_spaceship = {}
    for i in range(1,n+1):
        try:
            x = requests.get('https://scrappyart.s3.ap-south-1.amazonaws.com/json/' + str(i), stream = True)
        except:
            print("Unable to extact image details from :",i)

        data = json.loads(x.text)
 
        if (i%200==0):
            print("Extracting squirell: ",i)

        try:
            yy = [i['value'] for i in data['attributes'] if name in i['value'].lower()]
            if(len(yy)!=0):
                squirrel_spaceship[yy[0]] = data['name'].split('#')[1]
                # print(yy[0])
                # print(data['name'].split('#')[1])
        except: 
            pass
        
    return squirrel_spaceship


n=2000
name = 'astronaut'

squirrel_spaceship = get_astronaut_squirrel(name,n)
print(squirrel_spaceship)