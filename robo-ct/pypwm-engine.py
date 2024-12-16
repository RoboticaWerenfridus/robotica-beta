draw_text("Controllers: " + str(pygame.joystick.get_count()), font, pygame.Color("azure"), 10, 10)
for joystick in joysticks:
    draw_text("Battery Level: " + str(joystick.get_power_level()), font, pygame.Color("azure"), 10, 35)
    draw_text("Controller Type: " + str(joystick.get_name()), font, pygame.Color("azure"), 10, 60)
    draw_text("Number of axes: " + str(joystick.get_numaxes()), font, pygame.Color("azure"), 10, 85)
