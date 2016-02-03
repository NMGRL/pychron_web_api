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
from flask.ext.restless import APIManager

# ============= local library imports  ==========================
from models import db, AnalysisTbl, IrradiationPositionTbl, IrradiationTbl, LevelTbl, ProductionTbl


def create_api(app):
    prefix = '/api/v0'

    api_manager = APIManager(app, flask_sqlalchemy_db=db)

    api = ((AnalysisTbl, 'analysis', {'methods': ['GET']}),
           (IrradiationPositionTbl, 'iposition', {'methods': ['GET']}),
           (IrradiationTbl, 'irradiation', {'methods': ['GET']}),
           (LevelTbl, 'level',  {'methods': ['GET']}),
           (ProductionTbl, 'production',  {'methods': ['GET']}))
    for table, cname, kw in api:
        api_manager.create_api(table, collection_name=cname, url_prefix=prefix,  **kw)

# ============= EOF =============================================
