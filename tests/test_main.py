"""
Test for bug.
"""
from pygeos_macos_shapely_incompatibility import main

import geopandas as gpd
import pytest
from shapely.geometry import MultiPolygon, MultiLineString
from shapely.affinity import translate

TRACES = gpd.read_file("KB11/KB11_traces.geojson")
AREA = gpd.read_file("KB11/KB11_area.geojson")

MULTIPOLY = MultiPolygon([area for area in AREA.geometry.values])
SHIFTED_MULTIPOLY = translate(MULTIPOLY, xoff=30)
NEG_SHIFTED_MULTIPOLY = translate(MULTIPOLY, xoff=-30)
MULTIPOLY_TWICE = MultiPolygon([*NEG_SHIFTED_MULTIPOLY.geoms, *SHIFTED_MULTIPOLY.geoms])
MULTILINE_GDF = gpd.GeoDataFrame(
    geometry=[MultiLineString([trace for trace in TRACES.geometry.values])]
)
POLYGON = AREA.geometry.values[0]


@pytest.mark.parametrize(
    "area",
    [AREA, MULTIPOLY, MULTIPOLY_TWICE, POLYGON],
)
@pytest.mark.parametrize(
    "traces",
    [TRACES, MULTILINE_GDF],
)
@pytest.mark.parametrize(
    "keep_geom_type",
    [True, False],
)
@pytest.mark.parametrize(
    "strip_crs",
    [True, False],
)
def test_clip_bug(traces, area, keep_geom_type, strip_crs):
    if strip_crs:
        if isinstance(traces, gpd.GeoDataFrame):
            traces.crs = None
        if isinstance(area, gpd.GeoDataFrame):
            area.crs = None

    clipped = main.clip_bug(traces, area, keep_geom_type)

    assert isinstance(clipped, gpd.GeoDataFrame)
