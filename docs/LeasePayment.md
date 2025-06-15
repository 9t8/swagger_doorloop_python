# LeasePayment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**MongoId**](MongoId.md) |  | [optional] 
**reference** | **object** |  | [optional] 
**amount_received** | **object** |  | 
**payment_method** | [**PaymentMethods**](PaymentMethods.md) |  | 
**lease** | [**MongoId**](MongoId.md) |  | 
**received_from_tenant** | [**MongoId**](MongoId.md) |  | [optional] 
**deposit_to_account** | [**MongoId**](MongoId.md) |  | 
**auto_apply_payment_on_charges** | **object** |  | 
**auto_deposit** | **object** |  | [optional] 
**deposit_status** | **object** | Read Only | [optional] 
**reversed_payment** | **object** | If this payment was returned, will reference the returned payment | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

