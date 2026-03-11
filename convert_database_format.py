import argparse
import sys

import geopandas as gpd
import fiona
import json
import logging
from shapely.geometry import mapping

####This script is used to preprocess the data downloaded from the Minnesota Department of Transportation (MDoT), namely the National Truck Network based in Minnesota
def main(args):
    #print(args)
    logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))
    logging.getLogger().setLevel(logging.INFO)
    #path to esri file geodatabase (here: my downloads folder )
    #gdb_path ='/home/alexanderpetri/Downloads/fgdb_trans_federal_routes/trans_federal_routes.gdb'
    gdb_path = args.gdb_path #uses input file as command line argument
    logging.info(f"Loading file from {gdb_path}")
    layers = fiona.listlayers(gdb_path)#list all layers in the database (tables)
    logging.info(f"Available layers: {layers}")
    #read the esri database
    gdf = gpd.read_file(gdb_path, layer='National_Truck_Network_in_Minnesota')
    #print(gdf.head())
    #print(gdf.columns)
    #logging.info(f"Geometry column: {gdf.geometry.name}")
    #row_dict = gdf.iloc[1].to_dict()
    #for k, v in row_dict.items():
    #    print(f"{k}: {v}")
    #print(gdf.geom_type.value_counts())

    # Convert geometries to dicts that can easily be transferred into GeoJSON format
    gdf['geometry_geojson'] = gdf.geometry.apply(lambda geom: mapping(geom) if geom else None)

    # Keep only columns giving me the LRS information
    columns_to_keep = ['ROUTE_ID', 'FROM_MEASURE', 'TO_MEASURE', 'geometry_geojson']
    data = gdf[columns_to_keep].to_dict(orient='records')

    # Save as JSON
    with open('mndot_lrs.json', 'w') as f:
        json.dump(data, f)
    logging.info(f"Saved {len(data)} segments to mndot_lrs.json")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Conversion of an esri database into geojson format",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--gdb_path', type=str,required=True, help='Path to input database (.esri format)')
    args = parser.parse_args()

    main(args)
