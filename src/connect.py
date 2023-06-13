from databricks_api import DatabricksAPI

# Provide a host and token
db = DatabricksAPI(
    host="https://adb-7772147484121042.2.azuredatabricks.net",
    token="dapif71015e730f71f5e672c5dac3024d8ec"
)
db.cluster.pin_cluster(
    "0531-100622-mon30k1x",
    headers=None,
)
jobs_list = db.jobs.list_jobs(
    job_type=None,
    expand_tasks=None,
    limit=None,
    offset=None,
    headers=None,
    version=None,
)
print("Job name:- Job ID")

for job in jobs_list['jobs']:
  print(f"{job['job_name']}: {job['job_id']}")
  # print(f"{job['job_id']}")


clusters_list = db.cluster.list_clusters(headers=None)
print("Cluster name, cluster ID")

for cluster in clusters_list['clusters']:
  print(f"{cluster['cluster_name']}, {cluster['cluster_id']}")
