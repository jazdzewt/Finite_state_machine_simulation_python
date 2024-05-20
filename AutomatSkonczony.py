import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Wizualizacja Automatu Skonczonego')

background = pygame.image.load('background.png')

transitions = {
    'q0': {'0': 'q1', '1': 'q2'},
    'q1': {'0': 'q3', '1': 'q0'},
    'q2': {'0': 'q0', '1': 'q3'},
    'q3': {'0': 'q1', '1': 'q2'},
}

state_positions = {'q0': (60, 60), 'q1': (340, 60), 'q2': (60, 340), 'q3': (340, 340)}

clock = pygame.time.Clock()

current_state = 'q0'
previous_state = None

def find_inccorect (binary_array):
    bits = {'0', '1'}
    inccorect = [char for char in binary_array if char not in bits]
    return inccorect 

while True:
    binary_input = input("Wpisz ciag binarny: ")

    if all(char in '01' for char in binary_input):
        break
    else:
        wrong_characters = find_inccorect(binary_input)
        print(f"Zly ciag! {wrong_characters} - to nie liczby binarne!")

running = True
index = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    
    screen.blit(background, (0, 0))
    pygame.display.update()

    for state, pos in state_positions.items():
        if state == 'q3':
            pygame.draw.circle(screen, (50, 200, 100), pos, 40, 4)
            pygame.draw.circle(screen, (0, 0, 0), pos, 35, 4)
        else:  
            pygame.draw.circle(screen, (0, 0, 0), pos, 35, 4)
        text = pygame.font.SysFont(None, 30).render(state, True, (0, 0, 0))
        text_rect = text.get_rect(center=(pos[0], pos[1]))
        screen.blit(text, text_rect)
    screen.blit(pygame.font.SysFont(None, 30).render('START', True, (0, 0, 0)), (30, 8))

    pygame.draw.circle(screen, (200, 50, 50), state_positions[current_state], 35, 4)

    pygame.display.flip()

    if index < len(binary_input):
        bit = binary_input[index]
        previous_state = current_state
        current_state = transitions[current_state][bit]
        index += 1
        pygame.time.wait(1000)

    clock.tick(10)

    if index == len(binary_input) and current_state == 'q3':
        print(f"Ciag: {binary_input} zostal zaakceptowany!")
        running = False
    elif index == len(binary_input):
        print("Ciag nie zostal zaakceptowany!")
        running = False

pygame.quit()
sys.exit()
