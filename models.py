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

from application import app

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

    irradiation_positionID = db.Column(db.Integer, db.ForeignKey('IrradiationPositionTbl.id'))
    iposition = db.relationship('IrradiationPositionTbl', backref=db.backref('analyses', lazy='dynamic'))

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


class IrradiationPositionTbl(db.Model):
    __tablename__ = 'IrradiationPositionTbl'
    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(80))
    sampleID = db.Column(db.Integer)
    levelID = db.Column(db.Integer, db.ForeignKey('LevelTbl.id'))
    position = db.Column(db.Integer)
    note = db.Column(db.BLOB)
    weight = db.Column(db.Float)
    j = db.Column(db.Float)
    j_err = db.Column(db.Float)


class IrradiationTbl(db.Model):
    __tablename__ = 'IrradiationTbl'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    levels = db.relationship('LevelTbl', backref='irradiation')


class LevelTbl(db.Model):
    __tablename__ = 'LevelTbl'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    irradiationID = db.Column(db.Integer, db.ForeignKey('IrradiationTbl.id'))
    productionID = db.Column(db.Integer, db.ForeignKey('ProductionTbl.id'))
    holder = db.Column(db.String(45))
    z = db.Column(db.Float)

    positions = db.relationship('IrradiationPositionTbl', backref='level')

    note = db.Column(db.BLOB)


class ProductionTbl(db.Model):
    __tablename__ = 'ProductionTbl'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    levels = db.relationship('LevelTbl', backref='production')


# ============= EOF =============================================
