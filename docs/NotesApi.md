# swagger_client.NotesApi

All URIs are relative to *https://app.doorloop.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_note**](NotesApi.md#delete_note) | **DELETE** /notes/{noteId} | Delete a Note
[**get_note**](NotesApi.md#get_note) | **GET** /notes/{noteId} | Retrieve a Note
[**get_notes**](NotesApi.md#get_notes) | **GET** /notes | List all Notes
[**post_notes**](NotesApi.md#post_notes) | **POST** /notes | Create a Note
[**put_note**](NotesApi.md#put_note) | **PUT** /notes/{noteId} | Update a Note

# **delete_note**
> Note delete_note()

Delete a Note

Deletes a Note

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Key
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.NotesApi(swagger_client.ApiClient(configuration))

try:
    # Delete a Note
    api_response = api_instance.delete_note()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->delete_note: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Note**](Note.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_note**
> get_note()

Retrieve a Note

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Key
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.NotesApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve a Note
    api_instance.get_note()
except ApiException as e:
    print("Exception when calling NotesApi->get_note: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notes**
> InlineResponse20018 get_notes(filter_created_at_from=filter_created_at_from, filter_created_at_to=filter_created_at_to, filter_resource_id=filter_resource_id, filter_created_by=filter_created_by, filter_tags=filter_tags, filter_text=filter_text)

List all Notes

Lists all Notes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Key
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.NotesApi(swagger_client.ApiClient(configuration))
filter_created_at_from = NULL # object | Format: YYYY-MM-DD (optional)
filter_created_at_to = NULL # object | Format: YYYY-MM-DD (optional)
filter_resource_id = NULL # object |  (optional)
filter_created_by = NULL # object |  (optional)
filter_tags = NULL # object |  (optional)
filter_text = NULL # object | Filter by Note Title or Body (optional)

try:
    # List all Notes
    api_response = api_instance.get_notes(filter_created_at_from=filter_created_at_from, filter_created_at_to=filter_created_at_to, filter_resource_id=filter_resource_id, filter_created_by=filter_created_by, filter_tags=filter_tags, filter_text=filter_text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->get_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_created_at_from** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 
 **filter_created_at_to** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 
 **filter_resource_id** | [**object**](.md)|  | [optional] 
 **filter_created_by** | [**object**](.md)|  | [optional] 
 **filter_tags** | [**object**](.md)|  | [optional] 
 **filter_text** | [**object**](.md)| Filter by Note Title or Body | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_notes**
> Note post_notes(body=body)

Create a Note

Creates a Note

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Key
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.NotesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Note() # Note |  (optional)

try:
    # Create a Note
    api_response = api_instance.post_notes(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->post_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Note**](Note.md)|  | [optional] 

### Return type

[**Note**](Note.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_note**
> Note put_note(body=body)

Update a Note

Updates a Note

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Key
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.NotesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Note() # Note |  (optional)

try:
    # Update a Note
    api_response = api_instance.put_note(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->put_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Note**](Note.md)|  | [optional] 

### Return type

[**Note**](Note.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

