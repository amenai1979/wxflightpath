from unittest import TestCase
import uuid
from wxflightpath.audiorender import *


class TestAudioRender(TestCase):
    briefing = "this is your briefing captain. Weather is fine today, you should go flying!"
    id=str(uuid.uuid1())
    filename= renderaudio(title="audio_briefing_test" + id , input=briefing)
    def test_init(self):
        self.assertEqual(self.filename,"../audio/audio_briefing_test"+self.id+".mp3")
        self.assertGreaterEqual(os.path.getsize(self.filename),21600)

    def tearDown(self):
        # Clean up resources after each test method
        if os.path.exists(self.filename):
            os.remove(self.filename)




