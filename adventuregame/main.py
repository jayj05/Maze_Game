import pygame
import sys
from game_setup import MainWindow, GameMechanics, Player, TileMap, colors

WIN = MainWindow.WIN
FPS = GameMechanics.FPS 

trainer_sprite_sheet = pygame.image.load('Assets/trainer_sheet.png')
player = Player(trainer_sprite_sheet, 64, 64)

player_group = pygame.sprite.Group()
player_group.add(player)

tile_sprite_sheet = pygame.image.load('Assets/default_tiles_x.png')
csv_file = 'Assets/maze.csv'
tilemap = TileMap(tile_sprite_sheet, csv_file)

def main():
    
    running = True 
    clock = pygame.time.Clock()

    while running:

        collision = pygame.sprite.spritecollide(player, tilemap.tile_group, False)
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    player.move_backward()
                elif event.key == pygame.K_w:
                    player.move_forward()
                elif event.key == pygame.K_a:
                    player.move_left()
                elif event.key == pygame.K_d:
                    player.move_right()
                elif event.key == pygame.K_q:
                    pass
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    player.move_backward_done()
                elif event.key == pygame.K_w:
                    player.move_forward_done()
                elif event.key == pygame.K_a:
                    player.move_left_done()
                elif event.key == pygame.K_d:
                    player.move_right_done()

        for tile in collision:
            if tile.type == 'walkable':
                pass
            elif tile.type == 'border':
                pass 
            elif tile.type == 'exit':
                pass
    
        WIN.fill(colors.BLACK)
        tilemap.draw_map(WIN)
        player_group.draw(WIN)
        player_group.update()
        pygame.display.update()

if __name__ == "__main__":
    main()