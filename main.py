import time
import pygame
import animations
import Emotiv.main_cortex
import threading

font_name = pygame.font.match_font('arial')
def game_over_screen(screen, background):
    screen.blit(background, (0,0))


def game_loop():
    # start game first

    #when score is 3 win
    win_score = 3
    timer = 180 #3 minute timer

    pygame.init()
    window = (500, 500)
    screen = pygame.display.set_mode(window)
    #x, y = screen.get_size()
    #window = (500, 500)

    background = pygame.Surface(window)
    clock = pygame.time.Clock()
    running = True


    # initializing sprites
    mario = animations.MarioSprite()
    groupMario = pygame.sprite.Group(mario)

    #coin
    reward = animations.Coin()

    #stores direction of where player is going
    command = ""

    while running:
        if(mario.score == win_score):
            #game over/you win or you lose screen
            screen.blit(pygame.image.load('images/win.jpg'), window)
            print("You win")
            time.sleep(5)
            return


        mario.update()
        reward.update()

        #call function that checks if collision happens
        #score = rocket_collide(rocketPlayer, reward, score)
        mario.checkCollision(reward, window)


        #update sprites
        screen.blit(background, (0, 0))
        screen.blit(mario.image, (mario.x, mario.y))
        screen.blit(reward.image, (reward.x, reward.y))

        #keys
        # keys = pygame.key.get_pressed()
        # move_x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        # move_y = keys[pygame.K_DOWN] - keys[pygame.K_UP]
        # mario.move(move_x * 10, move_y * 10)

        # read action from emotiv
        action = objectCortex.cortex.action
        #print("yay action", action)
        if(action == "left"):
            print("go left")
            command = "left"

        if (action == "right"):
            print("go right")
            command = "right"

        if (action == "drop"):
            print("go down")
            command("down")

        if (action == "lift"):
            print("go left")
            command("up")

        mario.move(command)

        for event in pygame.event.get():
            # if event is of type quit then
            # set running bool to false
            if event.type == pygame.QUIT or event.type == pygame.K_q:
                running = False

        pygame.display.update()
        clock.tick(10)


#end game loop function

def start_reading(cor):
    objectCortex.start(objectCortex.cortex)
#end cortex reading


objectCortex = Emotiv.main_cortex.CortexStuff(Emotiv.main_cortex.url, Emotiv.main_cortex.user,
                                              Emotiv.main_cortex.clientID, Emotiv.main_cortex.clientSecret)

#start thread 1
thread1 = threading.Thread(target = game_loop)
thread1.start()

# start readings
thread2 = threading.Thread(target = start_reading, args = (objectCortex,))
thread2.start()



