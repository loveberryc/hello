# 这是一个pygame的最小开发框架
import pygame
import sys
import random
from pygame.locals import *
pygame.init()  # 初试化pygame

white_colour = pygame.Color(200, 255, 200)  # 白色
black_colour = pygame.Color(0, 0, 0)  # 黑色
red_colour = pygame.Color(100,0,0)   # 红色
green_colour = pygame.Color(30,100,0)   # 绿色
game_surface = pygame.display.set_mode((600, 400))  # 设置pygame游戏框大小
pygame.display.set_caption("贪吃蛇")  # 设置游戏标题

def new_direction(key,direction):
    if key == 119 and direction != "down":
        direction = "up"
    elif key == 115 and direction != "up":
        direction = "down"
    elif key == 100 and direction != "left":
        direction = "right"
    elif key == 97 and direction != "right":
        direction = "left"
    elif key == 27:
        sys.exit()
    else:
        pass
    return direction
def new_position(head_position,direction):
    if direction == "up":
        head_position[1] -= 20
    elif direction == "down":
        head_position[1] += 20
    elif direction == "left":
        head_position[0] -= 20
    elif direction == "right":
        head_position[0] += 20
    else:
        pass
    return head_position

def main():
    print("按空格开始")
    t = 1
    head_position = [100, 100]  # 蛇的初试位置
    food_position = [300, 100]  # 食物的初始位置
    snake_position = [[100, 100]]
    empty_position = []
    for i in range(30):
        for j in range(20):
            empty_position.append([i*20,j*20])
    direction = "right"  # 初始化方向
    EVENT_time = pygame.USEREVENT + 1
    while True:
        game_surface.fill(black_colour)  # 背景填充为黑色
        for i in range(len(snake_position)):
            pygame.draw.rect(game_surface, white_colour, Rect(snake_position[i][0], snake_position[i][1], 20, 20))  # 在[100, 100]处画20*20的矩形
        pygame.draw.rect(game_surface, red_colour, Rect(food_position[0], food_position[1], 20, 20))
        pygame.draw.rect(game_surface, green_colour, Rect(head_position[0], head_position[1], 20, 20))# 在[100, 100]处画20*20的矩形
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == 32:
                t = -t
                if t == -1:
                    pygame.time.set_timer(EVENT_time, 600)
                    break
                elif t == 1:
                    pygame.time.set_timer(EVENT_time, 200)
                    break
            if event.type == pygame.QUIT:  # 如果是退出键则退出游戏
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                direction = new_direction(event.key, direction)
            elif event.type == EVENT_time:
                head_position = new_position(head_position, direction)
                snake_position.insert(0,[head_position[0],head_position[1]])
                if head_position in empty_position:
                    empty_position.remove(head_position)
                else:
                    print("game over")
                    sys.exit()
                if food_position == head_position:
                    food_position = random.choice(empty_position)
                else:
                    empty_position.append(snake_position.pop())
        if head_position[0] < 0 or head_position[0]>590:
                print("game over")
                sys.exit()
        elif head_position[1] < 0 or head_position[1] > 390:
                print("game over")
                sys.exit()
            # 增加死亡判断功能
        pygame.display.update()

main()