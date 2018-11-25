<template>
    <div>
        <AppHeader fixed>
        </AppHeader>
        <div class="app-body mt-0">
            <AppSidebar fixed>
                <SidebarHeader/>
                <SidebarForm/>
                <SidebarNav :navItems="nav"></SidebarNav>
                <SidebarFooter/>
                <SidebarMinimizer/>
            </AppSidebar>
            <main class="main">
                <Breadcrumb :list="list"/>
                <div class="container-fluid">
                    <!--<router-view></router-view>-->
                </div>
            </main>
            <AppAside fixed>
                <DefaultAside/>
            </AppAside>
        </div>
        <TheFooter>
        </TheFooter>
    </div>
</template>

<script>
    import nav from './components/shared/_nav.js'
    import {
        Aside as AppAside,
        AsideToggler,
        Breadcrumb,
        Footer as TheFooter,
        Header as AppHeader,
        Sidebar as AppSidebar,
        SidebarFooter,
        SidebarForm,
        SidebarHeader,
        SidebarMinimizer,
        SidebarNav,
        SidebarToggler
    } from './components/shared'
    import DefaultAside from './components/containers/Aside.vue'
    import DefaultHeaderDropdownAccnt from './components/containers/DropdownAccnt.vue'

    export default {
        name: 'app',
        components: {
            AsideToggler,
            AppHeader,
            AppSidebar,
            AppAside,
            TheFooter,
            Breadcrumb,
            DefaultAside,
            DefaultHeaderDropdownAccnt,
            SidebarForm,
            SidebarFooter,
            SidebarToggler,
            SidebarHeader,
            SidebarNav,
            SidebarMinimizer
        },
        data() {
            return {oken app provides Django database migrations.

You'll also need to create tokens for your users.

from rest_framework.authtoken.models import Token

token = Token.objects.create(user=...)
print(token.key)
For clients to authenticate, the token key should be included in the Authorization HTTP header. The key should be prefixed by the string literal "Token", with whitespace separating the two strings. For example:

Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
Note: If you want to use a different keyword in the header, such as Bearer, simply subclass TokenAuthentication and set the keyword class variable.

If successfully authenticated, TokenAuthentication provides the following credentials.

request.user will be a Django User instance.
request.auth will be a rest_framework.authtoken.models.Token instance.
Unauthenticated responses that are denied permission will result in an HTTP 401 Unauthorized response with an appropriate WWW-Authenticate header. For example:

WWW-Authenticate: Token
The curl command line tool may be useful for testing token authenticated APIs. For example:

curl -X GET http://127.0.0.1:8000/api/example/ -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'
Note: If you use TokenAuthentication in production you must ensure that your API is only available over https.

Generating Tokens
By using signals
If you want every user to have an automatically generated Token, you can simply catch the User's post_save signal.

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
Note that you'll want to ensure you place this code snippet in an installed models.py module, or some other location that will be imported by Django on startup.

If you've already created some users, you can generate tokens for all existing users like this:

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

for user in User.objects.all():
    Token.objects.get_or_create(user=user)
By exposing an api endpoint
When using TokenAuthentication, you may want to provide a mechanism for clients to obtain a token given the username and password. REST framework provides a built-in view to provide this behavior. To use it, add the obtain_auth_token view to your URLconf:

from rest_framework.authtoken import views
                nav: nav.items
            }
        },
        computed: {
            // name () {
            //   return this.$route.name
            // },
            // list () {
            //   return this.$route.matched.filter((route) => route.name || route.meta.label )
            // }
        }
    }
</script>
