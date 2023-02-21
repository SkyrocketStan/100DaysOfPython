# Step 5 - Follow all the followers

1. Inside the follow() method find all the follow buttons in the modal (popup)
   and click on each of them in turn. Add a 1 second delay between each click,
   so you can seem more human. e.g.
   ![](https://img-c.udemycdn.com/redactor/raw/2020-08-25_09-59-32-fd7f7957ed362ae11091cdd39e0e878d.gif)

2. Sometimes, you'll encounter an account that you have already followed, in
   this case, when you press on the button it will generate a popup asking if
   you want to unfollow that person e.g.
   ![](https://img-c.udemycdn.com/redactor/raw/2020-08-25_10-02-02-72bd0a36e702accb73e96e58de2b0d2c.png)

3. When this happens the follow button is hidden under the popup and you
   will get a ElementClickInterceptedException if you try to continue
   clicking on the follow button. Handle this exception and when it occurs,
   simply click on the "Cancel" button to dismiss the popup and continue to
   follow other people.
   e.g.   ![](https://img-c.udemycdn.com/redactor/raw/2020-08-25_10-07-44-2cef356f98ad3b5c6c8efde3ee0e38b6.gif)

