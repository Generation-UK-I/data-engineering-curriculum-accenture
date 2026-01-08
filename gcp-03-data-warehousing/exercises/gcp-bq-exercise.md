# GCP-BQ-Exercise

## Load Data to GCS - Optional

1. Create a bucket with name `2022-jlr-de-training-<your-name>`.
1. Load raw data for the session (all the files under dataset directory) to your GCS bucket using `gsutil` commands. (use this bucket for the next exercises)

## Load Data to Bigquery

1. Load raw data for trips at `2018-01-02` to the trips table under your raw dataset.
1. Fill your `fact_region_gender_daily` table under your data warehouse dataset with the trips for `2018-01-02`.
1. Fill your `fact_trips_daily` table under your data warehouse dataset with the trips for `2018-01-02`.

## Data Mart

1. Using your `fact_region_gender_daily` and `dim_regions` tables in you data warehouse dataset, write a query that results region-name and total trips for the top-3 regions that had most trips for females at `2018-01-01` with the Descending order based on total_trips.
1. Create a view with name `top_2_region_by_capacity` under you data mart dataset that shows region_id, total_capacity for the top-2 stations with the Descending order based on total_capacity.
