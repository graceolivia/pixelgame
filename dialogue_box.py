import pygame

class DialogueBox:
    def __init__(self, screen, font, width, height, position, bg_color, text_color, hover_color):
        self.screen = screen
        self.font = font
        self.width = width
        self.height = height
        self.position = position
        self.bg_color = bg_color
        self.text_color = text_color
        self.hover_color = hover_color
        self.dialogue = ""
        self.options = {}
        self.option_rects = []

    def set_dialogue(self, dialogue, options):
        self.dialogue = dialogue
        self.options = options
        self.option_rects = []

    def draw(self):
        pygame.draw.rect(self.screen, self.bg_color, (self.position[0], self.position[1], self.width, self.height))
        lines = self.dialogue.split('\n')
        for i, line in enumerate(lines):
            rendered_text = self.font.render(line, True, self.text_color)
            self.screen.blit(rendered_text, (self.position[0] + 10, self.position[1] + 10 + i * 30))

        y_offset = self.position[1] + 10 + len(lines) * 30
        mouse_pos = pygame.mouse.get_pos()
        self.option_rects = []
        for option, next_dialogue in self.options.items():
            option_color = self.hover_color if pygame.Rect(self.position[0] + 10, y_offset, self.font.size(option)[0], self.font.size(option)[1]).collidepoint(mouse_pos) else self.text_color
            rendered_option = self.font.render(option, True, option_color)
            option_rect = rendered_option.get_rect(topleft=(self.position[0] + 10, y_offset))
            self.screen.blit(rendered_option, option_rect.topleft)
            self.option_rects.append((option_rect, next_dialogue))
            y_offset += 40

    def get_option_at_pos(self, pos):
        for option_rect, next_dialogue in self.option_rects:
            if option_rect.collidepoint(pos):
                return next_dialogue
        return None
