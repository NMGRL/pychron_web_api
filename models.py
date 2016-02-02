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
from flask.ext.sqlalchemy import SQLAlchemy

from app import app
db = SQLAlchemy(app)


class AnalysisTbl(db.Model):
    __tablename__ = 'AnalysisTbl'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.TIMESTAMP)
    # tag = db.Column(db.String(45))
    uuid = db.Column(db.String(32))
    analysis_type = db.Column(db.String(45))
    aliquot = db.Column(db.Integer)
    increment = db.Column(db.Integer)

    irradiation_positionID = db.Column(db.Integer)

    measurementName = db.Column(db.String(45))
    extractionName = db.Column(db.String(45))
    postEqName = db.Column(db.String(45))
    postMeasName = db.Column(db.String(45))

    mass_spectrometer = db.Column(db.String(45))
    extract_device = db.Column(db.String(45))
    extract_value = db.Column(db.Float)
    extract_units = db.Column(db.String(45))
    cleanup = db.Column(db.Float)
    duration = db.Column(db.Float)

    weight = db.Column(db.Float)
    comment = db.Column(db.String(80))
    # repository_associations = relationship('RepositoryAssociationTbl', backref='analysis')
    # change = relationship('AnalysisChangeTbl', uselist=False, backref='analysis')
    # measured_position = relationship('MeasuredPositionTbl', uselist=False, backref='analysis')


# class Person(db.Model):
#     id = db.db.Column(db.db.Integer, primary_key=True)
#     first_name = db.db.Column(db.Text)
#     last_name = db.db.Column(db.Text)


# db.create_all()


# ============= EOF =============================================



