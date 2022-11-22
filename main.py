import dtlpy as dl
import random
import datetime

# login to DL platform
if dl.token_expired():
    dl.login()

# create a new project
project = dl.projects.create(project_name='azmi-dataloop-assignment-submission')

# create a dataset for the project and add 3 labels to it
dataset = project.datasets.create(dataset_name='dataset-azmi')
dataset.add_label(label_name='class')
dataset.add_label(label_name='class2')
dataset.add_label(label_name='key')

# upload 5 photos to the dataset
dataset.items.upload(local_path="/Users/azmi_abu/Desktop/photos")

# create metadata dictionary for user and add UTM for each picture
items = dataset.items.get_all_items()
for item in items:
    # deleting all previous annotations
    item.annotations.delete(filters=dl.Filters(resource=dl.FILTERS_RESOURCE_ANNOTATION))
    item.metadata['user'] = dict()
    item.metadata['user']['collectionTime'] = str(datetime.datetime.now())
    item.update()

# loop over each picture and label them accordingly, for the final picture add point annotations as well
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
            print(rand_y, rand_x)
    item.annotations.upload(builder)

# add query filter to retrieve all pictures labeled as 'class' and print their ID and name
filters = dl.Filters()
filters.add_join(field='label', values='class')
items = dataset.items.get_all_items(filters=filters)

for item in items:
    print('Item ID is: ', item.id)
    print('Item Name is: ', item.name)

# retrieve annotations list from the dataset
filters = dl.Filters()
filters.resource = dl.FILTERS_RESOURCE_ANNOTATION
filters.add(field='type', values='point')
pages = dataset.annotations.list(filters=filters)

# loop over the annotations and print the requested data
for page in pages:
    for annotation in page:
        print('Item ID is: ', annotation.item.id)
        print('Item Name is: ', annotation.item.name)
        print('Annotation ID is: ', annotation.id)
        print('Annotation Label is: ', annotation.label)
        print('Annotation Position is: (', annotation.x, ',', annotation.y, ')')
        print('----------------------------------------------------')
