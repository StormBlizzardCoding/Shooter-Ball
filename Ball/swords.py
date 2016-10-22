img = 'image'
data = 'data'
name = 'name'

def makedata(damage, **args):
    odata = args
    odata['damage'] = int(damage)

balls = [
    {name:'Knife',
     bimg:'Sword00.png',
     data:makedata(1)
     }#,{
#     name:'',
#     img:'Sword.png',
#     data:makedata(1)
#     }#,{
#     name:'',
#     img:'Sword.png',
#     data:makedata(1)
#     }
     ]
