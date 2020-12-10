# discord_ads_web_app
Web app associated with discord ads bot.

This is going to be a web app with flask as the back end, postgres as the database, front end is TBD. To set up:

`git clone <git clone url>`

`cd discord_ads_web_app`

I use pipenv. Run:

`pipenv install`

to install all python packages, and then run 

`pipenv shell`. 

This will create a virtual environment and put you in it (if you don't know what this means, I would recommend 
looking it up.)

Separately, you'll need to install Postgresql. 

Make sure to change the related env variables in .env to match your environment!

Heads up that this project uses Flask blueprints, which basically is a module in the app. I've created a blueprint for advertisers (you can see the advertisers folder under /app) and one for discord_users. Each of these blueprints can contain their own templates, static assets, and routes, allowing for better separation of code. There is also a top level templates, static, and routes.py for shared stuff.