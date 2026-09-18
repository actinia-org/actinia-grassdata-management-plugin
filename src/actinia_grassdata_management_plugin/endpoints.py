#!/usr/bin/env python
"""Copyright (c) 2018-2025 mundialis GmbH & Co. KG.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Add endpoints to flask app with endpoint definitions and routes
"""

__license__ = "GPLv3"
__author__ = "Carmen Tawalika, Anika Weinmann"
__copyright__ = "Copyright 2022-2024 mundialis GmbH & Co. KG"
__maintainer__ = "mundialis GmbH & Co. KG"

from flask_restful_swagger_2 import Api, Resource

from actinia_grassdata_management_plugin.rest.map_layer_management import (
    RasterLayersResource,
)
from actinia_grassdata_management_plugin.rest.map_layer_management import (
    VectorLayersResource,
)
from actinia_grassdata_management_plugin.rest.raster_colors import (
    SyncPersistentRasterColorsResource,
)
from actinia_grassdata_management_plugin.rest.raster_layer import (
    RasterLayerResource,
)
from actinia_grassdata_management_plugin.rest.raster_legend import (
    SyncEphemeralRasterLegendResource,
)
from actinia_grassdata_management_plugin.rest.raster_renderer import (
    SyncEphemeralRasterRendererResource,
)
from actinia_grassdata_management_plugin.rest.raster_renderer import (
    SyncEphemeralRasterRGBRendererResource,
)
from actinia_grassdata_management_plugin.rest.raster_renderer import (
    SyncEphemeralRasterShapeRendererResource,
)
from actinia_grassdata_management_plugin.rest.strds_management import (
    STRDSManagementResource,
    SyncSTRDSListerResource,
)
from actinia_grassdata_management_plugin.rest.strds_raster_management import (
    STRDSRasterManagement,
)
from actinia_grassdata_management_plugin.rest.strds_renderer import (
    SyncEphemeralSTRDSRendererResource,
)
from actinia_grassdata_management_plugin.rest.vector_layer import (
    VectorLayerResource,
)
from actinia_grassdata_management_plugin.rest.vector_renderer import (
    SyncEphemeralVectorRendererResource,
)


def get_endpoint_class_name(endpoint_class: Resource) -> str:
    """Create the name for the given endpoint class."""
    return endpoint_class.__name__.lower()


