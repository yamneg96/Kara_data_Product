SELECT DISTINCT
    message_date::date AS date,
    EXTRACT(MONTH FROM message_date) AS month,
    EXTRACT(YEAR FROM message_date) AS year
FROM stg_telegram_messages
