

# all_the_recipes
Project goal: 
Examine recipe data from a food website. Use machine learning to predict which recipes will perform the best among users. Create a visualization to communicate findings.

Preliminary project plan with updates:
1. Choose a website.   
I decided to use allrecipes.com because of clear HTML formatting making it easy to scrape the desired data. I also like the community aspect of it, use of ratings/reviews, etc.   
2. Scrape the data
I wrote scrape_script.py and used XPath to identify the desired components to pull out of each page. I used the get_pages.py script and some manual messing around to figure out which indexes represented valid pages. Then I deployed muliple instances of the scraping script to download the data for each of roughly 250,000 pages.
3. Clean the data and put into appropriate database  
Most of the problems I found during data cleaning were caused by undesired newline characters in the description field. First I combined all the data using a combination of spreadsheet software and the combine_data.py script. Then I used clean_up_format.py and more_cleaning.py to deal with some lingering problems.  
The next thing I examined was the duplicate entries. I found that there were 133,574 duplicates out of 217,878 total recipes. Of these, The "Johnsonville Three Cheese Italian Style Chicken Sausage Skillet Pizza" represented 133,292 of the repeat entries. The rest were repeated only once or twice.  
  

4. Exploratory data analysis (python: numpy/pandas/matplotlib)
5. Machine learning (python: scikit learn)
6. Create a visualization (HTML, javascript)
