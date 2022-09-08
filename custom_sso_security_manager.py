import logging
from superset.security import SupersetSecurityManager

class CustomSsoSecurityManager(SupersetSecurityManager):

    def oauth_user_info(self, provider, response=None):
        if provider == 'MaterialAzureSSO':
            me = self.appbuilder.sm.oauth_remotes[provider].get('https://graph.microsoft.com/v1.0/me').json()
            return { 'name' : me['displayName'], 'email' : me['mail'], 'id' : me['id'], 'username' : me['userPrincipalName'], 'first_name': me['givenName'], 'last_name': me['surname']}
