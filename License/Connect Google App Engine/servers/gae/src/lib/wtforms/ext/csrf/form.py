"""Form that automatically includes a `CsrfField`.

Example usage::

    from wtforms import TextField
    from wtforms.ext.csrf import CsrfForm, secret
    from myapp import get_identifier
    
    # Your app should set this value once, probably with other 
    # config settings.
    secret.CSRF_KEY = 'reusing an example key would be silly'

    class SecureForm(CsrfForm):
        name = TextField()

    form = SecureForm(unique_userid=get_identifier)
    
Now, ```form`` has a field ``form.csrf`` that needs to be included in the 
form output (just like other fields) and will be verified on 
``form.validate()``.
"""
from wtforms.form import Form
from wtforms.ext.csrf.fields import CsrfField


class CsrfForm(Form):
    """
    Form that automatically includes a `CsrfField`.
    
    This form is mainly intended for convenience so that you don't accidentally
    forget to include a `CsrfField` in a form. However, it is still your 
    responsibility to include the widget output in the form. If you forget,
    the form will throw errors when you try to validate (as you would expect).    
    """
    
    def __init__(self, unique_userid, formdata=None, obj=None, prefix='',
                 csrf_field_name='csrf', **kwargs):
        """
        Create the CsrfForm.
        
        :param unique_userid:
            A unique id that you can tie to a user. See the documentation on 
            `CsrfField.__init__()` for further details.
            
            If unique_userid is a constant (i.e. not a callable), you **must** 
            regenerate the form on each request. Otherwise, the csrf value
            will be the same for each user / request.
        :parm csrf_field_name:
            By default, the csrf field will be named 'csrf'. You can override 
            the default with this parameter.
        """
        unbound = CsrfField(unique_userid)
        self._unbound_fields.append((csrf_field_name, unbound))
        super(CsrfForm, self).__init__(formdata=formdata, obj=obj, 
                                       prefix=prefix, **kwargs)
        self._unbound_fields.remove((csrf_field_name, unbound))
