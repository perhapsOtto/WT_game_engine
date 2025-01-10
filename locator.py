from audio import Audio


class Locator():

    audio = None

    def provide_audio(self, audio:Audio):
        Locator.audio = audio

    def get_audio(self):
        return Locator.audio