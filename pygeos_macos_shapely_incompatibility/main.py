"""
Reproduce bug.
"""
import geopandas as gpd


def clip_bug(traces, area, keep_geom_type):

    clipped = gpd.clip(traces, area, keep_geom_type=keep_geom_type)

    assert clipped.shape[0] > 0

    return clipped
