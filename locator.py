from audio import Audio
from input import Input


class Locator():
    '''supplies access of various systems globally'''

    audio = None
    input = None
    scene = None
    delete_queue = []

    def provide_audio(audio:Audio):
        '''provide the audio system'''
        Locator.audio = audio

    def provide_input(input:Input):
        '''provide the input system'''
        Locator.input = input

    def provide_scene(scene):
        '''provide the scene system'''
        Locator.scene = scene

    def get_audio():
        '''returns the audio system'''
        return Locator.audio
    
    def get_input():
        '''returns the input system'''
        return Locator.input.input_queue
    
    def get_scene():
        '''returns the scene system'''
        return Locator.scene
    
    def queue_free(obj):
        '''queues obj to be deleted'''
        Locator.delete_queue.append(obj)