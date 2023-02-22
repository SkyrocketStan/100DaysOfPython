# Capstone Project Program Requirements

As we get closer to the latter part of the course, and as you build up your
skills every day, the challenges are going to become more life-like and more
challenging. As a developer, you will spend most of your time figuring out how
to do things using Google and StackOverflow. It's rare that I come across a new
project and already know exactly what code I need to write.

In this capstone project, you will need to apply everything you've learnt about
website and web scraping with Beautiful Soup and Selenium to complete the
project and fulfil the project requirements. You might also need to do your own
research and revision to complete the task.

But first, you need to create a new form in Google Forms.

1. Go to https://docs.google.com/forms/ and create your own form:
   ![](https://img-c.udemycdn.com/redactor/raw/2020-08-25_15-17-58-d30a61ad923994f10cb01b2d3c9c0d48.png)

2. Add 3 questions to the form, make all questions "short-answer":
   ![](https://img-c.udemycdn.com/redactor/raw/2020-08-25_15-20-27-e452a75ff00354982fbac16869f59e1d.png)

3. Click send and copy the link address of the form. You will need to use this
   in your program.
   ![](https://img-c.udemycdn.com/redactor/raw/2020-08-25_15-21-47-ce68f626cee655ddf83ec94b56eb912f.png)

4. Go to this web address on Zillow and see how the website is structured, this
   is where you'll be scraping the data from:
   ![](https://img-c.udemycdn.com/redactor/raw/2020-08-25_15-24-26-6abfaeb4f90b56e995d4f0df38b61d05.png)

Program Requirements:

- Use BeautifulSoup/Requests to scrape all the listings from the Zillow web
  address (Step 4 above).

- Create a list of links for all the listings you scraped. e.g.
  ![](https://img-c.udemycdn.com/redactor/raw/2020-08-25_15-44-03-cb3327d64e803a957cb15bc1f76a7bd4.png)

- Create a list of prices for all the listings you scraped. e.g.
  ![](https://img-c.udemycdn.com/redactor/raw/2020-08-25_15-46-01-e6685011b9c0862037454140314a17b9.png)

- Create a list of addresses for all the listings you scraped. e.g.
  ![](https://img-c.udemycdn.com/redactor/raw/2020-08-25_15-46-59-18b592d30cf361e9ad9348e830b7bce6.png)

- Use Selenium to fill in the form you created (step 1,2,3 above). Each
  listing should have its price/address/link added to the form. You will need to
  fill in a new form for each new listing. e.g.
  ![](https://img-c.udemycdn.com/redactor/raw/2020-08-25_15-50-47-7e40268135497ea3e84762091f48779d.gif)

- Once all the data has been filled in, click on the "Sheet" icon to create a
  Google Sheet from the responses to the Google Form. You should end up with a
  spreadsheet with all the details from the properties.
  ![](https://img-c.udemycdn.com/redactor/raw/2020-08-25_15-53-14-f90af01c1dc026dd5a9fa9cba2e6dd44.png)
  ![](https://img-c.udemycdn.com/redactor/raw/2020-08-25_15-53-33-5cc79771a88de0ff918068a99ecbc371.png)
