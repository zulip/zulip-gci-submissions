# Tools and Customization

### Review User Guides On:
 - Import users and channels from Slack
 - Restrict new users by email domain
 - Allow joining without an invitation
 - Manage who can send invitations
 - Set the default language for new users

The procedures and user experience for all the above operations are pretty straightforward.
The key is the simplicity: we don't want to over complicate the steps for a simple task.
I did all the listed operations on a local dev instance in MacOS High Sierra, by following all the guides word by word.

### Breakdown:
#### Import users and channels from Slack
[Link.](https://zulip.com/help/import-users-and-channels-from-slack)
The link `Your Account` is pretty much useless and irrelevant. The steps are otherwise easy to follow and appropriate.

#### Restrict new users by email domain
[Link.](https://zulip.com/help/restrict-user-email-addresses-to-certain-domains)
The steps for this operation are straightforward and easy to follow. I have no suggestions.

#### Allow joining without an invitation
[Link.](https://zulip.com/help/allow-anyone-to-join-without-an-invitation)
Step 2 has incorrect English. It should be `To limit new members of your organization to those who have been invited, click the  Users need an invitation to join checkbox.` instead of `To limit new members of your organization to those who have been invited to do so, click the  Users need an invitation to join checkbox.`.

#### Manage who can send invitations
[Link.](https://zulip.com/help/only-allow-admins-to-invite-new-users)
A link to the previous operation documentation might be useful as it is directly referred in step 2. Furthermore the `this` in step 2 (in the line between step 2 and step 3) is quite ambiguous, ie. it can refer to any of the 2 checkboxes mentioned in the previous line (ie. step 2). It needs to be clarified that we are specifically talking about the `Only admins can invite new users` checkbox. It would also help in searching and navigating the documentation if the title of the page could match the link in the left side navigation drawer. It happened that I knew what heading I was looking for, but the I couldn't find a link in the left navigation drawer that matched it.
 
#### Set the default language for new users
[Link.](https://zulip.com/help/change-the-default-language-for-your-organization)
The documentation for the operation is short, concise and easy to follow. The `default language` option is actually a dropdown list, so the step 2 should be combined with step 3 and should be more like `Select the appropriate option from the dropdown list in the Default Language Option under the Language and Notifications settings.`.

### Conclusion:
The documentation for the listed operations were pretty precise and easy to follow. Not many questions popped up in my head. The suggestion to match the Documentation page titles with the links in the left side navigation bar, would definitely make navigating and searching the documentation easier (I can tell from my personal experience). The documentation for these operations is very consistent in language and format.
