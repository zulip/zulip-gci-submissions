I had no problems writing the bot. It was a simple and straight-forward 
procedure of following the guide.

I then started the bot to check for the first time if it was working. Satisfied
, I went to the bash window running the bot and used `Ctrl+C`. However the 
process wasn't successfully stopped and I started to get multiple responses 
from the bot. This was fixed by a restart, which was suggeseted in 
chat.zulip.org (Thanks to Xavier Cooney).

I proceeded to write the test for the bot, which was again an easy task.

My next problem was running the test, which kept failing with attribute errors.
 Again I found help in chat.zulip.org , where Robert Hönig told me I had to 
 activate the venv (Thanks)

Finally the test had an error, but I fixed that by changing the method call 
from `verify_reply` to `get_response` and used `assertEqual` instead to 
ensure the reply from the bot was correct