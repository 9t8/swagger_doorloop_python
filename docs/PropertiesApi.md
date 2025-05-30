# swagger_client.PropertiesApi

All URIs are relative to *https://app.doorloop.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_properties**](PropertiesApi.md#get_properties) | **GET** /properties | List all Properties
[**get_property**](PropertiesApi.md#get_property) | **GET** /properties/{propertyId} | Retrieve a Property

# **get_properties**
> InlineResponse2002 get_properties(filter_text=filter_text, filter_group=filter_group, filter_class=filter_class, filter_owner=filter_owner)

List all Properties

Lists all Properties

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
api_instance = swagger_client.PropertiesApi(swagger_client.ApiClient(configuration))
filter_text = NULL # object | Filter by Property Name (optional)
filter_group = NULL # object | Filter by Portfolio Id (optional)
filter_class = NULL # object | Filter by Property Class (optional)
filter_owner = NULL # object | Filter by Property Owner (optional)

try:
    # List all Properties
    api_response = api_instance.get_properties(filter_text=filter_text, filter_group=filter_group, filter_class=filter_class, filter_owner=filter_owner)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertiesApi->get_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_text** | [**object**](.md)| Filter by Property Name | [optional] 
 **filter_group** | [**object**](.md)| Filter by Portfolio Id | [optional] 
 **filter_class** | [**object**](.md)| Filter by Property Class | [optional] 
 **filter_owner** | [**object**](.md)| Filter by Property Owner | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_property**
> ModelProperty get_property()

Retrieve a Property

Retrieves a Property

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
api_instance = swagger_client.PropertiesApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve a Property
    api_response = api_instance.get_property()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PropertiesApi->get_property: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ModelProperty**](ModelProperty.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

