import pygame

class Item:
    def __init__(self, x, y, width, height):
        self.x = x  # 아이템의 왼쪽 위 좌표 x값
        self.y = y
        self.width = width # 아이템의 가로 길이(왼쪽에서 오른쪽까지 몇 픽셀인지)
        self.height = height        
        self.collected = False  # 게임 초기 상태 = 아이템 수집 안함 (처음엔 False)

    def draw(self, display_surface, color):
        if not self.collected: # 아이템이 수집되지 않으면 사각형으로 아이템 그림
            pygame.draw.rect(display_surface, color, (self.x, self.y, self.width, self.height))

    def collision(self, character_x, character_y, ellipse_x_radius, ellipse_y_radius):
        if self.collected: # 이미 수집된 아이템이라면 충돌 검사 안 함
            return False
        # 캐릭터와 아이템의 x축 충돌 여부 확인 
        x_collision = character_x + ellipse_x_radius > self.x and character_x - ellipse_x_radius < self.x + self.width
        #캐릭터의 오른쪽 끝이 아이템의 왼쪽 끝보다 오른쪽에 있다. 캐릭터의 왼쪽 끝이 아이템의 오른쪽 끝보다 왼쪽에 있다
        y_collision = character_y + ellipse_y_radius > self.y and character_y - ellipse_y_radius < self.y + self.height

        if x_collision and y_collision:  # x축과 y축이 모두 겹치면 충돌
            self.collected = True # 아이템을 수집한 상태로 표시
            return True # 충돌 발생 = 수집 함 

        return False # 충돌하지 않음 = 수집 안함