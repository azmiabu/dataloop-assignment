import dtlpy as dl
import random
import time

#login to DL platform
if dl.token_expired():
    dl.login()

#create a new project
project = dl.projects.create(project_name='azmi-dataloop-assignment-submission')

#create a dataset for the project and add 3 labels to it
dataset = project.datasets.create(dataset_name='dataset-azmi')
dataset.add_label(label_name='class')
dataset.add_label(label_name='class2')
dataset.add_label(label_name='key')

#upload 5 photos to the dataset and add the "sleep" function to wait for the pictures to be uploaded
dataset.items.upload(local_path="/Users/azmi_abu/Desktop/photos")
time.sleep(5)

#create metadata dictionary for user and add UTM for each picture
items = dataset.items.get_all_items()
for item in items:
    item.metadata['user'] = dict()
    item.metadata['user']['collectionTime'] = item.created_at
    item.update()

#loop over each picture and label them accordingly, for the final picture add point annotations as well
for i, item in enumerate(items):
    builder = item.annotations.builder()
    if i < 2:
        builder.add(annotation_definition=dl.Classification(label='class'))
    else:
        builder.add(annotation_definition=dl.Classification(label='class2'))
    if i == 4:
        for z in range(5):
            rand_x = random.randint(0, item.width)
            rand_y = random.randint(0, item.height)
            builder.add(annotation_definition=dl.Point(x=rand_x, y=rand_y, label='key'))
    item.annotations.upload(builder)

#add query filter to retrieve all pictures labeled as 'class' and print their ID and name
filters = dl.Filters()
filters.add_join(field='label', values='class')
items = dataset.items.get_all_items(filters=filters)

for item in items:
    print('Item ID is: ', item.id)
    print('Item Name is: ', item.name)

#retrieve all items that contain point annotations from the dataset
filters = dl.Filters()
filters.add_join(field='type', values='point')
items = dataset.items.get_all_items(filters=filters)

#annotation filtering to retrieve all point annotations for each of the items containing point annotations
filters = dl.Filters(resource=dl.FILTERS_RESOURCE_ANNOTATION)
filters.add(field='type', values='point')

for item in items:
    print('Item ID is: ', item.id)
    print('Item Name is: ', item.name)
    annotations = item.annotations.list(filters=filters)
    for annotation in annotations:
        print(annotation)

#this method doesn't work for some reason although it was mentioned in the cheat sheet:
# filters = dl.Filters()
# filters.resource = 'annotation'
# filters.add(field='type', values='point')
#
# for item in items:
#     print('Item ID is: ', item.id)
#     print('Item Name is: ', item.name)
#     annotations = item.annotations.list(filters=filters)
#     for annotation in annotations:
#         print(annotation)


