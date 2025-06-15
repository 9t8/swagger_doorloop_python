# swagger_client.LeaseChargesApi

All URIs are relative to *https://app.doorloop.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_lease_charge**](LeaseChargesApi.md#delete_lease_charge) | **DELETE** /lease-charges/{leaseChargeId} | Delete a Lease Credit
[**get_lease_charge**](LeaseChargesApi.md#get_lease_charge) | **GET** /lease-charges/{leaseChargeId} | Retrieve a Lease Charge
[**get_lease_charges**](LeaseChargesApi.md#get_lease_charges) | **GET** /lease-charges | List all Lease Charges
[**post_lease_charge**](LeaseChargesApi.md#post_lease_charge) | **POST** /lease-charges | Create a Lease Charge
[**put_lease_charge**](LeaseChargesApi.md#put_lease_charge) | **PUT** /lease-charges/{leaseChargeId} | Update a Lease Charge

# **delete_lease_charge**
> LeaseTransaction delete_lease_charge()

Delete a Lease Credit

Deletes a Lease Credit

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
api_instance = swagger_client.LeaseChargesApi(swagger_client.ApiClient(configuration))

try:
    # Delete a Lease Credit
    api_response = api_instance.delete_lease_charge()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaseChargesApi->delete_lease_charge: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LeaseTransaction**](LeaseTransaction.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lease_charge**
> LeaseTransaction get_lease_charge(lease_charge_id)

Retrieve a Lease Charge

Retrieves a Lease Charge

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
api_instance = swagger_client.LeaseChargesApi(swagger_client.ApiClient(configuration))
lease_charge_id = NULL # object | 

try:
    # Retrieve a Lease Charge
    api_response = api_instance.get_lease_charge(lease_charge_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaseChargesApi->get_lease_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_charge_id** | [**object**](.md)|  | 

### Return type

[**LeaseTransaction**](LeaseTransaction.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lease_charges**
> InlineResponse2009 get_lease_charges(filter_lease=filter_lease, filter_property=filter_property, filter_owner=filter_owner, filter_date_from=filter_date_from, filter_date_to=filter_date_to)

List all Lease Charges

Lists all Lease Charges

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
api_instance = swagger_client.LeaseChargesApi(swagger_client.ApiClient(configuration))
filter_lease = NULL # object | Filter by Lease Id (optional)
filter_property = NULL # object | Filter by Property Id (optional)
filter_owner = NULL # object | Filter by Owner Id (optional)
filter_date_from = NULL # object | Filter by Date (YYYY-MM-DD) (optional)
filter_date_to = NULL # object | Filter by Date (YYYY-MM-DD) (optional)

try:
    # List all Lease Charges
    api_response = api_instance.get_lease_charges(filter_lease=filter_lease, filter_property=filter_property, filter_owner=filter_owner, filter_date_from=filter_date_from, filter_date_to=filter_date_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaseChargesApi->get_lease_charges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_lease** | [**object**](.md)| Filter by Lease Id | [optional] 
 **filter_property** | [**object**](.md)| Filter by Property Id | [optional] 
 **filter_owner** | [**object**](.md)| Filter by Owner Id | [optional] 
 **filter_date_from** | [**object**](.md)| Filter by Date (YYYY-MM-DD) | [optional] 
 **filter_date_to** | [**object**](.md)| Filter by Date (YYYY-MM-DD) | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_lease_charge**
> LeaseTransaction post_lease_charge(body=body)

Create a Lease Charge

Created a Lease Charge

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
api_instance = swagger_client.LeaseChargesApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Create a Lease Charge
    api_response = api_instance.post_lease_charge(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaseChargesApi->post_lease_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**LeaseTransaction**](LeaseTransaction.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_lease_charge**
> LeaseTransaction put_lease_charge(body=body)

Update a Lease Charge

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
api_instance = swagger_client.LeaseChargesApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Update a Lease Charge
    api_response = api_instance.put_lease_charge(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaseChargesApi->put_lease_charge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**LeaseTransaction**](LeaseTransaction.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

