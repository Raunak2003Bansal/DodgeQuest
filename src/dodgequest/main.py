import pygame

def main():
    pygame.init()

    screen = pygame.display.set_mode((800,600))
    width, height = screen.get_size()
    pygame.display.set_caption("Dodge Quest")
    screen.fill((30,30,30))
    pygame.draw.rect(screen, (255,255,255), (100, 100, 200, 200))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__=="__main__":
    main()