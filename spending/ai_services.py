


def getbudgetplan(response_data):
    monthly_total = response_data.get("monthly_data")
    category_summary = response_data.get("category_summary")

    category_summary_text = "" 

    for di in category_summary:
        category_summary_text += f".{di.get("category")} - ₹ {di.get("total")} \n"

    print(category_summary_text)
