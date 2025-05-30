# swagger_client.FilesApi

All URIs are relative to *https://app.doorloop.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_file**](FilesApi.md#delete_file) | **DELETE** /files/{fileId} | Delete a File
[**download_file**](FilesApi.md#download_file) | **GET** /files/{fileId}/download | Download a File
[**get_file**](FilesApi.md#get_file) | **GET** /files/{fileId} | Retrieve a File
[**get_files**](FilesApi.md#get_files) | **GET** /files | List all Files
[**post_files**](FilesApi.md#post_files) | **POST** /files | Upload a File
[**put_file**](FilesApi.md#put_file) | **PUT** /files/{fileId} | Update a File

# **delete_file**
> file delete_file()

Delete a File

Deletes a File

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))

try:
    # Delete a File
    api_response = api_instance.delete_file()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->delete_file: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**file**](file.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file**
> download_file()

Download a File

Downloads a File

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))

try:
    # Download a File
    api_instance.download_file()
except ApiException as e:
    print("Exception when calling FilesApi->download_file: %s\n" % e)
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

# **get_file**
> file get_file()

Retrieve a File

Retrieves a File Metadata

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve a File
    api_response = api_instance.get_file()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->get_file: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**file**](file.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_files**
> InlineResponse20019 get_files(filter_resource_id=filter_resource_id, filter_created_at_from=filter_created_at_from, filter_created_at_to=filter_created_at_to, filter_created_by=filter_created_by, filter_tags=filter_tags, filter_text=filter_text)

List all Files

Lists all Files

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))
filter_resource_id = NULL # object |  (optional)
filter_created_at_from = NULL # object | Format: YYYY-MM-DD (optional)
filter_created_at_to = NULL # object | Format: YYYY-MM-DD (optional)
filter_created_by = NULL # object |  (optional)
filter_tags = NULL # object |  (optional)
filter_text = NULL # object | Filter by File Name or Notes (optional)

try:
    # List all Files
    api_response = api_instance.get_files(filter_resource_id=filter_resource_id, filter_created_at_from=filter_created_at_from, filter_created_at_to=filter_created_at_to, filter_created_by=filter_created_by, filter_tags=filter_tags, filter_text=filter_text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesApi->get_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_resource_id** | [**object**](.md)|  | [optional] 
 **filter_created_at_from** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 
 **filter_created_at_to** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 
 **filter_created_by** | [**object**](.md)|  | [optional] 
 **filter_tags** | [**object**](.md)|  | [optional] 
 **filter_text** | [**object**](.md)| Filter by File Name or Notes | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_files**
> post_files()

Upload a File

Upoads a File

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
api_instance = swagger_client.FilesApi(swagger_client.ApiClient(configuration))

try:
    # Upload a File
    api_instance.post_files()
except ApiException as e:
    print("Exception when calling FilesApi->post_files: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_file**
> put_file()

Update a File

Updates a File Metadata

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FilesApi()

try:
    # Update a File
    api_instance.put_file()
except ApiException as e:
    print("Exception when calling FilesApi->put_file: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

