Simulates DB with a list using different approaches to assign uuids to requestors.  For example, you have a bag of marbles, where people need to pick a single marble, yet they don't care what marble they get as long as they don't pick the same one as someone else.

See Makefile for different operations.

todo:
* design pattern for request routes
* add formal logging
* dependency injection
* flake8
* mypy
* autopep8?
* isort
* use object instead of tuple
* asynchronous update
* asynchronous reload when low


Get uuid `curl http://localhost:8000`

simulate a select query to get an available uuid then an update query to mark the uuid as used (duplicate uuids)
```
http_req_duration..............: avg=43.76ms  min=556µs  med=48.17ms max=52.89ms p(90)=51.55ms p(95)=51.7ms
```
simulate a select for update query to get an available uuid and mark the uuid as used (correct uuids)
```
http_req_duration..............: avg=78.01ms  min=134µs   med=47.4ms  max=228.25ms p(90)=223.96ms p(95)=225.27ms
```
simulate calling a stored procedure that selects 5 uuids (back ups in the case of simultaneous queries) and tries to update 1 to used (correct uuids)
```
http_req_duration..............: avg=24.27ms  min=207µs  med=25.64ms max=40.78ms p(90)=29.37ms p(95)=35.06ms
```
preload uuids into memory using the provider class that allows requests to get a uuid from memory and then synchronously sends an update query to mark the uuid as used.
```
http_req_duration..............: avg=23.65ms  min=193µs   med=25.77ms max=30.05ms p(90)=27.97ms  p(95)=29.17ms
```
preloaded uuids into memory using the provider class that allows requests to get a uuid from memory and then synchronously sends an update query to mark the uuid as used.  Additionally, when the provider class is low on uuids a request will synchronously load more uuids from the DB
```
http_req_duration..............: avg=40.41ms  min=0s      med=23.98ms max=2.34s   p(90)=30.61ms p(95)=35.67ms
```
preloaded uuids into memory using the provider class with no update query sent, simulating an asynchronous call to the DB to mark the uuid as used (planned for async update in future)
```
http_req_duration..............: avg=3.27ms   min=242µs med=2.97ms  max=10.72ms p(90)=6.51ms  p(95)=7.2ms
```