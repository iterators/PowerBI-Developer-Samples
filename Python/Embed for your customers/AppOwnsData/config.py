# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

class BaseConfig(object):

    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'ServicePrincipal'

    # Workspace Id in which the report is present
    WORKSPACE_ID = '5c2c2c9c-8cde-40e3-b2ab-ac53dadd6801'
    
    # Report Id for which Embed token needs to be generated
    REPORT_ID = 'dbb0723d-6422-406b-bb30-64bafd8d4cc6'
    
    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = 'f1044067-8c60-4022-98d8-69306c5f7238'
    
    # Client Id (Application Id) of the AAD app
    CLIENT_ID = '015256e0-7d36-44cd-8f53-eacfffabfa7c'
    
    
    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = 'New0hueHXKVgb7G2IlbgsFm+zA9UC0VjLa2YS+e99Qk='
    #CLIENT_SECRET = '17f40f3c-7b9c-4059-8131-6f527947bc60'
    
    # Scope of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY = 'https://login.microsoftonline.com/organizations'
    
    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = ''
    
    # Master user email password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = ''