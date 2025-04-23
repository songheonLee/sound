import pygame
from character8 import Character8
from wall2 import Wall2
from enemy import Enemy

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

# FPS 설정
fps = 60
clock = pygame.time.Clock()

# 캐릭터 객체 생성 (초기 위치는 (260, 280), 반지름 30, 타원의 반지름 가로 27, 세로 34)
character = Character8(60, 100, 30, 27, 30)

# 원 데이터를 저장할 리스트 생성
circle_data = []

enemy = Enemy(300, 300, 30, 27, 30)
circle_data.append(enemy)

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

# 게임 루프 시작
running = True
frame = 0

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

    # 모든 적 그리기
    for enemy in circle_data:
        enemy.Draw(frame, display_surface, red, character)

    # 화면 업데이트
    pygame.display.update()

    # FPS 조절
    clock.tick(fps)

# Pygame 종료
pygame.quit()