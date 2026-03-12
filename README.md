# lrs_fastapi: A test project accessing and showing information for an esri geodataset

## Installation Guide <a name="installationguide"></a>
Clone the repository:<br />
`git clone git@github.com:aljpetri/lrs_fastapi.git`<br />
`cd lrs_fastapi`<br />

Create a virtual environment:<br />
`python -m venv venv`<br />
`source venv/bin/activate`<br />

Install dependencies:<br />
`pip install -r requirements.txt`<br />

## Converting an esri database you downloaded into GeoJSON:
`python convert_database_format.py --gdb_path [Path/To/Database/On/Your/System] `<br/>

## Web interface usage <a name="Web Interface "></a>
Start the fastapi server (development mode):<br />
`fastapi dev`<br />
Open the main page in your browser:<br />

`http://127.0.0.1:8000`<br />

The interface allows you to:<br />

List all routes<br />

Find segments by route and milepoint<br />


