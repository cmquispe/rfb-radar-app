def generate_insights(criteria, entities):
    insights = []

    for brand, values in entities.items():
        max_idx = values.index(max(values))
        min_idx = values.index(min(values))

        insights.append(
            f"{brand} performs strongest in {criteria[max_idx]} and weakest in {criteria[min_idx]}."
        )

    return insights
