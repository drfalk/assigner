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

select then update (duplicate uuids)
```
http_req_duration..............: avg=43.76ms  min=556µs  med=48.17ms max=52.89ms p(90)=51.55ms p(95)=51.7ms
```
select for update (correct uuids)
```
http_req_duration..............: avg=78.01ms  min=134µs   med=47.4ms  max=228.25ms p(90)=223.96ms p(95)=225.27ms
```
stored procedure select 5 update 1 (correct uuids)
```
http_req_duration..............: avg=24.27ms  min=207µs  med=25.64ms max=40.78ms p(90)=29.37ms p(95)=35.06ms
```
preloaded uuids into provider with synchronous update
```
http_req_duration..............: avg=23.65ms  min=193µs   med=25.77ms max=30.05ms p(90)=27.97ms  p(95)=29.17ms
```
preloaded uuids into provider with synchronous update, one request synchronously loading more uuids
```
http_req_duration..............: avg=40.41ms  min=0s      med=23.98ms max=2.34s   p(90)=30.61ms p(95)=35.67ms
```
preloaded uuids into provider no update (planned for async update in future)
```
http_req_duration..............: avg=3.27ms   min=242µs med=2.97ms  max=10.72ms p(90)=6.51ms  p(95)=7.2ms
```