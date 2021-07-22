import pymunk.pygame_util
import pygame
import pymunk
import random
from sys import exit

#分辨率

SCREEN_WIDTH=400
SCREEN_HEIGHT=600
pygame.init()
screen=pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
draw_options = pymunk.pygame_util.DrawOptions(screen)
pygame.display.set_caption("1107")

#帧数
ticks=60
clock=pygame.time.Clock()

#死线
def DrawLine(screen):
    LineColcor=(0,255,255)
    Line_Start =(0,100)
    Line_End=(720,100)
    Line_Width=3
    pygame.draw.line(screen,LineColcor,Line_Start,Line_End,Line_Width)

#背景
background=pygame.image.load("image/background.png")

#鼠标
Number_Mouse = 0

#pymunk空间设置
space = pymunk.Space()

#pymunk重力设置
space.gravity = 0, 900

#生成地面以及墙壁
ground_0 = space.static_body
segment_0= pymunk.Segment(ground_0, (0,SCREEN_HEIGHT), (SCREEN_WIDTH,SCREEN_HEIGHT), 1)
segment_1=pymunk.Segment(ground_0,(-50,0),(-50,600),50)
segemt_2=pymunk.Segment(ground_0,(450,0),(450,600),50)
segment_0.elasticity = 1
segment_0.friction=100000
space.add(segment_0,segment_1,segemt_2)

#水果类别
class PuTao():
    def __init__(self):
        self.mass = 4000  # 质量
        self.radius = 20  # 半径
        self.body = pymunk.Body(self.mass, moment=10)
        self.circle = pymunk.Circle(self.body, self.radius)
        self.circle.elasticity = 0.15
        self.circle.friction = 100000
        self.circle.collision_type = 1
        self.high=0
    def High(self):
        return self.high
    def Higher(self):
        self.high+=1
    def Circle(self):
        return self.radius
    def Draw(self):
        self.image = pygame.image.load('image/01.png')
        self.image = pygame.transform.smoothscale(self.image, (self.radius*2, self.radius*2))
        return self.image
class YingTao:
    def __init__(self):
        self.mass = 9000  # 质量
        self.radius = 30  # 半径
        self.body = pymunk.Body(self.mass, moment=10)
        self.circle = pymunk.Circle(self.body, self.radius)
        self.circle.elasticity = 0.15
        self.circle.friction = 0.9
        self.circle.collision_type = 2
        self.high = 0
    def High(self):
        return self.high
    def Higher(self):
        self.high+=1
    def Circle(self):
        return self.radius
    def Draw(self):
        self.image = pygame.image.load('image/02.png')
        self.image = pygame.transform.smoothscale(self.image, (self.radius*2, self.radius*2))
        return self.image
class Hanamaru:
    def __init__(self):
        self.mass = 17640  # 质量
        self.radius = 42  # 半径
        self.body = pymunk.Body(self.mass, moment=10)
        self.circle = pymunk.Circle(self.body, self.radius)
        self.circle.elasticity = 0.15
        self.circle.friction = 0.9
        self.circle.collision_type = 3
        self.high = 0
    def High(self):
        return self.high
    def Higher(self):
        self.high+=1
    def Circle(self):
        return self.radius
    def Draw(self):
        self.image = pygame.image.load('image/03.png')
        self.image = pygame.transform.smoothscale(self.image, (self.radius*2, self.radius*2))
        return self.image
class NingMeng:
    def __init__(self):
        self.mass = 21160  # 质量
        self.radius = 46  # 半径
        self.body = pymunk.Body(self.mass, moment=10)
        self.circle = pymunk.Circle(self.body, self.radius)
        self.circle.elasticity = 0.15
        self.circle.friction = 0.9
        self.circle.collision_type=4
        self.high = 0
    def High(self):
        return self.high
    def Higher(self):
        self.high+=1
    def Circle(self):
        return self.radius
    def Draw(self):
        self.image = pygame.image.load('image/04.png')
        self.image = pygame.transform.smoothscale(self.image, (self.radius*2, self.radius*2))
        return self.image
class MiHouTao:
    def __init__(self):
        self.mass = 33640  # 质量
        self.radius = 58  # 半径
        self.body = pymunk.Body(self.mass, moment=10)
        self.circle = pymunk.Circle(self.body, self.radius)
        self.circle.elasticity = 0.15
        self.circle.friction = 0.9
        self.circle.collision_type = 5
        self.high = 0
    def High(self):
        return self.high
    def Higher(self):
        self.high+=1
    def Circle(self):
        return self.radius
    def Draw(self):
        self.image = pygame.image.load('image/05.png')
        self.image = pygame.transform.smoothscale(self.image, (self.radius*2, self.radius*2))
        return self.image
