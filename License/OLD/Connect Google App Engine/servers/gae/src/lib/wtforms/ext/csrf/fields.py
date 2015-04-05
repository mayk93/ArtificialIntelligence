"""
Provides a `Field` to protect against csrf attacks.

Before using this form, you must set `wtforms.ext.csrf.secret.CSRF_KEY`.
If unset, `CsrfField` will throw an error.

Example usage::

    from wtforms import Form, TextField
    from wtforms.ext.csrf import CsrfField, secret
    from myapp import get_identifier
    
    secret.CSRF_KEY = 'reusing an example key would be silly'

    class SecureForm(Form):
        name = TextField()
        csrf = CsrfField(unique_userid=get_identifier)
    
Then, in your html form markup, include the csrf field as you would do
for any other field. When rendered, it will outup a hidden form field
where the value is a keyed hash of the unique_userid.
"""
import hmac
from wtforms.fields import HiddenField
from wtforms.ext.csrf import secret

class CsrfField(HiddenField):
    "Field to protect against csrf attacks."
    
    def __init__(self, unique_userid, **kwargs):
        """
        Construct a new CsrfField.

        :param unique_userid:
            A unique value representing something that identifies the user. It
            can be a session variable, a cookie value, an email, or some other
            identifier that uniquely identifies a user.
            
            The value can either be static (e.g. a string or int), or it can be
            a callable item. If you are going to reuse the form for multiple 
            requests or users, `unique_userid` **must** be a callable, or the 
            csrf token that is generated will be the same for every request.
        :param **kwargs:
            All other kwargs are the same as the Field class.
        """
        super(CsrfField, self).__init__(**kwargs)
        self._unique_userid = unique_userid
        
    def _csrf_value(self):
        "Returns the value to be displayed in forms and to be verified."
        if secret.CSRF_KEY is None:
            raise secret.UnsetCsrfKeyError('wtforms.ext.csrf.secret.CSRF_KEY'
                            ' must be set.')
        try:
            id = self._unique_userid()
        except TypeError:
            id = self._unique_userid
            
        return hmac.new(secret.CSRF_KEY, id).hexdigest()
        
    def _value(self):
        return self._csrf_value()
    
    def pre_validate(self, form):
        if self.data != self._csrf_value():
            raise ValueError(self.gettext(u'CSRF token is not valid.'))

    def populate_obj(self, obj, name):
        """Populates `obj.<name>` with the field's data if `obj.<name>` exists.
        
        Normally, this would set the value of the object or create `obj.<name>`
        if it doesn't exist, but in most cases we don't want to add the csrf
        value to the object.
        """
        if hasattr(obj, name):
            setattr(obj, name, self.data)
    