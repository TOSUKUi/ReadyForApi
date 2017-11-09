# ReadyFor-API
[![Build Status](https://travis-ci.org/TOSUKUi/readyfor-api.svg?branch=master)](https://travis-ci.org/TOSUKUi/readyfor-api)
An object-oriented python 3.5+ library for scraping the ReadyFor Web site.

## Whats this?
https://readyfor.jp

The package to scrape ReadyFor web site easily like a accessing official api.
ITs easy to use. I recommend to my use this library for scraping readyfor.

## Installation
pip install readyfor-api

※available at python 3.5+

## How to Use
```python
>>> import readyforapi
>>> readyforapi.core.set_tokens(_facebook_token="<your facebook app token>")
>>> project = readyforapi.project.Project(project_id=10946)
Or:
>>> project = readyforapi.project.Project(project_key="beehive")
# easy to get project data
>>> project.name
beehive
>>> project.author
<User "三宅 伸一"　(144824)>
>>> project
<Project "beehive" (10946)>
>>> project.buckers
[<User "たむら ゆうや" (283668)>, ...., <User "川畑真央" (277481)>]
# this data was gotten at 2017-05-11 09:36:20 JST
```



## LICENSE
[MIT](LICENSE)