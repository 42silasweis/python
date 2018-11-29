#Makes tnt fall and explode, kind of like vanilla. Sadly, only one tnt can be going at a time.

from mcpi.minecraft import Minecraft
from mcpi import block
from mcpi import event
from time import sleep

def init():
    mc = Minecraft.create("127.0.0.1", 4711)
    return mc

def init():
    mc = Minecraft.create("10.183.3.9", 4711)
    return mc

def tnt(mc,x,y,z):
    for each in range(30):
        for other in range(1):
            mc.setBlock(x,y,z,46)
            sleep(0.1)
            mc.setBlock(x,y,z,80)
            sleep(0.025)
        if mc.getBlock(x,y-1,z)==0:
            mc.setBlock(x,y,z,0)
            y=y-7
    mc.postToChat("SSSSSssssss.......")
    sphere(mc,x,y,z)

def sphere(mc,x,y,z):
    radius=13
    for x1 in range(radius*-1,radius+1):
        for y1 in range(radius*-1,radius+1):
            for z1 in range(radius*-1,radius+1):
                if (x1**2)+(y1**2)+(z1**2)<=(radius+1)**2:
                        mc.setBlocks(x+0, y+0, z-2, x+0, y+0, z-3, 35,13)
                        mc.setBlocks(x+0, y+0, z-4, x+0, y+0, z-4, 35,15)
                        mc.setBlocks(x+0, y+0, z-5, x+0, y+0, z-6, 35,13)
                        mc.setBlocks(x+0, y+0, z-7, x+0, y+0, z-7, 35,15)
                        mc.setBlocks(x+0, y+0, z-8, x+0, y+0, z-9, 35,13)
                        mc.setBlocks(x+0, y+1, z-2, x+0, y+1, z-3, 35,13)
                        mc.setBlocks(x+0, y+1, z-4, x+0, y+1, z-7, 35,15)
                        mc.setBlocks(x+0, y+1, z-8, x+0, y+1, z-9, 35,13)
                        mc.setBlocks(x+0, y+2, z-2, x+0, y+2, z-3, 35,13)
                        mc.setBlocks(x+0, y+2, z-4, x+0, y+2, z-7, 35,15)
                        mc.setBlocks(x+0, y+2, z-8, x+0, y+2, z-9, 35,13)
                        mc.setBlocks(x+0, y+3, z-2, x+0, y+3, z-4, 35,13)
                        mc.setBlocks(x+0, y+3, z-5, x+0, y+3, z-6, 35,15)
                        mc.setBlocks(x+0, y+3, z-7, x+0, y+3, z-9, 35,13)
                        mc.setBlocks(x+0, y+4, z-2, x+0, y+4, z-2, 35,13)
                        mc.setBlocks(x+0, y+4, z-3, x+0, y+4, z-4, 35,15)
                        mc.setBlocks(x+0, y+4, z-5, x+0, y+4, z-6, 35,13)
                        mc.setBlocks(x+0, y+4, z-7, x+0, y+4, z-8, 35,15)
                        mc.setBlocks(x+0, y+4, z-9, x+0, y+4, z-9, 35,13)
                        mc.setBlocks(x+0, y+5, z-2, x+0, y+5, z-2, 35,13)
                        mc.setBlocks(x+0, y+5, z-3, x+0, y+5, z-4, 35,15)
                        mc.setBlocks(x+0, y+5, z-5, x+0, y+5, z-6, 35,13)
                        mc.setBlocks(x+0, y+5, z-7, x+0, y+5, z-8, 35,15)
                        mc.setBlocks(x+0, y+5, z-9, x+0, y+5, z-9, 35,13)
                        mc.setBlocks(x+0, y+6, z-2, x+0, y+6, z-9, 35,13)
                        mc.setBlocks(x+0, y+7, z-2, x+0, y+7, z-9, 35,13)
                        
def checkBlock(mc):
    blockEvent=mc.events.pollBlockHits()
    for each in blockEvent:
        x=each.pos.x
        y=each.pos.y
        z=each.pos.z
        if mc.getBlock(x,y,z)==46:
            tnt(mc,x,y,z)

def main():
    mc=init()
    while True:
        checkBlock(mc)

main()
