# StatusPage.io Integration Investigation

* [StatusPage.io](https://statuspage.io) is a customer relationship management software used by businesses 
  to update and inform their customers via Email or Webhook notifications.

* StatusPage.io provides a platform for businesses to create a custom Status Page.

* StatusPage.io already has integrations with Slack & can send out a notification to slack for the following cases:-

1. Creation of a new incident.

2. Updating the incident.

3. Adding a member to the team.

4. Removing a member from the team.

5. Changing status of components( e.g. API, Management Portal)

6. Time Notifications (Amount of time for which the incident is open.) [ Automatically generated, no Webhook payload]


* The Notification model image: https://github.com/MadElf1337/zulip-gci-submissions/blob/patch-12/webhook-integrations/StatusPage.io/notification_model.PNG

* The New Incident addition notification is: https://github.com/MadElf1337/zulip-gci-submissions/blob/patch-12/webhook-integrations/StatusPage.io/new_incident.PNG

* The Incident Update notification is: https://github.com/MadElf1337/zulip-gci-submissions/blob/patch-12/webhook-integrations/StatusPage.io/update_incident.PNG 

* The member addition notification is: https://github.com/MadElf1337/zulip-gci-submissions/blob/patch-12/webhook-integrations/StatusPage.io/adding_member.PNG

* The member removal notification is: https://github.com/MadElf1337/zulip-gci-submissions/blob/patch-12/webhook-integrations/StatusPage.io/removing_member.PNG

* The Component Status change notification is: https://github.com/MadElf1337/zulip-gci-submissions/blob/patch-12/webhook-integrations/StatusPage.io/adding_component.PNG

* The Time Notification is: https://github.com/MadElf1337/zulip-gci-submissions/blob/patch-12/webhook-integrations/StatusPage.io/incident_time.PNG

* Other Component Screenshots couldn't be added as they require a paid subscription to StatusPage.io services.
   (Only 2 components are free, API & Management Portal)

## Links
<br>
Slack API: https://api.slack.com/
<br>
StatusPage.io API: https://api.statuspage.io/v1/
<br>
(For StatusPage.io, API needs to configured first, & a key is required, which is obtained through the StatusPage.io
account.)


## Other Notes

* No webhook payload was generated when a member was added to/removed from the StatusPage.io team,
  but the app sent a message to the channel.
   (This might be happening as the notification for addition or removal of a member might not be configured by StatusPage.io
   for a webhook subscriber.) 
