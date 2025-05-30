# swagger_client.LeasesApi

All URIs are relative to *https://app.doorloop.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_lease**](LeasesApi.md#get_lease) | **GET** /leases/{leaseId} | Retrieve a Lease
[**get_lease_tenants**](LeasesApi.md#get_lease_tenants) | **GET** /leases/tenants | List all Lease Tenants
[**get_leases**](LeasesApi.md#get_leases) | **GET** /leases | List all Leases
[**post_leases_move_in**](LeasesApi.md#post_leases_move_in) | **POST** /leases/move-in | Move in Tenant
[**post_leases_move_out**](LeasesApi.md#post_leases_move_out) | **POST** /leases/move-out | Move out Tenant

# **get_lease**
> Lease get_lease(lease_id)

Retrieve a Lease

Retrieves a Lease

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
api_instance = swagger_client.LeasesApi(swagger_client.ApiClient(configuration))
lease_id = NULL # object | 

try:
    # Retrieve a Lease
    api_response = api_instance.get_lease(lease_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeasesApi->get_lease: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lease_id** | [**object**](.md)|  | 

### Return type

[**Lease**](Lease.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lease_tenants**
> InlineResponse2005 get_lease_tenants(filter_group=filter_group, filter_property=filter_property, filter_lease=filter_lease, filter_status=filter_status, filter_text=filter_text, filter_moved_in_at_from=filter_moved_in_at_from, filter_moved_in_at_to=filter_moved_in_at_to, filter_moved_out_at_from=filter_moved_out_at_from, filter_moved_out_at_to=filter_moved_out_at_to)

List all Lease Tenants

Retrieves a list of all lease tenants, meaning, tenants that have been associated with an active list.  This endpoint includes additional information related to the lease for each tenant in DoorLoop, with the full Tenant object included as well.  If a tenant is associated with multiple leases, the tenant will appear in the results here once for each lease it is associated with.

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
api_instance = swagger_client.LeasesApi(swagger_client.ApiClient(configuration))
filter_group = NULL # object | Filter by Portfolio Id (optional)
filter_property = NULL # object | Filter by Property Id (optional)
filter_lease = NULL # object | Filter by Lease Id (optional)
filter_status = NULL # object | Filter by Status (optional)
filter_text = NULL # object | Filter by Tenant Name / Email (optional)
filter_moved_in_at_from = NULL # object | Filter by Move In Date (YYYY-MM-DD) (optional)
filter_moved_in_at_to = NULL # object | Filter by Move In Date (YYYY-MM-DD) (optional)
filter_moved_out_at_from = NULL # object | Filter by Move Out Date (YYYY-MM-DD) (optional)
filter_moved_out_at_to = NULL # object | Filter by Move Out Date (YYYY-MM-DD) (optional)

try:
    # List all Lease Tenants
    api_response = api_instance.get_lease_tenants(filter_group=filter_group, filter_property=filter_property, filter_lease=filter_lease, filter_status=filter_status, filter_text=filter_text, filter_moved_in_at_from=filter_moved_in_at_from, filter_moved_in_at_to=filter_moved_in_at_to, filter_moved_out_at_from=filter_moved_out_at_from, filter_moved_out_at_to=filter_moved_out_at_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeasesApi->get_lease_tenants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_group** | [**object**](.md)| Filter by Portfolio Id | [optional] 
 **filter_property** | [**object**](.md)| Filter by Property Id | [optional] 
 **filter_lease** | [**object**](.md)| Filter by Lease Id | [optional] 
 **filter_status** | [**object**](.md)| Filter by Status | [optional] 
 **filter_text** | [**object**](.md)| Filter by Tenant Name / Email | [optional] 
 **filter_moved_in_at_from** | [**object**](.md)| Filter by Move In Date (YYYY-MM-DD) | [optional] 
 **filter_moved_in_at_to** | [**object**](.md)| Filter by Move In Date (YYYY-MM-DD) | [optional] 
 **filter_moved_out_at_from** | [**object**](.md)| Filter by Move Out Date (YYYY-MM-DD) | [optional] 
 **filter_moved_out_at_to** | [**object**](.md)| Filter by Move Out Date (YYYY-MM-DD) | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_leases**
> InlineResponse2004 get_leases(authorization, filter_group=filter_group, filter_property=filter_property, filter_owner=filter_owner, filter_text=filter_text, filter_start_date_from=filter_start_date_from, filter_start_date_to=filter_start_date_to, filter_end_date_from=filter_end_date_from, filter_end_date_to=filter_end_date_to, filter_property_class=filter_property_class, filter_unit=filter_unit, filter_tenant=filter_tenant, filter_outstanding_balance_greater_than=filter_outstanding_balance_greater_than, filter_status=filter_status, filter_term=filter_term)

List all Leases

Lists all Leases

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
api_instance = swagger_client.LeasesApi(swagger_client.ApiClient(configuration))
authorization = NULL # object | Your API key goes here
filter_group = NULL # object | Filters by Portfolio Id (optional)
filter_property = NULL # object | Filter by Property Id (optional)
filter_owner = NULL # object | Filter by Owner Id (optional)
filter_text = NULL # object | Filter by Lease Name (optional)
filter_start_date_from = NULL # object | Filter by Start Date (YYYY-MM-DD) (optional)
filter_start_date_to = NULL # object | Filter by Start Date (YYYY-MM-DD) (optional)
filter_end_date_from = NULL # object | Filter by End Date (YYYY-MM-DD) (optional)
filter_end_date_to = NULL # object | Filter by End Date (YYYY-MM-DD) (optional)
filter_property_class = NULL # object | Filter by Property Class (optional)
filter_unit = NULL # object | Filter by Unit Id (optional)
filter_tenant = NULL # object | Filter by Tenant Id (optional)
filter_outstanding_balance_greater_than = NULL # object | Filter by Min Outstanding Balance (optional)
filter_status = NULL # object | Filter by Status (optional)
filter_term = NULL # object | Filter by Term (optional)

try:
    # List all Leases
    api_response = api_instance.get_leases(authorization, filter_group=filter_group, filter_property=filter_property, filter_owner=filter_owner, filter_text=filter_text, filter_start_date_from=filter_start_date_from, filter_start_date_to=filter_start_date_to, filter_end_date_from=filter_end_date_from, filter_end_date_to=filter_end_date_to, filter_property_class=filter_property_class, filter_unit=filter_unit, filter_tenant=filter_tenant, filter_outstanding_balance_greater_than=filter_outstanding_balance_greater_than, filter_status=filter_status, filter_term=filter_term)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeasesApi->get_leases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | [**object**](.md)| Your API key goes here | 
 **filter_group** | [**object**](.md)| Filters by Portfolio Id | [optional] 
 **filter_property** | [**object**](.md)| Filter by Property Id | [optional] 
 **filter_owner** | [**object**](.md)| Filter by Owner Id | [optional] 
 **filter_text** | [**object**](.md)| Filter by Lease Name | [optional] 
 **filter_start_date_from** | [**object**](.md)| Filter by Start Date (YYYY-MM-DD) | [optional] 
 **filter_start_date_to** | [**object**](.md)| Filter by Start Date (YYYY-MM-DD) | [optional] 
 **filter_end_date_from** | [**object**](.md)| Filter by End Date (YYYY-MM-DD) | [optional] 
 **filter_end_date_to** | [**object**](.md)| Filter by End Date (YYYY-MM-DD) | [optional] 
 **filter_property_class** | [**object**](.md)| Filter by Property Class | [optional] 
 **filter_unit** | [**object**](.md)| Filter by Unit Id | [optional] 
 **filter_tenant** | [**object**](.md)| Filter by Tenant Id | [optional] 
 **filter_outstanding_balance_greater_than** | [**object**](.md)| Filter by Min Outstanding Balance | [optional] 
 **filter_status** | [**object**](.md)| Filter by Status | [optional] 
 **filter_term** | [**object**](.md)| Filter by Term | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_leases_move_in**
> Lease post_leases_move_in(body=body)

Move in Tenant

Moves in a Tenant

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
api_instance = swagger_client.LeasesApi(swagger_client.ApiClient(configuration))
body = swagger_client.LeasesMoveinBody() # LeasesMoveinBody |  (optional)

try:
    # Move in Tenant
    api_response = api_instance.post_leases_move_in(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeasesApi->post_leases_move_in: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LeasesMoveinBody**](LeasesMoveinBody.md)|  | [optional] 

### Return type

[**Lease**](Lease.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_leases_move_out**
> post_leases_move_out(body=body)

Move out Tenant

Moves out a Tenant

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
api_instance = swagger_client.LeasesApi(swagger_client.ApiClient(configuration))
body = swagger_client.LeasesMoveoutBody() # LeasesMoveoutBody |  (optional)

try:
    # Move out Tenant
    api_instance.post_leases_move_out(body=body)
except ApiException as e:
    print("Exception when calling LeasesApi->post_leases_move_out: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LeasesMoveoutBody**](LeasesMoveoutBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

