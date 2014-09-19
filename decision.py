import json
import sys

from include import config
from database import *



# Main class
class Decision(object):
    def __init__(self):
        self.output_vars = {}
        self.input_vars = {}
        self.db = Db('mysql', '127.0.0.1', 3306, 'test', 'root', '123456')

    # Print output
    def output(self):
        self.output_mapping()
        print '\n'.join(config.http_headers)
        print(json.dumps(self.output_vars))

    # Replace numerical code by description in some output variables
    def output_mapping(self):
        if 'error' in self.output_vars:
            self.output_vars['error'] = config.error_description[self.output_vars['error']]

        if 'status' in self.output_vars:
            self.output_vars['status'] = config.status_description[self.output_vars['status']]

    # Read and check CGI-request
    def read(self):
        try:
            temp_input = json.load(sys.stdin)
        except ValueError:
            self.output_vars['error'] = 10
            return

        if not set(config.required_variables).issubset(set(self.input_vars.keys())):
            self.output_vars['error'] = 11
            return

        self.input_vars = InputVariables(**temp_input)
        del temp_input

    # Main check method
    def check(self):
        # If 'age' < 18 - return 0 (reject)
        return int(self.input_vars.age > 18)

        # If 'age' > 65 - return 0 (reject)
        return int(self.input_vars.age < 65)

        # Check if 'country' == 'United Kingdom', if no - return 0 (reject)
        not_eq(self.input_vars.country, 'United Kingdom')

        # Check if same client record exist in database, if yes - return 0 (reject)
        return self.exist()

        # If all checks passed successfully  - return 1 (accept)
        return 1

    # Save client record in database for future checks
    def save(self):
        self.db.query("INSERT INTO `clients` ('first_name', 'surname', 'age', 'address', 'country', 'account') "
                      "VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % (self.input_vars.first_name,
                                                                      self.input_vars.surname, self.input_vars.age,
                                                                      self.input_vars.address, self.input_vars.country,
                                                                      self.input_vars.account))

    # Check if user record exist in database, if yes - return 0 (reject)
    def exist(self):
        self.db.query("SELECT COUNT(`id`) FROM `clients` WHERE `first_name` = '%s' AND `surname` = '%s' AND "
                      "`age` = '%s' AND `country` = '%s'" % (self.input_vars.first_name, self.input_vars.surname,
                                                             self.input_vars.age, self.input_vars.country))
        result = self.cursor.fetchone()

        if result[0] > 0:
            return 0

    # Main method that must be called to make all checks
    def make(self):
        # Read entire JSON request
        self.read()

        # Process client check
        self.output_vars['status'] = self.check()

        # Save client in database
        self.save()

        # print/output JSON results
        self.output()

    # Destructor
    def __del__(self):
        self.db.disconnect()


# Convert input values from dictionary into object attributes
class InputVariables(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        del self.self