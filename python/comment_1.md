# Stage 1 - Understand the objectives and making it DRY

After cleaning the direct and obvious formal flaws from the code (Indenting according to PEP8 with 4 Spaces and an unused variable: https://www.python.org/dev/peps/pep-0008/), it is about understanding the business objectives of the code and understanding what is a repetition and what is potentially business logic, i.e. unclean, but still intended.


## Business Logic



## DRYing up on block level 
The code is Class with @staticmethod decorators, this means that we do not need to create an object to access the class methods. 

The first things that spring even to a relatively untrained eye are repeated code blocks:

### Doubled CSV Import

The Import of the CSV is doubled in both the where and find_by functions. This may make sense in combination with the staticmethod class, but overall is weird. We neither bind data to functionality nor functionality to data. Rather we are hiding plain functions in a class, with relatively little reason as they don't share any underlying data structure. The data is imported twice and could come from two completely different sources. Actually this is a misleading use of a class, we could argue.

### Multiple mappings to dictionaries

In both functions we find many mappings of code blocks that can cleaned by extracting them into a separate function and the string literals into lists. Here the first real question arises. What is this code actually trying to achieve? 

We are seeing three steps:
1. Data import
2. Data checking (all columns present?)
3. Data filtering (Prepare Result by add matches to new dictionary)


Here's the intermediate codebase"
{{gist 5abfff10e1776d7bf2efe1c4ba1fca15}}

## Analysis

We went through this code very roughly, without even trying to get any closer to what it intends to do. So these were mainly semantic and structural edits. However, we may even go further. Many areas in the code are still doubled across the two functions or they are very imperative and could be replace by built-ins (Python Built-Ins: https://docs.python.org/3/library/functions.html).

We will go about these things in our next post!
