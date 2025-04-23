import pygame

class Character8:
    def __init__(self, x, y, radius, ellipse_x_radius, ellipse_y_radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.ellipse_x_radius = ellipse_x_radius
        self.ellipse_y_radius = ellipse_y_radius

    def set_input(self, key, walls):
        offset = 20
                
        if key == pygame.K_a:  # 왼쪽
            o_x = self.x - offset # 왼쪽으로 이동할 x 좌표
            if not self.collision(o_x, self.y, walls): #충돌 안하면 코드 실행
                self.x -= offset
                print(o_x)
        elif key == pygame.K_d:  # 오른쪽
            o_x = self.x + offset # 오른쪽으로 이동할 x 좌표
            if not self.collision(o_x, self.y, walls): #충돌 안하면 코드 실행
                self.x += offset
                print(o_x)
        elif key == pygame.K_w:  # 위쪽
            o_y = self.y - offset # 위쪽으로 이동할 y좌표 
            if not self.collision(self.x, o_y, walls): #충돌 안하면 코드 실행 
                self.y -= offset 
                print(o_y)
        elif key == pygame.K_s:  # 아래쪽
            o_y = self.y + offset # 아래쪽으로 이동할 y좌표
            if not self.collision(self.x, o_y, walls): #충돌 안하면 코드 실행 
                self.y += offset
                print(o_y)
        
        self.collision(self.x, self.y, walls)
        
    def set_position(self, x, y):
        self.x = x
        self.y = y

    def draw(self, frame, display_surface, color, walls):
        if frame <= 30:
            # 원 그리기
            pygame.draw.circle(display_surface, color, (int(self.x), int(self.y)), self.radius)
        else:
            # 타원 그리기
            pygame.draw.ellipse(display_surface, color, (int(self.x) - self.ellipse_x_radius, int(self.y) - self.ellipse_y_radius, self.ellipse_x_radius * 2, self.ellipse_y_radius * 2))

    
    
    def collision(self, character_x, character_y, walls):
        for wall in walls:
            # x축 겹치는지 체크
            x_collision = character_x + self.ellipse_x_radius > wall.x and character_x - self.ellipse_x_radius < wall.x + wall.width
            # character_x =캐릭터의 중앙x 좌표 self.ellipse_x_radius =타원의 가로 반지름 wall.x = 벽의 왼쪽 x 좌표
            y_collision = character_y + self.ellipse_y_radius > wall.y and character_y - self.ellipse_y_radius < wall.y + wall.height
            # 두 조건이 모두 충족하면 충돌
            if x_collision and y_collision:
                return True # 충돌 발생
        return False  # 충돌 없음