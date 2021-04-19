import csv
import os
import pandas

#Gets the CSV file via Pandas and detects the header of the columns
col_list = ["No.", 'PosX', "PosY", "PosZ", "Rx", "Ry", "Rz", "DWNx", "DWNy", "DWNz", "Lx", "Ly", "Lz", "DLx", "DLy", "DLz", "DRx", "DRy", "DRz", "CLx", "CLy", "CLz", "CRx", "CRy", "CRz", "CDLx", "CDLy", "CDLz", "CDRx", "CDRy", "CDRz", "PLx", "PLy", "PLz", "PRx", "PRy", "PRz", "PDLx", "PDLy", "PDLz", "PDRx", "PDRy", "PDRz"]
allCols = pandas.read_csv("rmc.csv", usecols = col_list)
#Each variable is assigned to the corresponding column list
number = allCols["No."]
posx = allCols["PosX"]
posy =  allCols["PosY"]
posz = allCols["PosZ"]
rx = allCols["Rx"]
ry = allCols["Ry"]
rz = allCols["Rz"]
dwnx = allCols["DWNx"]
dwny = allCols["DWNy"]
dwnz = allCols["DWNz"]
lx = allCols["Lx"]
ly = allCols["Ly"]
lz = allCols["Lz"]
dlx = allCols["DLx"]
dly = allCols["DLy"]
dlz = allCols["DLz"]
drx = allCols["DRx"]
dry = allCols["DRy"]
drz = allCols["DRz"]
clx = allCols["CLx"]
cly = allCols["CLy"]
clz = allCols["CLz"]
crx = allCols["CRx"]
cry = allCols["CRy"]
crz = allCols["CRz"]
cdlx = allCols["CDLx"]
cdly = allCols["CDLy"]
cdlz = allCols["CDLz"]
cdrx = allCols["CDRx"]
cdry = allCols["CDRy"]
cdrz = allCols["CDRz"]
plx = allCols["PLx"]
ply = allCols["PLy"]
plz = allCols["PLz"]
prx = allCols["PRx"]
pry = allCols["PRy"]
prz = allCols["PRz"]
pdlx = allCols["PDLx"]
pdly = allCols["PDLy"]
pdlz = allCols["PDLz"]
pdrx = allCols["PDRx"]
pdry = allCols["PDRy"]
pdrz = allCols["PDRz"]
groupSize = input("Enter your group size: ")
groupSize = int(groupSize)
def grouping(startInd, size, lisx, lisy, lisz): #function to make an array of variable size from base array
    a = []
    b = []
    c = []
    group = []
    startInd -= 1
    end = startInd + size
    while(startInd < end):
        a.append(lisx[startInd])
        b.append(lisy[startInd])
        c.append(lisz[startInd])
        startInd+=1
    group.append(a)
    group.append(b)
    group.append(c)
    return group
