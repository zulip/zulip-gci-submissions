Reviewing user guides: Reading Messages, Part 1
=====

In this document, I reviewed the following:

* Navigation and unread counts
* View the Markdown source of a message
* View the exact time a message was sent
* View an image at full size
* Collapse a message
* Star a message
* Emoji reactions

-----

Navigation and unread counts
-----

The order of the subsection doesn't make sense alphabetically. It also doesn't
match with the title of the section ("Navigation and unread counts"). I suggest
swapping the order between two subsection so it matches the section title, and
it also make sense alphabetically.

In the explanation of **Unread messages**, below "These goals are achieved...",
it definitely takes a very descriptive approach of explaining the details. To
support this style of explanation, I suggest adding a supporting figure (such
as screenshot) to make it easier for the user to understand.

In the **Navigation** section, Some user may actually prefer *not* catching up
certain discussions that happened while they are away from their computer. I
suggest adding more detail on how to prevent the automated "left to your first
unread message" if possible. If it is not possible, maybe add more emphasis on
that, too.

View the Markdown source of a message
-----

The introduction looks good. So moving on.

I see that it takes the same approach to explain the steps, so I suggest
putting a helping figure (like screenshot) to guide more on how the user should
view the markdown source of a message.

On step 1, the user may don't have the ability to "hover over a message" if
they are on their phone. I suggest explaining about this so the guide can get
more coverage (not just PC users, but also non-PC users).

I have yet to find another way to view the markdown source of message if my
message is *not* too old to edit. Do the user actually have to use the edit
button, beside the chevron, just to see the markdown source of their own
message? Will the message than be marked as (EDITED) if they do so, even though
no changes are made? I suggest putting more information on that.

View the exact time a message was sent
-----

I suggest a more specific title, such as "View the exact time a message was
sent and received in the server". I haven't known about this yet because I
haven't tried it, but if the user sends the message at 7:00 AM, only to find
out that their internet are down at that moment, will the timestamp change to
reflect the time it was received in the server, or will it stay the same?

The figure doesn't indicate anything, or I personally think that the figure
doesn't point it so that it is more obvious to me to notice. Maybe I'm just 
used to seeing arrows more than red boxes, maybe I'm just used to seeing 
circles more than red boxes. I think it didn't seem obvious because there's
also this blue box, which doesn't indicate anything. If it doesn't indicate
anything, It follows that the red boxes *shouldn't* indicate anythng either.
It all boils down to this: You can make the mark of the timestamp a little bit
more obvious than a red box (maybe a red circle, to differentiate it between
the blue box), or just put a red arrow, pointing to the timestamp. You would
think that this is a little bit overkill to point this out because of the
simplicity of the section, but it is a good habit to actively try to avoid this
type of thinking to make a better documentation.

I suggest adding more information on how the user can see the *actual* exact
time a message was sent, it is by hovering their mouse to the timestamp. Also
consider non-PC users on how they would accomplish the same task as they were
on their PC.

View an image at full size
-----

This is optional, but I think the screenshots here should be connected to each
other. To explain this point more clearly, Take a look at the first screenshot.
It shows a message with `octopus.png`, but in the second screenshot, after
reading "clicking it will open a lightbox modal with varying options...", you
apparently get a picture of a sunset. Which is quite amusing, believe me. But I
would prefer more on the flow of the article. 

I suggest changing "Images can be opened in new tabs by clicking the Open
button..." to something along the lines of "Clicking Open on the lightbox modal
will create a new tab on your browser to show the image.". This can be
beneficial for non-browser users, because they might not expect this new tab to
be a browser tab, they might expect it to be  Gallery in Android, for example,
or another instance of Zulip popping out just to preview the image in Windows
or Linux or Mac.

I suggest minor changes about how shortcut keys should be typed in the tip. So
"press the escape key" should become "press the `Esc` key". Also, the x icon is
obvious enough, so I think the icon alone will do just fine ("Click the x (X)
icon" to "Click the X icon").

Collapse a message
-----

There is a shortcut to collapsing the selected message, I suggest adding that
as a boxed yellow tip below step 2, telling that just by clicking the message
and press `-`, the message will collapse.

The wording in step 1 could be reduced to "Hover on a message, then select the
chevron icon beside the timestamp <+to reveal an actions dropdown>" for 
simplicity.

It would be nice if there is a screenshot on how to dropdown looks like, but I
guess it is optional and not needed for this section because it's obvious
enough.

Star a message
-----

Add a tip about starring the message with just using shortcuts, mainly the `*`
key. It is best to put the tip below step 2 because it is optional to
accomplish the task itself, but it is related enough to be a tip.

I suggest another addition about how starred messages is not local to their own
computer, meaning that it can also show up in their non-PC client of Zulip (it
syncs together).

Another screenshot to help visualize the process will be great. But again, with
such simple article like this, I don't think it is needed, but I recommend it
though.

Emoji reactions
-----

It's maybe just me, but the introduction is not what I wanted to hear. The tone
is like "instead of actually spending a relatively quick time to write and
respond to a message, you can even do it more quickly by just responding it 
with a single emoji". I suggest changing it such that it becomes more formal,
like "You can quickly show your reaction for a certain message by doing an
emoji reaction to a message. Here's how you do it:".

Step 2 can definitely be "simplified" to "Hover a message to show three new
icons beside the timestamp, then click the (`smiley_face_icon`) to reveal the
emoji menu".

The next statement after that should be its own tip. It should be separated
from the step, as it is just showing an alternative way of doing it.

Finally, the steps wouldn't work for their own message, because the smiley face
is actually on the dropdown menu, I suggest putting an information regarding 
that as a blue boxed note.
