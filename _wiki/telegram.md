---
layout: wiki
title: telegram
create: 2015-05-27
update: 2015-05-27
---

## telegram bot

Name    Description Usage
9gag.lua    9GAG for telegram   !9gag: Send random image from 9gag
boobs.lua   Gets a random boobs or butts pic    !boobs: Get a boobs NSFW image. :underage:
!butts: Get a butts NSFW image. :underage:
btc.lua Bitcoin global average market value (in EUR or USD) !btc [EUR|USD] [amount]
bugzilla.lua    Lookup bugzilla status update   /bot bugzilla [bug number]
calculator.lua  Calculate math expressions with mathjs API  !calc [expression]: evaluates the expression and sends the result.
channels.lua    Plugin to manage channels. Enable or disable channel.   !channel enable: enable current channel
!channel disable: disable current channel
danbooru.lua    Gets a random fresh or popular image from Danbooru  !danbooru - gets a random fresh image from Danbooru :underage:
!danboorud - random daily popular image :underage:
!danbooruw - random weekly popular image :underage:
!danboorum - random monthly popular image :underage:
dogify.lua  Create a doge image with words. !dogify (words/or phrases/separated/by/slashes) - Create a doge image with the words.
download_media.lua  When bot receives a media msg, download the media.  
echo.lua    Simplest plugin ever!   !echo [whatever]: echoes the msg
eur.lua Real-time EURUSD market price   !eur [USD]
expand.lua  Expand a shorten URL to the original.   !expand [url]
fortunes_uc3m.lua   Fortunes from Universidad Carlos III    !uc3m
get.lua Retrieves variables saved with !set !get (value_name): Returns the value_name value.
giphy.lua   GIFs from telegram with Giphy API   !gif (term): Search and sends GIF from Giphy. If no param, sends a trending GIF.
!giphy (term): Search and sends GIF from Giphy. If no param, sends a trending GIF.
google.lua  Searches Google and send results    !google [terms]: Searches Google and send results
gps.lua generates a map showing the given GPS coordinates   !gps latitude,longitude: generates a map showing the given GPS coordinates
hackernews.lua  Show top 5 hacker news (ycombinator.com)    !hackernews
hello.lua   Says hello to someone   say hello to [name]
help.lua    Help plugin. Get info from other plugins.   !help: Show list of plugins.
!help all: Show all commands for every plugin.
!help [plugin name]: Commands for that plugin.
id.lua  Know your id or the id of a chat members.   !id: Return your ID and the chat id if you are in one.
!id(s) chat: Return the IDs of the chat members.
images.lua  When user sends image URL (ends with png, jpg, jpeg) download and send it to origin.    
imdb.lua    IMDB plugin for Telegram    !imdb [movie]
img_google.lua  Search image with Google API and sends it.  !img [term]: Random search an image with Google API.
invite.lua  Invite other user to the chat group !invite name [user_name]
!invite id [user_id]
isup.lua    Check if a website or server is up. !isup [host]: Performs a HTTP request or Socket (ip:port) connection
!isup cron [host]: Every 5mins check if host is up. (Requires privileged user)
!isup cron delete [host]: Disable checking that host.
location.lua    Gets information about a location, maplink and overview !loc (location): Gets information about a location, maplink and overview
magic8ball.lua  Magic 8Ball !magic8ball
media.lua   When user sends media URL (ends with gif, mp4, pdf, etc.) download and send it to origin.   
minecraft.lua   Searches Minecraft server and sends info    !mine [ip]: Searches Minecraft server on specified IP and sends info. Default port: 25565
!mine [ip] [port]: Searches Minecraft server on specified IP and port and sends info.
pili.lua    Shorten an URL with pili.la service !pili [url]: Short the url
plugins.lua Plugin to manage other plugins. Enable, disable or reload.  !plugins: list all plugins.
!plugins enable [plugin]: enable plugin.
!plugins disable [plugin]: disable plugin.
!plugins disable [plugin] chat: disable plugin only this chat.
!plugins reload: reloads all plugins.
quotes.lua  Quote plugin, you can create and retrieves random quotes    !addquote [msg]
!quote
rae.lua Spanish dictionary  !rae [word]: Search that word in Spanish dictionary.
roll.lua    Roll some dice! !roll d | d
search_youtube.lua  Search video on YouTube and send it.    !youtube [term]: Search for a YouTube video and send it.
set.lua Plugin for saving values. get.lua plugin is necessary to retrieve them. !set [value_name] [data]: Saves the data with the value_name name.
stats.lua   Plugin to update user stats.    !stats: Returns a list of Username [telegram_id]: msg_num
steam.lua   Grabs Steam info for Steam links.   
time.lua    Displays the local time in an area  !time [area]: Displays the local time in that area
translate.lua   Translate some text !translate text. Translate the text to English.
!translate target_lang text.
!translate source,target text
tweet.lua   Random tweet from user  !tweet id [id]: Get a random tweet from the user with that ID
!tweet id [id] last: Get a random tweet from the user with that ID
!tweet name [name]: Get a random tweet from the user with that name
!tweet name [name] last: Get a random tweet from the user with that name
twitter.lua When user sends twitter URL, send text and images to origin. Requires OAuth Key.    
twitter_send.lua    Sends a tweet   !tw [text]: Sends the Tweet with the configured account.
version.lua Shows bot version   !version: Shows bot version
vote.lua    Plugin for voting in groups.    !voting reset: Reset all the votes.
!vote [number]: Cast the vote.
!voting stats: Shows the statistics of voting.
weather.lua weather in that city (Madrid is default)    !weather (city)
webshot.lua Take an screenshot of a web.    !webshot [url]
wiki.lua    Searches Wikipedia and send results !wiki [terms]: Searches wiki and send results
!wiki_set [wiki]: sets the wikimedia site for this chat
!wiki_get: gets the current wikimedia site
xkcd.lua    Send comic images from xkcd !xkcd (id): Send an xkcd image and title. If not id, send a random one
youtube.lua Sends YouTube info and image.   