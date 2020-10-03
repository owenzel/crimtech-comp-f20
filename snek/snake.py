import random
import pygame
import sys

# global variables
WIDTH = 24
HEIGHT = 24
SIZE = 20
SCREEN_WIDTH = WIDTH * SIZE
SCREEN_HEIGHT = HEIGHT * SIZE

DIR = {
    'u' : (0, -1), # north is -y
    'd' : (0, 1),
    'l' : (-1,0),
    'r' : (1,0)
}

class Snake(object):
    l = 1
    body = [(WIDTH // 2 + 1, HEIGHT // 2),(WIDTH // 2, HEIGHT // 2)]
    direction = 'r'
    dead = False
    start = False
    grow = False

    def __init__(self):
        pass
    
    def get_color(self, i):
        hc = (40,50,100)
        tc = (90,130,255)
        return tuple(map(lambda x,y: (x * (self.l - i) + y * i ) / self.l, hc, tc))

    def get_head(self):
        return self.body[0]

    def turn(self, dir):
        # See section 3, "Turning the snake".
        self.direction = dir

    def collision(self, x, y):
        # See section 2, "Collisions", and section 4, "Self Collisions"
        if x < 0 or x > WIDTH - 1 or y < 0 or y > HEIGHT - 1:
            return True
        for i in range(2, len(self.body)):
            if x == self.body[i][0] and y == self.body[i][1]:
                return True
        
        return False
    
    def coyote_time(self):
        # TODO: See section 13, "coyote time".
        pass

    def move(self):
        # See section 1, "Move the snake!". You will be revisiting this section a few times.
        #For the length of the body:
        #Move the first cell down in the direction given
        #Move the second cell into the place of the first cell 
        #Move the third cell into the place of the second cell
        #and so on until we reach the end (self.body[0][0] + DIR[self.direction][0], self.body[0][1] + DIR[self.direction][1])

        temp = (self.body[0][0], self.body[0][1])
        self.body[0] = (self.body[0][0] + DIR[self.direction][0], self.body[0][1] + DIR[self.direction][1])
        for i in range(1, len(self.body)):
            if self.collision(self.body[0][0], self.body[0][1]):
                self.kill()
                return
            self.body[i] = temp
            temp = (self.body[i][0], self.body[i][1])
        if self.grow:
            #self.body.insert(0, (self.body[0][0] + DIR[self.direction][0], self.body[0][1] + DIR[self.direction][1]))
            self.body.append(temp)
            self.grow = False

    def kill(self):
        # See section 11, "Try again!" **NOTE: I completed this later in the file
        self.dead = True

    def draw(self, surface):
        for i in range(len(self.body)):
            p = self.body[i]
            pos = (p[0] * SIZE, p[1] * SIZE)
            r = pygame.Rect(pos, (SIZE, SIZE))
            pygame.draw.rect(surface, self.get_color(i), r)

    def handle_keypress(self, k):
        if k == pygame.K_UP:
            self.turn('u')
        if k == pygame.K_DOWN:
            self.turn('d')
        if k == pygame.K_LEFT:
            self.turn('l')
        if k == pygame.K_RIGHT:
            self.turn('r')
        # Implements feature #10
        if k == pygame.K_SPACE:
            self.start = True
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type != pygame.KEYDOWN:
                continue
            self.handle_keypress(event.key)
    
    def wait_for_key(self):
        # see section 10, "wait for user input". **NOTE: I completed this elsewhere
        pass


# returns an integer between 0 and n, inclusive.
def rand_int(n):
    return random.randint(0, n)

class Apple(object):
    position = (10,10)
    color = (233, 70, 29)
    def __init__(self):
        self.place([])

    def place(self, snake):
        # TODO: see section 6, "moving the apple".
        pos = self.position
        for i in range(len(snake)):
            if snake[i][0] == self.position[0] and snake[i][1] == self.position[1]:
                pos = (rand_int(WIDTH - 2), rand_int(HEIGHT - 2))
        self.position = pos

    def draw(self, surface):
        pos = (self.position[0] * SIZE, self.position[1] * SIZE)
        r = pygame.Rect(pos, (SIZE, SIZE))
        pygame.draw.rect(surface, self.color, r)

def draw_grid(surface):
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            r = pygame.Rect((x * SIZE, y * SIZE), (SIZE, SIZE))
            color = (169,215,81) if (x+y) % 2 == 0 else (162,208,73)
            pygame.draw.rect(surface, color, r)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)

    snake = Snake()
    apple = Apple()

    score = 0

    while True:
        # TODO: see section 10, "incremental difficulty".
        clock.tick(10)
        snake.check_events()
        draw_grid(surface)
        # Implements feature #10
        if snake.start == True:        
            snake.move()

        snake.draw(surface)
        apple.draw(surface)
        # see section 5, "Eating the Apple".
        if snake.get_head()[0] == apple.position[0] and snake.get_head()[1] == apple.position[1]:
            print("the snake ate an apple!")
            score += 1
            snake.l += 1
            snake.grow = True
            apple.place(snake.body)
        
        screen.blit(surface, (0,0))
        # see section 8, "Display the Score"
        textsurface = myfont.render(f"Score: {score}", False, (0, 0, 0))
        screen.blit(textsurface,(0,0))

        pygame.display.update()
        if snake.dead:
            print('You died. Score: %d' % score)
            # Implements feature #11
            print('Restarting...')
            snake.l = 1
            snake.body = [(WIDTH // 2 + 1, HEIGHT // 2),(WIDTH // 2, HEIGHT // 2)]
            snake.direction = 'r'
            snake.start = False
            apple.position = (10,10)
            score = 0
            snake.dead = False
            #pygame.quit()
            #sys.exit(0)

if __name__ == "__main__":
    main()