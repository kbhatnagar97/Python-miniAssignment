Python Track
Mini Assignment


Overview
You need to extract the data from a CSV file and write plane function to derive the inferences listed in the task list.

The link to the csv file is here with some sample data https://drive.google.com/open?id=1WEw65E9-5CBsTadbgAIQbL6UPOL2SH7p

Note: Use of numpy and pandas is not allowed for this assignment.

Fork and Clone the repo 
git@git.hashedin.com:hu17linkers/python-mini-assignment.git
Task List
Design a function to know how many times a product of the “Bachmann” brand was purchased. The function should return integer value.
Design a function to get the most costly product in the data provided. The function should return id as the integer value.
Design a function to get the most selling product in the data provided. The function should return a string which is the name of the product.
Design a function to list all the products whose rating was “3” more than once. The function should return a unique list of products.
Design a function to know how many times a “S” size was purchased by male and females. The function should return a dictionary of following format 
{
male:count, 
female:count
}
Design a function to list all the items where the review contains the following content “Nulla justo.” The function should return a unique list of products.
Design a function to identify the review titled as “Bad Quality” affected by which color most. Function to return the string with color name.

Note: Please return the data from the function as mentioned above.


For Evaluation:
Please add following function to main.py
def getResult():
    ##Replace testFunction with your function created for each task.
    return {
	"task1":testFunction(),
	"task2":testFunction(),
	"task3":testFunction(),
	"task4":testFunction(),
	"task5":testFunction(),
	"task6":testFunction(),
	"task7":testFunction()
	}


