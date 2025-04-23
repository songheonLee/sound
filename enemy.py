import pygame


class Enemy:
    def __init__(self, x, y, radius, ellipse_x_radius, ellipse_y_radius, targets=None): # 객체가 생성될 때 호출되는 메서드
        self.x = x
        self.y = y
        self.radius = radius
        self.ellipse_x_radius = ellipse_x_radius # 타원의 가로 반지름
        self.ellipse_y_radius = ellipse_y_radius # 타원의 세로 반지름 
        self.targets = targets if targets else []
        self.target_index = 0
        self.speed = 2
        
    def SetPosition(self, x, y): # 객체의 위치를 설정하는 메서드
        self.x = x
        self.y = y
       
    def SetRadius(self, r): # 반지름 
        self.radius = r

    def SetEllipseLength(self, x, y): # 타원
        self.ellipse_x_radius = x
        self.ellipse_y_radius = y

    def update_position(self):
        if not self.targets: # targets가 없으면
            return           # 위치 업데이트 안 함 함수 종료

        target_x, target_y = self.targets[self.target_index] # self.targets에서 현재 목표 좌표를 가져온다 self.target_index는 현재 가고 있는 목표 좌표 인덱스
        ax = target_x - self.x # 목표 x - 현재 x = 목표까지의 x값 거리
        ay = target_y - self.y
        ba = (ax ** 2 + ay ** 2) ** 0.5 #ba 현재 위치와 목표 사이의 직선 거리 두 점 사기의 직선 거리

        if ba <= 0:
            # 목표 지점에 도달하면 다음 타겟으로
            self.x, self.y = target_x, target_y # 현재 좌표 = 타켓 좌표 목표 지점에 도착 
            self.target_index = (self.target_index + 1) % len(self.targets) # 타켓이 4니까 나누기 4 다시 루프 len = 길이, 개수 
        else:
            # 방향에 따라 속도만큼 이동
            self.x += self.speed * ax / ba # 적이 현재 위치에서 목표 위치로 조금씩 이동 ax / ba = x축 단위 방향 (1프레임에 얼마나 가야 하는지 비율)
            self.y += self.speed * ay / ba 

    def Draw(self, frame, display_surface, color, character):  # 화면에 그리기
        self.update_position()  # 위치 업데이트
        
        # 원 또는 타원 그리기
        if frame <= 30:
            pygame.draw.circle(display_surface, color, (int(self.x), int(self.y)), self.radius)
        else:
            pygame.draw.ellipse(display_surface, color, (int(self.x) - self.ellipse_x_radius, int(self.y) - self.ellipse_y_radius, self.ellipse_x_radius * 2, self.ellipse_y_radius * 2))

        if self.collision(self.x, self.y, character): 
            print("충돌 발생!")
        
 
    def collision(self, enemy_x, enemy_y, character):
       # x축 겹치는지 체크
        x_collision = enemy_x + self.ellipse_x_radius > character.x - character.ellipse_x_radius and enemy_x - self.ellipse_x_radius < character.x + character.ellipse_x_radius
        
        y_collision = enemy_y + self.ellipse_y_radius > character.y - character.ellipse_y_radius and enemy_y - self.ellipse_y_radius < character.y + character.ellipse_y_radius
        # x축 y축 고려하여 충돌 판별
        return x_collision and y_collision
