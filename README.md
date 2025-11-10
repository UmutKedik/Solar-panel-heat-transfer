📘 Description

This Python script simulates a solar water heating system using a simplified energy balance approach.
It estimates how the temperature of a water tank changes over several days under given sunlight, efficiency, and ambient temperature conditions.

The model assumes:

The tank has uniform temperature (no stratification).

Solar input and heat losses are constant during each time step.

Water is the heat storage medium.

⚙️ How It Works

The simulation runs on a second-by-second loop (dt = 1 s), where for each time step:

1-Solar gain adds heat during sunlight hours:
2-Heat loss occurs continuously to the surrounding air:
3-The water temperature changes based on energy balance:

The loop continues for the selected number of days, printing the tank temperature at the end of each day and the total pump working hours (when the sun is shining).

🔧 Inputs

When you run the program, it will ask for:

Panel_area — surface area of the solar collector (m²)

Tank_Volume — water tank capacity (liters)

Daily_avg_temp — average outdoor temperature (°C)

Daily_sun_time_hours — average daily sunlight duration (hours)

days — number of days to simulate (max 30)

🌡️ Constants (default)
Constant	Meaning	Typical Value	Unit

Starting_tank_temp	Initial tank temperature	12.0	°C

Solar	Solar radiation intensity	800	W/m²

Panel_efficiency	Collector efficiency	0.8	

densityWater	Density of water	1.0	kg/L

heatCapacityWater	Specific heat of water	4180	J/kg°C

tankHeatLoss	Overall heat loss coefficient	5.0	W/°C

dt	Time step	1.0	s