groups = int((len(number)//groupSize) + 1) #Calculate total number of sections based group size
groups += int(groups//groupSize + 1) #Readjust for error
multiplier = 0
startMul = 1
counter = 0
for part in range(groups):
    counter+=1
    pathname = "Section" + (str(counter))
    adder = startMul+groupSize
    if (adder > len(number)): #Check if section will surpass the end of the input list
        diff =  adder - len(number) - 1
        groupSize -= diff
        grouppos = grouping(startMul,groupSize, posx, posy, posz)
        groupr = grouping(startMul,groupSize, rx, ry, rz)
        groupdwn = grouping(startMul,groupSize, dwnx, dwny, dwnz)
        groupl = grouping(startMul,groupSize, lx, ly, lz)
        groupdl = grouping(startMul,groupSize, dlx, dly, dlz)
        groupdr = grouping(startMul,groupSize, drx, dry, drz)
        groupcl = grouping(startMul,groupSize, clx, cly, clz)
        groupcr = grouping(startMul,groupSize, crx, cry, crz)
        groupcdl = grouping(startMul,groupSize, cdlx, cdly, cdlz)
        groupcdr = grouping(startMul,groupSize, cdrx, cdry, cdrz)
        grouppl = grouping(startMul,groupSize, plx, ply, plz)
        grouppr = grouping(startMul,groupSize, prx, pry, prz)
        grouppdl = grouping(startMul,groupSize, pdlx, pdly, pdlz)
        grouppdr = grouping(startMul,groupSize, pdrx, pdry, pdrz)
        os.mkdir(pathname) #Create directory
        os.chdir(pathname) #Navigate to directory
        textFilCenter = "Center" + str(counter) + ".txt"
        textFilRight = "Right" + str(counter) + ".txt"
        textFilDown = "Down" + str(counter) + ".txt"
        textFilLeft = "Left" + str(counter) + ".txt"
        textFilDownLeft = "DownLeft" + str(counter) + ".txt"
        textFilDownRight = "DownRight" + str(counter) + ".txt"
        textFilCenterLeft = "CenterLeft" + str(counter) + ".txt"
        textFilCenterRight = "CenterRight" + str(counter) + ".txt"
        textFilCenterDownLeft = "CenterDownLeft" + str(counter) + ".txt"
        textFilCenterDownRight = "CenterDownRight" + str(counter) + ".txt"
        textFilPlateLeft = "PlateLeft" + str(counter) + ".txt"
        textFilPlateRight = "PlateRight" + str(counter) + ".txt"
        textFilPlateDownLeft = "PlateDownLeft" + str(counter) + ".txt"
        textFilPlateDownRight = "PlateDownRight" + str(counter) + ".txt"
        zerogrouppos = grouppos[0]
        onegrouppos = grouppos[1]
        twogrouppos = grouppos[2]
        zerogroupr = groupr[0]
        onegroupr = groupr[1]
        twogroupr = groupr[2]
        zerogroupdwn = groupdwn[0]
        onegroupdwn = groupdwn[1]
        twogroupdwn = groupdwn[2]
        zerogroupl = groupl[0]
        onegroupl = groupl[1]
        twogroupl = groupl[2]
        zerogroupdl = groupdl[0]
        onegroupdl = groupdl[1]
        twogroupdl = groupdl[2]
        zerogroupdr = groupdr[0]
        onegroupdr = groupdr[1]
        twogroupdr = groupdr[2]
        zerogroupcl = groupcl[0]
        onegroupcl = groupcl[1]
        twogroupcl = groupcl[2]
        zerogroupcr = groupcr[0]
        onegroupcr = groupcr[1]
        twogroupcr = groupcr[2]
        zerogroupcdl = groupcdl[0]
        onegroupcdl = groupcdl[1]
        twogroupcdl = groupcdl[2]
        zerogroupcdr = groupcdr[0]
        onegroupcdr = groupcdr[1]
        twogroupcdr = groupcdr[2]
        zerogrouppl = grouppl[0]
        onegrouppl = grouppl[1]
        twogrouppl = grouppl[2]
        zerogrouppr = grouppr[0]
        onegrouppr = grouppr[1]
        twogrouppr = grouppr[2]
        zerogrouppdl = grouppdl[0]
        onegrouppdl = grouppdl[1]
        twogrouppdl = grouppdl[2]
        zerogrouppdr = grouppdr[0]
        onegrouppdr = grouppdr[1]
        twogrouppdr = grouppdr[2]
        with open(textFilCenter, 'w') as f:   #Creates 1 .txt file including 3 columns (x, y, z) from the segmented arrays for each output
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogrouppos,onegrouppos,twogrouppos))
        with open(textFilRight, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogroupr,onegroupr,twogroupr))
        with open(textFilDown, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogroupdwn,onegroupdwn,twogroupdwn))
        with open(textFilLeft, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogroupl,onegroupl,twogroupl))
        with open(textFilDownLeft, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogroupdl,onegroupdl,twogroupdl))
        with open(textFilDownRight, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogroupdr,onegroupdr,twogroupdr))
        with open(textFilCenterLeft, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogroupcl,onegroupcl,twogroupcl))
        with open(textFilCenterRight, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogroupcr,onegroupcr,twogroupcr))
        with open(textFilCenterDownLeft, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogroupcdl,onegroupcdl,twogroupcdl))
        with open(textFilCenterDownRight, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogroupcdr,onegroupcdr,twogroupcdr))
        with open(textFilPlateLeft, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogrouppl,onegrouppl,twogrouppl))
        with open(textFilPlateRight, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogrouppr,onegrouppr,twogrouppr))
        with open(textFilPlateDownLeft, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogrouppdl,onegrouppdl,twogrouppdl))
        with open(textFilPlateDownRight, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogrouppdr,onegrouppdr,twogrouppdr))
        os.chdir("/Users/peter/Documents/3D3/")
    else:
        grouppos = grouping(startMul,groupSize, posx, posy, posz)
        groupr = grouping(startMul,groupSize, rx, ry, rz)
        groupdwn = grouping(startMul,groupSize, dwnx, dwny, dwnz)
        groupl = grouping(startMul,groupSize, lx, ly, lz)
        groupdl = grouping(startMul,groupSize, dlx, dly, dlz)
        groupdr = grouping(startMul,groupSize, drx, dry, drz)
        groupcl = grouping(startMul,groupSize, clx, cly, clz)
        groupcr = grouping(startMul,groupSize, crx, cry, crz)
        groupcdl = grouping(startMul,groupSize, cdlx, cdly, cdlz)
        groupcdr = grouping(startMul,groupSize, cdrx, cdry, cdrz)
        grouppl = grouping(startMul,groupSize, plx, ply, plz)
        grouppr = grouping(startMul,groupSize, prx, pry, prz)
        grouppdl = grouping(startMul,groupSize, pdlx, pdly, pdlz)
        grouppdr = grouping(startMul,groupSize, pdrx, pdry, pdrz)
        startMul+=groupSize-1 #Adjusts the group size to fix a problem involving 3D modeling
        os.mkdir(pathname)
        os.chdir(pathname)
        textFilCenter = "Center" + str(counter) + ".txt"
        textFilRight = "Right" + str(counter) + ".txt"
        textFilDown = "Down" + str(counter) + ".txt"
        textFilLeft = "Left" + str(counter) + ".txt"
        textFilDownLeft = "DownLeft" + str(counter) + ".txt"
        textFilDownRight = "DownRight" + str(counter) + ".txt"
        textFilCenterLeft = "CenterLeft" + str(counter) + ".txt"
        textFilCenterRight = "CenterRight" + str(counter) + ".txt"
        textFilCenterDownLeft = "CenterDownLeft" + str(counter) + ".txt"
        textFilCenterDownRight = "CenterDownRight" + str(counter) + ".txt"
        textFilPlateLeft = "PlateLeft" + str(counter) + ".txt"
        textFilPlateRight = "PlateRight" + str(counter) + ".txt"
        textFilPlateDownLeft = "PlateDownLeft" + str(counter) + ".txt"
        textFilPlateDownRight = "PlateDownRight" + str(counter) + ".txt"
        zerogrouppos = grouppos[0]
        onegrouppos = grouppos[1]
        twogrouppos = grouppos[2]
        zerogroupr = groupr[0]
        onegroupr = groupr[1]
        twogroupr = groupr[2]
        zerogroupdwn = groupdwn[0]
        onegroupdwn = groupdwn[1]
        twogroupdwn = groupdwn[2]
        zerogroupl = groupl[0]
        onegroupl = groupl[1]
        twogroupl = groupl[2]
        zerogroupdl = groupdl[0]
        onegroupdl = groupdl[1]
        twogroupdl = groupdl[2]
        zerogroupdr = groupdr[0]
        onegroupdr = groupdr[1]
        twogroupdr = groupdr[2]
        zerogroupcl = groupcl[0]
        onegroupcl = groupcl[1]
        twogroupcl = groupcl[2]
        zerogroupcr = groupcr[0]
        onegroupcr = groupcr[1]
        twogroupcr = groupcr[2]
        zerogroupcdl = groupcdl[0]
        onegroupcdl = groupcdl[1]
        twogroupcdl = groupcdl[2]
        zerogroupcdr = groupcdr[0]
        onegroupcdr = groupcdr[1]
        twogroupcdr = groupcdr[2]
        zerogrouppl = grouppl[0]
        onegrouppl = grouppl[1]
        twogrouppl = grouppl[2]
        zerogrouppr = grouppr[0]
        onegrouppr = grouppr[1]
        twogrouppr = grouppr[2]
        zerogrouppdl = grouppdl[0]
        onegrouppdl = grouppdl[1]
        twogrouppdl = grouppdl[2]
        zerogrouppdr = grouppdr[0]
        onegrouppdr = grouppdr[1]
        twogrouppdr = grouppdr[2]
        with open(textFilCenter, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogrouppos,onegrouppos,twogrouppos))
        with open(textFilRight, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogroupr,onegroupr,twogroupr))
        with open(textFilDown, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogroupdwn,onegroupdwn,twogroupdwn))
        with open(textFilLeft, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogroupl,onegroupl,twogroupl))
        with open(textFilDownLeft, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogroupdl,onegroupdl,twogroupdl))
        with open(textFilDownRight, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogroupdr,onegroupdr,twogroupdr))
        with open(textFilCenterLeft, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogroupcl,onegroupcl,twogroupcl))
        with open(textFilCenterRight, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogroupcr,onegroupcr,twogroupcr))
        with open(textFilCenterDownLeft, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogroupcdl,onegroupcdl,twogroupcdl))
        with open(textFilCenterDownRight, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogroupcdr,onegroupcdr,twogroupcdr))
        with open(textFilCenterDownRight, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogrouppl,onegrouppl,twogrouppl))
        with open(textFilPlateLeft, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogrouppl,onegrouppl,twogrouppl))
        with open(textFilPlateRight, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogrouppr,onegrouppr,twogrouppr))
        with open(textFilPlateDownLeft, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogrouppdl,onegrouppdl,twogrouppdl))
        with open(textFilPlateDownRight, 'w') as f:
            writer = csv.writer(f, delimiter = '\t')
            writer.writerows(zip(zerogrouppdr,onegrouppdr,twogrouppdr))
        os.chdir("/Users/peter/Documents/3D3")