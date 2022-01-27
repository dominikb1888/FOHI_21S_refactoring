# The cleaning story continued - Built-Ins are coming!

In the first post, we looked at cleaning our code on the block level. We identified two import blocks we moved to a separate function, several similar blocks of mappings we replaced with a for loop.

In this post, we will look at the next level of granularity. We will check the code for further repetitions and see where code style can be improved to become less imperative.

This will require some more thinking toward what the code does or tries to achieve. Therefore we look at the data structures and their transformations first. The best way to do this quickly and to also see iteratively how things change is in a Jupyter Notebook.

We look at three Transformations:
1. CSV -> csv_data
2. csv_data to mapped
3. mapped to output


## CSV Import

The CSV Import has been moved to a separate function. Here is our snippet again:

´´´{python}

class FundingRaised:
    def _import_csv(filepath="../startup_funding.csv"):
        with open(filepath, "rt") as csvfile:
            data = csv.reader(csvfile, delimiter=",", quotechar='"')
            # skip header
            next(data)
            csv_data = []
            for row in data:
                csv_data.append(row)

    return csv_data
´´´

A CSV file is a set of lines with comma-separated content. Usually there is a header line in line 1 and content in all following lines. With linear reading, we will thus receive lines represented as list of elements. We are checking just the commands inside our functions:

´´´{Python}
import csv

with open("../startup_funding.csv", "rt") as csvfile:
    data = csv.reader(csvfile, delimiter=",", quotechar='"')
    # skip header
    next(data)
    csv_data = []
    for row in data:
        csv_data.append(row)

csv_data

´´´

The only change to the previous code snippet is that we remove the function name and return value. Instead we reference the csv file directly and call the variable csv_data directly to see the output. Don't forget to import the csv module in the code cell you are using.

If we analyze the output we can see that we receive a list of list with no headers. This is the first hint to problems in the code. Why would I remove the headers from a table on import just to remap them later. Very weird. Let's try to verify this assumption by checking the next steps!


## csv_data -> mapped

How does the transformation of our list continue? Let's look the where function first.

The first step in this transformation is a filter operation, and a weird one two. We need to remap the position of our original header (we placed this information in a dict to clean up before) to the position in our list. I added comments to each line of code in plain English.  


´´´´{Python}
# We need to keep an order of the columns to make sure we can remap that to the content our csv_data list of lists. 
columns_dict = {1: "company_name", 4: "city", 5: "state", 9: "round"}
# To filter we need to first check for all options in above dict. Apparently our users aren't allowed to search for something else. This is business logic. We will discuss this later!
for key, column in columns_dict.items():
    # We will only take columns from the options dict our user passes that match our columns_dict above. 
    if column in options:
        # Create a temp list to hold our filtered results
        result = []
        for row in csv_data:
            # Let's iterate through our csv_data and see if the search term from our users options occurs in the right column within our csv_data
            if row[key] == options[column]:
                # if yes, we append this to our result list, i.e. a valid search result!
                result.append(row)
                
        # We overwrite our csv_data Variable, with our search result, mmmmmm                
        csv_data = result

´´´

Ui, ui. So basically our brief search implementation needs to keep a strict register of our column order to work. Otherwise we would not be able to match our users search request to the right column in our list of lists (aka a very bad version of a database).

I wonder what happens, if we remove the check for only these 4 columns and allow for all. If our test cases, which are describing the business logic do not test for any edge case here, we could just throw this line out. So, let's do this!



