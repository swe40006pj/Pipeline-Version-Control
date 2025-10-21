from flask import Flask, request, jsonify, render_template, abort

app = Flask(__name__)

# Categories & units (temperature handled separately; others use linear scaling vs. a base unit)
CATEGORIES = {
    "temperature": {
        "label": "Temperature",
        "units": {
            "C": "Celsius (°C)",
            "F": "Fahrenheit (°F)"
        }
    },
    "length": {
        "label": "Length",
        "units": {
            "m": "Meter (m)",
            "cm": "Centimeter (cm)",
            "inch": "Inch (in)",
            "ft": "Foot (ft)"
        }
    },
    "weight": {
        "label": "Weight",
        "units": {
            "g": "Gram (g)",
            "kg": "Kilogram (kg)",
            "lb": "Pound (lb)",
            "oz": "Ounce (oz)"
        }
    },
    "energy": {
        "label": "Energy/Calories",
        "units": {
            "kJ": "Kilojoule (kJ)",
            "kcal": "Kilocalorie (kcal)",
            "BTU": "British thermal unit (BTU)"
        }
    },
    "area": {
        "label": "Area",
        "units": {
            "cm2": "Square centimeter (cm²)",
            "m2": "Square meter (m²)",
            "ft2": "Square foot (ft²)",
            "acre": "Acre (acre)"
        }
    },
    "volume": {
        "label": "Volume (Liquids, US)",
        "units": {
            "ml": "Milliliter (mL)",
            "L": "Liter (L)",
            "floz": "Fluid ounce (fl oz, US)",
            "cup": "Cup (US)",
            "gallon": "Gallon (US)"
        }
    }
}

# Linear categories: conversion factors to a base unit
# length base: m; weight base: g; energy base: kJ; area base: m²; volume base: L (US liquid units)
LINEAR_BASE = {
    "length": {
        "m": 1.0,
        "cm": 0.01,
        "inch": 0.0254,
        "ft": 0.3048
    },
    "weight": {
        "g": 1.0,
        "kg": 1000.0,
        "lb": 453.59237,
        "oz": 28.349523125
    },
    "energy": {
        "kJ": 1.0,
        "kcal": 4.184,             # 1 kcal = 4.184 kJ
        "BTU": 1.05505585262       # 1 BTU (IT) ≈ 1.05505585262 kJ
    },
    "area": {
        "m2": 1.0,
        "cm2": 1e-4,               # 1 cm² = 1e-4 m²
        "ft2": 0.09290304,         # 1 ft² = 0.09290304 m²
        "acre": 4046.8564224       # 1 acre = 4046.8564224 m²
    },
    "volume": {
        "L": 1.0,
        "ml": 0.001,                       # 1 mL = 0.001 L
        "floz": 0.0295735295625,           # US fl oz
        "cup": 0.2365882365,               # US cup
        "gallon": 3.785411784              # US liquid gallon
    }
}

def convert_linear(category: str, from_u: str, to_u: str, value: float) -> float:
    base = LINEAR_BASE[category]
    if from_u not in base or to_u not in base:
        abort(400, description="Unsupported unit for category.")
    value_in_base = value * base[from_u]
    return value_in_base / base[to_u]

def convert_temperature(from_u: str, to_u: str, value: float) -> float:
    if from_u == to_u:
        return value
    if from_u == "C" and to_u == "F":
        return value * 9/5 + 32
    if from_u == "F" and to_u == "C":
        return (value - 32) * 5/9
    abort(400, description="Unsupported temperature conversion.")

@app.route("/")
def index():
    return render_template("index.html")

@app.get("/api/categories")
def list_categories():
    return jsonify(CATEGORIES)

@app.get("/api/convert")
def api_convert():
    category = request.args.get("category", type=str)
    from_u   = request.args.get("from", type=str)
    to_u     = request.args.get("to", type=str)
    value    = request.args.get("value", type=float)

    if from_u: from_u = from_u.strip()
    if to_u: to_u = to_u.strip()

    if category not in CATEGORIES:
        abort(400, description="Unknown category.")
    if value is None:
        abort(400, description="Missing numeric 'value'.")

    units = CATEGORIES[category]["units"].keys()
    if from_u not in units or to_u not in units:
        abort(400, description="Units not allowed for this category.")

    if category == "temperature":
        result = convert_temperature(from_u, to_u, value)
    else:
        result = convert_linear(category, from_u, to_u, value)

    return jsonify({
        "category": category,
        "from": from_u,
        "to": to_u,
        "value": value,
        "result": round(result, 6)
    })

print("Jenkins test run: verifying webhook automation")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
