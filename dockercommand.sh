docker run \
-it \
--name data-copier \
--network data-copier-nw \
--rm \
-v <host data source>:/retail_db_json \
data-copier \
python /data-copier/app/app.py departments,categories
