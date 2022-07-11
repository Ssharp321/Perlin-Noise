import Distances as dist, time, random, math
from PIL import Image, ImageDraw

POINTS = int(input("How many points: "))
WIDTH = 400
HEIGHT = 200
points = []
INCHESWIDE = 1920
INCHESTOPIXELS = INCHESWIDE/WIDTH


for _ in range(POINTS):
    points.append([random.randint(0,WIDTH),random.randint(0,HEIGHT)])

im = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(im)


for x in range(WIDTH):
    for y in range(HEIGHT):
        out = [math.inf]
        xInches = x*INCHESTOPIXELS
        yInches = y*INCHESTOPIXELS
        for point in enumerate(points):
            pointScaled = [point[1][0]*INCHESTOPIXELS,point[1][1]*INCHESTOPIXELS]
            distance = dist.distancePointEst(pointScaled,[xInches,yInches])
            if out[0] > distance: out = [distance,pointScaled]
        out = dist.distanceCircle(pointScaled,0,[xInches,yInches])
        out = int(out)
        draw.point([x,y],(out,out,out))
            
im.save(f'output{WIDTH}x{HEIGHT}.png', 'PNG')