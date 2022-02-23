import pygame
import sys
import random
# khởi tạo các thành phần
    # WIDTH là chiều rộng khung hình
    # HEIGHT là chiều cao khung hình
WIDTH = 400
HEIGHT = 400

    # GRID là độ rộng của ô
GRID = 20
    #GRID_WIDTH là chia bao nhiêu ô theo chiều rộng
    #GRID_HEIGHT là chia bao nhiêu ô theo chiều cao
        # ở đây là 20 ô dọc và 20 ô ngang 
        # 20 X 20
GRID_WIDTH = WIDTH / GRID
GRID_HEIGHT = HEIGHT / GRID
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
surface = pygame.Surface(screen.get_size())
surface = surface.convert()
     # di chuyển của con rắn qua từng ô
UP    = (0, -1)
DOWN  = (0, 1)
LEFT  = (-1, 0)
RIGHT = (1, 0)
stop =(0,0)
# vẽ bàn caro với 2 màu 
def drawGrid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x + y) % 2 == 0:
                a = pygame.Rect((x*GRID, y*GRID), (GRID, GRID))
                pygame.draw.rect(surface, (144,238,144), a)
            else:
                b = pygame.Rect((x*GRID, y*GRID), (GRID, GRID))
                pygame.draw.rect(surface, (143,188,143), b)

# vẽ con rắn
class Snake(object):
    # khởi tạo các phần tử liên quan đến con rắn
        # length là chiều dài con rắn
        # positions là tọa độ
        # direction là sự di chuyển của con rắn
            # lên, xuống, phải, trái
        # color là màu của rắn
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH / 2), (HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (255,255,0)

        # đầu con rắn
    def get_head_position(self):
        return self.positions[0]

        # câu lệnh thực hiện rẽ
            # nếu ko va vào thân thì tiếp tục
            # nếu đầu chạm vào thân thì hiện số điểm
    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

        # chơi lại từ đầu
    def reset(self):
        self.length = 1
        self.positions =  [((WIDTH / 2), (HEIGHT / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

        #câu lệnh di chuyển
    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x*GRID)) % WIDTH), (cur[1] + (y*GRID)) % HEIGHT)
        # khởi tạo lệnh if kiểm tra vị trí
            # nếu chiều dài thân lớn hơn 2 và điểm mới(thân mới)
                # tồn tại trong rắn thì chơi lại
            
            # nếu không 
                # đầu tiến lên ô mới và xóa phần đuôi di chuyển
        while len(self.positions) > 2 and new in self.positions[2:]:
            # hiển thị kết quả nếu bị tông vào đuôi
            
            drawGrid(surface)
            myfont = pygame.font.SysFont("comicsansms", 20)
            mesg = myfont.render("You Lost! Press C-Play Again or Q-Quit", False, (255,0,0))
            screen.blit(mesg, [WIDTH / 10, HEIGHT / 3])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_c:
                        self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()            
       
    # vẽ con rắn
    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRID, GRID))
            pygame.draw.rect(surface, self.color , r)
            #pygame.draw.rect(surface, (144,238,144), r, 1)
            
    # thiết lập các phím điều khiển con rắn            
    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)
                elif event.key == pygame.K_d:
                    self.turn(stop)


# vẽ miếng thức ăn
class Food(object):
    # khởi tạo các thuộc tính của miếng thức ăn
        # position là tọa độ 
        # color là màu
    def __init__(self):
        self.position = (0, 0)
        self.color = (255, 0, 0)
        self.randomize_position()

    # thiết lập vị trí bất kì cho thức ăn theo trục WIDTH,HEIGHT
    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH-1) * GRID, random.randint(0, GRID_HEIGHT-1) * GRID)

    # thiết lập vẽ miếng thức ăn.
    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRID, GRID))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (255, 0, 0), r, 1)
dis = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    pygame.init()
    # cài đặt tốc độ di chuyển của con rắn
        # tức là tốc độ bao nhiêu khung hình trên giây
    clock = pygame.time.Clock()
    # cài đặt màn hình
    # vẽ ô caro, rắn và thức ăn 
    drawGrid(surface)
    snake = Snake()
    food = Food()
    # cài đặt phông chữ
    myfont = pygame.font.SysFont("comicsansms", 16)
    # cài đặt điểm ở góc màn hình
    score = 0 

    while True:
        clock.tick(5)
        snake.handle_keys()
        drawGrid(surface)
        snake.move()
        # khi đầu rắn qua vị trí của điểm thức ăn
            # chiều dài con rắn tăng 1
            # điểm thêm 1
            # chuyển vị trí của miếng thức ăn
        if snake.get_head_position() == food.position:
            snake.length += 1
            score += 1
            food.randomize_position()

        # vẽ con rắn với độ dài mới
        # vẽ miếng thức ăn ở vị trí mới
        snake.draw(surface)
        food.draw(surface) 

        # hiển thị điểm số
        screen.blit(surface, (0,0))
        text = myfont.render("D=STOP,Score {0}".format(score), 1, (0,0,0))
        screen.blit(text, (5, 10))
        pygame.display.update()

if __name__ =="__main__":
    main()