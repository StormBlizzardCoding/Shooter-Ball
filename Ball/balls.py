img = 'image'
data = 'data'
name = 'name'
slot = 'slot'

def makedata(health, speed, **args):
    odata = args
    odata['health'] = int(health)

balls = [
    {name:'Little Bad Ball',
     img:'Ball00.png',
     data:makedata(20,10),
     slot:[4,[(0,50,0),(50,0,90),(0,-50,180),(-50,0,270)]]
     },{
     name:'Armoured Blues',
     img:'Ball01.png',
     data:makedata(25,10,armour=2),
     slot:[4,[(0,50,0),(50,0,90),(0,-50,180),(-50,0,270)]]
     },{
     name:'Square Plus 10',
     img:'Ball.png',
     data:makedata(30,10,bonusdamage=[10,0,0]),
     slot:[4,[(0,50,0),(50,0,90),(0,-50,180),(-50,0,270)]]
     }#,{
#     name:'',
#     img:'Ball.png',
#     data:makedata(20,10),
#     slot:[4,[(0,50,0),(50,0,90),(0,-50,180),(-50,0,270)]]
#     }#,{
#     name:'',
#     img:'Ball.png',
#     data:makedata(20,10),
#     slot:[4,[(0,50,0),(50,0,90),(0,-50,180),(-50,0,270)]]
#     }
     ]
