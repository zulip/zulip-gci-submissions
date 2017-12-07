#!/usr/bin/env python

from zulip_bots.test_lib import StubBotTestCase

class TestHelpBot(StubBotTestCase):
    bot_name = "lunch"

    def test_bot(self):
        dialog = [
            ('', "I don't think I can do that. :frowning:")
        ]

        self.verify_dialog(dialog)
