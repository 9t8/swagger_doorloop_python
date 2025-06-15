# swagger_client.LeaseCreditsApi

All URIs are relative to *https://app.doorloop.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_lease_credits_lease_credit_id**](LeaseCreditsApi.md#delete_lease_credits_lease_credit_id) | **DELETE** /lease-credits/{leaseCreditId} | Delete a Lease Credit
[**get_lease_credit**](LeaseCreditsApi.md#get_lease_credit) | **GET** /lease-credits/{leaseCreditId} | Retrieve a Lease Credit
[**get_lease_credits**](LeaseCreditsApi.md#get_lease_credits) | **GET** /lease-credits | List all Lease Credits
[**post_lease_credit**](LeaseCreditsApi.md#post_lease_credit) | **POST** /lease-credits | Create a Lease Credit
[**put_lease_credit**](LeaseCreditsApi.md#put_lease_credit) | **PUT** /lease-credits/{leaseCreditId} | Update a Lease Credit

# **delete_lease_credits_lease_credit_id**
> LeaseTransaction delete_lease_credits_lease_credit_id()

Delete a Lease Credit

Delete Lease Credits

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LeaseCreditsApi()

try:
    # Delete a Lease Credit
    api_response = api_instance.delete_lease_credits_lease_credit_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaseCreditsApi->delete_lease_credits_lease_credit_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LeaseTransaction**](LeaseTransaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lease_credit**
> LeaseTransaction get_lease_credit(lease_credit_id)

Retrieve a Lease Credit

Retrieves a Lease Credits

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
api_instance = swagger_client.LeaseCreditsApi(swagger_client.ApiClient(configuration))
lease_credit_id = NULL # object | 

try:
    # Retrieve a Lease Credit
    api_response = api_instance.get_lease_credit(lease_credit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaseCreditsApi->get_lease_credit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_credit_id** | [**object**](.md)|  | 

### Return type

[**LeaseTransaction**](LeaseTransaction.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lease_credits**
> InlineResponse2009 get_lease_credits(filter_lease=filter_lease, filter_property=filter_property, filter_owner=filter_owner, filter_date_from=filter_date_from, filter_date_to=filter_date_to)

List all Lease Credits

Lists all Lease Credits

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
api_instance = swagger_client.LeaseCreditsApi(swagger_client.ApiClient(configuration))
filter_lease = NULL # object | Filter by Lease Id (optional)
filter_property = NULL # object | Filter by Property Id (optional)
filter_owner = NULL # object | Filter by Owner Id (optional)
filter_date_from = NULL # object | Filter by Date (YYYY-MM-DD) (optional)
filter_date_to = NULL # object | Filter by Date (YYYY-MM-DD) (optional)

try:
    # List all Lease Credits
    api_response = api_instance.get_lease_credits(filter_lease=filter_lease, filter_property=filter_property, filter_owner=filter_owner, filter_date_from=filter_date_from, filter_date_to=filter_date_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaseCreditsApi->get_lease_credits: %s\n" % e)
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

# **post_lease_credit**
> LeaseTransaction post_lease_credit(body=body)

Create a Lease Credit

Creates a Lease Credit

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
api_instance = swagger_client.LeaseCreditsApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Create a Lease Credit
    api_response = api_instance.post_lease_credit(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaseCreditsApi->post_lease_credit: %s\n" % e)
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

# **put_lease_credit**
> LeaseTransaction put_lease_credit(body=body)

Update a Lease Credit

Updates a Lease Credit

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
api_instance = swagger_client.LeaseCreditsApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Update a Lease Credit
    api_response = api_instance.put_lease_credit(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaseCreditsApi->put_lease_credit: %s\n" % e)
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

