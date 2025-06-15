# swagger_client.ReportsApi

All URIs are relative to *https://app.doorloop.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_reports_balance_sheet**](ReportsApi.md#get_reports_balance_sheet) | **GET** /reports/balance-sheet-summary | Balance Sheet
[**get_reports_cash_flow_statement**](ReportsApi.md#get_reports_cash_flow_statement) | **GET** /reports/cash-flow-statement | Cash Flow Statement
[**get_reports_profit_and_loss**](ReportsApi.md#get_reports_profit_and_loss) | **GET** /reports/profit-and-loss-summary | Profit &amp; Loss
[**get_reports_rent_roll**](ReportsApi.md#get_reports_rent_roll) | **GET** /reports/rent-roll | Rent Roll

# **get_reports_balance_sheet**
> ProfitAndLossReportItem get_reports_balance_sheet(filter_accounting_method, filter_group=filter_group, filter_property=filter_property, filter_property_owner=filter_property_owner, filter_date_from=filter_date_from, filter_date_to=filter_date_to)

Balance Sheet

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
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))
filter_accounting_method = NULL # object | Cash / Accrual
filter_group = NULL # object | Filter by Portfolio Id (optional)
filter_property = NULL # object | Filter by Property Id (optional)
filter_property_owner = NULL # object | Filter by Owner Id (optional)
filter_date_from = NULL # object | Format: YYYY-MM-DD (optional)
filter_date_to = NULL # object | Format: YYYY-MM-DD (optional)

try:
    # Balance Sheet
    api_response = api_instance.get_reports_balance_sheet(filter_accounting_method, filter_group=filter_group, filter_property=filter_property, filter_property_owner=filter_property_owner, filter_date_from=filter_date_from, filter_date_to=filter_date_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_reports_balance_sheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_accounting_method** | [**object**](.md)| Cash / Accrual | 
 **filter_group** | [**object**](.md)| Filter by Portfolio Id | [optional] 
 **filter_property** | [**object**](.md)| Filter by Property Id | [optional] 
 **filter_property_owner** | [**object**](.md)| Filter by Owner Id | [optional] 
 **filter_date_from** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 
 **filter_date_to** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 

### Return type

[**ProfitAndLossReportItem**](ProfitAndLossReportItem.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reports_cash_flow_statement**
> ProfitAndLossReportItem get_reports_cash_flow_statement(filter_accounting_method, filter_group=filter_group, filter_property=filter_property, filter_property_owner=filter_property_owner, filter_date_from=filter_date_from, filter_date_to=filter_date_to)

Cash Flow Statement

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
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))
filter_accounting_method = NULL # object | Cash / Accrual
filter_group = NULL # object | Filter by Portfolio Id (optional)
filter_property = NULL # object | Filter by Property Id (optional)
filter_property_owner = NULL # object | Filter by Owner Id (optional)
filter_date_from = NULL # object | Format: YYYY-MM-DD (optional)
filter_date_to = NULL # object | Format: YYYY-MM-DD (optional)

try:
    # Cash Flow Statement
    api_response = api_instance.get_reports_cash_flow_statement(filter_accounting_method, filter_group=filter_group, filter_property=filter_property, filter_property_owner=filter_property_owner, filter_date_from=filter_date_from, filter_date_to=filter_date_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_reports_cash_flow_statement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_accounting_method** | [**object**](.md)| Cash / Accrual | 
 **filter_group** | [**object**](.md)| Filter by Portfolio Id | [optional] 
 **filter_property** | [**object**](.md)| Filter by Property Id | [optional] 
 **filter_property_owner** | [**object**](.md)| Filter by Owner Id | [optional] 
 **filter_date_from** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 
 **filter_date_to** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 

### Return type

[**ProfitAndLossReportItem**](ProfitAndLossReportItem.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reports_profit_and_loss**
> ProfitAndLossReportItem get_reports_profit_and_loss(filter_accounting_method, filter_group=filter_group, filter_property=filter_property, filter_property_owner=filter_property_owner, filter_date_from=filter_date_from, filter_date_to=filter_date_to)

Profit & Loss

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
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))
filter_accounting_method = NULL # object | Cash / Accrual
filter_group = NULL # object | Filter by Portfolio Id (optional)
filter_property = NULL # object | Filter by Property Id (optional)
filter_property_owner = NULL # object | Filter by Owner Id (optional)
filter_date_from = NULL # object | Format: YYYY-MM-DD (optional)
filter_date_to = NULL # object | Format: YYYY-MM-DD (optional)

try:
    # Profit & Loss
    api_response = api_instance.get_reports_profit_and_loss(filter_accounting_method, filter_group=filter_group, filter_property=filter_property, filter_property_owner=filter_property_owner, filter_date_from=filter_date_from, filter_date_to=filter_date_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_reports_profit_and_loss: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_accounting_method** | [**object**](.md)| Cash / Accrual | 
 **filter_group** | [**object**](.md)| Filter by Portfolio Id | [optional] 
 **filter_property** | [**object**](.md)| Filter by Property Id | [optional] 
 **filter_property_owner** | [**object**](.md)| Filter by Owner Id | [optional] 
 **filter_date_from** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 
 **filter_date_to** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 

### Return type

[**ProfitAndLossReportItem**](ProfitAndLossReportItem.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reports_rent_roll**
> InlineResponse20016 get_reports_rent_roll(filter_group=filter_group, filter_property=filter_property, filter_owner=filter_owner, filter_as_of_date=filter_as_of_date)

Rent Roll

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
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))
filter_group = NULL # object | Filter by Portfolio Id (optional)
filter_property = NULL # object | Filter by Property Id (optional)
filter_owner = NULL # object | Filter by Owner Id (optional)
filter_as_of_date = NULL # object | Format: YYYY-MM-DD (optional)

try:
    # Rent Roll
    api_response = api_instance.get_reports_rent_roll(filter_group=filter_group, filter_property=filter_property, filter_owner=filter_owner, filter_as_of_date=filter_as_of_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_reports_rent_roll: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_group** | [**object**](.md)| Filter by Portfolio Id | [optional] 
 **filter_property** | [**object**](.md)| Filter by Property Id | [optional] 
 **filter_owner** | [**object**](.md)| Filter by Owner Id | [optional] 
 **filter_as_of_date** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

