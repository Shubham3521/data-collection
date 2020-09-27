# data-collection

This is flask application which can be easily hosted on heroku and contains python-3.7.9

This application consists of following components

1. Input form for data collection
2. Email Sending on AWS SES
3. Can be easily hosted on heroku

Steps to run this project on heroku

1. heroku login
2. heroku create datacollectr12. (my app name on heroku)
3. heroku addons:create heroku-postgresql:hobby-dev --app datacollectr1 (adding postgressql)
4. heroku conffig --app datacollectr1
5. heroku git:remote --app datacollectr1
6. git push heroku master
