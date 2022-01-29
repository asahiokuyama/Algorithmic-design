import rhinoscriptsyntax as rs
import random 

#text_layer
name = "text"
color = rs.CreateColor([0,0,0])
visiable = True
loocked = False
parent = "grid"
textlayer = rs.AddLayer(name,color,visiable,parent)

#color
name = "under900"
color_under900 = rs.CreateColor([255,0,0])
visiable = True
loocked = False
parent = None
under900Layer = rs.AddLayer(name,color_under900,visiable,parent)

name = "over900"
color_over900 = rs.CreateColor([0,0,0])
visiable = True
loocked = False
parent = None
over900Layer = rs.AddLayer(name,color_over900,visiable,parent)


wPitch = 0
dPitch = 0
hPitch = 0

number = 1

for i in range(0,10):
    for j in range(0,10):
        W = random.randint(300,1800)#width
        D = random.randint(300,1800)#depth
        H = random.randint(300,1800)#height

        point1 = [wPitch,D+dPitch,hPitch]
        point2 = [wPitch,dPitch,hPitch]
        point3 = [W+wPitch,dPitch,hPitch]
        point4 = [W+wPitch,D+dPitch,hPitch]
        point5 = [wPitch,D+dPitch,H]
        point6 = [wPitch,dPitch,H]
        point7 = [W+wPitch,dPitch,H]
        point8 = [W+wPitch,D+dPitch,H]

        corners = [point1,point2,point3,point4,point5,point6,point7,point8]

        
        no_text = "No."+str(number)
        text ="W"+str(W) + "D" + str(D)+"H"+str(H)
        no_point = [wPitch,dPitch-500,hPitch]
        point = [wPitch,dPitch-1000,hPitch]
        height = 20
        font = "Arial"
        font_style = 0
        justification = 2+262144
        rs.AddText(no_text,no_point,height,font,font_style,justification)
        rs.AddText(text,point,height,font,font_style,justification)
            
        if H>=900:
            BoxID = rs.AddBox(corners)
            rs.ObjectLayer(BoxID,under900Layer)
        elif H<900:
            print("ss")
            BoxID = rs.AddBox(corners)
            rs.ObjectLayer(BoxID,over900Layer)
        
        
        
        wPitch += 4000
        number += 1
    dPitch += 4000
    wPitch = 0

