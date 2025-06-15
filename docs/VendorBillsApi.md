# swagger_client.VendorBillsApi

All URIs are relative to *https://app.doorloop.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_vendor_bill**](VendorBillsApi.md#delete_vendor_bill) | **DELETE** /vendor-bills/{vendorBillId} | Delete a Vendor Bill
[**get_vendor_bill**](VendorBillsApi.md#get_vendor_bill) | **GET** /vendor-bills/{vendorBillId} | Retrieve a Vendor Bill
[**get_vendor_bills**](VendorBillsApi.md#get_vendor_bills) | **GET** /vendor-bills | List all Vendor Bills
[**post_vendor_bill**](VendorBillsApi.md#post_vendor_bill) | **POST** /vendor-bills | Create a Vendor Bill
[**put_vendor_bill**](VendorBillsApi.md#put_vendor_bill) | **PUT** /vendor-bills/{vendorBillId} | Update a Vendor Bill

# **delete_vendor_bill**
> VendorTransaction delete_vendor_bill()

Delete a Vendor Bill

Deletes a Vendor Bill

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
api_instance = swagger_client.VendorBillsApi(swagger_client.ApiClient(configuration))

try:
    # Delete a Vendor Bill
    api_response = api_instance.delete_vendor_bill()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorBillsApi->delete_vendor_bill: %s\n" % e)
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

# **get_vendor_bill**
> VendorTransaction get_vendor_bill()

Retrieve a Vendor Bill

Retrieves a Vendor Bill

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
api_instance = swagger_client.VendorBillsApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve a Vendor Bill
    api_response = api_instance.get_vendor_bill()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorBillsApi->get_vendor_bill: %s\n" % e)
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

# **get_vendor_bills**
> InlineResponse20015 get_vendor_bills(filter_group=filter_group, filter_property=filter_property, filter_vendor=filter_vendor, filter_date_from=filter_date_from, filter_date_to=filter_date_to, filter_due_date_from=filter_due_date_from, filter_due_date_to=filter_due_date_to, filter_open_bills=filter_open_bills)

List all Vendor Bills

Lists all Vendor Bills

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
api_instance = swagger_client.VendorBillsApi(swagger_client.ApiClient(configuration))
filter_group = NULL # object | Filter by Portfolio Id (optional)
filter_property = NULL # object | Filter by Property Id (optional)
filter_vendor = NULL # object | Filter by Vendor Id (optional)
filter_date_from = NULL # object | Format: YYYY-MM-DD (optional)
filter_date_to = NULL # object | Format: YYYY-MM-DD (optional)
filter_due_date_from = NULL # object | Format: YYYY-MM-DD (optional)
filter_due_date_to = NULL # object | Format: YYYY-MM-DD (optional)
filter_open_bills = NULL # object | If set to true will return only bills with an open balance  (optional)

try:
    # List all Vendor Bills
    api_response = api_instance.get_vendor_bills(filter_group=filter_group, filter_property=filter_property, filter_vendor=filter_vendor, filter_date_from=filter_date_from, filter_date_to=filter_date_to, filter_due_date_from=filter_due_date_from, filter_due_date_to=filter_due_date_to, filter_open_bills=filter_open_bills)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorBillsApi->get_vendor_bills: %s\n" % e)
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

# **post_vendor_bill**
> VendorTransaction post_vendor_bill(body=body)

Create a Vendor Bill

Creates a Vendor Bill

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
api_instance = swagger_client.VendorBillsApi(swagger_client.ApiClient(configuration))
body = swagger_client.VendorTransaction() # VendorTransaction |  (optional)

try:
    # Create a Vendor Bill
    api_response = api_instance.post_vendor_bill(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorBillsApi->post_vendor_bill: %s\n" % e)
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

# **put_vendor_bill**
> VendorTransaction put_vendor_bill(body=body)

Update a Vendor Bill

Updates a Vendor Bill

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
api_instance = swagger_client.VendorBillsApi(swagger_client.ApiClient(configuration))
body = swagger_client.VendorTransaction() # VendorTransaction |  (optional)

try:
    # Update a Vendor Bill
    api_response = api_instance.put_vendor_bill(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorBillsApi->put_vendor_bill: %s\n" % e)
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

