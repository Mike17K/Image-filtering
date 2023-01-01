
# import the pygame module
import pygame
  
screen = pygame.display.set_mode((300, 300))

        
pygame.display.flip()


running = True

blue=190
color_array=[]
while running:
    pos = [None,None]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.mouse.get_pressed()[0]:
            try:
                pos=event.pos
            except AttributeError:
                pass
            
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos=pygame.mouse.get_pos()
            if event.button == 4:
                blue = min(blue + 15, 255)
                for i in range(255):
                    for j in range(255):
                        screen.set_at((i, j), (i,j,blue))
                pygame.display.flip()
                print('Blue: ',blue)
            if event.button == 5:
                blue = max(blue - 15, 0)
                for i in range(255):
                    for j in range(255):
                        screen.set_at((i, j), (i,j,blue))
                pygame.display.flip()
                print('Blue: ',blue)

           
    if pos!=[None,None]:
        if pos[0]<255 and pos[0]>0 and pos[1]<255 and pos[1]>0:
            screen.set_at((pos[0], pos[1]), (pos[0],pos[1],blue))
            pygame.display.flip()  
            color_array.append([pos[0],pos[1],blue])
            print([pos[0],pos[1],blue],len(color_array))
       

f = open("dataRGBforBlue.txt", "w")

text=''
for i in range(len(color_array)):
    text+=str(color_array[i][0])+' '
    text+=str(color_array[i][1])+' '
    text+=str(color_array[i][2])+' '
    text+='\n'
text=text[:-1]

f.write(text)

f.close()
