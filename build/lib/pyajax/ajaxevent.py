"""
from pyajax import ajaxevent
config = [{
    'handler':{
        'event':{'url':'https://example.com/api','target':'html-id-of-button-or-anything','method':'click'},
        'input':{'query-param-1': 'html-id-of-input', 'query-parmam-2':'html-id-of-input'},
        'action':{'html-id-of-output-1':'json-element-1','html-id-of-output-2':'json-element-2'}
    }
}]
script = ajaxevent(config).buildscript()
return script
"""
class ajaxevent:
    def __init__(self, config):
        self.config = config
    
    def buildscript(self):
        script  = "<script type='text/javascript'>"
        script += "$(function() {"
        
        for callback in self.config:
            uinputs = list(("'%s': $('#%s').val()" % (key, val)) for key, val in callback['handler']['input'].items())
            actions = list(("$('#%s').html(response.%s);" % (key, val)) for key, val in callback['handler']['action'].items())
            
            script += """
            $('#%s').bind('%s', function() {
                $.getJSON('%s', %s).done(function(response){%s});
                return false;
            });
            """ % (callback['handler']['event']['target'], 
                   callback['handler']['event']['method'], 
                   callback['handler']['event']['url'],
                   "{"+",".join(uinputs)+"}",
                   "".join(actions))
        
        script += "});" 
        script += "</script>" 
        
        return script