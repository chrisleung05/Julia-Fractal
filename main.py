from PIL import Image

def main():
    width = 19200
    height = 10800
    zoom = 4

    bitmap = Image.new("RGB", (width, height), "white")
    pixels = bitmap.load()
    xcor = -0.7
    ycor = 0.27015
    xmov = 0.0
    ymov = 0.0
    maxiterations = 1020

    for x in range (width):
        for y in range (height):
            tempx = 1.5*(x-width/2)/(0.5*zoom*width) + xmov
            tempy = 1.0*(y-height/2)/(0.5*zoom*height) + ymov
            i = maxiterations
            while tempx*tempx + tempy*tempy <4 and i > 1:
                res = tempx*tempx - tempy*tempy + xcor
                tempy = 2.0*tempx*tempy + xcor
                tempx = res
                i-=1
            pixels[x,y] = (i<<21) + (i<<10) + i*8


    bitmap.save('outputjulia.png', 'PNG')

if __name__ == "__main__":
    main()
