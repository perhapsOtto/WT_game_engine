import simpleaudio
from audioplayer import AudioPlayer

class Audio():

    def __init__(self, resource):
        pass#sound = AudioSegment.from_wav("sounds/project_3.wav")

    def play_sound(self, sound, volume):
        """adds sound to the audio queue"""
        #TODO: play sound
        pass

    def play_sound_imm(self, sound, volume):
        """sends sound to the audio player immediately (don't overuse)"""
        #sound_object = simpleaudio.WaveObject.from_wave_file(sound)
        #play_object = sound_object.play()
        test=AudioPlayer(sound).play(block=False)

    def stop_sound(self, sound):
        """stops sound"""
        #TODO: how the heck is this gonna happen (sound IDs?)
        pass

