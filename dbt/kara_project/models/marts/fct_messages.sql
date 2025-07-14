SELECT
    id AS message_id,
    channel_id,
    message_date,
    LENGTH(text) AS message_length,
    has_media
FROM stg_telegram_messages
