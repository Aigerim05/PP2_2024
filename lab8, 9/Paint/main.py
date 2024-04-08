import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

screen.fill((255, 255, 255))
font = pygame.font.SysFont("comicsansms", 15)

#drawing text in rectangle
def draw_text_in_rect(text, rect, bound_color="black"):
    surface = font.render(text, True, bound_color)
    rect_of_text = surface.get_rect(center=rect.center)
    pygame.draw.rect(screen, bound_color, rect, 1)
    screen.blit(surface, rect_of_text)



w, h = 100, 100
x1 = 10
y1 = 10
x2 = 10
y2 = 10


isMouseDown = False
mode = None
color =  (128, 0, 128)

colors = [
    (255, 0, 0),     # Red
    (128, 0, 128),   # Purple
    (0, 128, 0),     # Green
    (0, 0, 255),     # Blue
    (255, 165, 0),   # Orange
    (255, 192, 203), # Pink
    (0, 0, 0)        # Black
]

tools = ["rect", "circ", "brush", "erase", "square", "right", "equil", "rhomb"]
tool_boxes = []
color_boxes = []
selected_color = (0, 0, 0)

# rectangles for tools bar
for i in range(len(tools)):
    box = pygame.Rect(i*50, 0, 50, 40)
    tool_boxes.append(box)

# rectangles for colors bar
for i, color in enumerate(colors):
        rect = pygame.Rect(400 + i*26, 0, 26, 40)
        color_boxes.append(rect)

while True:
    # drawing tools bar
    for i in range(len(tools)):
        box = pygame.Rect(i*50, 0, 50, 40)
        draw_text_in_rect(tools[i], box)
        
    # drawing colors bar
    for i, color in enumerate(colors):
        rect = pygame.Rect(400 + i*26, 0, 26, 40)
        pygame.draw.rect(screen, color, rect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()

        # tools selection
            if tool_boxes[0].collidepoint(x, y):
                mode = tools[0]
            if tool_boxes[1].collidepoint(x, y):
                mode = tools[1]
            if tool_boxes[2].collidepoint(x, y):
                mode = tools[2]
            if tool_boxes[3].collidepoint(x, y):
                mode = tools[3]
            if tool_boxes[4].collidepoint(x, y):
                mode = tools[4]
            if tool_boxes[5].collidepoint(x, y):
                mode = tools[5]
            if tool_boxes[6].collidepoint(x, y):
                mode = tools[6]
            if tool_boxes[7].collidepoint(x, y):
                mode = tools[7]

        # color selection       
            if event.button == 1:
                for i, rect in enumerate(color_boxes):
                    if rect.collidepoint(event.pos):
                        selected_color = colors[i]

        # drawing figures
            if mode == 'rect' and event.pos[1] > 40:
                pygame.draw.rect(screen, selected_color, pygame.Rect(x, y, 80, 60), 1)

            if mode == 'circle' and event.pos[1] > 40:
                pygame.draw.circle(screen, selected_color, (x, y), 40)
            
            if mode == 'brush':
                x1 = event.pos[0]
                y1 = event.pos[1]
                isMouseDown = True

            if mode == 'erase': 
                selected_color = (255, 255, 255)
                x1 = event.pos[0]
                y1 = event.pos[1]
                isMouseDown = True
            
            if mode == 'square' and event.pos[1] > 40:
                pygame.draw.rect(screen, selected_color, pygame.Rect(x, y, 60, 60), 1)

            if mode == 'right' and event.pos[1] > 40:
                pygame.draw.polygon(screen, selected_color,[(x, y), (x, y+60), (x+60, y+60)], 1)
            
            if mode == 'equil' and event.pos[1] > 40:
                pygame.draw.polygon(screen, selected_color,[(x, y), (x-30, y+30), (x+30, y+30)], 1)
            
            if mode == 'rhomb' and event.pos[1] > 40:
                pygame.draw.polygon(screen, selected_color, [(x, y), (x+30, y+30), (x, y+2*30), (x - 30, y + 30)], 1)

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                isMouseDown = False
                
        # drawing line      
        if event.type == pygame.MOUSEMOTION:
            if isMouseDown:                      
                x2 = event.pos[0]                       
                y2 = event.pos[1]          
                pygame.draw.line(screen, selected_color, (x1, y1), (x2, y2), 10)
                x1 = x2                        
                y1 = y2   

    pygame.display.update()
    clock.tick(60)


        