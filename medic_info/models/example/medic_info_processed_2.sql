-- models/medic_info_processed.sql
{{ config(materialized='table') }}  

SELECT
    CAST(date AS DATE) AS date,  
    sender,
    content
FROM {{ source('medic_info_raw_source', 'medic_info_raw') }} 
