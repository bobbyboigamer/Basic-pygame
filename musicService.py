import pygame
import random

class MusicService:
  def get_Background_Music():
    return [
        'Music/She_studious_girl_by_tohomoko.mp3',
        'Music/2Hardlight_Groove_by_iteachvader.mp3', 
        'Music/Wanderer_-_A_cool_vs_dave_and_bambi_agony_series_fantrack.mp3',
        'Music/Cirno_trumpet.mp3',
        'Music/2Hardlight_Groove_by_iteachvader.mp3',
    ]
  
def startMusic(volume):
    if pygame.mixer.music.get_busy():
        return

    musics = MusicService.get_Background_Music()
    filename = random.choice(musics)
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()