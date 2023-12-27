import pygame
import random

class MusicService:
  def get_Background_Music():
    return [
        'Music/She_studious_girl_by_tohomoko.mp3',
        'Music/2Hardlight_Groove_by_iteachvader.mp3', 
        'Music/2Hardlight_Groove_by_iteachvader.mp3',
    ]
  
def startMusic(volume):
    if pygame.mixer.music.get_busy():
        return

    musics = MusicService.get_Background_Music()
    filename = random.choice(musics)
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()