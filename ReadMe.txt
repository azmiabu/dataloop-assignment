In this assignment we added pictures to the DL platform, we added some labels and associated them to the corresponding pictures. We also added some
queries to retrieve pictures and annotations that have satisfy the queries.

In part I we did so using the UI:
* at first we add all the pictures to the platform
* to add a labels to the dataset we need to first create a recipe and add all the labels to it.
* to associate a label to a picture you need to choose the desired picture by double clicking on it, then choose at least one of the annotation tools
  on the bottom left side of the screen and then choose the desired label
* if you wish to add an attribute, go to the recipe screen and create a section, add the desired labels to the section and add as many attributes as 
  you like, those attributes will be available for the added labels/scopes

In part II we did the same thing using python code, it is very helpful to use the DL cheat sheet: https://dataloop.ai/docs/sdk-cheatsheet?highlight=cheat 
in addition to what we did in part I, in this part we added queries to retrieve the data only relevant to the desired query, for instance:
we wanted to retrieve all the pictures that were labeled as "class", to do so we need to follow the steps:
* create a filter: filters = dl.Filters()
* add a query and specify the desire value: filters.add_join(field='label', values='class')
* finally, retrieve all the items that satisfy the query: items = dataset.items.get_all_items(filters=filters)

Link to UI part of assignment: https://console.dataloop.ai/projects/dc303e69-e4be-45f9-bcf0-6d0010cdcb2e
Link to python part of assignment: https://console.dataloop.ai/projects/a76c13e9-a401-4f72-b0e9-bc606d627c7e
