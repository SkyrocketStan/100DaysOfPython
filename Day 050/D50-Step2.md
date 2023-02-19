Step 2 - Navigate to Login Page
In order to avoid dual verification with a phone every time we log in, we'll need to use the Facebook/Google login. The Google login flow requires a lot more steps than Facebook login, so we'll go with Facebook in this challenge.

1. Using Selenium and Python Navigate to the Tinder website (https://tinder.com/) and click on LOG IN then LOGIN WITH FACEBOOK. See below:
![](https://img-b.udemycdn.com/redactor/raw/2020-08-21_15-09-13-c82d3512f06309199abbd002ce971f31.png)
If successful, you should see a pop-up for Facebook login:
![](https://img-b.udemycdn.com/redactor/raw/2020-08-21_15-14-05-a9c66cf9149f34720e387144bd02c6fc.png)
HINT 1: Make sure you've already manually signed-in and verified your phone number with Tinder as we can't automate the phone number verification. You only have to do this once.
<br><br>HINT 2: If you are getting a NoSuchElementException, make sure you've added some delay between clicking on buttons so that the new element has enough time to load.
<br><br>HINT 3: You might find it easier to right click on the element and get the XPath to use with Selenium. e.g.
![](https://img-b.udemycdn.com/redactor/raw/2020-08-21_15-17-01-2cdd16603c955114c440cb5ff8e94e95.png)