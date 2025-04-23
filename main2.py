import pygame
from character8 import Character8
from wall2 import Wall2
from enemy import Enemy
from item import Item
# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width, screen_height = 1000, 700
display_surface = pygame.display.set_mode((screen_width, screen_height))

# 창 제목 설정
pygame.display.set_caption("원 애니메이션")

# 색상 정의
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# 폰트 설정
game_font = pygame.font.SysFont('malgungothic', 72) # SysFont = 시스템에 설치된 기본 글꼴 중에서 선택해서 사용하는 함수 맑은 고딕 폰트, 크기 72

# 노래 설정
bgm_sound = pygame.mixer.Sound('C:\sound/헤네시스.mp3')
bgm_sound.play(-1) # 무한 반복 재생
item_sound = pygame.mixer.Sound('C:/sound/아이템획득.mp3')  # 아이템 획득 사운드
win_sound = pygame.mixer.Sound('C:/sound/승리.wav')   # 게임 승리 사운드
lose_sound = pygame.mixer.Sound('C:/sound/패배.wav') # 게임 패배 사운드
# FPS 설정
fps = 60
clock = pygame.time.Clock()

# 캐릭터 객체 생성 (초기 위치는 (260, 280), 반지름 30, 타원의 반지름 가로 27, 세로 34)
character = Character8(40, 300, 30, 27, 30)

# 중앙벽 객체 생성(여백, 세로 위치, 여백을 제외 한 가로 길이, 세로 길이)
frist_wall = Wall2(150, 270, 40 , 260) # 첫번쨰 벽
second_wall = Wall2(330, 170, 40, 260) # 두번쨰 벽
third_wall = Wall2(490, 270, 40, 260) # 세번쨰 벽
fourth_wall = Wall2(650, 170, 40, 260) # 네번쨰 벽
fifth_wall = Wall2(810, 270, 40, 260) # 다섯번쨰 벽
top_wall = Wall2(90, 70, 820, 40) # 위쪽 벽 왼쪽으로 60 위쪽으로 66 떨어진 위치 가로 880 세로 40
bttom_wall = Wall2(90, 590, 820, 40)
topoutline_wall = Wall2(0, 0, 1000, 10) # 테두리
btoomoutline_wall = Wall2(0, 690, 1000, 10)
leftoutline_wall = Wall2(0, 0, 10, 720)
rightoutline_wall = Wall2(990, 0, 10, 720)

# 벽을 리스트
walls = [frist_wall, second_wall, third_wall, fourth_wall, fifth_wall, top_wall, bttom_wall, topoutline_wall, btoomoutline_wall, leftoutline_wall, rightoutline_wall]

 #적 데이터를 저장할 리스트 생성  120, 240
circle_data = [
    Enemy(120, 240, 30, 27, 30, targets=[(120, 240), (120, 560), (220, 560), (220, 240)]),
    Enemy(300, 460, 30, 27, 30, targets=[(300, 460), (400, 460), (400, 140), (300, 140)]),
    Enemy(460, 560, 30, 27, 30, targets=[(460, 560), (560, 560), (560, 240), (460, 240)]),
    Enemy(620, 140, 30, 27, 30, targets=[(620, 140), (620, 460), (720, 460), (720, 140)]),
    Enemy(780, 560, 30, 27, 30, targets=[(780, 560), (880, 560), (880, 240), (780, 240)]),
    Enemy(940, 40, 30, 27, 30, targets=[(940, 40), (60, 40), (60, 140), (940, 140)]),
    Enemy(60, 660, 30, 27, 30, targets=[(60, 660), (60, 560), (940, 560), (940, 660)])
]

items = [] # 총 145개 아이템

# 🔷 1. 탑벽 왼쪽 세로줄 아이템 (x=40, y=30부터 62씩 증가, 11개)
for i in range(11):
    items.append(Item(40, 30 + i * 62, 20, 20))

# 🔷 2. 탑벽 가로줄 아이템 (x=100부터 60씩 증가, y=30, 총 15개)
for i in range(15):
    items.append(Item(100 + i * 60, 30, 20, 20))

# 🔷 3. 탑벽 오른쪽 세로줄 아이템 (x=940, y=30부터 62씩 증가, 11개)
for i in range(11):
    items.append(Item(940, 30 + i * 62, 20, 20))

