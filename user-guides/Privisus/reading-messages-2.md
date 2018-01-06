Reviewing user guides: Reading Messages, Part 2
=====

In this document, I reviewed the following:

* Share a message or conversation
* Advanced search
* View a message's edit history
* View messages from a stream
* View messages from a topic
* View messages from a user
* View messages containing files or links

----

# Share a message or conversation

Introduction is fine, though the section could work just fine if the
introduction wasn't there.

The first step is not needed, as step 2 already implicitly "covers" step 1.

In my Zulip client (I'm running on Debian 9.3 stretch), it actually shows "Copy
link to conversation", not "Link to conversation". I haven't tested it anywhere
else yet, but I figure it would be useful to point that out. I suggest changing
"Link to conversation" to "Copy link to conversation" if the text is consistent
across all platforms.

Since this is a documentation, it would be informative to show what is the
format of the chat link. When I tried it myself, I get the format of 
`https://organization.link/#narrow/stream/streamname/subject/subjectname/
near/numbers`. I suggest putting that information for completeness.

The fourth step isn't really a step, it just explains the mechanism of the
process. I suggest not numbering this step so the next steps are shifted up by
1 and turning this step into a blue info box.

Step 5 is not useful, or it doesn't deserve a step for its current usefulness.
I suggest adding a little bit of information on how the user actually *shares*
the link (maybe say, by pasting it (`Ctrl+V`) to the chat, or something else).

I would also suggest an alternative approach aside from above. Step 5 can be
turned into a conclusion by not numbering it, thus completing the section.

# Advanced search

The introduction looks amazing, the figure (screenshot) is actually used
properly this time. 

I would suggest adding a subsection called **Operators** for easier navigation.
Upon reading this article, I decided to write the current structure of the
section, which looks something like this:

* Searching for messages
    1. (not named: about operators)
    2. Features and limitations
    3. Search operators
    4. Difference between `keyword`, `key phrase`, and `"key phrase"`
    5. Keyboard shortcuts

I'd like to say that (5) is actually justified to have its own subsection, so
it's fine to keep it that way.

(1), (3), and (4) could be merged into one called **Operators** subsection, and
the order should be changed for easier navigation such that it looks something
like this:

* Searching for messages
    1. Operators
        - Definition
	- Search operators
	- Differences between `keyword`, `key phrase`, and `"key phrase"`
    2. Features and limitations
    3. Keyboard shortcuts

Finally, the documentation doesn't really explain *how* should the user input
the search operators, it just explains the definition and the others. While I
see that it actually does explain how, I suggest expanding the explanation and
add more examples to guide the user into using the search operators.

# View a message's edit history

This section explains about how the user can view a message's edit history.
Introduction looks pretty good, but I would suggest chaning the second
statement into a boxed blue note just for consistency

The figure is used correctly and is marked with red numbers, indicating clearly
the description of each number. It even has the its own figure title, "Message
edit history modal", which is a plus from my side.

I suggest just changing "simply click the x (X) icon" to just "simply click the
X icon" as  it is pretty self-explanatory. Also I suggest adding a note about
how the user can exit the history modal with just pressing `Esc` on their
keyboard if they're using their PC.

# View messages

Because each section is too short to compile a full review on each one of them,
I decided to merge all four sections into a single review. This review can be
generalized and applied into each one of the section, so I don't have to type
the same thing over and over again.

In this section of the review, I reviewed about:

* View messages from a stream
* View messages from a topic
* View messages from a user
* View messages containing files or links

-----

These sections appear to lack a helping figure (such as screenshot). Most of
the time it is not needed, but for a topic like "View messages", it is
important to provide some expectation for what the user is going to see.

Seeing the pattern of the steps, it is easy to see that the steps that are
written can get repetitive. I suggest rewriting it such that it covers all
three sections into just one step, thus combining these three sections into one
section only.

Alternatively, aside from combining three sections into one section, I suggest
combining all four of the section into just one section. The section then can 
be divided into subections for easier navigation. Here's an example:

* View messages
	- View general messages (from a stream, topic, or user)
	- View messages containing files or links

It is up to the documenter how to approach these suggestions and I'm fine with 
both of them.

