import pygame
import random

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("game")

player_x = 200
player_y = 200
player_width = 20
player_height = 20
player_vel = 10

object_width = 30
object_height = 30

player_vel = 5

run = True

score = 0

# Create a list to store stationary objects
objects = []

# Define a class for objects

collision_sound = pygame.mixer.Sound("collision_sound.wav")


class GameObject:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        pygame.draw.rect(win, (50, 125, 113),
                         (self.x, self.y, self.width, self.height))

# Function to check for collisions between two rectangles


def is_inside_rect(rect, point):
    x, y, width, height = rect
    px, py = point
    return x <= px <= x + width and y <= py <= y + height


def generate_objects():
    for _ in range(5):  # Adjust the number of new objects to your preference
        new_object = GameObject(
            random.randint(0, 500 - player_width),
            random.randint(0, 500 - player_height),
            player_width, player_height
        )
        objects.append(new_object)


def is_collision(rect1, rect2):
    x1, y1, width1, height1 = rect1
    x2, y2, width2, height2 = rect2
    if (x1 < x2 + width2 and x1 + width1 > x2 and
            y1 < y2 + height2 and y1 + height1 > y2):
        return True
    return False


# Create stationary objects
objects.append(GameObject(100, 100, object_width, object_height))
objects.append(GameObject(300, 300, object_width, object_height))
objects.append(GameObject(400, 150, object_width, object_height))

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_x > 0:
        player_x -= player_vel
    if keys[pygame.K_d] and player_x < 500 - player_width:
        player_x += player_vel
    if keys[pygame.K_w] and player_y > 0:
        player_y -= player_vel
    if keys[pygame.K_s] and player_y < 500 - player_height:
        player_y += player_vel

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (player_x, player_y,
                     player_width, player_height))

    # Draw and check for collisions with stationary objects
    for obj in objects:
        obj.draw()
        if is_collision((player_x, player_y, player_width, player_height), (obj.x, obj.y, obj.width, obj.height)):
            objects.remove(obj)
            score += 1

            collision_sound.play()

    if not objects:
        generate_objects()

    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (95, 50, 199))
    win.blit(text, (20, 20))

    pygame.display.update()

pygame.quit()
