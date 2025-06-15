# swagger_client.TenantsApi

All URIs are relative to *https://app.doorloop.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tenant**](TenantsApi.md#delete_tenant) | **DELETE** /tenants/{tenantId} | Delete a Tenant
[**get_tenant**](TenantsApi.md#get_tenant) | **GET** /tenants/{tenantId} | Retrieve a Tenant
[**get_tenants**](TenantsApi.md#get_tenants) | **GET** /tenants | Retrieve all Tenants
[**post_tenant**](TenantsApi.md#post_tenant) | **POST** /tenants | Create a Prospect
[**put_tenant**](TenantsApi.md#put_tenant) | **PUT** /tenants/{tenantId} | Update a Tenant

# **delete_tenant**
> Tenant delete_tenant()

Delete a Tenant

Deletes a Tenant

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
api_instance = swagger_client.TenantsApi(swagger_client.ApiClient(configuration))

try:
    # Delete a Tenant
    api_response = api_instance.delete_tenant()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsApi->delete_tenant: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Tenant**](Tenant.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant**
> Tenant get_tenant(tenant_id)

Retrieve a Tenant

Retrieves a Tenant.  In DoorLoop there are 2 types of Tenants: if (type = LEASE_TENANT): This tenant has been associated with a lease. if (type = PROSPECT_TENANT): This tenant has not been associated with a leasa and is considered a \"Prospect\".

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
api_instance = swagger_client.TenantsApi(swagger_client.ApiClient(configuration))
tenant_id = NULL # object | 

try:
    # Retrieve a Tenant
    api_response = api_instance.get_tenant(tenant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsApi->get_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | [**object**](.md)|  | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenants**
> InlineResponse2006 get_tenants(filter_group=filter_group, filter_property=filter_property, filter_lease=filter_lease, filter_text=filter_text, filter_unit=filter_unit, filter_type=filter_type)

Retrieve all Tenants

Retrieves all Tenants.  In DoorLoop there are 2 types of Tenants: if (type = LEASE_TENANT): This tenant has been associated with a lease. if (type = PROSPECT_TENANT): This tenant has not been associated with a leasa and is considered a \"Prospect\".

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
api_instance = swagger_client.TenantsApi(swagger_client.ApiClient(configuration))
filter_group = NULL # object | Filter by Portfolio Id (optional)
filter_property = NULL # object | Filter by Property Id (optional)
filter_lease = NULL # object | Filter by Lease Id (optional)
filter_text = NULL # object | Filter by Tenant Name / Email (optional)
filter_unit = NULL # object | Filter by Unit Id (optional)
filter_type = NULL # object | Filter by Tenant Type (optional)

try:
    # Retrieve all Tenants
    api_response = api_instance.get_tenants(filter_group=filter_group, filter_property=filter_property, filter_lease=filter_lease, filter_text=filter_text, filter_unit=filter_unit, filter_type=filter_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsApi->get_tenants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_group** | [**object**](.md)| Filter by Portfolio Id | [optional] 
 **filter_property** | [**object**](.md)| Filter by Property Id | [optional] 
 **filter_lease** | [**object**](.md)| Filter by Lease Id | [optional] 
 **filter_text** | [**object**](.md)| Filter by Tenant Name / Email | [optional] 
 **filter_unit** | [**object**](.md)| Filter by Unit Id | [optional] 
 **filter_type** | [**object**](.md)| Filter by Tenant Type | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, multipart/form-data

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tenant**
> Tenant post_tenant(body=body)

Create a Prospect

Creates a Prospect. In DoorLoop there are 2 types of Tenants: if (type = LEASE_TENANT): This tenant has been associated with a lease. if (type = PROSPECT_TENANT): This tenant has not been associated with a leasa and is considered a \"Prospect\".  All Tenants are created as a PROSPECT_TENANT, and their type changes once they are associated with a lease.

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
api_instance = swagger_client.TenantsApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Create a Prospect
    api_response = api_instance.post_tenant(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsApi->post_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_tenant**
> Tenant put_tenant(body=body)

Update a Tenant

Updates a Tenant

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
api_instance = swagger_client.TenantsApi(swagger_client.ApiClient(configuration))
body = NULL # object |  (optional)

try:
    # Update a Tenant
    api_response = api_instance.put_tenant(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenantsApi->put_tenant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

