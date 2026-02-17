import pygame

# --- Textbox Configuration ---
LINES_PER_PAGE = 3

class Textbox:
    def __init__(self, width, height):
        self.width = width
        self.height = 150
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.set_alpha(200)
        self.surface.fill((30, 30, 30))
        self.x = 0
        self.y = height - 150
        self.visible = False
        self.font = pygame.font.SysFont("Arial", 26)
        self.text = ""
        self.lines = []
        self.current_line_index = 0
        self.lines_per_page = LINES_PER_PAGE
        self.z_pressed = False

    def set_text(self, text):
        self.text = text
        self.lines = text.split('\n')
        self.current_line_index = 0
        self.visible = True

    def advance(self):
        if self.current_line_index + self.lines_per_page >= len(self.lines):
            self.visible = False
            self.current_line_index = 0
        else:
            self.current_line_index += self.lines_per_page

    def draw(self, screen):
        if self.visible:
            self.surface.fill((30, 30, 30))
            start_idx = self.current_line_index
            end_idx = min(start_idx + self.lines_per_page, len(self.lines))
            current_lines = self.lines[start_idx:end_idx]
            y_offset = 20
            for line in current_lines:
                text_surf = self.font.render(line, True, (255, 255, 255))
                self.surface.blit(text_surf, (30, y_offset))
                y_offset += 35
            screen.blit(self.surface, (self.x, self.y))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            if not self.z_pressed and self.visible:
                self.advance()
                self.z_pressed = True
        else:
            self.z_pressed = False


def check_dialogue(npc_list, player, screen, textbox):
    """Check if player is colliding with any NPC and handle dialogue"""
    keys = pygame.key.get_pressed()
    
    # Check if Z key is pressed to initiate dialogue
    if keys[pygame.K_z]:
        if not textbox.visible and not textbox.z_pressed:
            for npc_rect, npc_text in npc_list:
                if player.rect.colliderect(npc_rect):
                    textbox.set_text(npc_text)
                    textbox.z_pressed = True
                    break
    
    # Update and draw textbox
    textbox.update()
    textbox.draw(screen)