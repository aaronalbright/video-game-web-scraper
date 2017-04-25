# Video Game Web Scraper

(ReadMe last updated 3/20/2016)

* * *

Note: **vg_scraper.py** is the main python program. The rest are for the individual sites.

My program scrapes three websites:

* [VGChartz][1]
* [HowLongToBeat][2]
* [Metacritic][3]

The goal is to find the correlation between the top 100 highest-selling games, the top 100 highest-rated games and the top 100 longest-played games.

I was originally only going to do either VGChartz or Metacritic, but I ended up figuring out both after running into a wall with Metacritic and a 403 error (see below).

I can technically scrape more than 100, especially on VGChartz, but HowLongtoBeat limits most if it's "all time" stats to 100.

## Process 
My program sessionally scrapes the various "Top 100" sections are the respective websites. For VGCharts, it gets the top 100 best-selling games. On Metacritic, it fetches the top 100 highest-rated games on the websites (pulled from both critics and user entries). It then dumps the data into their their respective files.

HowLongToBeat is where things get tricky, but luckily the site is built to where I can get whatever I end up needing/choosing.

The site gets its data largely from user submission. Either a) a user enters their Steam profile (a PC gaming software) then the website then pulls the data from or b) a user can enter the information manually.

Because of this, the "hours played" on some games are more reliable than others. I figured fetching games that have the most user-entries would be a more reliable source of how long a game took play, as opposed to taking a game one user entered a 1,000 hours played on.

With a simple URL change, I can easily pull the top 100 longest games if needed.

## Issues

At first, Metacritic and HowLongToBeat kept giving me 403 and 406 errors. They were essentially rejecting my scraper because it could tell I wasn't a real browsing requesting the URL. Luckily, I figured out how to add a User Agent to the URL request, which basically tells the server that the program is using a browser.

I also had issues with global variables in Python. Turns out the solution was as simple as declaring the variable as "global" before defining it.

For some reason, Metacritic formats its game titles with hard returns before and after the string. From the looks of it, the text is actually a text node and BS is just fetching the string, not value. Unless I can find a way to just get the value from the node, I'm stuck with the returns. 

VGCharts, while it has a ton of useful, is poorly formatted. It's just one ugly table with zero classes or formatting. I couldn't figure out to only scrape the names and sales numbers because they are all wrapped in the same tags. I'd rather just not use it.


[1]:http://vgchartz.com
[2]:http://howlongtobeat.com
[3]:http://www.metacritic.com/game



