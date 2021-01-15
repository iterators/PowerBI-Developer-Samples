# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

class BaseConfig(object):

    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'ServicePrincipal'

    # Workspace Id in which the report is present
    WORKSPACE_ID = '85c9e9b7-25ad-435e-917a-ec5e6e42caf4'
    
    # Report Id for which Embed token needs to be generated
    REPORT_ID = '0b2c38f3-a387-4796-94a5-1501bda04f02'
    
    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = '5e1a3b2b-ed9a-4bba-aee9-83d557b70ad6'
    
    # Client Id (Application Id) of the AAD app
    CLIENT_ID = '3c095539-7eed-4e5b-9fa3-6230181c83fa'
    
    
    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = 'tkrBB9/1eHFiiUMQR6+Yf6Yvv3oHeNdW0Wintz2c7l8='
    
    
    # Scope of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY = 'https://login.microsoftonline.com/organizations'
    
    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = ''
    
    # Master user email password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = ''