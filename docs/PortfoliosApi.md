# swagger_client.PortfoliosApi

All URIs are relative to *https://app.doorloop.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_property_group**](PortfoliosApi.md#get_property_group) | **GET** /property-groups/{portfolioId} | Retrieve a Portfolio
[**get_property_groups**](PortfoliosApi.md#get_property_groups) | **GET** /property-groups | List all Portfolios

# **get_property_group**
> InlineResponse20010 get_property_group()

Retrieve a Portfolio

Retreieves a Portfolio

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
api_instance = swagger_client.PortfoliosApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve a Portfolio
    api_response = api_instance.get_property_group()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfoliosApi->get_property_group: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_property_groups**
> InlineResponse20010 get_property_groups()

List all Portfolios

Lists all Portfolios

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
api_instance = swagger_client.PortfoliosApi(swagger_client.ApiClient(configuration))

try:
    # List all Portfolios
    api_response = api_instance.get_property_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfoliosApi->get_property_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

