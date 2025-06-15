# Lease

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**MongoId**](MongoId.md) |  | [optional] 
**_property** | [**MongoId**](MongoId.md) |  | 
**name** | **object** |  | 
**notes** | **object** |  | [optional] 
**reference** | **object** | Read Only | [optional] 
**start** | **object** | Format: YYYY-MM-DD | 
**end** | **object** | Required if term &#x3D;&#x3D; AtWill. Format: YYYY-MM-DD | [optional] 
**term** | **object** |  | 
**rollover_to_at_will** | **object** | If set to true, the lease will automatically rollover to \&quot;At Will\&quot; (Month to Month) at the end of the fixed term. | [optional] 
**units** | **object** | An array of Unit Ids for this lease | 
**status** | **object** | Read Only | 
**evicton_pending** | **object** |  | [optional] 
**proof_of_insurance_required** | **object** |  | [optional] 
**total_balancedue** | **object** | Read Only | [optional] 
**total_deposits_held** | **object** | Read Only | [optional] 
**total_recurring_rent** | **object** | Read Only | [optional] 
**total_recurring_payments** | **object** | Read Only | [optional] 
**total_recurring_credits** | **object** | Read Only | [optional] 
**total_recurring_charges** | **object** | Read Only | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

