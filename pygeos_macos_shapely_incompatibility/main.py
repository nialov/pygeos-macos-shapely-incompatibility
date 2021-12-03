"""
Reproduce bug.
"""
import geopandas as gpd


def clip_bug():
    traces = gpd.read_file("KB11/KB11_traces.geojson")
    area = gpd.read_file("KB11/KB11_area.geojson")

    clipped = gpd.clip(traces, area)

    return clipped
