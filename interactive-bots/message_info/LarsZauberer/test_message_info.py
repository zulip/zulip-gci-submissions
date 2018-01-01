from zulip_bots.test_lib import BotTestCase

class TestHelpBot(BotTestCase):
    bot_name = "message_info"  # type: str

    def test_followup_stream(self) -> None:
        message = dict(
            type='privat',
            sender_email='message-info-bot@zulip.larszauberer.zulipdev.org',
        )