import pickle

# Load trained model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_cost(area, floors, location, material, building_type):

    location_map = {'Rural': 1, 'Urban': 2, 'Metro': 3}
    material_map = {'Low': 1, 'Medium': 2, 'High': 3}
    building_map = {'Residential': 1, 'Commercial': 2}

    features = [[
        area,
        floors,
        location_map[location],
        material_map[material],
        building_map[building_type]
    ]]

    prediction = max (0,model.predict(features)[0])

    cost_per_sqft = prediction / area

    return round(prediction, 2), round(cost_per_sqft, 2)