class Tomato:
    def __init__(self):
        self.mass = 49000  # 质量
        self.radius = 70  # 半径
        self.body = pymunk.Body(self.mass, moment=10)
        self.circle = pymunk.Circle(self.body, self.radius)
        self.circle.elasticity = 0.15
        self.circle.friction = 0.9
        self.circle.collision_type = 6
        self.high = 0
    def High(self):
        return self.high
    def Higher(self):
        self.high+=1
    def Circle(self):
        return self.radius
    def Draw(self):
        self.image = pygame.image.load('image/06.png')
        self.image = pygame.transform.smoothscale(self.image, (self.radius*2, self.radius*2))
        return self.image
class MoMo:
    def __init__(self):
        self.mass = 54760  # 质量
        self.radius = 74  # 半径
        self.body = pymunk.Body(self.mass, moment=10)
        self.circle = pymunk.Circle(self.body, self.radius)
        self.circle.elasticity = 0.15
        self.circle.friction = 0.9
        self.circle.collision_type = 7
        self.high = 0
    def High(self):
        return self.high
    def Higher(self):
        self.high+=1
    def Circle(self):
        return self.radius
    def Draw(self):
        self.image = pygame.image.load('image/07.png')
        self.image = pygame.transform.smoothscale(self.image, (self.radius*2, self.radius*2))
        return self.image
class BoLuo:
    def __init__(self):
        self.mass = 100000  # 质量
        self.radius = 100  # 半径
        self.body = pymunk.Body(self.mass, moment=10)
        self.circle = pymunk.Circle(self.body, self.radius)
        self.circle.elasticity = 0.15
        self.circle.friction = 0.9
        self.circle.collision_type = 8
        self.high = 0
    def High(self):
        return self.high
    def Higher(self):
        self.high+=1
    def Circle(self):
        return self.radius
    def Draw(self):
        self.image = pygame.image.load('image/08.png')
        self.image = pygame.transform.smoothscale(self.image, (self.radius*2, self.radius*2))
        return self.image
class YeZi:
    def __init__(self):
        self.mass = 116640  # 质量
        self.radius = 108  # 半径
        self.body = pymunk.Body(self.mass, moment=10)
        self.circle = pymunk.Circle(self.body, self.radius)
        self.circle.elasticity = 0.15
        self.circle.friction = 0.9
        self.circle.collision_type = 9
        self.high = 0
    def High(self):
        return self.high
    def Higher(self):
        self.high+=1
    def Circle(self):
        return self.radius
    def Draw(self):
        self.image = pygame.image.load('image/09.png')
        self.image = pygame.transform.smoothscale(self.image, (self.radius*2, self.radius*2))
        return self.image
class BanXiGua:
    def __init__(self):
        self.mass = 144000  # 质量
        self.radius = 120  # 半径
        self.body = pymunk.Body(self.mass, moment=10)
        self.circle = pymunk.Circle(self.body, self.radius)
        self.circle.elasticity = 0.15
        self.circle.friction = 0.9
        self.circle.collision_type = 10
        self.high = 0
    def High(self):
        return self.high
    def Higher(self):
        self.high+=1
    def Circle(self):
        return self.radius
    def Draw(self):
        self.image = pygame.image.load('image/10.png')
        self.image = pygame.transform.smoothscale(self.image, (self.radius*2, self.radius*2))
        return self.image
class XiGua:
    def __init__(self):
        self.mass = 243360  # 质量
        self.radius = 156  # 半径
        self.body = pymunk.Body(self.mass, moment=10)
        self.circle = pymunk.Circle(self.body, self.radius)
        self.circle.elasticity = 0.15
        self.circle.friction = 0.9
        self.circle.collision_type = 11
        self.high = 0
    def High(self):
        return self.high
    def Higher(self):
        self.high+=1
    def Circle(self):
        return self.radius
    def Draw(self):
        self.image = pygame.image.load('image/11.png')
        self.image = pygame.transform.smoothscale(self.image, (self.radius*2, self.radius*2))
        return self.image
