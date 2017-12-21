Reviewing user guides: Account Basics, Part 2
=====

In this document, I reviewed the following:

* Joining an organization
* Signing in
* Signing out
* Keyboard shortcuts
* Deactivate your account
* Zulip glossary
* The Zulip browser window
-----

Joining an organization
-----

The introduction looks great, so moving on.


Recall from **Change the date and time format**: `If you prefer to see the 
time displayed in a 24-hour format, you can do so easily using the following 
procedure: (1), (2), (3),...`

Basically, `if x, then do:`

The first sentence before the comma on step 1, which is `To join a Zulip 
organization`, should not be included into the step, it should be above the 
steps, after the introductory paragraph, just like above.

Now before all the steps, it becomes:

`...Administrators manage the organization, controlling the specific settings 
of the organizations that they own.`

`To join a Zulip organization, you can do so be using the following procedure:`

`(1) First, navigate to the URL...`

On step 4, it should be specified how long should the user wait for an email 
before clicking on the resend link.

On step 5, not only you should agree to the Terms of Service, you should also 
*read* it. I suggest simply changing it into "`... prompted to enter your Full 
name and to read and agree to the Terms of Service.`" (which is then 
emphasized more at step 6)

Signing in
-----

In the first tip, for the sake of consistency, it is probably the best choice 
to change `e-mail` to `email`

While it is great that this section covers all the ways you can get in, this 
section should also explain about what happens when

* You have the same email on each Zulip, Google, and GitHub account
* You don't have the same email

And tried to sign in using one of the ways.

This section can also explain, or add a little note about how to disable one 
method of login when that one  account is compromised.

Signing out
-----

Because it is so concise I almost have nothing to say here. Maybe a few will 
do:

* On step 1 of **Logging out on a browser**, you can also just press `g` to 
open the menu, I suggest adding "(or press `g`)" after `Click on the cog icon`
* In the end (conclusion), tell the user what should happen after the user 
signed out (will the user be redirected to the sign-in page, will the user be 
redirected to the Zulip server page)
* Honestly you can make it even shorter by just:

1. Click the menu icon
        * on a browser, it's the cog icon (or press `g`)
        * on the iOS app, it's the menu icon
        * on the Android app, it's the overflow icon
2.       Click the **Log out** option from the dropdown menu that appears.

Keyboard shortcuts
-----

Some user may don't know what/where `Fn` is, I suggest putting some 
information regarding `Fn` key.

For a key that both small letter and capital letter are used for a different 
shortcut, I suggest that it should be explicitly stated for easier navigation

From:  
**New stream message**: `c`  
**New private message**: `C`

To:  
**New stream message**:  Small `c`  
**New private message**: Capital `C`

I don't see any pattern regarding the arrangements for the *shortcut action*. 
I suggest sorting it alphabetically.

From: ..., `Reply to message`, `New stream message`, `New private message`, ...

To: ..., `New private message`, `New stream message`, `Reply to message`, ...

Between **Drafts** and **Menus** is "*Keyboard navigation (e.g. arrow keys) 
works as expected.*" I think it is better to just remove it altogether because 
keyboard navigation is already documented on **Navigation** and **Streams 
settings page**

Deactivate your account
-----

I would personally swap the order for step 1 (into `Navigate to settings page, 
then click to Your account tab`).

The use of blue boxed note and `Please note` should generally be consistent to 
just one way. ~~I suggest turning `Please note` statements into blue boxed 
"**Note:**"~~ You know what, after reading the entire thing, it's probably the 
best to turn the boxed blue note into a paragraph, slipping it between `Please 
note` and `in addition`, because that's when we tell the user the consequences 
that will happen if the user deactivates the account

Move the disclaimer to the top such that the user knows before it's too late. 
(For example, if the user's intent is to recreate their account, they won't be 
able to, but they have followed step 4 before reading the disclaimer. Now the 
disclaimer becomes useless.)

Zulip glossary
-----

**emoji** is not exclusive (many people already knew it), so I suggest 
removing it (**emoji reaction** however, can mean something else, so don't 
remove it).

I suggest rewording the meaning of `/me` from `is a reference to one's one 
name` to `is a reference to one's own name`

**private message** has an common acronym **PM** , so I suggest putting the 
common acronym beside the word. (becomes **private message (PM)**)

The Zulip browser window
-----

I think there's a typo in the first paragraph: `There are three major 
components the your Zulip browser window`.

I suggest changing it to `There are three major components on your Zulip 
browser window`

Specifying what components are there is also helpful `There are three major 
components on your Zulip browser window: Central panel, left sidebar, and 
right sidebar`

I suggest elaborating more about the streams section. In the screenshot, there 
are three vibrant streams (Denmark, Scotland, and Verona), and there are many 
more at the bottom, but the color are not so vibrant. I think it should be 
explained  more on why the streams are like that.

Finally, the right sidebar needs additional info on the circle icon (green, 
orange, white).

