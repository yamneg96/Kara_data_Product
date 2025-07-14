SELECT
    id,
    text,
    date::timestamp AS message_date,
    has_media
FROM raw_telegram_messages