def create_project_endpoints(flask_api: Api) -> None:
    """Add resources with "project" inside the endpoint url to the api.

    Args:
        apidoc (Api): Flask api.
    """
    # Raster management
    flask_api.add_resource(
        RasterLayersResource,
        "/projects/<string:project_name>/mapsets/"
        "<string:mapset_name>/raster_layers",
        "/locations/<string:project_name>/mapsets/"
        "<string:mapset_name>/raster_layers",
        endpoint=get_endpoint_class_name(RasterLayersResource),
    )
    flask_api.add_resource(
        RasterLayerResource,
        "/projects/<string:project_name>/mapsets/"
        "<string:mapset_name>/raster_layers/<string:raster_name>",
        "/locations/<string:project_name>/mapsets/"
        "<string:mapset_name>/raster_layers/<string:raster_name>",
        endpoint=get_endpoint_class_name(RasterLayerResource),
    )
    flask_api.add_resource(
        SyncEphemeralRasterLegendResource,
        "/projects/<string:project_name>/mapsets/"
        "<string:mapset_name>/raster_layers/<string:raster_name>/legend",
        "/locations/<string:project_name>/mapsets/"
        "<string:mapset_name>/raster_layers/<string:raster_name>/legend",
        endpoint=get_endpoint_class_name(SyncEphemeralRasterLegendResource),
    )
    flask_api.add_resource(
        SyncPersistentRasterColorsResource,
        "/projects/<string:project_name>/mapsets/"
        "<string:mapset_name>/raster_layers/<string:raster_name>/colors",
        "/locations/<string:project_name>/mapsets/"
        "<string:mapset_name>/raster_layers/<string:raster_name>/colors",
        endpoint=get_endpoint_class_name(SyncPersistentRasterColorsResource),
    )
    flask_api.add_resource(
        SyncEphemeralRasterRendererResource,
        "/projects/<string:project_name>/mapsets/"
        "<string:mapset_name>/raster_layers/<string:raster_name>/render",
        "/locations/<string:project_name>/mapsets/"
        "<string:mapset_name>/raster_layers/<string:raster_name>/render",
        endpoint=get_endpoint_class_name(SyncEphemeralRasterRendererResource),
    )
    flask_api.add_resource(
        SyncEphemeralRasterRGBRendererResource,
        "/projects/<string:project_name>/mapsets/"
        "<string:mapset_name>/render_rgb",
        "/locations/<string:project_name>/mapsets/"
        "<string:mapset_name>/render_rgb",
        endpoint=get_endpoint_class_name(
            SyncEphemeralRasterRGBRendererResource
        ),
    )
    flask_api.add_resource(
        SyncEphemeralRasterShapeRendererResource,
        "/projects/<string:project_name>/mapsets/"
        "<string:mapset_name>/render_shade",
        "/locations/<string:project_name>/mapsets/"
        "<string:mapset_name>/render_shade",
        endpoint=get_endpoint_class_name(
            SyncEphemeralRasterShapeRendererResource
        ),
    )
    # STRDS management
    flask_api.add_resource(
        SyncSTRDSListerResource,
        "/projects/<string:project_name>/mapsets/"
        "<string:mapset_name>/strds",
        "/locations/<string:project_name>/mapsets/"
        "<string:mapset_name>/strds",
        endpoint=get_endpoint_class_name(SyncSTRDSListerResource),
    )
    flask_api.add_resource(
        STRDSManagementResource,
        "/projects/<string:project_name>/mapsets/"
        "<string:mapset_name>/strds/<string:strds_name>",
        "/locations/<string:project_name>/mapsets/"
        "<string:mapset_name>/strds/<string:strds_name>",
        endpoint=get_endpoint_class_name(STRDSManagementResource),
    )
    flask_api.add_resource(
        STRDSRasterManagement,
        "/projects/<string:project_name>/mapsets/"
        "<string:mapset_name>/strds/<string:strds_name>/raster_layers",
        "/locations/<string:project_name>/mapsets/"
        "<string:mapset_name>/strds/<string:strds_name>/raster_layers",
        endpoint=get_endpoint_class_name(STRDSRasterManagement),
    )
    # Vector management
    flask_api.add_resource(
        VectorLayersResource,
        "/projects/<string:project_name>/mapsets/"
        "<string:mapset_name>/vector_layers",
        "/locations/<string:project_name>/mapsets/"
        "<string:mapset_name>/vector_layers",
        endpoint=get_endpoint_class_name(VectorLayersResource),
    )
    flask_api.add_resource(
        VectorLayerResource,
        "/projects/<string:project_name>/mapsets/"
        "<string:mapset_name>/vector_layers/<string:vector_name>",
        "/locations/<string:project_name>/mapsets/"
        "<string:mapset_name>/vector_layers/<string:vector_name>",
        endpoint=get_endpoint_class_name(VectorLayerResource),
    )
    flask_api.add_resource(
        SyncEphemeralVectorRendererResource,
        "/projects/<string:project_name>/mapsets/"
        "<string:mapset_name>/vector_layers/<string:vector_name>/render",
        "/locations/<string:project_name>/mapsets/"
        "<string:mapset_name>/vector_layers/<string:vector_name>/render",
        endpoint=get_endpoint_class_name(SyncEphemeralVectorRendererResource),
    )
    flask_api.add_resource(
        SyncEphemeralSTRDSRendererResource,
        "/projects/<string:project_name>/mapsets/"
        "<string:mapset_name>/strds/<string:strds_name>/render",
        "/locations/<string:project_name>/mapsets/"
        "<string:mapset_name>/strds/<string:strds_name>/render",
        endpoint=get_endpoint_class_name(SyncEphemeralSTRDSRendererResource),
    )


#  endpoints loaded if run as actinia-core plugin as well as standalone app
def create_endpoints(flask_api: Api) -> None:
    """Create plugin endpoints."""

    # add deprecated location endpoints
    create_project_endpoints(flask_api)
