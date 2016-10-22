img = 'image'
data = 'data'
name = 'name'
bimg = 'bimg'
bslt = 'bslot'

def makedata(damage, rate, speed, **args):
    odata = args
    odata['damage'] = int(damage)
    odata['rate'] = int(rate)
    odata['speed'] = int(speed)

balls = [
    {name:'Simple Gun',
     img:'Gun00.png',
     bimg:'Bullet00.png',
     bslt:[(0,20)],
     data:makedata(1,5)
     }#,{
#     name:'',
#     img:'Gun.png',
#     bimg:'Bullet.png',
#     bslt:[(0,20)],
#     data:makedata(1,5)
#     }#,{
#     name:'',
#     img:'Gun.png',
#     bimg:'Bullet.png',
#     bslt:[(0,20)],
#     data:makedata(1,5)
#     }
     ]
