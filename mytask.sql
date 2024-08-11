CREATE TASK mytask_hour
  WAREHOUSE = mywh
  SCHEDULE = 'USING CRON 0 9-17 * * SUN America/Los_Angeles'
  AS
    SELECT CURRENT_TIMESTAMP;
