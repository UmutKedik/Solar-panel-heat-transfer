#input parameters from user
Panel_area = float(input("Please enter the panel area (m2) : "))
Tank_Volume = float(input("Please enter the tank capacity (Liter) : "))
Daily_avg_temp = float(input("Please avarage daily temperature (°C) : "))
Daily_sun_time_hours = float(input("Please write avarage daily sun duration in the area (hours) : "))   # Daily sun duration in hours

# --- Input validation ---
if Panel_area <= 0 or Tank_Volume <= 0 or Daily_sun_time_hours <= 0:
    print("Error: Panel area, tank volume, and sunlight duration must be positive numbers.")
    exit()

#constants
Starting_tank_temp = 12.0    # °C
Daily_sun_time = Daily_sun_time_hours * 3600   # Daily sun duration in seconds
Panel_efficiency = 0.8
Solar = 800.0 #Solar irradiance (sunlight power per area) W/m²
dt = 1.0 

# derived values
densityWater = 1.0   # 1 Liter= 1 kg
heatCapacityWater = 4180.0 #energy needed to change the tank’s temperature
massWaterTank = Tank_Volume * densityWater
tankHeatLoss = 5.0

# --- Days input ---
days = float(input("How many days do you want to simulate (max 30)? : "))
if days <= 0:
    print("Error: Number of days must be positive.")
    exit()
if days > 30:
    days = 30

sim_time = int(days * 24 * 3600)
TankTemp = Starting_tank_temp
Pump_hours = 0.0
t = 0.0
day_index = 0

print("Starting tank temp:",Starting_tank_temp)
while t < sim_time:
    if (t % 86400) < Daily_sun_time:
        Heat_input_from_solar = Panel_area * Solar * Panel_efficiency
        Pump_hours += dt / 3600.0
    else:
        Heat_input_from_solar = 0.0

    Heat_loss_to_environment = tankHeatLoss * (TankTemp - Daily_avg_temp)
    TankTemp += (Heat_input_from_solar - Heat_loss_to_environment) * dt / (massWaterTank * heatCapacityWater)

    if (t % 86400) == 0 and t > 0:
        day_index += 1
        print("After day", day_index, "tank temp is", round(TankTemp, 2), "°C")

    t += dt

print("\nFinal tank temp after", int(days), "days:", round(TankTemp, 2), "°C")
print("Pump ran for", round(Pump_hours, 2), "hours total.")
