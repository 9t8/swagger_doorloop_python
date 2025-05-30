# swagger_client.CommunicationsApi

All URIs are relative to *https://app.doorloop.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_communication**](CommunicationsApi.md#delete_communication) | **DELETE** /communications/{communicationId} | Delete a Communication
[**get_communication**](CommunicationsApi.md#get_communication) | **GET** /communications/{communicationId} | Retrieve a Communication
[**get_communications**](CommunicationsApi.md#get_communications) | **GET** /communications | List all Communication Logs
[**post_communication**](CommunicationsApi.md#post_communication) | **POST** /communications | Create a Communication Log
[**put_communication**](CommunicationsApi.md#put_communication) | **PUT** /communications/{communicationId} | Update a Communication

# **delete_communication**
> Communication delete_communication()

Delete a Communication

Deletes a Communication Log Entry

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
api_instance = swagger_client.CommunicationsApi(swagger_client.ApiClient(configuration))

try:
    # Delete a Communication
    api_response = api_instance.delete_communication()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunicationsApi->delete_communication: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Communication**](Communication.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_communication**
> Communication get_communication()

Retrieve a Communication

Retrieves a Communication Log Entry

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
api_instance = swagger_client.CommunicationsApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve a Communication
    api_response = api_instance.get_communication()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunicationsApi->get_communication: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Communication**](Communication.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_communications**
> InlineResponse20017 get_communications(filter_sent_at_from=filter_sent_at_from, filter_sent_at_to=filter_sent_at_to, filter_participant_linked_to_type=filter_participant_linked_to_type, filter_participant_linked_to_id=filter_participant_linked_to_id, filter_thread_id=filter_thread_id, filter_status=filter_status, filter_type=filter_type)

List all Communication Logs

Lists all Communication Log Entries

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
api_instance = swagger_client.CommunicationsApi(swagger_client.ApiClient(configuration))
filter_sent_at_from = NULL # object | Format: YYYY-MM-DD (optional)
filter_sent_at_to = NULL # object | Format: YYYY-MM-DD (optional)
filter_participant_linked_to_type = NULL # object |  (optional)
filter_participant_linked_to_id = NULL # object |  (optional)
filter_thread_id = NULL # object |  (optional)
filter_status = NULL # object |  (optional)
filter_type = NULL # object |  (optional)

try:
    # List all Communication Logs
    api_response = api_instance.get_communications(filter_sent_at_from=filter_sent_at_from, filter_sent_at_to=filter_sent_at_to, filter_participant_linked_to_type=filter_participant_linked_to_type, filter_participant_linked_to_id=filter_participant_linked_to_id, filter_thread_id=filter_thread_id, filter_status=filter_status, filter_type=filter_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunicationsApi->get_communications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_sent_at_from** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 
 **filter_sent_at_to** | [**object**](.md)| Format: YYYY-MM-DD | [optional] 
 **filter_participant_linked_to_type** | [**object**](.md)|  | [optional] 
 **filter_participant_linked_to_id** | [**object**](.md)|  | [optional] 
 **filter_thread_id** | [**object**](.md)|  | [optional] 
 **filter_status** | [**object**](.md)|  | [optional] 
 **filter_type** | [**object**](.md)|  | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_communication**
> Communication post_communication(body=body)

Create a Communication Log

Creates a Communication Log Entry

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
api_instance = swagger_client.CommunicationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Communication() # Communication |  (optional)

try:
    # Create a Communication Log
    api_response = api_instance.post_communication(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunicationsApi->post_communication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Communication**](Communication.md)|  | [optional] 

### Return type

[**Communication**](Communication.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_communication**
> Communication put_communication(body=body)

Update a Communication

Updates a Communication Log Entry

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
api_instance = swagger_client.CommunicationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Communication() # Communication |  (optional)

try:
    # Update a Communication
    api_response = api_instance.put_communication(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommunicationsApi->put_communication: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Communication**](Communication.md)|  | [optional] 

### Return type

[**Communication**](Communication.md)

### Authorization

[Key](../README.md#Key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

