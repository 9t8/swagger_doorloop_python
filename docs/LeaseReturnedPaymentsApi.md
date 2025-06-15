# swagger_client.LeaseReturnedPaymentsApi

All URIs are relative to *https://app.doorloop.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_lease_reversed_payment**](LeaseReturnedPaymentsApi.md#delete_lease_reversed_payment) | **DELETE** /lease-reversed-payments/{leaseReversedPaymentId} | Delete a Lease Returned Payment
[**get_lease_reversed_payment**](LeaseReturnedPaymentsApi.md#get_lease_reversed_payment) | **GET** /lease-reversed-payments/{leaseReversedPaymentId} | Retrieve a Lease Returned Payment
[**get_lease_reversed_payments**](LeaseReturnedPaymentsApi.md#get_lease_reversed_payments) | **GET** /lease-reversed-payments | List all Lease Returned Payments
[**post_lease_reversed_payments**](LeaseReturnedPaymentsApi.md#post_lease_reversed_payments) | **POST** /lease-reversed-payments | Create a Lease Returned Payment

# **delete_lease_reversed_payment**
> LeaseReversedPayment delete_lease_reversed_payment()

Delete a Lease Returned Payment

Deletes a Lease Returned Payment

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
api_instance = swagger_client.LeaseReturnedPaymentsApi(swagger_client.ApiClient(configuration))

try:
    # Delete a Lease Returned Payment
    api_response = api_instance.delete_lease_reversed_payment()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaseReturnedPaymentsApi->delete_lease_reversed_payment: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LeaseReversedPayment**](LeaseReversedPayment.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lease_reversed_payment**
> LeaseReversedPayment get_lease_reversed_payment(lease_reversed_payment_id)

Retrieve a Lease Returned Payment

Retrieves a Lease Returned Payment

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
api_instance = swagger_client.LeaseReturnedPaymentsApi(swagger_client.ApiClient(configuration))
lease_reversed_payment_id = NULL # object | 

try:
    # Retrieve a Lease Returned Payment
    api_response = api_instance.get_lease_reversed_payment(lease_reversed_payment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaseReturnedPaymentsApi->get_lease_reversed_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_reversed_payment_id** | [**object**](.md)|  | 

### Return type

[**LeaseReversedPayment**](LeaseReversedPayment.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lease_reversed_payments**
> InlineResponse2008 get_lease_reversed_payments(filter_lease=filter_lease, filter_property=filter_property, filter_payment_method=filter_payment_method, filter_owner=filter_owner, filter_date_from=filter_date_from, filter_date_to=filter_date_to)

List all Lease Returned Payments

Lists all Lease Returned Payments

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
api_instance = swagger_client.LeaseReturnedPaymentsApi(swagger_client.ApiClient(configuration))
filter_lease = NULL # object | Filter by Lease Id (optional)
filter_property = NULL # object | Filter by Property Id (optional)
filter_payment_method = NULL # object | Filter by Payment Method (optional)
filter_owner = NULL # object | Filter by Owner Id (optional)
filter_date_from = NULL # object | Filter by Date (YYYY-MM-DD) (optional)
filter_date_to = NULL # object | Filter by Date (YYYY-MM-DD) (optional)

try:
    # List all Lease Returned Payments
    api_response = api_instance.get_lease_reversed_payments(filter_lease=filter_lease, filter_property=filter_property, filter_payment_method=filter_payment_method, filter_owner=filter_owner, filter_date_from=filter_date_from, filter_date_to=filter_date_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaseReturnedPaymentsApi->get_lease_reversed_payments: %s\n" % e)
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

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_lease_reversed_payments**
> LeaseReversedPayment post_lease_reversed_payments(body=body)

Create a Lease Returned Payment

Create a Lease Returned Payment which marks an existing Lease Payment as returned

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
api_instance = swagger_client.LeaseReturnedPaymentsApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Create a Lease Returned Payment
    api_response = api_instance.post_lease_reversed_payments(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaseReturnedPaymentsApi->post_lease_reversed_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**LeaseReversedPayment**](LeaseReversedPayment.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

