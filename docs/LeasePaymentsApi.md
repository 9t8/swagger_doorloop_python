# swagger_client.LeasePaymentsApi

All URIs are relative to *https://app.doorloop.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_lease_payment**](LeasePaymentsApi.md#delete_lease_payment) | **DELETE** /lease-payments/{leasePaymentId} | Delete a Lease Payment
[**get_lease_payment**](LeasePaymentsApi.md#get_lease_payment) | **GET** /lease-payments/{leasePaymentId} | Retrieve a Lease Payment
[**get_lease_payments**](LeasePaymentsApi.md#get_lease_payments) | **GET** /lease-payments | List all Lease Payments
[**post_lease_payment**](LeasePaymentsApi.md#post_lease_payment) | **POST** /lease-payments | Create a Lease Payment
[**put_lease_payment**](LeasePaymentsApi.md#put_lease_payment) | **PUT** /lease-payments/{leasePaymentId} | Update a Lease Payment

# **delete_lease_payment**
> LeasePayment delete_lease_payment()

Delete a Lease Payment

Deletes a Lease Payment

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
api_instance = swagger_client.LeasePaymentsApi(swagger_client.ApiClient(configuration))

try:
    # Delete a Lease Payment
    api_response = api_instance.delete_lease_payment()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeasePaymentsApi->delete_lease_payment: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LeasePayment**](LeasePayment.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lease_payment**
> LeasePayment get_lease_payment(lease_payment_id)

Retrieve a Lease Payment

Retrieves a Lease Payment

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
api_instance = swagger_client.LeasePaymentsApi(swagger_client.ApiClient(configuration))
lease_payment_id = NULL # object | The Lease Payment Id

try:
    # Retrieve a Lease Payment
    api_response = api_instance.get_lease_payment(lease_payment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeasePaymentsApi->get_lease_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_payment_id** | [**object**](.md)| The Lease Payment Id | 

### Return type

[**LeasePayment**](LeasePayment.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lease_payments**
> InlineResponse2007 get_lease_payments(filter_lease=filter_lease, filter_property=filter_property, filter_payment_method=filter_payment_method, filter_owner=filter_owner, filter_date_from=filter_date_from, filter_date_to=filter_date_to)

List all Lease Payments

Lists all Lease Payments

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
api_instance = swagger_client.LeasePaymentsApi(swagger_client.ApiClient(configuration))
filter_lease = NULL # object | Filter by Lease Id (optional)
filter_property = NULL # object | Filter by Property Id (optional)
filter_payment_method = NULL # object | Filter by Payment Method (optional)
filter_owner = NULL # object | Filter by Owner Id (optional)
filter_date_from = NULL # object | Filter by Date (YYYY-MM-DD) (optional)
filter_date_to = NULL # object | Filter by Date (YYYY-MM-DD) (optional)

try:
    # List all Lease Payments
    api_response = api_instance.get_lease_payments(filter_lease=filter_lease, filter_property=filter_property, filter_payment_method=filter_payment_method, filter_owner=filter_owner, filter_date_from=filter_date_from, filter_date_to=filter_date_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeasePaymentsApi->get_lease_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_lease** | [**object**](.md)| Filter by Lease Id | [optional] 
 **filter_property** | [**object**](.md)| Filter by Property Id | [optional] 
 **filter_payment_method** | [**object**](.md)| Filter by Payment Method | [optional] 
 **filter_owner** | [**object**](.md)| Filter by Owner Id | [optional] 
 **filter_date_from** | [**object**](.md)| Filter by Date (YYYY-MM-DD) | [optional] 
 **filter_date_to** | [**object**](.md)| Filter by Date (YYYY-MM-DD) | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_lease_payment**
> LeasePayment post_lease_payment(body=body)

Create a Lease Payment

Creates a Lease Payment

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
api_instance = swagger_client.LeasePaymentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.LeasePayment() # LeasePayment |  (optional)

try:
    # Create a Lease Payment
    api_response = api_instance.post_lease_payment(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeasePaymentsApi->post_lease_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LeasePayment**](LeasePayment.md)|  | [optional] 

### Return type

[**LeasePayment**](LeasePayment.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_lease_payment**
> LeasePayment put_lease_payment(body=body)

Update a Lease Payment

Updates a Lease Payment

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
api_instance = swagger_client.LeasePaymentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.LeasePayment() # LeasePayment |  (optional)

try:
    # Update a Lease Payment
    api_response = api_instance.put_lease_payment(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeasePaymentsApi->put_lease_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LeasePayment**](LeasePayment.md)|  | [optional] 

### Return type

[**LeasePayment**](LeasePayment.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

