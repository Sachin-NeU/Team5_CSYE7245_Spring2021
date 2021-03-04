import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
## @type: DataSource
## @args: [format_options = {"quoteChar":"\"","withHeader":True,"separator":",","multiline":True}, connection_type = "s3", format = "csv", connection_options = {"paths": ["s3://sevir/CATALOG.csv"]}, transformation_ctx = "DataSource0"]
## @return: DataSource0
## @inputs: []
DataSource0 = glueContext.create_dynamic_frame.from_options(format_options = {"quoteChar":"\"","withHeader":True,"separator":",","multiline":True}, connection_type = "s3", format = "csv", connection_options = {"paths": ["s3://sevir/CATALOG.csv"]}, transformation_ctx = "DataSource0")
## @type: SelectFields
## @args: [paths = ["id", "event_id", "file_name", "file_index", "img_type", "time_utc", "minute_offsets", "episode_id", "event_type", "llcrnrlat", "llcrnrlon", "urcrnrlat", "urcrnrlon", "proj", "size_x", "size_y", "height_m", "width_m", "data_min", "data_max", "pct_missing"], transformation_ctx = "Transform2"]
## @return: Transform2
## @inputs: [frame = DataSource0]
Transform2 = SelectFields.apply(frame = DataSource0, paths = ["id", "event_id", "file_name", "file_index", "img_type", "time_utc", "minute_offsets", "episode_id", "event_type", "llcrnrlat", "llcrnrlon", "urcrnrlat", "urcrnrlon", "proj", "size_x", "size_y", "height_m", "width_m", "data_min", "data_max", "pct_missing"], transformation_ctx = "Transform2")
## @type: DataSource
## @args: [format_options = {"withHeader":True,"separator":",","quoteChar":"\""}, connection_type = "s3", format = "csv", connection_options = {"paths": ["s3://myfirstbucketadwait/storminput/StormEvents_locations.csv"]}, transformation_ctx = "DataSource3"]
## @return: DataSource3
## @inputs: []
DataSource3 = glueContext.create_dynamic_frame.from_options(format_options = {"withHeader":True,"separator":",","quoteChar":"\""}, connection_type = "s3", format = "csv", connection_options = {"paths": ["s3://myfirstbucketadwait/storminput/StormEvents_locations.csv"]}, transformation_ctx = "DataSource3")
## @type: SelectFields
## @args: [paths = ["YEARMONTH", "EPISODE_ID", "EVENT_ID", "LOCATION_INDEX", "RANGE", "AZIMUTH", "LOCATION", "LATITUDE", "LONGITUDE", "LAT2", "LON2"], transformation_ctx = "Transform0"]
## @return: Transform0
## @inputs: [frame = DataSource3]
Transform0 = SelectFields.apply(frame = DataSource3, paths = ["YEARMONTH", "EPISODE_ID", "EVENT_ID", "LOCATION_INDEX", "RANGE", "AZIMUTH", "LOCATION", "LATITUDE", "LONGITUDE", "LAT2", "LON2"], transformation_ctx = "Transform0")
## @type: DataSource
## @args: [format_options = {"withHeader":True,"separator":",","quoteChar":"\""}, connection_type = "s3", format = "csv", connection_options = {"paths": ["s3://myfirstbucketadwait/storminput/StormEvents_fatalities.csv"]}, transformation_ctx = "DataSource2"]
## @return: DataSource2
## @inputs: []
DataSource2 = glueContext.create_dynamic_frame.from_options(format_options = {"withHeader":True,"separator":",","quoteChar":"\""}, connection_type = "s3", format = "csv", connection_options = {"paths": ["s3://myfirstbucketadwait/storminput/StormEvents_fatalities.csv"]}, transformation_ctx = "DataSource2")
## @type: SelectFields
## @args: [paths = ["EVENT_ID", "FATALITY_ID", "FAT_YEARMONTH", "FAT_DAY", "FAT_TIME", "FATALITY_TYPE", "FATALITY_DATE", "FATALITY_AGE", "FATALITY_SEX", "FATALITY_LOCATION", "EVENT_YEARMONTH"], transformation_ctx = "Transform5"]
## @return: Transform5
## @inputs: [frame = DataSource2]
Transform5 = SelectFields.apply(frame = DataSource2, paths = ["EVENT_ID", "FATALITY_ID", "FAT_YEARMONTH", "FAT_DAY", "FAT_TIME", "FATALITY_TYPE", "FATALITY_DATE", "FATALITY_AGE", "FATALITY_SEX", "FATALITY_LOCATION", "EVENT_YEARMONTH"], transformation_ctx = "Transform5")
## @type: Join
## @args: [columnConditions = ["="], joinType = left, keys2 = ["EVENT_ID"], keys1 = ["event_id"], transformation_ctx = "Transform7"]
## @return: Transform7
## @inputs: [frame1 = Transform2, frame2 = Transform5]
Transform2DF = Transform2.toDF()
Transform5DF = Transform5.toDF()
Transform7 = DynamicFrame.fromDF(Transform2DF.join(Transform5DF, (Transform2DF['event_id'] == Transform5DF['EVENT_ID']), "left"), glueContext, "Transform7")
## @type: SelectFields
## @args: [paths = ["id", "file_name", "event_id", "FAT_YEARMONTH", "FATALITY_ID", "file_index", "img_type", "time_utc", "minute_offsets", "episode_id", "event_type", "llcrnrlat", "llcrnrlon", "urcrnrlat", "urcrnrlon", "proj", "size_x", "size_y", "height_m", "width_m", "data_min", "data_max", "pct_missing", "FAT_DAY", "FAT_TIME", "FATALITY_TYPE", "FATALITY_DATE", "FATALITY_AGE", "FATALITY_SEX", "FATALITY_LOCATION", "EVENT_YEARMONTH"], transformation_ctx = "Transform1"]
## @return: Transform1
## @inputs: [frame = Transform7]
Transform1 = SelectFields.apply(frame = Transform7, paths = ["id", "file_name", "event_id", "FAT_YEARMONTH", "FATALITY_ID", "file_index", "img_type", "time_utc", "minute_offsets", "episode_id", "event_type", "llcrnrlat", "llcrnrlon", "urcrnrlat", "urcrnrlon", "proj", "size_x", "size_y", "height_m", "width_m", "data_min", "data_max", "pct_missing", "FAT_DAY", "FAT_TIME", "FATALITY_TYPE", "FATALITY_DATE", "FATALITY_AGE", "FATALITY_SEX", "FATALITY_LOCATION", "EVENT_YEARMONTH"], transformation_ctx = "Transform1")
## @type: Join
## @args: [columnConditions = ["="], joinType = left, keys2 = ["EVENT_ID"], keys1 = ["event_id"], transformation_ctx = "Transform8"]
## @return: Transform8
## @inputs: [frame1 = Transform1, frame2 = Transform0]
Transform1DF = Transform1.toDF()
Transform0DF = Transform0.toDF()
Transform8 = DynamicFrame.fromDF(Transform1DF.join(Transform0DF, (Transform1DF['event_id'] == Transform0DF['EVENT_ID']), "left"), glueContext, "Transform8")
## @type: SelectFields
## @args: [paths = ["id", "file_name", "event_id", "FAT_YEARMONTH", "FATALITY_ID", "YEARMONTH", "EPISODE_ID", "LOCATION_INDEX", "RANGE", "AZIMUTH", "LOCATION", "LATITUDE", "LONGITUDE", "LAT2", "LON2", "file_index", "img_type", "time_utc", "minute_offsets", "episode_id", "event_type", "llcrnrlat", "llcrnrlon", "urcrnrlat", "urcrnrlon", "proj", "size_x", "size_y", "height_m", "width_m", "data_min", "data_max", "pct_missing", "FAT_DAY", "FAT_TIME", "FATALITY_TYPE", "FATALITY_DATE", "FATALITY_AGE", "FATALITY_SEX", "FATALITY_LOCATION", "EVENT_YEARMONTH"], transformation_ctx = "Transform6"]
## @return: Transform6
## @inputs: [frame = Transform8]
Transform6 = SelectFields.apply(frame = Transform8, paths = ["id", "file_name", "event_id", "FAT_YEARMONTH", "FATALITY_ID", "YEARMONTH", "EPISODE_ID", "LOCATION_INDEX", "RANGE", "AZIMUTH", "LOCATION", "LATITUDE", "LONGITUDE", "LAT2", "LON2", "file_index", "img_type", "time_utc", "minute_offsets", "episode_id", "event_type", "llcrnrlat", "llcrnrlon", "urcrnrlat", "urcrnrlon", "proj", "size_x", "size_y", "height_m", "width_m", "data_min", "data_max", "pct_missing", "FAT_DAY", "FAT_TIME", "FATALITY_TYPE", "FATALITY_DATE", "FATALITY_AGE", "FATALITY_SEX", "FATALITY_LOCATION", "EVENT_YEARMONTH"], transformation_ctx = "Transform6")
## @type: DataSource
## @args: [format_options = {"withHeader":True,"separator":",","quoteChar":"\""}, connection_type = "s3", format = "csv", connection_options = {"paths": ["s3://myfirstbucketadwait/storminput/StormEvents_details.csv"]}, transformation_ctx = "DataSource1"]
## @return: DataSource1
## @inputs: []
DataSource1 = glueContext.create_dynamic_frame.from_options(format_options = {"withHeader":True,"separator":",","quoteChar":"\""}, connection_type = "s3", format = "csv", connection_options = {"paths": ["s3://myfirstbucketadwait/storminput/StormEvents_details.csv"]}, transformation_ctx = "DataSource1")
## @type: SelectFields
## @args: [paths = ["BEGIN_YEARMONTH", "BEGIN_DAY", "BEGIN_TIME", "END_YEARMONTH", "END_DAY", "END_TIME", "EPISODE_ID", "EVENT_ID", "STATE", "STATE_FIPS", "YEAR", "MONTH_NAME", "EVENT_TYPE", "CZ_TYPE", "CZ_FIPS", "CZ_NAME", "WFO", "BEGIN_DATE_TIME", "CZ_TIMEZONE", "END_DATE_TIME", "INJURIES_DIRECT", "INJURIES_INDIRECT", "DEATHS_DIRECT", "DEATHS_INDIRECT", "DAMAGE_PROPERTY", "DAMAGE_CROPS", "SOURCE", "MAGNITUDE", "MAGNITUDE_TYPE", "FLOOD_CAUSE", "CATEGORY", "TOR_F_SCALE", "TOR_LENGTH", "TOR_WIDTH", "TOR_OTHER_WFO", "TOR_OTHER_CZ_STATE", "TOR_OTHER_CZ_FIPS", "TOR_OTHER_CZ_NAME", "BEGIN_RANGE", "BEGIN_AZIMUTH", "BEGIN_LOCATION", "END_RANGE", "END_AZIMUTH", "END_LOCATION", "BEGIN_LAT", "BEGIN_LON", "END_LAT", "END_LON", "EPISODE_NARRATIVE", "EVENT_NARRATIVE", "DATA_SOURCE"], transformation_ctx = "Transform3"]
## @return: Transform3
## @inputs: [frame = DataSource1]
Transform3 = SelectFields.apply(frame = DataSource1, paths = ["BEGIN_YEARMONTH", "BEGIN_DAY", "BEGIN_TIME", "END_YEARMONTH", "END_DAY", "END_TIME", "EPISODE_ID", "EVENT_ID", "STATE", "STATE_FIPS", "YEAR", "MONTH_NAME", "EVENT_TYPE", "CZ_TYPE", "CZ_FIPS", "CZ_NAME", "WFO", "BEGIN_DATE_TIME", "CZ_TIMEZONE", "END_DATE_TIME", "INJURIES_DIRECT", "INJURIES_INDIRECT", "DEATHS_DIRECT", "DEATHS_INDIRECT", "DAMAGE_PROPERTY", "DAMAGE_CROPS", "SOURCE", "MAGNITUDE", "MAGNITUDE_TYPE", "FLOOD_CAUSE", "CATEGORY", "TOR_F_SCALE", "TOR_LENGTH", "TOR_WIDTH", "TOR_OTHER_WFO", "TOR_OTHER_CZ_STATE", "TOR_OTHER_CZ_FIPS", "TOR_OTHER_CZ_NAME", "BEGIN_RANGE", "BEGIN_AZIMUTH", "BEGIN_LOCATION", "END_RANGE", "END_AZIMUTH", "END_LOCATION", "BEGIN_LAT", "BEGIN_LON", "END_LAT", "END_LON", "EPISODE_NARRATIVE", "EVENT_NARRATIVE", "DATA_SOURCE"], transformation_ctx = "Transform3")
## @type: Join
## @args: [columnConditions = ["="], joinType = right, keys2 = ["event_id"], keys1 = ["EVENT_ID"], transformation_ctx = "Transform4"]
## @return: Transform4
## @inputs: [frame1 = Transform3, frame2 = Transform6]
Transform3DF = Transform3.toDF()
Transform6DF = Transform6.toDF()
Transform4 = DynamicFrame.fromDF(Transform3DF.join(Transform6DF, (Transform3DF['EVENT_ID'] == Transform6DF['event_id']), "right"), glueContext, "Transform4")
## @type: DataSink
## @args: [connection_type = "s3", format = "csv", connection_options = {"path": "s3://myfirstbucketadwait/stormoutput/", "partitionKeys": []}, transformation_ctx = "DataSink0"]
## @return: DataSink0
## @inputs: [frame = Transform4]
DataSink0 = glueContext.write_dynamic_frame.from_options(frame = Transform4, connection_type = "s3", format = "csv", connection_options = {"path": "s3://myfirstbucketadwait/stormoutput/", "partitionKeys": []}, transformation_ctx = "DataSink0")
job.commit()