# Expense

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**MongoId**](MongoId.md) |  | [optional] 
**pay_from_account** | **object** |  | 
**payment_method** | **object** |  | 
**pay_to_resource_type** | **object** |  | [optional] 
**pay_to_resource_id** | **object** |  | [optional] 
**lines** | **object** |  | 
**memo** | **object** |  | [optional] 
**reference** | **object** | If not provided will be generated automatically by the server. | [optional] 
**_date** | **object** | Format: YYYY-MM-DD | 
**batch** | **object** |  | [optional] 
**total_amount** | **object** | Read Only. Calculated as sum of lines.amount. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

