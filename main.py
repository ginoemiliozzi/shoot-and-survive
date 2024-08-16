import pygame
from game import Game


this_game = Game(monsters_amount=3)

screen, players, shots, monsters, hud, terrain = this_game.get_components()

while True:
    keys = pygame.key.get_pressed()
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
 
    # Update sprites
    players.update(keys, events)
    shots.update()
    monsters.update()

    # Draw everything
    screen.blit(terrain, (0, 0))
    monsters.draw(screen)
    players.draw(screen)
    shots.draw(screen)
    hud.render()

    if not players.sprite:
        hud.game_over()
    elif not monsters.sprites():
        this_game.next_level()
    
    pygame.display.flip()
