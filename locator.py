from audio import Audio
from input import Input


class Locator():

    audio = None
    input = None
    scene = None
    delete_queue = []

    def provide_audio(audio:Audio):
        Locator.audio = audio

    def provide_input(input:Input):
        Locator.input = input

    def provide_scene(scene):
        Locator.scene = scene

    def get_audio():
        return Locator.audio
    
    def get_input():
        return Locator.input.input_queue
    
    def get_scene():
        return Locator.scene
    
    def queue_free(obj):
        Locator.delete_queue.append(obj)