Fruit=[]
putao=PuTao()
yingtao=YingTao()
hanamaru=Hanamaru()
ningmeng=NingMeng()
mihoutao=MiHouTao()
#生成水果
def Creat_Fruit(x,y=50,i=0,a=0):
    if i==0:
        if a == 1:
            putao = PuTao()
            putao.body.position = x, 50
            space.add(putao.body, putao.circle)
            Fruit.append(putao)
        if a == 2:
            yingtao = YingTao()
            yingtao.body.position = x, 50
            space.add(yingtao.body, yingtao.circle)
            Fruit.append(yingtao)
        if a == 3:
            hanamaru = Hanamaru()
            hanamaru.body.position = x, 50
            space.add(hanamaru.body, hanamaru.circle)
            Fruit.append(hanamaru)
        if a == 4:
            ningmeng = NingMeng()
            ningmeng.body.position = x, 50
            space.add(ningmeng.body, ningmeng.circle)
            Fruit.append(ningmeng)
        if a == 5:
            mihoutao = MiHouTao()
            mihoutao.body.position = x, 50
            space.add(mihoutao.body, mihoutao.circle)
            Fruit.append(mihoutao)
    if i==1:
        yingtao = YingTao()
        yingtao.body.position = x, y
        space.add(yingtao.body, yingtao.circle)
        Fruit.append(yingtao)
    if i==2:
        hanamaru = Hanamaru()
        hanamaru.body.position = x, y
        space.add(hanamaru.body, hanamaru.circle)
        Fruit.append(hanamaru)
    if i==3:
        ningmeng = NingMeng()
        ningmeng.body.position = x, y
        space.add(ningmeng.body, ningmeng.circle)
        Fruit.append(ningmeng)
    if i==4:
        mihoutao = MiHouTao()
        mihoutao.body.position = x, y
        space.add(mihoutao.body, mihoutao.circle)
        Fruit.append(mihoutao)
    if i==5:
        tomato = Tomato()
        tomato.body.position = x, y
        space.add(tomato.body, tomato.circle)
        Fruit.append(tomato)
    if i==6:
        momo = MoMo()
        momo.body.position = x, y
        space.add(momo.body, momo.circle)
        Fruit.append(momo)
    if i==7:
        boluo = BoLuo()
        boluo.body.position = x, y
        space.add(boluo.body, boluo.circle)
        Fruit.append(boluo)
    if i==8:
        yezi = YeZi()
        yezi.body.position = x, y
        space.add(yezi.body, yezi.circle)
        Fruit.append(yezi)
    if i==9:
        banxigua = BanXiGua()
        banxigua.body.position = x, y
        space.add(banxigua.body, banxigua.circle)
        Fruit.append(banxigua)
    if i==10:
        xigua = XiGua()
        xigua.body.position = x, y
        space.add(xigua.body, xigua.circle)
        Fruit.append(xigua)

#分数计算

class Score():
    def __init__(self):
        self.score=0
Score_Final=Score()

#碰撞检测

def coll_begin (arbiter,space,data):
    Shape_0=arbiter.shapes[0]
    Shape_1 = arbiter.shapes[1]
    i=arbiter.shapes[0].collision_type
    x1, y1 = arbiter.shapes[0].body.position
    x2, y2 = arbiter.shapes[1].body.position
    if y1 > y2:
        space.remove(arbiter.shapes[1], arbiter.shapes[1].body)
        space.remove(arbiter.shapes[0], arbiter.shapes[0].body)
        for fruit in Fruit:
            if fruit.body.position==arbiter.shapes[0].body.position:
                Fruit.remove(fruit)
        for fruit in Fruit:
            if fruit.body.position==arbiter.shapes[1].body.position:
                Fruit.remove(fruit)
        Creat_Fruit(x1,y1,i)
        if i!=10:
            Score_Final.score+=i
        elif i==10:
            Score_Final.score+=i
            Score_Final.score+=100
    if y1 < y2:
        space.remove(arbiter.shapes[0], arbiter.shapes[0].body)
        space.remove(arbiter.shapes[1], arbiter.shapes[1].body)
        for fruit in Fruit:
            if fruit.body.position==arbiter.shapes[0].body.position:
                Fruit.remove(fruit)
        for fruit in Fruit:
            if fruit.body.position==arbiter.shapes[1].body.position:
                Fruit.remove(fruit)
        Creat_Fruit(x2, y2, i)
        if i!=10:
            Score_Final.score+=i
        elif i==10:
            Score_Final.score+=i
            Score_Final.score+=100
    if y1 == y2:
        if x1 < x2:
            space.remove(arbiter.shapes[0], arbiter.shapes[0].body)
            space.remove(arbiter.shapes[1], arbiter.shapes[1].body)
            for fruit in Fruit:
                if fruit.body.position == arbiter.shapes[0].body.position:
                    Fruit.remove(fruit)
            for fruit in Fruit:
                if fruit.body.position == arbiter.shapes[1].body.position:
                    Fruit.remove(fruit)
            Creat_Fruit(x2, y2, i)
            if i != 10:
                Score_Final.score += i
            elif i == 10:
                Score_Final.score += i
                Score_Final.score += 100
