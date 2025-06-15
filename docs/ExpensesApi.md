# swagger_client.ExpensesApi

All URIs are relative to *https://app.doorloop.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_expense**](ExpensesApi.md#delete_expense) | **DELETE** /expenses/{expenseId} | Delete an Expense
[**get_expense**](ExpensesApi.md#get_expense) | **GET** /expenses/{expenseId} | Retrieve an Expense
[**get_expenses**](ExpensesApi.md#get_expenses) | **GET** /expenses | List all Expenses
[**post_expense**](ExpensesApi.md#post_expense) | **POST** /expenses | Create an Expense
[**put_expense**](ExpensesApi.md#put_expense) | **PUT** /expenses/{expenseId} | Update an Expense

# **delete_expense**
> Expense delete_expense()

Delete an Expense

Deletes an Expense

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
api_instance = swagger_client.ExpensesApi(swagger_client.ApiClient(configuration))

try:
    # Delete an Expense
    api_response = api_instance.delete_expense()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpensesApi->delete_expense: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Expense**](Expense.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expense**
> Expense get_expense()

Retrieve an Expense

Retrieves an Expense

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
api_instance = swagger_client.ExpensesApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve an Expense
    api_response = api_instance.get_expense()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpensesApi->get_expense: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Expense**](Expense.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_expenses**
> InlineResponse20014 get_expenses(filter_group=filter_group, filter_property=filter_property, filter_vendor=filter_vendor, filter_tenant=filter_tenant, filter_owner=filter_owner, filter_pay_from_account=filter_pay_from_account, filter_date_from=filter_date_from, filter_date_to=filter_date_to)

List all Expenses

Lists all Expenses

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
api_instance = swagger_client.ExpensesApi(swagger_client.ApiClient(configuration))
filter_group = NULL # object | Filter by Portfolio Id (optional)
filter_property = NULL # object | Filter by Property Id (optional)
filter_vendor = NULL # object | Filter by Vendor Id (optional)
filter_tenant = NULL # object | Filter by Tenant Id (optional)
filter_owner = NULL # object | Filter by Owner Id (optional)
filter_pay_from_account = NULL # object | Filter by Pay From Account Id (optional)
filter_date_from = NULL # object | Format: YYYY-MM-DD (optional)
filter_date_to = NULL # object | Format: YYYY-MM-DD (optional)

try:
    # List all Expenses
    api_response = api_instance.get_expenses(filter_group=filter_group, filter_property=filter_property, filter_vendor=filter_vendor, filter_tenant=filter_tenant, filter_owner=filter_owner, filter_pay_from_account=filter_pay_from_account, filter_date_from=filter_date_from, filter_date_to=filter_date_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpensesApi->get_expenses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_group** | [**object**](.md)| Filter by Portfolio Id | [optional] 
 **filter_property** | [**object**](.md)| Filter by Property Id | [optional] 
 **filter_vendor** | [**object**](.md)| Filter by Vendor Id | [optional] 
 **filter_tenant** | [**object**](.md)| Filter by Tenant Id | [optional] 
 **filter_owner** | [**object**](.md)| Filter by Owner Id | [optional] 
 **filter_pay_from_account** | [**object**](.md)| Filter by Pay From Account Id | [optional] 
 **filter_date_from** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 
 **filter_date_to** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_expense**
> Expense post_expense(body=body)

Create an Expense

Creates an Expense

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
api_instance = swagger_client.ExpensesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Expense() # Expense |  (optional)

try:
    # Create an Expense
    api_response = api_instance.post_expense(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpensesApi->post_expense: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Expense**](Expense.md)|  | [optional] 

### Return type

[**Expense**](Expense.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_expense**
> Expense put_expense(body=body)

Update an Expense

Updates an Expense

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
api_instance = swagger_client.ExpensesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Expense() # Expense |  (optional)

try:
    # Update an Expense
    api_response = api_instance.put_expense(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExpensesApi->put_expense: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Expense**](Expense.md)|  | [optional] 

### Return type

[**Expense**](Expense.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

