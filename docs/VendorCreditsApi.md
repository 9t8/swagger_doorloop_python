# swagger_client.VendorCreditsApi

All URIs are relative to *https://app.doorloop.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_vendor_credit**](VendorCreditsApi.md#delete_vendor_credit) | **DELETE** /vendor-credits/{vendorCreditId} | Delete a Vendor Credit
[**get_vendor_credit**](VendorCreditsApi.md#get_vendor_credit) | **GET** /vendor-credits/{vendorCreditId} | Retrieve a Vendor Credit
[**get_vendor_credits**](VendorCreditsApi.md#get_vendor_credits) | **GET** /vendor-credits | List all Vendor Credits
[**post_vendor_credit**](VendorCreditsApi.md#post_vendor_credit) | **POST** /vendor-credits | Create a Vendor Credit
[**put_vendor_credit**](VendorCreditsApi.md#put_vendor_credit) | **PUT** /vendor-credits/{vendorCreditId} | Update a Vendor Credit

# **delete_vendor_credit**
> VendorTransaction delete_vendor_credit()

Delete a Vendor Credit

Deletes a Vendor Credit

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
api_instance = swagger_client.VendorCreditsApi(swagger_client.ApiClient(configuration))

try:
    # Delete a Vendor Credit
    api_response = api_instance.delete_vendor_credit()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorCreditsApi->delete_vendor_credit: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VendorTransaction**](VendorTransaction.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor_credit**
> VendorTransaction get_vendor_credit()

Retrieve a Vendor Credit

Retrieves a Vendor Credit

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
api_instance = swagger_client.VendorCreditsApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve a Vendor Credit
    api_response = api_instance.get_vendor_credit()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorCreditsApi->get_vendor_credit: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VendorTransaction**](VendorTransaction.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor_credits**
> InlineResponse20015 get_vendor_credits(filter_group=filter_group, filter_property=filter_property, filter_vendor=filter_vendor, filter_date_from=filter_date_from, filter_date_to=filter_date_to, filter_due_date_from=filter_due_date_from, filter_due_date_to=filter_due_date_to, filter_open_bills=filter_open_bills)

List all Vendor Credits

Lists all Vendor Credits

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
api_instance = swagger_client.VendorCreditsApi(swagger_client.ApiClient(configuration))
filter_group = NULL # object | Filter by Portfolio Id (optional)
filter_property = NULL # object | Filter by Property Id (optional)
filter_vendor = NULL # object | Filter by Vendor Id (optional)
filter_date_from = NULL # object | Format: YYYY-MM-DD (optional)
filter_date_to = NULL # object | Format: YYYY-MM-DD (optional)
filter_due_date_from = NULL # object | Format: YYYY-MM-DD (optional)
filter_due_date_to = NULL # object | Format: YYYY-MM-DD (optional)
filter_open_bills = NULL # object | If set to true will return only bills with an open balance  (optional)

try:
    # List all Vendor Credits
    api_response = api_instance.get_vendor_credits(filter_group=filter_group, filter_property=filter_property, filter_vendor=filter_vendor, filter_date_from=filter_date_from, filter_date_to=filter_date_to, filter_due_date_from=filter_due_date_from, filter_due_date_to=filter_due_date_to, filter_open_bills=filter_open_bills)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorCreditsApi->get_vendor_credits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_group** | [**object**](.md)| Filter by Portfolio Id | [optional] 
 **filter_property** | [**object**](.md)| Filter by Property Id | [optional] 
 **filter_vendor** | [**object**](.md)| Filter by Vendor Id | [optional] 
 **filter_date_from** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 
 **filter_date_to** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 
 **filter_due_date_from** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 
 **filter_due_date_to** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 
 **filter_open_bills** | [**object**](.md)| If set to true will return only bills with an open balance  | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_vendor_credit**
> VendorTransaction post_vendor_credit(body=body)

Create a Vendor Credit

Creates a Vendor Credit

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
api_instance = swagger_client.VendorCreditsApi(swagger_client.ApiClient(configuration))
body = swagger_client.VendorTransaction() # VendorTransaction |  (optional)

try:
    # Create a Vendor Credit
    api_response = api_instance.post_vendor_credit(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorCreditsApi->post_vendor_credit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VendorTransaction**](VendorTransaction.md)|  | [optional] 

### Return type

[**VendorTransaction**](VendorTransaction.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_vendor_credit**
> VendorTransaction put_vendor_credit(body=body)

Update a Vendor Credit

Updates a Vendor Credit

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
api_instance = swagger_client.VendorCreditsApi(swagger_client.ApiClient(configuration))
body = swagger_client.VendorTransaction() # VendorTransaction |  (optional)

try:
    # Update a Vendor Credit
    api_response = api_instance.put_vendor_credit(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorCreditsApi->put_vendor_credit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VendorTransaction**](VendorTransaction.md)|  | [optional] 

### Return type

[**VendorTransaction**](VendorTransaction.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

