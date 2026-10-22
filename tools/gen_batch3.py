import json,os,math,numpy as np
from PIL import Image,ImageDraw,ImageFilter,ImageChops,ImageFont
R='/workspace/rp/pack/assets/nexus';OUT='/workspace/launch/skins-preview/batch3';os.makedirs(OUT,exist_ok=True)
def H(h):h=h.lstrip('#');return tuple(int(h[i:i+2],16) for i in(0,2,4))
def mix(a,b,t):return tuple(int(a[i]+(b[i]-a[i])*t) for i in range(3))
# Khaos Nexus palette
PAL=dict(black='#0d0b10',char='#26212c',steel='#8f8aa0',red='#9e1622',storm='#d1312b',orange='#ff7a1a',ember='#ffc14a',
 soul='#2fb8ff',soulhi='#b8f1ff',deep='#0f2a4a',gold='#e0a83a',wood='#5a3424',woodhi='#8a5a3a',cream='#fff4dc',corn='#ffd23a',
 purple='#4a2370',violet='#8b4fd8',green='#64d46a',night='#141c44',nighthi='#2c3c8a',leaf='#2f8a3a',lime='#a6f05a',aqua='#3ff0e0',teal='#0c5560',mag='#e05cff',plum='#3a1050')
def cell(c1,c2,pat):
  a=H(PAL[c1]);b=H(PAL[c2]);im=Image.new('RGBA',(16,16))
  for y in range(16):
    for x in range(16):
      t=y/15
      if pat=='glow':t=min(1,math.hypot(x-7.5,y-7.5)/9)
      c=mix(b,a,1-t) if pat!='glow' else mix(a,b,t)
      if pat=='metal':
        s=max(0,1-abs((x+y)-12)/3);c=mix(c,(255,255,255),.35*s)
      if pat=='fuller' and x in(7,8):c=mix(c,(255,255,255),.25)
      if pat=='wood' and y%4==1:c=mix(c,(0,0,0),.25)
      if pat=='bands':c=H(PAL[[c1,c2,'cream'][(y//5)%3]])
      if pat!='glow':
        if x==0 or y==0:c=mix(c,(255,255,255),.28)
        if x==15 or y==15:c=mix(c,(0,0,0),.35)
      im.putpixel((x,y),c+(255,))
  return im
def B(f,t,m):return(f,t,m)
def sword(edge,blade,core,guard,grip,pom):
  M={'b':(edge,blade,'metal'),'c':(core,core,'glow'),'g':(guard,'black','metal'),'h':(grip,'black','wood'),'p':(pom,pom,'glow')}
  E=[B((7,9,7.5),(9,30,8.5),'b'),B((6.5,10,7.75),(7,28,8.25),'b'),B((9,10,7.75),(9.5,28,8.25),'b'),B((7.75,30,7.5),(8.25,31.5,8.5),'b'),
     B((7.75,11,7.25),(8.25,27,8.75),'c'),
     B((3,7,6.5),(13,9,9.5),'g'),B((2,7.5,7),(3,10,9),'g'),B((13,7.5,7),(14,10,9),'g'),B((6.5,8.5,6.75),(9.5,10,9.25),'g'),
     B((7,1,7),(9,7,9),'h'),B((6.5,-1,6.5),(9.5,1,9.5),'p')]
  return M,E
def scythe():
  M={'h':('wood','black','wood'),'r':('char','black','metal'),'b':('storm','red','metal'),'e':('ember','orange','metal'),'c':('soul','deep','glow')}
  E=[B((7,-6,7),(9,26,9),'h'),B((6.5,4,6.5),(9.5,6,9.5),'r'),B((6.5,24,6.5),(9.5,28,9.5),'r'),B((7.25,25,6.25),(8.75,27,9.75),'c')]
  for i,(x,y,w) in enumerate([(9,25,4),(12,24,4),(15,22.5,4),(18,20.5,3.5),(20.5,18,3),(22.5,15,2.5),(23.5,12,2)]):
    E.append(B((x-1,y-.5,7.5),(x+4,y+w,8.5),'b'));E.append(B((x-1,y-.5,7.4),(x+4,y+.3,8.6),'e'))
  return M,E
def pick():
  M={'h':('wood','black','wood'),'r':('char','black','metal'),'s':('steel','char','metal'),'e':('orange','red','metal'),'c':('soul','deep','glow')}
  E=[B((7,-6,7),(9,22,9),'h'),B((6.5,0,6.5),(9.5,2,9.5),'r'),B((5.5,20,6),(10.5,25,10),'r'),B((6.5,21,5.5),(9.5,24,10.5),'c')]
  for s in(-1,1):
    for i,(o,y,h) in enumerate([(2.5,20.5,4),(6,20,3.5),(9,19,3),(11.5,17.5,2.5),(13.5,15.5,2)]):
      x0=8+s*o;x1=x0+s*3.5
      E.append(B((min(x0,x1),y,7),(max(x0,x1),y+h,9),'s'));E.append(B((min(x0,x1),y,6.9),(max(x0,x1),y+.6,9.1),'e'))
  return M,E
def hat(base,hi,band,gem,bend):
  M={'a':(hi,base,'plain'),'b':(band,'black','metal'),'g':(gem,gem,'glow')}
  E=[B((-1,0,-1),(17,1.5,17),'a'),B((2,1.5,2),(14,5,14),'a'),B((2,1.5,1.75),(14,3,14.25),'b'),B((2,1.5,14),(14,3,14.25),'b'),B((7,1.6,1.3),(9,3.4,1.75),'g')]
  s=11;x=2.5;y=5;z=2.5;dx=0
  for i in range(11):
    s*=0.86;dx+=bend*i*.12
    E.append(B((8-s/2+dx,y,8-s/2),(8+s/2+dx,y+1.5,8+s/2),'a'));y+=1.5
  E.append(B((7.2+dx+bend,y,7.2),(8.8+dx+bend*1.8,y+1.6,8.8),'g'))
  return M,E
def altar():
  M={'k':('char','black','plain'),'r':('storm','red','metal'),'o':('ember','orange','metal'),'c':('soul','deep','glow'),'v':('soulhi','soul','glow')}
  E=[B((0,0,0),(16,3,16),'k'),B((1,3,1),(15,5,15),'r'),B((2,5,2),(14,7,14),'k'),B((1.5,6.8,1.5),(14.5,7.3,14.5),'o')]
  for x,z in((1,1),(12,1),(1,12),(12,12)):E+= [B((x,7,z),(x+3,13,z+3),'k'),B((x+.5,13,z+.5),(x+2.5,15,z+2.5),'c')]
  E+=[B((5,7,5),(11,8.5,11),'r'),B((6.5,9.5,6.5),(9.5,15.5,9.5),'v'),B((7.25,15.5,7.25),(8.75,17,8.75),'v'),B((7.25,8.5,7.25),(8.75,9.5,8.75),'c')]
  return M,E
def harvester(g1='orange',g2='red',tr=('ember','orange','metal'),top='mine'):
  M={'k':('char','black','plain'),'s':('steel','char','metal'),'o':(g1,g2,'glow'),'e':tr,'c':('soul','deep','glow')}
  E=[B((0,0,0),(16,2,16),'s'),B((1,2,1),(15,13,15),'k'),B((0,13,0),(16,16,16),'s'),B((3,4,0.6),(13,11,1),'o'),B((3,4,15),(13,11,15.4),'o'),B((0.6,4,3),(1,11,13),'o'),B((15,4,3),(15.4,11,13),'o')]
  for x,z in((0,0),(14,0),(0,14),(14,14)):E.append(B((x,2,z),(x+2,13,z+2),'s'))
  E.append(B((2,15.5,2),(14,16.2,14),'e'))
  if top=='mine':E+=[B((5,16,5),(11,18,11),'s'),B((6.5,18,6.5),(9.5,20,9.5),'c')]
  elif top=='farm':
    M['w']=('wood','black','wood');M['l']=('lime','leaf','glow');M['g']=('leaf','black','plain')
    E+=[B((3,16,3),(13,17,13),'w')]
    for x,z,h in((4,4,4),(7,5,5.5),(10,4,4.5),(5,8,5),(9,9,6),(4,11,4),(11,11,5),(7.5,11,4.5)):
      E+=[B((x,17,z),(x+.8,17+h,z+.8),'g'),B((x-.3,17+h,z-.3),(x+1.1,17+h+1.6,z+1.1),'l')]
  elif top=='fish':
    M['w']=('teal','black','metal');M['a']=('aqua','teal','glow');M['p']=('wood','black','wood')
    E+=[B((3,16,3),(13,17,13),'w'),B((4,16.6,4),(12,17.2,12),'a'),B((12,16,12),(13.2,26,13.2),'p'),B((6,25,12.1),(12,25.8,13),'p'),B((6,21,12.3),(6.4,25,12.7),'s'),B((6,20,12.3),(7.8,20.6,12.7),'s'),B((7.4,20,12.3),(7.8,21.4,12.7),'s'),B((5.4,19,12.2),(6.6,20,12.8),'a')]
  elif top=='ess':
    M['w']=('plum','black','metal');M['m']=('mag','violet','glow')
    E+=[B((5,16,5),(11,17.5,11),'w')]
    for x,z in((5,5),(10,5),(5,10),(10,10)):E.append(B((x,17.5,z),(x+1,20,z+1),'w'))
    for a,y0,y1 in((1,19,20),(2,20,21.2),(3.2,21.2,23),(2,23,24.2),(1,24.2,25.4)):E.append(B((8-a/2*1.1,y0,8-a/2*1.1),(8+a/2*1.1,y1,8+a/2*1.1),'m'))
  return M,E
ITEMS=[
 ('ember_blade','Ember Blade','Moonlantern Crate','sword',sword('ember','storm','orange','char','wood','orange')),
 ('frostbloom_blade','Soulfrost Blade','Moonlantern Crate','sword',sword('soulhi','soul','soul','char','deep','soulhi')),
 ('rift_scythe','Rift Scythe','Moonlantern Crate','sword',scythe()),
 ('starforge_pickaxe','Starforge Pickaxe','Moonlantern Crate','tool',pick()),
 ('starry_hat','Starry Wizard Hat','Moonlantern Crate','hat',hat('night','nighthi','gold','soulhi',0)),
 ('cozy_witch_hat','Cozy Witch Hat','Harvest Stand (Halloween)','hat',hat('purple','violet','orange','green',0.9)),
 ('candy_corn_saber','Candy Corn Saber','Lantern Chest (Halloween)','sword',sword('cream','orange','corn','char','black','orange')),
 ('rift_altar','Rift Altar','Rift Altar (custom block)','block',altar()),
 ('harvester_mining','Mining Harvester','Harvesters (custom block)','block',harvester()),
 ('harvester_farming','Farming Harvester','Harvesters (custom block)','block',harvester('lime','leaf',('woodhi','wood','wood'),'farm')),
 ('harvester_fishing','Fishing Harvester','Harvesters (custom block)','block',harvester('aqua','teal',('soulhi','soul','metal'),'fish')),
 ('harvester_essence','Essence Harvester','Harvesters (custom block)','block',harvester('mag','plum',('violet','purple','metal'),'ess')),
]
for id,_,_,_,(M,E) in ITEMS:
  if id=='candy_corn_saber':M['b']=('corn','orange','bands')
DISP={'sword':{'gui':{'rotation':[0,0,-45],'translation':[0,0,0],'scale':[0.55,0.55,0.55]},'thirdperson_righthand':{'rotation':[0,-90,0],'translation':[0,4,1],'scale':[0.85,0.85,0.85]},'firstperson_righthand':{'rotation':[0,-90,25],'translation':[1,3,1],'scale':[0.68,0.68,0.68]},'ground':{'scale':[0.4,0.4,0.4]}},
 'hat':{'head':{'translation':[0,14.5,0],'scale':[1,1,1]},'gui':{'rotation':[25,45,0],'scale':[0.5,0.5,0.5]}},
 'block':{'gui':{'rotation':[30,225,0],'scale':[0.55,0.55,0.55]},'ground':{'scale':[0.25,0.25,0.25]}}}
DISP['tool']=DISP['sword']
FACES={'north':(2,0),'south':(2,1),'west':(0,0),'east':(0,1),'down':(1,0),'up':(1,1)}
def build(id,M,E,kind):
  keys=list(M);atlas=Image.new('RGBA',(64,64));cells={}
  for i,k in enumerate(keys):
    c=cell(*M[k]);atlas.paste(c,((i%4)*16,(i//4)*16));cells[k]=c
  sub='block' if kind=='block' else 'item'
  atlas.save(f'{R}/textures/{sub}/{id}.png')
  els=[]
  for f,t,m in E:
    i=keys.index(m);u0,v0=(i%4)*4,(i//4)*4
    e={'from':list(f),'to':list(t),'faces':{fn:{'uv':[u0,v0,u0+4,v0+4],'texture':'#0'} for fn in FACES}}
    if M[m][2]=='glow':e['light_emission']=15
    els.append(e)
  mdl={'credit':'Khaos Nexus','texture_size':[64,64],'textures':{'0':f'nexus:{sub}/{id}','particle':f'nexus:{sub}/{id}'},'elements':els,'display':DISP[kind]}
  json.dump(mdl,open(f'{R}/models/{sub}/{id}.json','w'),indent=1)
  json.dump({'model':{'type':'minecraft:model','model':f'nexus:{sub}/{id}'}},open(f'{R}/items/{id}.json','w'),indent=1)
  return cells
# ---- renderer (ortho, painter's, textured faces, glow) ----
def rot(yaw,pitch,roll):
  cy,sy,cp,sp,cr,sr=math.cos(yaw),math.sin(yaw),math.cos(pitch),math.sin(pitch),math.cos(roll),math.sin(roll)
  Rz=np.array([[cr,-sr,0],[sr,cr,0],[0,0,1]]);Ry=np.array([[cy,0,sy],[0,1,0],[-sy,0,cy]]);Rx=np.array([[1,0,0],[0,cp,-sp],[0,sp,cp]])
  return Rx@Ry@Rz
FIX={}
def render(E,M,cells,kind,S=1024):
  roll={'sword':-45,'tool':-45}.get(kind,0)
  Rm=rot(math.radians(-35),math.radians(22 if kind!='hat' else 28),math.radians(roll))
  L=np.array([-.5,.8,.6]);L/=np.linalg.norm(L)
  quads=[]
  for f,t,m in E:
    x0,y0,z0=f;x1,y1,z1=t
    fs=[((x0,y0,z1),(x1,y0,z1),(x1,y1,z1),(x0,y1,z1),(0,0,1)),((x1,y0,z0),(x0,y0,z0),(x0,y1,z0),(x1,y1,z0),(0,0,-1)),
        ((x1,y0,z1),(x1,y0,z0),(x1,y1,z0),(x1,y1,z1),(1,0,0)),((x0,y0,z0),(x0,y0,z1),(x0,y1,z1),(x0,y1,z0),(-1,0,0)),
        ((x0,y1,z1),(x1,y1,z1),(x1,y1,z0),(x0,y1,z0),(0,1,0)),((x0,y0,z0),(x1,y0,z0),(x1,y0,z1),(x0,y0,z1),(0,-1,0))]
    for *P,n in fs:
      n=Rm@np.array(n,float)
      if n[2]<=1e-6:continue
      P=[Rm@(np.array(p,float)-8) for p in P]
      quads.append((np.mean([p[2] for p in P]),P,n,m))
  allp=[p for q in quads for p in q[1]]
  if FIX.get(__import__('builtins').id(E)):allp+=[Rm@(np.array([x,y,z],float)-8) for x in(0,16) for y in(0,27) for z in(0,16)]
  allp=np.array(allp);mn=allp[:,:2].min(0);mx=allp[:,:2].max(0)
  sc=S*0.78/max(mx-mn);cen=(mn+mx)/2
  def scr(p):return(S/2+(p[0]-cen[0])*sc,S/2-(p[1]-cen[1])*sc)
  img=Image.new('RGBA',(S,S),(0,0,0,0));glow=Image.new('RGBA',(S,S),(0,0,0,0))
  for d,P,n,m in sorted(quads,key=lambda q:q[0]):
    em=M[m][2]=='glow'
    lam=1.0 if em else 0.42+0.68*max(0,float(n@L))
    rim=0 if em else max(0,1-abs(n[2]))**3*0.35
    tex=cells[m].convert('RGB').resize((64,64),Image.NEAREST)
    arr=np.clip(np.asarray(tex,float)*lam+np.array([90,140,255])*rim,0,255).astype('uint8');tex=Image.fromarray(arr)
    a,b,_,c=[scr(p) for p in P]
    # inverse affine: screen->tex. tex(0,63)=a? map a->(0,64),b->(64,64),c->(0,0)
    A=np.array([[a[0],a[1],1],[b[0],b[1],1],[c[0],c[1],1]])
    try:
      cu=np.linalg.solve(A,[0,64,0]);cv=np.linalg.solve(A,[64,64,0])
    except np.linalg.LinAlgError:continue
    w=tex.transform((S,S),Image.AFFINE,(*cu,*cv),Image.NEAREST)
    mask=Image.new('L',(S,S));ImageDraw.Draw(mask).polygon([scr(p) for p in P],fill=255)
    img.paste(w,(0,0),mask)
    if em:glow.paste(w,(0,0),mask)
  # backdrop
  bg=Image.new('RGBA',(S,S));yy,xx=np.mgrid[0:S,0:S];r=np.hypot(xx-S/2,yy-S*.45)/(S*.75)
  base=np.stack([mix(H('#2a1418'),H('#07070b'),min(1,v)) for v in np.linspace(0,1,256)])
  bg=Image.fromarray(np.concatenate([base[(np.clip(r,0,1)*255).astype(int)],np.full((S,S,1),255)],2).astype('uint8'),'RGBA')
  sh=Image.new('L',(S,S));ImageDraw.Draw(sh).ellipse((S*.25,S*.84,S*.75,S*.92),fill=150);sh=sh.filter(ImageFilter.GaussianBlur(S/40))
  bg=Image.composite(Image.new('RGBA',(S,S),(0,0,0,255)),bg,sh)
  al=img.split()[3].filter(ImageFilter.MaxFilter(5));outl=Image.new('RGBA',(S,S),(255,120,60,0));outl.putalpha(ImageChops.subtract(al,img.split()[3]).point(lambda v:v*0.35))
  bg.alpha_composite(outl);bg.alpha_composite(img)
  g=glow.filter(ImageFilter.GaussianBlur(S/45));bg=ImageChops.add(bg.convert('RGB'),g.convert('RGB').point(lambda v:int(v*.8))).convert('RGBA')
  g2=glow.filter(ImageFilter.GaussianBlur(S/14));bg=ImageChops.add(bg.convert('RGB'),g2.convert('RGB').point(lambda v:int(v*.5)))
  return bg.resize((512,512),Image.LANCZOS).filter(ImageFilter.UnsharpMask(1.6,70,2))
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',17) if os.path.exists('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf') else ImageFont.load_default()
F2=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',13) if os.path.exists('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf') else F
tiles=[]
for it in ITEMS:
  if it[0].startswith('harvester'):FIX[__import__('builtins').id(it[4][1])]=1
for id,name,crate,kind,(M,E) in ITEMS:
  cells=build(id,M,E,kind);im=render(E,M,cells,kind);im.save(f'{OUT}/{id}.png',optimize=True);tiles.append((im,name,crate))
W=300;cols=3;sh=Image.new('RGB',(cols*W,((len(tiles)+2)//3)*(W+44)),(10,9,13));d=ImageDraw.Draw(sh)
for k,(im,a,b) in enumerate(tiles):
  x=(k%3)*W;y=(k//3)*(W+44);sh.paste(im.resize((W-10,W-10),Image.LANCZOS),(x+5,y+5));d.text((x+12,y+W-2),a,fill=(255,200,140),font=F);d.text((x+12,y+W+19),b,fill=(140,200,255),font=F2)
sh.filter(ImageFilter.UnsharpMask(1,40,2)).save(f'{OUT}/contact_sheet.png',optimize=True)
json.dump([dict(id=i[0],name=i[1],crate=i[2],kind=i[3]) for i in ITEMS],open('/workspace/skins/b3/manifest.json','w'),indent=1)

H4=[Image.open(f'{OUT}/harvester_{k}.png') for k in ('mining','farming','fishing','essence')]
hs=Image.new('RGB',(4*480,520),(10,9,13));d=ImageDraw.Draw(hs)
for i,(im,n) in enumerate(zip(H4,('Mining','Farming','Fishing','Essence'))):
  hs.paste(im.resize((470,470),Image.LANCZOS),(i*480+5,5));d.text((i*480+20,482),n+' Harvester',fill=(255,200,140),font=F)
hs.filter(ImageFilter.UnsharpMask(1,40,2)).save(f'{OUT}/harvesters_set.png',optimize=True)
