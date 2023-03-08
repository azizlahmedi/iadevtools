# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin

import neoxam.adltrack.urls
import neoxam.backport.urls
import neoxam.champagne.urls
import neoxam.commons.urls
import neoxam.delivery.urls
import neoxam.eclipse.urls
import neoxam.factory_app.urls
import neoxam.gpatcher.urls
import neoxam.harry.urls
import neoxam.initial.urls
import neoxam.scrumcards.urls
import neoxam.scrumreport.urls
import neoxam.versioning.urls
import neoxam.webintake.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^scrumcards/', include(neoxam.scrumcards.urls)),
    url(r'^scrumreport/', include(neoxam.scrumreport.urls)),
    url(r'^adltrack/', include(neoxam.adltrack.urls)),
    url(r'^factory/', include(neoxam.factory_app.urls)),
    url(r'^backport/', include(neoxam.backport.urls)),
    url(r'^gpatcher/', include(neoxam.gpatcher.urls)),
    url(r'^initial/', include(neoxam.initial.urls)),
    url(r'^harry/', include(neoxam.harry.urls)),
    url(r'^webintake/', include(neoxam.webintake.urls)),
    url(r'^versioning/', include(neoxam.versioning.urls)),
    url(r'^champagne/', include(neoxam.champagne.urls)),
    url(r'^eclipse/', include(neoxam.eclipse.urls)),
    url(r'^delivery/', include(neoxam.delivery.urls)),
    url(r'^', include(neoxam.commons.urls)),
]
