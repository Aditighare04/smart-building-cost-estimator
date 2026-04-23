def chatbot_response(user_input):
    user_input = user_input.lower()

    if "cost" in user_input:
        return "Cost depends on area, materials, floors, and location."

    elif "area" in user_input:
        return "Larger area increases overall construction cost."

    elif "material" in user_input:
        return "High-quality materials increase cost but improve durability."

    elif "floor" in user_input:
        return "More floors increase structural and labor cost."

    elif "cheap" in user_input or "low cost" in user_input:
        return "To reduce cost, choose fewer floors, standard materials, and avoid extras like basement."

    elif "time" in user_input:
        return "Construction usually takes 6–12 months depending on size."

    elif "parking" in user_input:
        return "Parking increases cost but adds convenience and value."

    else:
        return "Ask about cost, materials, floors, or building features."
