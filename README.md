See Makefile for different operations.

todo:
* design pattern for request routes
* add formal logging
* dependency injection
* flake8
* mypy
* autopep8?


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