from databricks_api import DatabricksAPI

# Provide a host and token
db = DatabricksAPI(
    host="https://adb-1710922579126448.8.azuredatabricks.net",
    token="dapid24a84b27054a5fccabc962278928be0-3"
)
db.cluster.pin_cluster(
    "0531-100622-mon30k1x",
    headers=None,
)
jobs_list = db.jobs.list_jobs()
print("Job ID")

for job in jobs_list['jobs']:
  #print(f"{job.settings['job_name']}: {job['job_id']}")
   print(f"{job['job_id']}")

#db.jobs.run_now(
#    job_id="60062762225560"
#)

db.jobs.delete_job(
    "2079532391229" ,
    headers=None,
    version=None,
)


clusters_list = db.cluster.list_clusters(headers=None)
print("Cluster name, cluster ID")

for cluster in clusters_list['clusters']:
  print(f"{cluster['cluster_name']}, {cluster['cluster_id']}")
