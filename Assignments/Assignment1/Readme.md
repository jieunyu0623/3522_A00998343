# Assignment 1 

---------------------------------
A Budget Management Program written in Python.</br></br>
<b>Author: </b> Jieun Yu </br>
<b>Student Number:</b> A00998343</br>
<b>Set:</b> 3T
</br></br>

##Table of Contents

--------
* [Introduction] (#introduction)
  </br></br>
* [How To Use It?] (#How-to-use-it)
  </br></br>
* [Features] (#features)
  </br></br>

<a name="introduction"></a>
## Introduction

-------------------
This project is a budget management system mainly created for parents
with the child who needs to improve their budget management skills.</br></br>
By using this budget managing system, your child will learn how to efficiently spend and save money. 
When your child leaves home to go to university, they will not only have some savings on their bank account, but also
will have good budget managing skills.

<a name="How-to-use-it"></a>
## How To Use It?

---------------------
1. Nagivate to the ```driver.py```
   </br></br>
2. Run ```m.main_menu()``` to see the main menu, so you
can register a new user
   </br></br>
3. You will be prompted to enter user information  
   </br>
4. Please make sure you enter the correct type (numbers, letters) when you fill out the user information
   </br></br>
5. When you are asked for budget amount, please make sure your input is a positive value<br><br>
6. Please make sure to select the number options ONLY shown in the program <br><br> 
7. If you don't want to create a new user and use test users, run ```m.log_in()``` instead, so the program 
   starts from the user menu
   </br></br>

<a name="features"></a>
## Features

---------------------
* There are three different user types that control how much money the user can spend in each category:
   </br></br>
   * TroubleMaker
     * gets a warning if they exceed more than 75% of a budget category.
     * gets politely notified iIf they exceed a budget category.
     * gets locked out of conducting transactions in a budget category if they exceed it by
120% of the amount assigned to the budget in question.<br><br>
   * Rebel 
     * they get a warning for every transaction after exceeding 50% of a budget.
     * gets ruthlessly notified iIf they exceed a budget category.
     * gets locked out of conducting transactions in a budget category if they exceed it by
100% of the amount assigned to the budget in question.
     * If they exceed their budget in 2 or more categories then they get locked out of their
account completely<br><br>

   * Angel
      * Never gets locked out of a budget category. They can continue spending money even if
they exceed the budget in question.
      * Gets politely notified if they exceed a budget category.
      * Gets a warning if they exceed more than 90% of a budget.
    </br></br>
* There are four different types of budget categories:
   </br></br>
   * Games and Entertainment
   * Clothing and Accessories
   * Eating Out
   * Miscellaneous
    </br></br>
you can choose one budget category and record a transaction in that category.
