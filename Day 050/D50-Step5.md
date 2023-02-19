# Step 5 - Hit Like!
1. The final step is to like some people. Because it's the web version, we don't have to swipe right, all we need to do is to click on the "Like" button. You'll want to add **at least a 1 second delay** between "Likes" so that Tinder doesn't block you because you seem like a bot.
![](https://img-b.udemycdn.com/redactor/raw/2020-08-21_15-49-34-7a1f2a27c14e05ceaa2f7833f79b7870.png)

HINT 1: It takes a while for Tinder to load up people near you, this is not a fixed time as it depends on a number of factors. When it's loading, the "Like" button will not be reachable and you will get a

    NoSuchElementException 
if you try to find it. Use exception handling to handle this situation and wait 2 seconds before you retry.

HINT 2: Sometimes, as you are swiping, you'll get a match which is a pop-up on the same page. But this will mean that your Like button will be hidden behind the pop up and you'll get a 
    
    ElementClickInterceptedException. 
e.g.
![](https://img-b.udemycdn.com/redactor/raw/2020-08-24_08-22-53-eef36c0698acfe67157d5ffcee6c9749.png)

You'll need to dismiss this by clicking on "BACK TO TINDER" to continue swiping.

NOTE: On the free tier, Tinder only allows 100 "Likes" per day.