for i in range(1,11):
    handler=space.add_collision_handler(i,i)
    handler.post_solve=coll_begin

#分数显示

Text=pygame.font.SysFont(None,30)

#随机计算
class Random(object):
    def __init__(self):
        self.rana=random.randint(1,10)
    def random(self):
        if 1 <= self.rana <= 2:
            return 1
        if 3 <= self.rana <= 4:
            return 2
        if 5 <= self.rana <= 7:
            return 3
        if self.rana == 8:
            return 4
        if 9 <= self.rana <= 10:
            return 5
Mouse_Nothing=1
Mouse_Count=0

#延迟
Delay=0
Falldown=0
x=0

#运行循环
while True:
    # 帧数
    clock.tick(ticks)
    # 鼠标
    Mouse_X, Mouse_Y = pygame.mouse.get_pos()
    Mouse_Press = pygame.mouse.get_pressed()
    # 背景
    screen.blit(background, (0, 0))
    #分数
    Text_Show = Text.render('score: {}'.format(str(Score_Final.score)), 1, (0, 0, 0))
    screen.blit(Text_Show, (300, 30))
    # 死线
    DrawLine(background)
    DrawLine(screen)

    #绘制水果
    for f in Fruit:
        screen.blit(f.Draw(),(f.body.position.x-f.Circle(),f.body.position.y-f.Circle()))
    #小球位置
    if Mouse_Count == 0:
        b=Random()
        Mouse_Count = 1
    if 1 <= Mouse_Nothing <= 3 and Falldown==0:
        screen.blit(putao.Draw(), (Mouse_X - 20, 30))
    if Mouse_Nothing == 4 and Falldown==0:
        screen.blit(yingtao.Draw(), (Mouse_X - 30, 20))
    if Mouse_Nothing == 5 and Falldown==0:
        screen.blit(hanamaru.Draw(), (Mouse_X - 42, 8))
    if Mouse_Nothing > 5 and Falldown==0:
        if b.random() == 1:
            screen.blit(putao.Draw(), (Mouse_X - 20, 30))
        if b.random() == 2:
            screen.blit(yingtao.Draw(), (Mouse_X - 30, 20))
        if b.random() == 3:
            screen.blit(hanamaru.Draw(), (Mouse_X - 42, 8))
        if b.random() == 4:
            screen.blit(ningmeng.Draw(), (Mouse_X - 46, 4))
        if b.random() == 5:
            screen.blit(mihoutao.Draw(), (Mouse_X - 58, -8))
    # 下落
    for index in Mouse_Press:
        if Mouse_Press[0]==1:
            if Number_Mouse==0 and Falldown==0:
                    Number_Mouse=1
                    Mouse_Count = 0
                    Falldown=1
                    Mouse_Sure = Mouse_X
                    if Mouse_Nothing<=3:
                        Creat_Fruit(Mouse_Sure,50,0,1)
                    elif Mouse_Nothing==4:
                        Creat_Fruit(Mouse_Sure,50,0,2)
                    elif Mouse_Nothing==5:
                        Creat_Fruit(Mouse_Sure, 50, 0, 3)
                    else:
                        Creat_Fruit(Mouse_Sure,50,0,b.random())
                    Mouse_Nothing +=1
    #游戏失败检测
    for fruit in Fruit:
        if fruit.body.position.y<=100:
            fruit.Higher()
            if fruit.High()>=100:
                pygame.quit()
                quit()

    #下落延迟检测
    if Falldown==1:
        Delay += 1
        if Delay>=120:
            Falldown=0
            Delay=0
    # 更新
    pygame.display.update()
    space.step(0.01)

    #结束
    for event in pygame.event .get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    #鼠标抬起
    if event.type==pygame.MOUSEBUTTONUP:
        Number_Mouse=0

