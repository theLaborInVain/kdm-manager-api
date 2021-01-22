"""

    This module is used to manage API documentation.


"""

# standard library imports
from bson import json_util
from collections import OrderedDict
import json
import types

# second party imports
import flask

# application imports
import app
from app import API, utils
from app.docs import public, private, sections


# set a constant of the modules we actual document in this module
DOCUMENTED_OBJECTS = [
    app.models.settlements.Settlement,
    app.models.survivors.Survivor,
    app.models.users.User,
]


class DocumentationObject:

    """ Initialize one of these to work with the documentation, e.g.
    D = DocumentationObject() or similar. """


    def __init__(self):
        """ Sets self.items dictionary. """

        self.logger = utils.get_logger(log_name='docs')

        self.docs = {}
        for module in [public, private]:
            self.set_docs_from_module(module)

        self.sections = sections.sections


    def set_docs_from_module(self, module):
        """ Creates an entry in the self.items dict for each item in
        'module'. Only goes one level deep. """

        for module_dict, v in module.__dict__.items():
            if isinstance(v, dict) and not module_dict.startswith('_'):
                for dict_key in sorted(v.keys()):

                    doc = v[dict_key]
                    doc['handle'] = dict_key
                    doc['type'] = module.__name__.split('.')[-1]
                    doc['section'] = module_dict

                    # set defaults
                    if 'subsection' not in doc.keys():
                        doc['subsection'] = '__main__'

                    if not 'key' in doc.keys():
                         doc['key'] = False

                    if not 'methods' in doc.keys():
                        doc['methods'] = API.config['DEFAULT_METHODS']

                    self.docs[dict_key] = doc


    def dump_sections(self, return_type=None):
        """ Dumps self.sections. """
        if return_type == 'JSON':
            return json.dumps(self.sections, default=json_util.default)
        return self.sections


    def get_documented_endpoints(self):
        """ Returns a set (unique list) of currently documented endpoints. """

        output = set()
        for doc_handle, doc in self.docs.items():
            output.add(doc['name'])
        return sorted(list(output))


    def get_endpoint(self, endpoint):
        """ Returns a self.items dict where the 'name' == 'endpoint'."""

        for doc_handle, doc in self.docs.items():
            if doc['name'] == endpoint:
                return self.docs[doc_handle]


    def get_sections(self, render_as=list, item_type=None):
        """ Returns a list of section handles used by items whose 'type' attrib
        matches 'item_type'. The list starts out as a set and is unique."""

        sections = set()
        for doc_handle, doc in self.docs.items():
            if item_type is not None:
                if doc['type'] == item_type:
                    sections.add(doc['section'])
            else:
                sections.add(doc['section'])

        if render_as == list:
            return sorted(list(sections))

        return sections


    def get_subsections(self, section=None):
        """ Returns a list of subsection handles found on docs whose section
        matches 'section'. """

        subsections = set()

        for doc_handle, doc in self.docs.items():
            if doc['section'] == section:
                subsections.add(doc['subsection'])

        return sorted(list(subsections))


    def get_undocumented_methods(self):
        """ loops through the models that we document and reports a list of ones
        who aren't included in self.get_documented_endpoints(). """

        # first, go through our documented objects, and get a dictionary of
        #   all non built-in methods:
        output = {}
        for documented_object in DOCUMENTED_OBJECTS:
            object_name = documented_object.__name__.lower()
            output[object_name] = {}
            for method_name in dir(documented_object):
                method = getattr(documented_object, method_name)
                m_type = type(method)
                if (
                    method_name[0:2] != '__' and m_type == types.FunctionType
                    and getattr(method, '_web_method', False)
                ):
                    output[object_name][method_name] = {}
                    for attr in dir(method):
                        if isinstance(getattr(method, attr), (str, bool)):
                            output[object_name][method_name][attr] = getattr(
                                method,
                                attr
                            )

        # now, go through our documented endpoints, and del the methods that
        #   we've already got documented
        for endpoint in self.get_documented_endpoints():
            try:
                collection, action = endpoint.split('/')[1:3]
                if collection in output.keys():
                    if action in output[collection].keys():
                        del output[collection][action]
            except ValueError:
                pass

        return json.dumps(output)


    def render_as_json(self):
        """ Spits out a JSON representation of the documentation library meant
        to be iterated and displayed, e.g. as HTML. """

        output = {}

        for item_type in ['public', 'private']:
            output[item_type] = OrderedDict()
            sections = self.get_sections(item_type=item_type)
            for section in sections:
                output[item_type][section] = OrderedDict()
                subsections = self.get_subsections(section)
                for subsection in subsections:
                    docs = []
                    for doc_handle in sorted(self.docs.keys()):
                        doc = self.docs[doc_handle]
                        if doc['section'] == section and doc['subsection'] ==\
                        subsection:
                            docs.append(doc)
                    output[item_type][section][subsection] = docs

        return json.dumps(output, default=json_util.default)


    def request_response(self, action=None):
        """ Similar to the method of the same name in the Settlement and
        Survivor objects: pass this one an action to get a flask response,
        which flask can then return via routes.py. """

        # default response
        json_response = flask.Response(
            response=self.render_as_json(),
            status=200,
            mimetype="application/json"
        )

        if action == 'sections':
            json_response.set_data(self.dump_sections('JSON'))
            return json_response

        # see if the 'action' is one of our methods, try to return it
        if getattr(self, action, None) is not None:
            json_response.set_data(getattr(self, action)())
            return json_response

        # finally, if we don't handle 'action', just return the default response
        return json_response
