# swagger_client.UnitsApi

All URIs are relative to *https://app.doorloop.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_unit**](UnitsApi.md#get_unit) | **GET** /units/{unitId} | Retrieve a Unit
[**get_units**](UnitsApi.md#get_units) | **GET** /units | List all Units

# **get_unit**
> Unit get_unit(unit_id)

Retrieve a Unit

Retrieves a Unit

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
api_instance = swagger_client.UnitsApi(swagger_client.ApiClient(configuration))
unit_id = NULL # object | The Unit Id

try:
    # Retrieve a Unit
    api_response = api_instance.get_unit(unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitsApi->get_unit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unit_id** | [**object**](.md)| The Unit Id | 

### Return type

[**Unit**](Unit.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_units**
> InlineResponse2003 get_units(filter_group=filter_group, filter_property=filter_property, filter_owner=filter_owner, filter_text=filter_text)

List all Units

Lists all Units

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
api_instance = swagger_client.UnitsApi(swagger_client.ApiClient(configuration))
filter_group = NULL # object | Filters by Portfolio Id (optional)
filter_property = NULL # object | Filter by Property Id (optional)
filter_owner = NULL # object | Filter by Owner Id (optional)
filter_text = NULL # object | Filter by Unit Name (optional)

try:
    # List all Units
    api_response = api_instance.get_units(filter_group=filter_group, filter_property=filter_property, filter_owner=filter_owner, filter_text=filter_text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitsApi->get_units: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_group** | [**object**](.md)| Filters by Portfolio Id | [optional] 
 **filter_property** | [**object**](.md)| Filter by Property Id | [optional] 
 **filter_owner** | [**object**](.md)| Filter by Owner Id | [optional] 
 **filter_text** | [**object**](.md)| Filter by Unit Name | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

