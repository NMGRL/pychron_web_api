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

app = Flask('flask_pychron')
uri = 'mysql+pymysql://root:Argon@localhost/pychrondvc_dev?connect_timeout=3'
app.config['SQLALCHEMY_DATABASE_URI'] = uri
# ============= EOF =============================================