# 🔷 4. 바텀벽 가로줄 아이템 (x=100부터 60씩 증가, y=650, 총 15개)
for i in range(15):
    items.append(Item(100 + i * 60, 650, 20, 20))

for i in range(14): # 바텀벽 가로줄 위에 아이템 (x=100부터 60씩 증가 y=550 총 14개)
    items.append(Item(100 + i * 60, 550, 20, 20))

for i in range(14): # 탑벽 가로줄 아래 아이템 (x=100부터 60씩 증가 y=130 총 14개)
    items.append(Item(100 + i * 60, 130, 20, 20))

for i in range(2):
    items.append(Item(160, 180 + i * 50, 20, 20))

for i in range(2):
    items.append(Item(820, 180 + i * 50, 20, 20))

for i in range(2):
    items.append(Item(340, 450 + i * 50, 20, 20))

for i in range(6):
    items.append(Item(100, 190 + i * 60, 20, 20))

for i in range(6):
    items.append(Item(220, 190 + i * 60, 20, 20))

for i in range(6):
    items.append(Item(280, 190 + i * 60, 20, 20))

for i in range(6):
    items.append(Item(400, 190 + i * 60, 20, 20))

for i in range(6):
    items.append(Item(460, 190 + i * 60, 20, 20))

for i in range(2):
    items.append(Item(520, 190 + i * 60, 20, 20))

for i in range(6):
    items.append(Item(580, 190 + i * 60, 20, 20))

for i in range(3):
    items.append(Item(640, 430 + i * 60, 20, 20))

for i in range(6):
    items.append(Item(700, 190 + i * 60, 20, 20))

for i in range(6):
    items.append(Item(760, 190 + i * 60, 20, 20))

for i in range(6):
    items.append(Item(880, 190 + i * 60, 20, 20))

def game_over(display_surface):
    text = game_font.render("게임 오버!", True, red)  # render 실제 텍스트를 이미지로 바꾸는 함수 빨간색 텍스트 True 안티앨리어싱 설정 텍스트 테두리를 부드럽게 만듬
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))  # get_rect() 텍스트의 위치·크기를 담은 rect 객체를 만듬 화면 중앙 정렬
    display_surface.blit(text, text_rect) # 화면(display_surface)에 text를 text_rect 위치에 그림 blit() 그리는 함수 text_rect 텍스트가 그려질 위치와 크기 정보 center= 중심점을 어디로 할지 설정
    pygame.display.update()  # 텍스트 표시
    pygame.time.delay(2000)  # 2초 게임 일시 정지 2000 밀리초

def game_clear(display_surface):
    text = game_font.render("게임 클리어!", True, black)  # 검은색 텍스트
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    display_surface.blit(text, text_rect)
    pygame.display.update()
    pygame.time.delay(2000)  # 2초 게임 일시 정지

# 게임 루프 시작
running = True
frame = 0
score = 0

while running:  # 무한 루프
    frame += 1  # 프레임 증가
    if frame > 60:  # 60 프레임마다 초기화
        frame = 1

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            character.set_input(event.key, walls)  # 벽과 충돌 검사

    # 화면 배경을 흰색으로 채우기
    display_surface.fill(white)

    # 벽 그리기
    for wall in walls:
        wall.draw(display_surface, blue)

    # 캐릭터 그리기
    character.draw(frame, display_surface, black, walls)
    
    #아이템 그리기
    for item in items:
        item.draw(display_surface, green)
        if item.collision(character.x, character.y, character.ellipse_x_radius, character.ellipse_y_radius): # 아이템과 캐릭터가 충돌했는지 확인하고 충돌하면 True로 바꿔 먹은걸로 처리
            item_sound.play()
            score += 100

    # 모든 적 그리기
    for enemy in circle_data:
        enemy.Draw(frame, display_surface, red, character)

    # 적과 충돌 확인
    for enemy in circle_data:
        if enemy.collision(enemy.x, enemy.y, character):
            lose_sound.play()
            game_over(display_surface)
            print("게임 오버!")
            pygame.time.delay(2000) # 2초 딜레이
            running = False
            break

    if score >= 14500:
        win_sound.play()
        game_clear(display_surface)
        print('게임 클리어!')
        pygame.time.delay(2000) # 2초 딜레이
        running = False

    # 화면 업데이트
    pygame.display.update()

    # FPS 조절
    clock.tick(fps)

# Pygame 종료
pygame.quit()