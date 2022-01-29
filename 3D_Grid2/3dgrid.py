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