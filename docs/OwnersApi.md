# swagger_client.OwnersApi

All URIs are relative to *https://app.doorloop.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_owner**](OwnersApi.md#delete_owner) | **DELETE** /owners/{ownerId} | Delete an Owner
[**get_owner**](OwnersApi.md#get_owner) | **GET** /owners/{ownerId} | Retrieve an Owner
[**get_owners**](OwnersApi.md#get_owners) | **GET** /owners | List all Owners
[**post_owner**](OwnersApi.md#post_owner) | **POST** /owners | Create an Owner
[**put_owner**](OwnersApi.md#put_owner) | **PUT** /owners/{ownerId} | Update an Owner

# **delete_owner**
> Owner delete_owner()

Delete an Owner

Deletes an Owner

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
api_instance = swagger_client.OwnersApi(swagger_client.ApiClient(configuration))

try:
    # Delete an Owner
    api_response = api_instance.delete_owner()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwnersApi->delete_owner: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Owner**](Owner.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_owner**
> Owner get_owner()

Retrieve an Owner

Retrieves an Owner

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
api_instance = swagger_client.OwnersApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve an Owner
    api_response = api_instance.get_owner()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwnersApi->get_owner: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Owner**](Owner.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_owners**
> InlineResponse20012 get_owners(filter_group=filter_group, filter_property=filter_property, filter_active=filter_active, filter_text=filter_text, filter_management_ends_before=filter_management_ends_before, filter_created_at_from=filter_created_at_from, filter_created_at_to=filter_created_at_to)

List all Owners

Lists all Owners

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
api_instance = swagger_client.OwnersApi(swagger_client.ApiClient(configuration))
filter_group = NULL # object | Filter by Portfolio Id (optional)
filter_property = NULL # object | Filter by Property Id (optional)
filter_active = NULL # object | Filter by Active/Inactive (optional)
filter_text = NULL # object | Filter by Owner Name / Email (optional)
filter_management_ends_before = NULL # object | Format: YYYY-MM-DD (optional)
filter_created_at_from = NULL # object | Format: YYYY-MM-DD (optional)
filter_created_at_to = NULL # object | Format: YYYY-MM-DD (optional)

try:
    # List all Owners
    api_response = api_instance.get_owners(filter_group=filter_group, filter_property=filter_property, filter_active=filter_active, filter_text=filter_text, filter_management_ends_before=filter_management_ends_before, filter_created_at_from=filter_created_at_from, filter_created_at_to=filter_created_at_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwnersApi->get_owners: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_group** | [**object**](.md)| Filter by Portfolio Id | [optional] 
 **filter_property** | [**object**](.md)| Filter by Property Id | [optional] 
 **filter_active** | [**object**](.md)| Filter by Active/Inactive | [optional] 
 **filter_text** | [**object**](.md)| Filter by Owner Name / Email | [optional] 
 **filter_management_ends_before** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 
 **filter_created_at_from** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 
 **filter_created_at_to** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_owner**
> Owner post_owner(body=body)

Create an Owner

Creates an Owner

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
api_instance = swagger_client.OwnersApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Create an Owner
    api_response = api_instance.post_owner(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwnersApi->post_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**Owner**](Owner.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_owner**
> Owner put_owner(body=body)

Update an Owner

Updates an Owner

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
api_instance = swagger_client.OwnersApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Update an Owner
    api_response = api_instance.put_owner(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OwnersApi->put_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**Owner**](Owner.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

