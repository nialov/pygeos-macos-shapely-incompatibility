"""
Test for bug.
"""
from pygeos_macos_shapely_incompatibility import main

import geopandas as gpd


def test_clip_bug():

    clipped = main.clip_bug()

    assert isinstance(clipped, gpd.GeoDataFrame)
