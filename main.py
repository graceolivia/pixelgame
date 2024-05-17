import pygame
import sys
from dialogues import dialogues
from dialogue_box import DialogueBox

pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Branching Dialogue Game")

font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

char_speed = 5
char_image = pygame.image.load("girl.gif")
char_rect = char_image.get_rect()
char_rect.topleft = (width // 2, height // 2)

# load the spritesheet
spritesheet = pygame.image.load("npc.png")

# sprite sheet settings
frame_width = 16  # width of each frame
frame_height = 16  # height of each frame
num_frames = 4  # number of frames in the spritesheet

# extract frames from the spritesheet
npc_frames = []
for i in range(num_frames):
    frame = spritesheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
    frame = pygame.transform.scale(frame, (frame_width * 4, frame_height * 4))  # scale frames
    frame = pygame.transform.flip(frame, True, False)  # flip frames horizontally
    npc_frames.append(frame)

npc_rect = npc_frames[0].get_rect()
npc_rect.topleft = (width - (width // 4), height // 2)

# animation settings
npc_frame_index = 0
npc_frame_delay = 100  # milliseconds
npc_last_update = pygame.time.get_ticks()

dialogue_box = DialogueBox(screen, font, width, 150, (0, height - 150), (50, 50, 50), (255, 255, 255), (255, 0, 0))
current_dialogue = 'start'
selected_option = None

dialogue_box_visible = False

while True:
    for event in pygame.event.get():
        print(dialogue_box_visible)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                selected_option = 'left'
            elif event.key == pygame.K_RIGHT:
                selected_option = 'right'
            elif event.key == pygame.K_UP:
                selected_option = 'yes'
            elif event.key == pygame.K_DOWN:
                selected_option = 'no'
            elif event.key == pygame.K_RETURN and selected_option:
                if selected_option == 'exit':
                    print("Exit option selected. Hiding dialogue box.")
                    dialogue_box_visible = False
                else:
                    current_dialogue = dialogues[current_dialogue]['options'].get(selected_option, 'end')
                    dialogue_box.set_dialogue(dialogues[current_dialogue]['text'], dialogues[current_dialogue]['options'])
                selected_option = None
        elif event.type == pygame.MOUSEBUTTONDOWN and dialogue_box_visible:
            next_dialogue = dialogue_box.get_option_at_pos(event.pos)
            if next_dialogue:
                if next_dialogue == 'exit':
                    print("Exit option selected. Hiding dialogue box.")
                    dialogue_box_visible = False
                else:
                    current_dialogue = next_dialogue
                    dialogue_box.set_dialogue(dialogues[current_dialogue]['text'], dialogues[current_dialogue]['options'])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        char_rect.x -= char_speed
    if keys[pygame.K_RIGHT]:
        char_rect.x += char_speed
    if keys[pygame.K_UP]:
        char_rect.y -= char_speed
    if keys[pygame.K_DOWN]:
        char_rect.y += char_speed

    if char_rect.left < 0:
        char_rect.left = 0
    if char_rect.right > width:
        char_rect.right = width
    if char_rect.top < 0:
        char_rect.top = 0
    if char_rect.bottom > height:
        char_rect.bottom = height

    if char_rect.colliderect(npc_rect) and not dialogue_box_visible:
        current_dialogue = 'collision_event'
        dialogue_box.set_dialogue(dialogues[current_dialogue]['text'], dialogues[current_dialogue]['options'])
        dialogue_box_visible = True

    # update npc frame for animation
    current_time = pygame.time.get_ticks()
    if current_time - npc_last_update > npc_frame_delay:
        npc_frame_index = (npc_frame_index + 1) % num_frames
        npc_last_update = current_time

    screen.fill((0, 0, 0))

    screen.blit(char_image, char_rect.topleft)
    screen.blit(npc_frames[npc_frame_index], npc_rect.topleft)

    if dialogue_box_visible:
        dialogue_box.draw()

    pygame.display.flip()

    clock.tick(30)
