# Runscope Integration Investigation

* [Runscope](https://runscope.com) is a company that provides solutions for API Performance Testing.

* Runscope helps a company to conduct API Performance tests on an independent, hassle-free platform.

* Runscope already has integrations with Slack & generates notifications in Slack for the following cases:

  1. Test Passed

  2. Test Failed

* The Notification Model is:
  <br>
  ![The Notification Model Image](notification_model.PNG)

* The 'Test Passed' notification is:
  <br>
  ![The 'Test Passed' notification](test_passed.PNG)

* The 'Test Failed' notification is:
  <br>
  ![The 'Test Failed' notification](test_failed.PNG)


## Links

Slack API - https://api.slack.com


## Other Notes
* Paid Subscription to Runscope enables users to create a larger team. 
  It also increases test limits & amount of requests stored per bucket.
* The Notification Model attached above shows notifications generated for Email.
  Slack receives only 'Test Passed' & 'Test Failed' notifications.
