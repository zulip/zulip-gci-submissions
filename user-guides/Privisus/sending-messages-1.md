Reviewing user guides: Sending Messages, Part 1
=====

In this document, I reviewed the following:

* Send a stream message
* Private messages
* Send a private message
* Group private messages
* Format your message using Markdown
* Preview your message before sending
* Message drafts

-----

Send a new stream message
-----

The first paragraph is not needed ("Follow the following steps to x") because
it contributes no value to the documentation. I suggest changing it to explain
why the user might want to send a new stream message for a new topic, instead
of the current one.

It is best to put only the essentials at every step. On step 2, "When you begin
typing a stream name, autocomplete suggestions will appear", will more likely
be considered a yellow boxed tip, rather than a must know to accomplish the
task.

The topic field should have more general guideline other than just 60 character
limit. Tell the user what they should actually put in the Topic field, what is
appropriate and what is *more* appropriate.

The tip below step 5 is a good touch. It introduces to the user the concept of
shortcuts, but the necessity is still questionable, especially in a user
documentation, where the user just wants to know about a particular topic and
not the other. Should we allow this in a user documentation? The other tip (the
last one), however, is more appropriate to put in there because it suits more
to the section. In the end, I think there must be a line drawn to add the right
and suitable tip.

Private messages
-----

Again, it is not necessary to put the "Follow the following steps..." into the
documentation. It **is** the documentation, meant to act as a reference for
something.

Step 1 shows clearly what the user should do and what the user should expect
from doing so, with a helping figure as needed. This is how I like the step to
be written.

The last sentence of step 2 is not needed to complete the task. I suggest
changing it to note/tip.

Below step 4, You can see that having an unrelated (but can be useful tip) 
can be a clutter to the section. Also refer to (above section) as to why
we should draw a line for appropriate tip.

Send a private message
-----

I highly suggest changing the LEFT green sidebar heading title to be exactly
what it is, Seeing "Private messages" being click and the content's heading title
is "Send a private message" (which is the next article's title), is
confusing.

The last article showed the same topic, I don't see a reason for a separate one
instead of just merging both article together. If it is **really** necessary,
more specific title should be used to differentiate between the articles.

I feel this section should have a helping figure to explain the steps more
clearly, just like the previous one.

If you noticed carefully, you can see that the first subsection title is
missing, while the second subsection title is there ("View your private message
history with a user and compose"). I don't know if this is intentional, but I
suggest adding the subsection title for structure.

Group private messages
-----

Honestly this article should also be merged with the previous two, and just
name it to "Private messages". I don't feel like it deserves another article
just to explain about private messages.

In the tip, I suggest adding a link to where each location is, maybe direct
the user to **Account basics -- The Zulip browser window** will be more useful
(where is the *filter* that you're talking about? where is the right sidebar?
I only see the left one)

Another reason to merge the articles is to avoid duplicate tip, as shown in
"Private messages" and "Group private messages". They both have the same exact
tip at the end. This wouldn't have happened if it was just one article. I am
aware that maybe some of the duplicate ones are justifiable to not be removed,
but I think removing this one would be more appropriate. While it may take some
time to merge the articles, I think it will come up more concise and simplified
than the three articles put separately.

Format messages using Markdown
-----

When I entered the link of "GitHub Flavored Markdown", I get directed to the
tables section. Does the implementation starts from here, or is it just a
misleading link? I suggest explaining more about how much it varies between the
GFM and the Zulip markdown.

This article contains many useful figures, which is great. However, this can
lead to some minor navigation problems. Putting a brief table of content on top
of the article should do it.

In the **Extra emphasis** subsection, The user should know that the order of
the emphasis doesn't matter, the user just needs to remember how to properly
wrap the text with them (`** * is this okay? ** *`, and `** * is this more
okay? * **`). I suggest this, turning it to a boxed yellow tip.

Preview your message before sending
-----

Oh look, this one actually has the same title as the sidebar. Nice.

I don't have anything to say here. I mean it is just two sentence with a figure
attached between them. I do have a couple suggestion though. The figure should
show the initial state (before clicking the eye) instead of just the after
state (after clicking the eye). I recommend putting both figures, or just the
initial state figure.

Message drafts
-----

The introduction looks great. So moving on.

In the note, it says "Drafts are stored in your client". I think in the
documentation, it is appropriate to say *where* it is stored. Is it actually
stored **inside** the executable client? is it stored somewhere else? Can the
user backup the draft? I suggest adding more information on that.

While it is obvious, some user may don't know where compose box is located. I
suggest linking the first occurence of "compose box" to **Account basics -- The
Zulip browser window**.

Finally, I suggest a minor addition into how the draft is sorted (is it
descending or ascending)
