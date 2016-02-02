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
from flask import render_template, Blueprint
# ============= local library imports  ==========================
docs = Blueprint('docs', __name__, template_folder='templates')


@docs.route("/v0/media/")
def media():
    return render_template('v0/media.html')


@docs.route("/v0/oauth/")
def oauth():
    return render_template('oauth.html')


@docs.route("/v0/oauth_authorizations/")
def oauth_authorizations():
    return render_template('oauth_authorizations.html')


@docs.route("/v0/auth/")
def auth():
    return render_template('auth.html')


@docs.route("/v0/troubleshooting/")
def troubleshooting():
    return render_template('troubleshooting.html')


@docs.route("/v0/versions/")
def versions():
    return render_template('versions.html')


@docs.route("/v0/activity/events/")
def activity_events():
    return render_template('activity_events.html')


@docs.route("/v0/activity/events/types/")
def activity_events_types():
    return render_template('activity_events_types.html')


@docs.route("/v0/activity/feeds/")
def activity_feeds():
    return render_template('activity_feeds.html')


@docs.route("/v0/activity/notifications/")
def activity_notifications():
    return render_template('activity_notifications.html')


@docs.route("/v0/activity/starring/")
def activity_starring():
    return render_template('activity_starring.html')


@docs.route("/v0/activity/watching/")
def activity_watching():
    return render_template('activity_watching.html')

# ============= EOF =============================================
