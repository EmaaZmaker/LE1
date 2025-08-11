import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("adding image and background image...")
background_image=pygame.transform.scale(pygame.image.load("background.jpg").convert(),(500,500))
Penguin_image=pygame.transform.scale(pygame.image.load("Penguin.webp").convert_alpha(),(200,200))
penguin_rect=Penguin_image.get_rect(center=(500//2,500//2-30))
text=pygame.font.Font(None,50).render("hello there!",True,pygame.Color("White"))
text_rect=text.get_rect(center=(500//2,500//2+200))

def game_loop():
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        screen.blit(background_image,(0,0))
        screen.blit(Penguin_image,penguin_rect)
        screen.blit(text,text_rect)
        pygame.display.flip()
    pygame.quit()
game_loop()