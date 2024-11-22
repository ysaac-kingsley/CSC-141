def make_cars(make, model, **info):
    info["Manufacturer"] = make
    info["Car model"] = model
    return info

print(make_cars("Toyota", "Sienna", year=2012, color= "grey"))