# ===============================================================================
# Copyright 2015 Jake Ross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================

# ============= enthought library imports =======================
# ============= standard library imports ========================
from flask import Flask
# ============= local library imports  ==========================
from os import getenv


class PychronWebAPIApp(Flask):
    def __init__(self, *args, **kw):
        super(PychronWebAPIApp, self).__init__(*args, **kw)

        self.jinja_options = dict(Flask.jinja_options)
        self.jinja_options['extensions'] = ['jinja2_highlight.HighlightExtension']

app = PychronWebAPIApp('pychron_web_api')

use_local = int(getenv('USE_LOCAL', 0))
if use_local:
    user = getenv('LOCALHOST_DB_USER')
    pwd = getenv('LOCALHOST_DB_PWD')
    host = 'localhost'
    name = 'pychrondvc_dev'
else:
    user = getenv('ARGONSERVER_DB_USER')
    pwd = getenv('ARGONSERVER_DB_PWD')
    host = getenv('ARGONSERVER_HOST')
    name = 'pychrondvc'

uri = 'mysql+pymysql://{0}:{1}@{2}/{3}?connect_timeout=3'.format(user, pwd, host, name)
app.config['SQLALCHEMY_DATABASE_URI'] = uri

# ============= EOF =============================================
