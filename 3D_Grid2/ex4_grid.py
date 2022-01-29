import rhinoscriptsyntax as rs

#print("hello worlds")

#point = [600,300,0]
#print("test")
#print(point)
#rs.AddPoint(point)

#start = [0,0,0]
#end = [300,300,0]
#rs.AddLine(start,end)

#text = "xo"
#point = [0,0,0]
#height = 20
#font = "Arial"
#font_style = 0
#justification = 2+262144

#rs.AddText(text, point, height, font, font_style, justification)

#t0 = [0,0,0]
#rs.AddPoint(t0)

#pt1 = [300,0,0]
#rs.AddPoint(pt1)

#pt2 = [600,0,0]
#rs.AddPoint(pt2)

xpitch = 100
xNum = 3
print("start")
for i in range(xNum):
    #point
    print(i)
    pt = [xpitch*i,0,0]
    rs.AddPoint(pt)
    
    #text
    text = "x"+str(i)
    point = [xpitch*i,-20,0]
    height = 20
    font = "Arial"
    font_style = 0
    justification = 2+262144
    rs.AddText(text, point, height, font, font_style, justification)
print("end")


import rhinoscriptsyntax as rs

print("start")
xNum = 5
yNum = 5
zNum = 5
xPitch = 150
yPitch = 100
zPitch = 300

for z in range(zNum):
    for y in range(yNum):
        for x in range(xNum):
            print("x=%s,y=%s,z=%s"%(x,y,z))
            #point
            pt = [xPitch*x,yPitch*y,zPitch*z]
            rs.AddPoint(pt)
            
            text = "X"+str(x) + "Y" + str(y)+"Z"+str(z)
            point = [xPitch*x,yPitch*y-20,zPitch*z]
            height = 20
            font = "Arial"
            font_style = 0
            justification = 2+262144
            rs.AddText(text,point,height,font,font_style,justification)
print("end")


#grid_layer
name = "grid"
color = rs.CreateColor([255,0,0])
visiable = True
loocked = False
parent = None
gridlayer = rs.AddLayer(name,color,visiable,parent)

#point_layer
name = "point"
color = rs.CreateColor([0,255,0])
visiable = True
loocked = False
parent = "grid"
pointlayer = rs.AddLayer(name,color,visiable,parent)

#text_layer
name = "text"
color = rs.CreateColor([0,0,0])
visiable = True
loocked = False
parent = "grid"
textlayer = rs.AddLayer(name,color,visiable,parent)

#x
name = "xLine"
color = rs.CreateColor([255,0,0])
visiable = True
loocked = False
parent = "grid"
xLinelayer = rs.AddLayer(name,color,visiable,parent)

#y
name = "yLine"
color = rs.CreateColor([0,255,0])
visiable = True
loocked = False
parent = "grid"
yLinelayer = rs.AddLayer(name,color,visiable,parent)

#z
name = "zLine"
color = rs.CreateColor([0,0,255])
visiable = True
loocked = False
parent = "grid"
zLinelayer = rs.AddLayer(name,color,visiable,parent)

for z in range(zNum):
    for y in range(yNum):
        for x in range(xNum):
            print("x=%s,y=%s,z=%s"%(x,y,z))
            #point
            pt = [xPitch*x,yPitch*y,zPitch*z]
            rs.AddPoint(pt)
            
            text = "X"+str(x) + "Y" + str(y)+"Z"+str(z)
            point = [xPitch*x,yPitch*y-20,zPitch*z]
            height = 20
            font = "Arial"
            font_style = 0
            justification = 2+262144
            rs.AddText(text,point,height,font,font_style,justification)
            
            if x<xNum-1:
                start = [xPitch*x,yPitch*y,zPitch*z]
                end = [xPitch*(x+1),yPitch*y,zPitch*z]
                rs.AddLine(start,end)
            if y<yNum-1:
                start = [xPitch*x,yPitch*y,zPitch*z]
                end = [xPitch*x,yPitch*(y+1),zPitch*z]
                rs.AddLine(start,end)
            if z<zNum-1:
                start = [xPitch*x,yPitch*y,zPitch*z]
                end = [xPitch*x,yPitch*y,zPitch*(z+1)]
                rs.AddLine(start,end)
                
print("end")

#最終結果

import rhinoscriptsyntax as rs

#grid_layer
name = "grid"
color = rs.CreateColor([255,0,0])
visiable = True
loocked = False
parent = None
gridlayer = rs.AddLayer(name,color,visiable,parent)

#point_layer
name = "point"
color = rs.CreateColor([0,255,0])
visiable = True
loocked = False
parent = "grid"
pointlayer = rs.AddLayer(name,color,visiable,parent)

#text_layer
name = "text"
color = rs.CreateColor([0,0,0])
visiable = True
loocked = False
parent = "grid"
textlayer = rs.AddLayer(name,color,visiable,parent)

#x
name = "xLine"
color = rs.CreateColor([255,0,0])
visiable = True
loocked = False
parent = "grid"
xLinelayer = rs.AddLayer(name,color,visiable,parent)

#y
name = "yLine"
color = rs.CreateColor([0,255,0])
visiable = True
loocked = False
parent = "grid"
yLinelayer = rs.AddLayer(name,color,visiable,parent)

#z
name = "zLine"
color = rs.CreateColor([0,0,255])
visiable = True
loocked = False
parent = "grid"
zLinelayer = rs.AddLayer(name,color,visiable,parent)

print("start")
xNum = 5
yNum = 5
zNum = 5
xPitch = 100
yPitch = 100
zPitch = 100

for z in range(zNum):
    for y in range(yNum):
        for x in range(xNum):
            print("x=%s,y=%s,z=%s"%(x,y,z))
            #point
            pt = [xPitch*x,yPitch*y,zPitch*z]
            pointID = rs.AddPoint(pt)
            rs.ObjectLayer(pointID,pointlayer)
            
            text = "X"+str(x) + "Y" + str(y)+"Z"+str(z)
            point = [xPitch*x,yPitch*y-20,zPitch*z]
            height = 20
            font = "Arial"
            font_style = 0
            justification = 2+262144
            textID = rs.AddText(text,point,height,font,font_style,justification)
            rs.ObjectLayer(textID,textlayer)
            
            if x<xNum-1:
                start = [xPitch*x,yPitch*y,zPitch*z]
                end = [xPitch*(x+1),yPitch*y,zPitch*z]
                xLineID = rs.AddLine(start,end)
                rs.ObjectLayer(xLineID,xLinelayer)
            if y<yNum-1:
                start = [xPitch*x,yPitch*y,zPitch*z]
                end = [xPitch*x,yPitch*(y+1),zPitch*z]
                yLineID = rs.AddLine(start,end)
                rs.ObjectLayer(yLineID,yLinelayer)
            if z<zNum-1:
                start = [xPitch*x,yPitch*y,zPitch*z]
                end = [xPitch*x,yPitch*y,zPitch*(z+1)]
                zLineID = rs.AddLine(start,end)
                rs.ObjectLayer(zLineID,zLinelayer)
                
print("end")