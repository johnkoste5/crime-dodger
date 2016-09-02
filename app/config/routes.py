"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

"""
    This is where you define routes

    Start by defining the default controller
    Pylot will look for the index method in the default controller to handle the base route

    Pylot will also automatically generate routes that resemble: '/controller/method/parameters'
    For example if you had a products controller with an add method that took one parameter
    named id the automatically generated url would be '/products/add/<id>'
    The automatically generated routes respond to all of the http verbs (GET, POST, PUT, PATCH, DELETE)
"""
routes['default_controller'] = 'Welcome'
routes['/crimes'] = 'Crimes#index'
routes['/login'] = 'Users#login'
routes['/logout'] = 'Users#logout'
routes['/splash'] = 'Users#splash'
routes['/users/<id>'] = 'Users#profile'
routes['/update_favorites/<id>'] = 'Favorites#edit'
routes['/delete_favorites/<id>'] = 'Favorites#delete'
routes['/confrim_delete/<id>'] = 'Favorites#confirm_delete'

routes['POST']['/confirm_edit/<id>'] = 'Favorites#confirm_edit'


routes['POST']['/users/<id>/add'] = 'Users#add'
routes['POST']['/users/create'] = 'Users#create'
routes['POST']['/users/login'] = 'Users#check_login'
routes['/delete_page/<id>'] = 'Favorites#delete_page'
routes['/edit_page/<id>'] = 'Favorites#edit_page'
 

routes['/jquery'] = 'Crimes#jquery'
routes['/marker'] = 'Crimes#marker'
routes['/marker2'] = 'Crimes#marker2'
routes['/directions'] = 'Crimes#directions'
routes['/directions2'] = 'Crimes#directions2'
# routes['/jsondata'] = 'Crimes#createMapData'
"""
    You can add routes and specify their handlers as follows:

    routes['VERB']['/URL/GOES/HERE'] = 'Controller#method'

    Note the '#' symbol to specify the controller method to use.
    Note the preceding slash in the url.
    Note that the http verb must be specified in ALL CAPS.

    If the http verb is not provided pylot will assume that you want the 'GET' verb.

    You can also use route parameters by using the angled brackets like so:
    routes['PUT']['/users/<int:id>'] = 'users#update'

    Note that the parameter can have a specified type (int, string, float, path).
    If the type is not specified it will default to string

    Here is an example of the restful routes for users:

    routes['GET']['/users'] = 'users#index'
    routes['GET']['/users/new'] = 'users#new'
    routes['POST']['/users'] = 'users#create'
    routes['GET']['/users/<int:id>'] = 'users#show'
    routes['GET']['/users/<int:id>/edit' = 'users#edit'
    routes['PATCH']['/users/<int:id>'] = 'users#update'
    routes['DELETE']['/users/<int:id>'] = 'users#destroy'
"""
