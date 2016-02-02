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
# ============= local library imports  ==========================
from flask import render_template

from app import app
# from v0 import create_v0
# create_v0()

from blueprints.v0_docs import docs
app.register_blueprint(docs)

from api.v0_api import create_api
create_api(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api_info')
def api_info():
    return render_template('api_info.html')


if __name__ == '__main__':
    app.run(debug=True)

# ============= EOF =============================================
