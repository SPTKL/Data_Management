# HOMEWORK 2
##### Description:
Your task is to compute the number of restaurants per each cuisine using 
the provided nyc_restaurant_inspections.csv data set. The CSV file is 
available for download under the Data Sets page on NYU Classes. The 
cuisine type can be extracted from the "CUISINE DESCRIPTION" column. 
Note that, a single restaurant may be inspected multiple times. You must 
use the "CAMIS" column to keep only unique restaurants while computing 
the number of restaurants per cuisine.

You MUST turn in a __Spark notebook__, AND a __Spark script__ that works 
on the NYU Dumbo cluster. For your script, the input and out file path 
should be specified through the command line. Basically, I should be 
able to run your script as:

spark-submit YOUR_SCRIPT.py nyc_restaurant_inspections.csv output_folder

and it will produce an output on HDFS under output_folder.

Using "hadoop fs -getmerge" or through the notebook, I should get the 
expected output similar to the below:


My Sites
Baiyue
Sites list begins here
Big Data Ma ...ection 001
 Tools  ASSIGNMENTS
Content begins here
 Opens in a new window
Assignment - In progress
Complete the form, then choose the appropriate button at the bottom.

Title
HW 2
Due
Jul 12, 2018 2:00 pm
Number of resubmissions allowed
Unlimited
Accept Resubmission Until
Jul 12, 2018 2:00 pm
Status
Not Started
Modified by instructor
Jul 5, 2018 1:47 pm
Instructions
Your task is to compute the number of restaurants per each cuisine 
using the provided nyc_restaurant_inspections.csv data set. The CSV 
file is available for download under the Data Sets page on NYU 
Classes. The cuisine type can be extracted from the "CUISINE 
DESCRIPTION" column. Note that, a single restaurant may be inspected 
multiple times. You must use the "CAMIS" column to keep only unique 
restaurants while computing the number of restaurants per cuisine.

You MUST turn in a Spark notebook, AND a Spark script that works on 
the NYU Dumbo cluster. For your script, the input and out file path 
should be specified through the command line. Basically, I should be 
able to run your script as:

spark-submit YOUR_SCRIPT.py nyc_restaurant_inspections.csv 
output_folder

and it will produce an output on HDFS under output_folder.

Using "hadoop fs -getmerge" or through the notebook, I should get the 
expected output similar to the below:
```
[('American', 6002),
 ('Chinese', 2399),
 ('Cafe', 1629),
 ('Other', 1296),
 ('Pizza', 1186),
 ('Italian', 1016),
 ('Mexican', 877),
 ('Japanese', 859),
 ('Latin (Cuban, Dominican, Puerto Rican, South & Central American)', 
840),
 ('Bakery', 733),
 ('Caribbean', 671),
 ('Spanish', 644),
 ('Donuts', 537),
 ('Pizza/Italian', 483),
 ('Chicken', 456),
 ('Sandwiches', 406),
 ('Juice, Smoothies, Fruit Salads', 382),
 ('Hamburgers', 378),
 ('Asian', 371),
 ('Ice Cream, Gelato, Yogurt, Ices', 339),
 ('Indian', 332),
 ('Jewish/Kosher', 327),
 ('French', 319),
 ('Delicatessen', 294),
 ('Thai', 286)]
```
