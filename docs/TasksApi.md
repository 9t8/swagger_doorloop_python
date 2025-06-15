# swagger_client.TasksApi

All URIs are relative to *https://app.doorloop.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_task**](TasksApi.md#delete_task) | **DELETE** /tasks/{taskId} | Deletes a Task
[**get_task**](TasksApi.md#get_task) | **GET** /tasks/{taskId} | Retrieve a Task
[**get_tasks**](TasksApi.md#get_tasks) | **GET** /tasks | Retrieve all Tasks
[**post_task**](TasksApi.md#post_task) | **POST** /tasks | Create a Task
[**post_task_update**](TasksApi.md#post_task_update) | **POST** /tasks/update | Post an Update on a Task
[**put_task**](TasksApi.md#put_task) | **PUT** /tasks/{taskId} | Update a Task

# **delete_task**
> Task delete_task()

Deletes a Task

Deletes a Task

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
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))

try:
    # Deletes a Task
    api_response = api_instance.delete_task()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->delete_task: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Task**](Task.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task**
> Task get_task()

Retrieve a Task

Retrieves a Task

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
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve a Task
    api_response = api_instance.get_task()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_task: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Task**](Task.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks**
> InlineResponse20011 get_tasks(filter_property_group=filter_property_group, filter_property=filter_property, filter_unit=filter_unit, filter_type=filter_type, filter_status=filter_status, filter_created_at_from=filter_created_at_from, filter_created_at_to=filter_created_at_to, filter_due_date_from=filter_due_date_from, filter_due_date_to=filter_due_date_to, filter_completed_at_from=filter_completed_at_from, filter_completed_at_to=filter_completed_at_to, filter_assigned_to_user=filter_assigned_to_user, filter_text=filter_text, filter_requested_by_id=filter_requested_by_id)

Retrieve all Tasks

Retrieves all Tasks

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
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
filter_property_group = NULL # object | Filter by Portfolio Id (optional)
filter_property = NULL # object | Filter by Property Id (optional)
filter_unit = NULL # object | Filter by Unit Id (optional)
filter_type = NULL # object | Filter by Task Type (optional)
filter_status = NULL # object | Filter by Task Status (optional)
filter_created_at_from = NULL # object | Format: YYYY-MM-DD (optional)
filter_created_at_to = NULL # object | Format: YYYY-MM-DD (optional)
filter_due_date_from = NULL # object | Format: YYYY-MM-DD (optional)
filter_due_date_to = NULL # object | Format: YYYY-MM-DD (optional)
filter_completed_at_from = NULL # object | Format: YYYY-MM-DD (optional)
filter_completed_at_to = NULL # object | Format: YYYY-MM-DD (optional)
filter_assigned_to_user = NULL # object | Filter by User Id or \"unassigned\" (optional)
filter_text = NULL # object | Filter by Subject, Description or Reference (optional)
filter_requested_by_id = NULL # object | Filter by Requested by User, Tenant or Owner Id (optional)

try:
    # Retrieve all Tasks
    api_response = api_instance.get_tasks(filter_property_group=filter_property_group, filter_property=filter_property, filter_unit=filter_unit, filter_type=filter_type, filter_status=filter_status, filter_created_at_from=filter_created_at_from, filter_created_at_to=filter_created_at_to, filter_due_date_from=filter_due_date_from, filter_due_date_to=filter_due_date_to, filter_completed_at_from=filter_completed_at_from, filter_completed_at_to=filter_completed_at_to, filter_assigned_to_user=filter_assigned_to_user, filter_text=filter_text, filter_requested_by_id=filter_requested_by_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_property_group** | [**object**](.md)| Filter by Portfolio Id | [optional] 
 **filter_property** | [**object**](.md)| Filter by Property Id | [optional] 
 **filter_unit** | [**object**](.md)| Filter by Unit Id | [optional] 
 **filter_type** | [**object**](.md)| Filter by Task Type | [optional] 
 **filter_status** | [**object**](.md)| Filter by Task Status | [optional] 
 **filter_created_at_from** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 
 **filter_created_at_to** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 
 **filter_due_date_from** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 
 **filter_due_date_to** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 
 **filter_completed_at_from** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 
 **filter_completed_at_to** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 
 **filter_assigned_to_user** | [**object**](.md)| Filter by User Id or \&quot;unassigned\&quot; | [optional] 
 **filter_text** | [**object**](.md)| Filter by Subject, Description or Reference | [optional] 
 **filter_requested_by_id** | [**object**](.md)| Filter by Requested by User, Tenant or Owner Id | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_task**
> Task post_task(body=body)

Create a Task

Creates a Task

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
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Create a Task
    api_response = api_instance.post_task(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->post_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**Task**](Task.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_task_update**
> Task post_task_update(body=body)

Post an Update on a Task

Posts an update on a task

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
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
body = swagger_client.TasksUpdateBody() # TasksUpdateBody |  (optional)

try:
    # Post an Update on a Task
    api_response = api_instance.post_task_update(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->post_task_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TasksUpdateBody**](TasksUpdateBody.md)|  | [optional] 

### Return type

[**Task**](Task.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_task**
> Task put_task(body=body)

Update a Task

Updates a Task

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
api_instance = swagger_client.TasksApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Update a Task
    api_response = api_instance.put_task(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->put_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**Task**](Task.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

