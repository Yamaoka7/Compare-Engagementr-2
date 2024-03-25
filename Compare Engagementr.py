def compare_engagement(handle_or_hashtag1, handle_or_hashtag2):
    # Fetch social media data for both handles/hashtags
    data1 = fetch_social_media_data(handle_or_hashtag1)
    data2 = fetch_social_media_data(handle_or_hashtag2)
    # Calculate engagement metrics for both
    engagement1 = calculate_engagement_metrics(data1)
    engagement2 = calculate_engagement_metrics(data2)
    return engagement1, engagement2

engagement1, engagement2 = compare_engagement("handle1", "handle2")
print("Engagement for Handle 1:", engagement1)
print("Engagement for Handle 2:", engagement2)
