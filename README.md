# Turing Python Library

Turing visual search and visually similar recommendations API library for python. The REST API documentation can be found here: [https://api.turingiq.com/doc/](https://api.turingiq.com/doc/)

Setup
-----
This package is available through pip and can be install using following command.
```console
pip3 install turing-api
```

Initialize
----------
import the `visualAPI` class as bellow.

```python
from turing_api.lib.visualAPI import VisualAPI
```

You can initialize the `VisualAPI` class with below parameters.

```python
api_key = 'your_api_key' # You can get API key when you login at: https://www.turingiq.com/login
mode = 'live'            # the mode can be either `live` or `sandbox`. Default mode is `live`.
visual_api = VisualAPI(api_key, mode)
```

Autocrop
--------

Detect objects in image and get bounding boxes around objects detected.

```python
# image_url is required field.
image_url = "https://example.com/image_url.jpg"

# now let's call the API.
response = visual_api.autocrop(image_url)
```

The bounding boxes returned by this method can be given to visual search to improve visual search quality.


Insert
------

You need to insert images to our index to query on them. The insert function can be written as below.

```python
# id is required field.
id = 'some_product_id'

# image_url is required field.
image_url = "https://example.com/image_url.jpg"

# filters argument is optional. You can specify upto 3 filters as per example given below.
# Filters can be useful when querying images from our index. You can apply any filter
# as per your requirement.
filters = {"filter1" : "onefilter", "filter2" : "twofilter", "filter3" : "threefilter"}

# metadata is optional. You can pass additional information about your image which will be
# returned when you query image from our index.
metadata = {"title" : "Image Title"}

# now let's call the API.
response = visual_api.insert(id, image_url, filters, metadata)
```

Update
------

If you need to update information to indexed image, you can use update function. If you call update function for id which is not already indexed, it will insert the image to index.

```python
# id is required field. Provide id for which you need to update the information.
id = 'some_product_id'

# image_url is optional field. You can pass `null` if you would like to keep URL unchanged.
image_url = "https://example.com/image_url.jpg"

# filters argument is optional. You can specify upto 3 filters as per example given below.
# Filters can be useful when querying images from our index. You can apply any filter
# as per your requirement. The filters you provide here will be overwritten.
filters = {"filter1" : "onefilter", "filter2" : "twofilter", "filter3" : "threefilter"}

# metadata is optional. You can pass additional information about your image which will be
# returned when you query image from our index. Existing metadata values will be overwritten
# based on keys supplied to this array.
metadata = {"title" : "Image Title"}

# now let's call the API.
response = visual_api.update(id, image_url, filters, metadata)
```

Delete
------

You can delete image from index with this method.

```python
# id is required field.
id = 'some_product_id'

# now let's call the API.
response = visual_api.delete(id)
```

Visual Search
-------------

Visual search can be used to search indexed images based on query image.

```python
# image_url is required field. The API will perform visual search on the image and return
image_url = "https://example.com/image_url.jpg"

# crop_box is optional field. You can supply empty array if you don't want to specify crop box.
# The format of crop box is [xmin, ymin, xmax, ymax]
crop_box = [188, 256, 656, 928]

# filters argument is optional. You can specify upto 3 filters.
# For example, if you specify filter1 = "nike", it will only return images which are indexed with
# "nike" as filter1.
filters = {"filter1" : "nike"}

# now let's call the API.
response = visual_api.search(image_url, crop_box, filters)
```

Visual Recommendations
----------------------

Visual recommendations give visually similar image recommendations which can be used to display recommendation widget on e-commerce sites which greatly improved CTR and conversion rates.

```python
# image_url is required field. The API will perform visual search on the image and return
id = "some_product_id"

# filters argument is optional. You can specify upto 3 filters.
# For example, if you specify filter1 = "nike", it will only return images which are indexed with
# "nike" as filter1.
filters = {"filter1" : "nike"}

# now let's call the API.
response = visual_api.recommendations(id, filters)
```


### Run Tests

```sh
API_KEY=api_key python3 test/visualAPITest.py
```

### Publish Package

```sh
python3 setup.py sdist bdist_wheel

twine upload
```
