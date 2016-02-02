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

app = Flask('pychron_web_api')


user = getenv('ARGONSERVER_DB_USER')
pwd = getenv('ARGONSERVER_DB_PWD')
host = getenv('ARGONSERVER_HOST')
name = 'pychrondvc'

uri = 'mysql+pymysql://{}:{}@{}/{}?connect_timeout=3'.format(user, pwd, host, name)
app.config['SQLALCHEMY_DATABASE_URI'] = uri

# ============= EOF =============================================



