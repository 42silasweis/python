#Makes tnt fall and explode, kind of like vanilla. Sadly, only one tnt can be going at a time.

from mcpi.minecraft import Minecraft
from mcpi import block
from mcpi import event
from time import sleep

#def init():
 #   mc = Minecraft.create("127.0.0.1", 4711)
  #  return mc

def init():
    mc = Minecraft.create("10.183.3.25", 4711)
    return mc

def tnt(mc,x,y,z):
    for each in range(30):
        for other in range(1):
            mc.setBlock(x,y,z,2)
            sleep(0.1)
            mc.setBlock(x,y,z,3)
            sleep(0.025)
        if mc.getBlock(x,y-1,z)==0:
            mc.setBlock(x,y,z,0)
            y=y-7
    mc.postToChat("SSSSSssssss.......")
    sphere(mc,x,y,z)

def sphere(mc,x,y,z):
    radius=50
    for x1 in range(radius*-1,radius+1):
        for y1 in range(radius*-1,radius+1):
            for z1 in range(radius*-1,radius+1):
                if (x1**2)+(y1**2)+(z1**2)<=(radius+1)**2:
                        mc.setBlocks(x-0, y+0, z+2, x-0, y+0, z+3, 35,13)
                        mc.setBlocks(x-0, y+0, z+4, x-0, y+0, z+4, 35,15)
                        mc.setBlocks(x-0, y+0, z+5, x-0, y+0, z+6, 35,13)
                        mc.setBlocks(x-0, y+0, z+7, x-0, y+0, z+7, 35,15)
                        mc.setBlocks(x-0, y+0, z+8, x-0, y+0, z+9, 35,13)
                        mc.setBlocks(x-0, y+1, z+2, x-0, y+1, z+3, 35,13)
                        mc.setBlocks(x-0, y+1, z+4, x-0, y+1, z+7, 35,15)
                        mc.setBlocks(x-0, y+1, z+8, x-0, y+1, z+9, 35,13)
                        mc.setBlocks(x-0, y+2, z+2, x-0, y+2, z+3, 35,13)
                        mc.setBlocks(x-0, y+2, z+4, x-0, y+2, z+7, 35,15)
                        mc.setBlocks(x-0, y+2, z+8, x-0, y+2, z+9, 35,13)
                        mc.setBlocks(x-0, y+3, z+2, x-0, y+3, z+4, 35,13)
                        mc.setBlocks(x-0, y+3, z+5, x-0, y+3, z+6, 35,15)
                        mc.setBlocks(x-0, y+3, z+7, x-0, y+3, z+9, 35,13)
                        mc.setBlocks(x-0, y+4, z+2, x-0, y+4, z+2, 35,13)
                        mc.setBlocks(x-0, y+4, z+3, x-0, y+4, z+4, 35,15)
                        mc.setBlocks(x-0, y+4, z+5, x-0, y+4, z+6, 35,13)
                        mc.setBlocks(x-0, y+4, z+7, x-0, y+4, z+8, 35,15)
                        mc.setBlocks(x-0, y+4, z+9, x-0, y+4, z+9, 35,13)
                        mc.setBlocks(x-0, y+5, z+2, x-0, y+5, z+2, 35,13)
                        mc.setBlocks(x-0, y+5, z+3, x-0, y+5, z+4, 35,15)
                        mc.setBlocks(x-0, y+5, z+5, x-0, y+5, z+6, 35,13)
                        mc.setBlocks(x-0, y+5, z+7, x-0, y+5, z+8, 35,15)
                        mc.setBlocks(x-0, y+5, z+9, x-0, y+5, z+9, 35,13)
                        mc.setBlocks(x-0, y+6, z+2, x-0, y+6, z+9, 35,13)
                        mc.setBlocks(x-0, y+7, z+2, x-0, y+7, z+9, 35,13)

                        
                        mc.setBlocks(x+0, y+0, z-1, x+0, y+0, z-8, 35,15)                    
                        mc.setBlocks(x-0, y+0, z-8, x-0, y+0, z-22, 0)
                        mc.setBlocks(x-0, y+1, z-25, x-0, y+1, z-31, 35,15)
                        mc.setBlocks(x-0, y+1, z-1, x-0, y+1, z-1, 35,15)
                        mc.setBlocks(x-0, y+1, z-7, x-0, y+1, z-8, 35,15)
                        mc.setBlocks(x-0, y+2, z-22, x-0, y+2, z-24, 35,15)
                        mc.setBlocks(x-0, y+2, z-31, x-0, y+2, z-31, 35,15)
                        mc.setBlocks(x-0, y+1, z-2, x-0, y+1, z-2, 35,7)
                        mc.setBlocks(x-0, y+1, z-3, x-0, y+1, z-7, 5)
                        mc.setBlocks(x-0, y+2, z-25, x-0, y+2, z-27, 35,11)
                        mc.setBlocks(x-0, y+2, z-28, x-0, y+2, z-30, 5)
                        mc.setBlocks(x-0, y+2, z-2, x-0, y+2, z-2, 35,15)
                        mc.setBlocks(x-0, y+2, z-3, x-0, y+2, z-5, 35,7)
                        mc.setBlocks(x-0, y+2, z-6, x-0, y+2, z-7, 35,11)
                        mc.setBlocks(x-0, y+2, z-8, x-0, y+2, z-8, 35,15)
                        mc.setBlocks(x-0, y+3, z-3, x-0, y+3, z-3, 35,15)
                        mc.setBlocks(x-0, y+3, z-4, x-0, y+3, z-4, 35,11)
                        mc.setBlocks(x-0, y+3, z-5, x-0, y+3, z-6, 35,7)
                        mc.setBlocks(x-0, y+3, z-7, x-0, y+3, z-7, 35,11)
                        mc.setBlocks(x-0, y+3, z-8, x-0, y+3, z-8, 35,15)
                        mc.setBlocks(x-0, y+3, z-22, x-0, y+3, z-22, 35,15)
                        mc.setBlocks(x-0, y+3, z-23, x-0, y+3, z-28, 35,11)
                        mc.setBlocks(x-0, y+3, z-29, x-0, y+3, z-30, 35,15)
                        mc.setBlocks(x-0, y+4, z-4, x-0, y+4, z-9, 35,15)
                        mc.setBlocks(x-0, y+4, z-22, x-0, y+4, z-22, 35,15)
                        mc.setBlocks(x-0, y+4, z-23, x-0, y+4, z-23, 35,11)
                        mc.setBlocks(x-0, y+4, z-24, x-0, y+4, z-28, 35,15)
                        mc.setBlocks(x-0, y+5, z-5, x-0, y+5, z-5, 35,15)
                        mc.setBlocks(x-0, y+5, z-6, x-0, y+5, z-7, 35,7)
                        mc.setBlocks(x-0, y+5, z-8, x-0, y+5, z-9, 35,15)
                        mc.setBlocks(x-0, y+5, z-23, x-0, y+5, z-23, 35,15)
                        mc.setBlocks(x-0, y+5, z-24, x-0, y+5, z-25, 35,11)
                        mc.setBlocks(x-0, y+5, z-26, x-0, y+5, z-26, 35,15)
                        mc.setBlocks(x-0, y+6, z-5, x-0, y+6, z-10, 35,15)
                        mc.setBlocks(x-0, y+6, z-23, x-0, y+6, z-26, 35,15)
                        mc.setBlocks(x-0, y+7, z-6, x-0, y+7, z-6, 35,15)
                        mc.setBlocks(x-0, y+7, z-7, x-0, y+7, z-10, 35,1)
                        mc.setBlocks(x-0, y+7, z-11, x-0, y+7, z-11, 35,15)
                        mc.setBlocks(x-0, y+7, z-22, x-0, y+7, z-27, 35,15)
                        mc.setBlocks(x-0, y+8, z-5, x-0, y+9, z-12, 35,15)
                        mc.setBlocks(x-0, y+8, z-6, x-0, y+9, z-11, 35,1)
                        mc.setBlocks(x-0, y+8, z-22, x-0, y+12, z-27, 35,15)
                        mc.setBlocks(x-0, y+8, z-23, x-0, y+12, z-26, 35,1)
                        mc.setBlocks(x-0, y+10, z-6, x-0, y+10, z-13, 35,15)
                        mc.setBlocks(x-0, y+10, z-7, x-0, y+10, z-12, 35,1)
                        mc.setBlocks(x-0, y+11, z-7, x-0, y+12, z-14, 35,15)
                        mc.setBlocks(x-0, y+11, z-8, x-0, y+12, z-13, 35,1)
                        mc.setBlocks(x-0, y+12, z-8, x-0, y+12, z-14, 35,15)
                        mc.setBlocks(x-0, y+12, z-8, x-0, y+12, z-13, 35,1)
                        mc.setBlocks(x-0, y+13, z-8, x-0, y+13, z-15, 35,15)
                        mc.setBlocks(x-0, y+13, z-9, x-0, y+13, z-14, 35,1)
                        
def checkBlock(mc):
    blockEvent=mc.events.pollBlockHits()
    for each in blockEvent:
        x=each.pos.x
        y=each.pos.y
        z=each.pos.z
        if mc.getBlock(x,y,z)==2:
            tnt(mc,x,y,z)

def main():
    mc=init()
    while True:
        checkBlock(mc)

main()
