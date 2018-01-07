Reviewing user guides: Account Basics, Part 1
=====

In this document, I reviewed the following:

* Change your name
* Change your email address
* Manage your password
* Edit your settings
* Set your avatar
* Change your default language
* Use 24-hour time
-----

Change your name
-----
 I suggest changing

From:  `It's easy to change how your name is shown in Zulip... `

To: `This section will show you how to change your display name in Zulip...`

While it is good to provide some sense of easiness to the user, it is best to keep it out of the documentation as it is not needed to "change my name" (I don't care if it's easy or not, the documentation will lead me through it anyway).

The second next thing, which is `With full Unicode support, you can spell your name exactly how you'd like it to be displayed.` Is meaningless without the user explicitly knows what Unicode is. I suggest explaining briefly why Unicode matters to spell my name exactly the way the user wanted it.

From: `With full Unicode support, you can spell your name exactly how you'd like it to be displayed.`

To: `With Unicode support, you can spell your name exactly how you'd like it and not just limited to a regular character on the qwerty keyboard. Example: 名字`

Otherwise, it seems redundant to put it.

I suggest changing the order of the step 1

From: `Go to the Your account tab of the Settings page.`

To: `Go to the Settings page, then click at the Your account tab`

This way, it's chronologically more pleasing to see and to do (maybe it is just my personal taste, maybe it's not).

Maybe it's just me, but I don't know what LDAP is. So maybe put the acronym for it?

Again, not trying to be a jerk here, but I don't think we need to congratulate the user for changing their full name, do we? I suggest changing it to more like a "conclusion" type of text, like in **Manage your password - If you forgot your password**'s conclusion: `You will receive an email with instructions on how to reset your password.`

So from: `Congratulations! You have updated your name.`

To something along the lines of: `Your name will be displayed immediately when you press "Save changes"`

Therefore it will be more informative and useful to the user.

 Change your email address
-----

I suggest changing the order of step 1 (see above, the reason is similar).

On the step 5, add more details on who sent the email, what is the title, and briefly tell the content that the user should expect. This is useful to verify the integrity of the email itself, and to avoid clicking the *wrong* "*confirmation link totally not a fake site to get my password*" (Even if you know you didn't request for an email change, the email may lead you into a false sense of urgency, something like: "If you didn't request for an email change, your account is being compromised, click here to protect your account", which can ironically lead to the user being compromised)

The current documentation didn't say how to differentiate between a normal user and a "Zulip organization administrator". I don't know how to either. Am I expected to know it before joining the organization? If I somehow forgot, is there a way to differentiate that by looking at the user list?  Maybe add some information on that.

Manage your password
-----
(the heading is actually **Change your password** but it doesn't matter, refers to the same thing)

I suggest changing the order of step 1 (see above).

Although it is not important, I feel it is better to be more explicit even though it is very obvious where the location of the "Change password" account.

From: `Click the Change password button located underneath your name.`

To: `Click the Change password button located underneath the Full Name field.`

From step 3: `You will first be asked...` When? It just shows another three boxes (it didn't really ask me to do anything, though). I suggest changing it into "`Three new boxes will appear when you clicked the button. Fill the boxes as described and click Save Changes to confirm your action`" (just like the step 3 in **if you forgot your password**. It directs the user explicitly and telling the exact step on how the user should do it)

After `You will receive an email with instructions on how to reset your password.`, adding a little bit of info about the contents of the email is useful to check the integrity of the email.

Edit your settings
-----

Looks fine here. It is clear, it is direct, and it is easy to follow. Couple suggestions:

* On the first step, you can also just press `g`, and the menu will show up.
* The first step and the second step can also be combined to just one step (press `g` or click the cog icon, and click on Settings) 
* Just like the first screenshot, the second screenshot should just show the tabs on the left, and not the entire settings screen.

Set your avatar
-----

The introduction is perfect. I personally like this style of documentation because while it is not obvious at first, it then explains to the user why does `By default, Zulip uses avatars from Gravatar.` matter at all.

If you don't get it already, I suggest changing the order of step 1 (see above)

This section lacks the conclusion text, I suggest adding it, telling the user what should happen after all the steps have been done (something like `Your avatar should update within x minutes/Your avatar should be updated shortly after you confirm your changes`).

Change your default language
-----

Again, I like the introduction style here. It is informative and clear, you can almost say that it somewhat makes me more *engaged*.

I suggest changing the order of step 1 (again, maybe just my personal taste)

The first tip, which is `You can help translate parts of Zulip by signing up for an account at Transifex.`, is not really a tip, is it? It's more like an *info*. I suggest changing it to info.

Lastly, recall from **Change your password -- If you forgot your password**'s conclusion text: `You will receive an email with instructions on how to reset your password.`

For the sake of consistency, let step 4 be the conclusion text (or the other way around. I personally prefer changing step 4 to the conclusion)

Use 24-hour time
-----

Introduction is good, steps are good (remember step 1 suggestion though, see above), but it lacks the conclusion (what should happen after all the steps have been accomplished?). Overall, it doesn't need much explanation to change the date and time format.

Finally, when reviewing the documentation, I noticed different heading titles between the green sidebar on the left, and the content heading on the top (some, but not all). In this case, **Use 24-hour time** (sidebar) and **Change the date and time format** (content). I don't know if this is intended, but just want to point that out.
