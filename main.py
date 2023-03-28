from models import *

background = transform.scale(image.load("i.png"), WINDOW_SIZE)

win_player1_label = font_label.render("Player 2 LOSER!!!", 1, GREEN)
win_player2_label = font_label.render("Player 1 LOSER!!!", 1, GREEN)

player1 = Player("Player.png", 10 ,WINDOW_SIZE[1] / 2 , 8, SPRITE_SIZE)
player2 = Player("Player.png", WINDOW_SIZE[0] - SPRITE_SIZE[0] * 2,
                 WINDOW_SIZE[1] / 2, 
                 8, 
                 SPRITE_SIZE)
ball = GameSprite("ball.png", WINDOW_SIZE[0] / 2 - SPRITE_SIZE[0] / 2, WINDOW_SIZE[1] / 2 - SPRITE_SIZE[1] / 2, 0, BALL_SIZE)
speed_x = 3
speed_y = 3


clock = time.Clock()

game = True
game_over = False


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not game_over:
        window.blit(background, (0, 0))
        
        player1.update_pos(1)
        player2.update_pos(2)
        
        ball.reset()
        player1.reset()
        player2.reset()
        
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        if ball.rect.y >= WINDOW_SIZE[1] - BALL_SIZE[1] or ball.rect.y <= 0:
            speed_y *= -1.1
        if sprite.collide_rect(ball, player1) or sprite.collide_rect(ball,player2):
            speed_x *= -1.1
            
        if ball.rect.x <= 0:
            window.blit(win_player1_label, (WINDOW_SIZE[0] / 2 - win_player1_label.get_width() / 2, WINDOW_SIZE[1] / 2 - win_player1_label.get_height() / 2))
            game_over = True 
              
        if ball.rect.x + ball.rect.width >= WINDOW_SIZE[0]:
            window.blit(win_player2_label, (WINDOW_SIZE[0] / 2 - win_player2_label.get_width() / 2, WINDOW_SIZE[1] / 2 - win_player2_label.get_height() / 2))
            game_over = True 
        clock.tick(FPS)
        display.update()