# swagger_client.VendorsApi

All URIs are relative to *https://app.doorloop.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_vendor**](VendorsApi.md#delete_vendor) | **DELETE** /vendors/{vendorId} | Delete a Vendor
[**get_vendor**](VendorsApi.md#get_vendor) | **GET** /vendors/{vendorId} | Retrieve a Vendor
[**get_vendors**](VendorsApi.md#get_vendors) | **GET** /vendors | List all Vendors
[**post_vendor**](VendorsApi.md#post_vendor) | **POST** /vendors | Create a Vendor
[**put_vendor**](VendorsApi.md#put_vendor) | **PUT** /vendors/{vendorId} | Update a Vendor

# **delete_vendor**
> Vendor delete_vendor()

Delete a Vendor

Deletes a Vendor

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
api_instance = swagger_client.VendorsApi(swagger_client.ApiClient(configuration))

try:
    # Delete a Vendor
    api_response = api_instance.delete_vendor()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->delete_vendor: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Vendor**](Vendor.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor**
> Vendor get_vendor()

Retrieve a Vendor

Retrieves a Vendor

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
api_instance = swagger_client.VendorsApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve a Vendor
    api_response = api_instance.get_vendor()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->get_vendor: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Vendor**](Vendor.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendors**
> InlineResponse20013 get_vendors(filter_property=filter_property, filter_active=filter_active, filter_insurance_expires_before=filter_insurance_expires_before, filter_open_balance=filter_open_balance, filter_created_at_from=filter_created_at_from, filter_created_at_to=filter_created_at_to)

List all Vendors

Lists all Vendors

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
api_instance = swagger_client.VendorsApi(swagger_client.ApiClient(configuration))
filter_property = NULL # object | Filter by Property Id (optional)
filter_active = NULL # object | Filter by Active/Inactive (optional)
filter_insurance_expires_before = NULL # object | Format: YYYY-MM-DD (optional)
filter_open_balance = NULL # object | If true, will return only vendors with an open balance (optional)
filter_created_at_from = NULL # object | Format: YYYY-MM-DD (optional)
filter_created_at_to = NULL # object | Format: YYYY-MM-DD (optional)

try:
    # List all Vendors
    api_response = api_instance.get_vendors(filter_property=filter_property, filter_active=filter_active, filter_insurance_expires_before=filter_insurance_expires_before, filter_open_balance=filter_open_balance, filter_created_at_from=filter_created_at_from, filter_created_at_to=filter_created_at_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->get_vendors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_property** | [**object**](.md)| Filter by Property Id | [optional] 
 **filter_active** | [**object**](.md)| Filter by Active/Inactive | [optional] 
 **filter_insurance_expires_before** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 
 **filter_open_balance** | [**object**](.md)| If true, will return only vendors with an open balance | [optional] 
 **filter_created_at_from** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 
 **filter_created_at_to** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_vendor**
> Vendor post_vendor(body=body)

Create a Vendor

Creates a Vendor

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
api_instance = swagger_client.VendorsApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Create a Vendor
    api_response = api_instance.post_vendor(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->post_vendor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**Vendor**](Vendor.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_vendor**
> Vendor put_vendor(body=body)

Update a Vendor

Updates a Vendor

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
api_instance = swagger_client.VendorsApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Update a Vendor
    api_response = api_instance.put_vendor(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->put_vendor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**Vendor**](Vendor.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

