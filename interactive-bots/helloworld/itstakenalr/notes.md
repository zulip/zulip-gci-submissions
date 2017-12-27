I got this error on my server when I tried to run the bot the first few times:

```
TypeError: Cannot set property 'stream' of undefined
    at Object.exports.set_compose_defaults (http://zulip.itstakenalr.zulipdev.org:9991/static/js/narrow_state.js:83:21)
    at fill_in_opts_from_current_narrowed_view (http://zulip.itstakenalr.zulipdev.org:9991/static/js/compose_actions.js:167:37)
    at Object.exports.start (http://zulip.itstakenalr.zulipdev.org:9991/static/js/compose_actions.js:191:12)
    at Object.exports.respond_to_message (http://zulip.itstakenalr.zulipdev.org:9991/static/js/compose_actions.js:300:13)
    at HTMLDivElement.select_message_function (http://zulip.itstakenalr.zulipdev.org:9991/static/js/click_handlers.js:134:29)
    at HTMLDivElement.blueslip_wrapper (webpack:///./static/js/blueslip.js?/srv/zulip-npm-cache/6995b3c81fdb08085d6fa027c980db6e34f322cf/~/source-map-loader:225:25)
    at HTMLDivElement.dispatch (webpack:////srv/zulip-npm-cache/6995b3c81fdb08085d6fa027c980db6e34f322cf/~/jquery/dist/jquery.js?/srv/zulip-npm-cache/6995b3c81fdb08085d6fa027c980db6e34f322cf/~/source-map-loader!/srv/zulip-npm-cache/6995b3c81fdb08085d6fa027c980db6e34f322cf/~/source-map-loader:5206:27)
    at HTMLDivElement.elemData.handle (webpack:////srv/zulip-npm-cache/6995b3c81fdb08085d6fa027c980db6e34f322cf/~/jquery/dist/jquery.js?/srv/zulip-npm-cache/6995b3c81fdb08085d6fa027c980db6e34f322cf/~/source-map-loader!/srv/zulip-npm-cache/6995b3c81fdb08085d6fa027c980db6e34f322cf/~/source-map-loader:5014:28)
```
 It got fixed itself the next day when I restarted the server, but it didn't work before when I restarted it.
