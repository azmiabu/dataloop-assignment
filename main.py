import dtlpy as dl
import random
import time
if dl.token_expired():
    dl.login()

project = dl.projects.create(project_name='azmi-dataloop-assignment-submission')

dataset = project.datasets.create(dataset_name='dataset-azmi')
dataset.add_label(label_name='class')
dataset.add_label(label_name='class2')
dataset.add_label(label_name='key')

dataset.items.upload(local_path="/Users/azmi_abu/Desktop/photos")
time.sleep(5)

items = dataset.items.get_all_items()
for item in items:
    item.metadata['user'] = dict()
    item.metadata['user']['collectionTime'] = item.created_at
    item.update()

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

filters = dl.Filters()
filters.add_join(field='label', values='class')
items = dataset.items.get_all_items(filters=filters)

for item in items:
    print('Item ID is: ', item.id)
    print('Item Name is: ', item.name)

filters = dl.Filters()
filters.add_join(field='type', values='point')
items = dataset.items.get_all_items(filters=filters)

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

filters = dl.Filters(resource=dl.FILTERS_RESOURCE_ANNOTATION)
filters.add(field='type', values='point')

for item in items:
    print('Item ID is: ', item.id)
    print('Item Name is: ', item.name)
    annotations = item.annotations.list(filters=filters)
    for annotation in annotations:
        print(annotation)




