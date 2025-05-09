# SIRV Influenza Simulation

This repository models the spread of influenza using a multi-species SIRV framework (Susceptible-Infectious-Recovered-Vaccinated). It simulates disease dynamics across:

* 🧍 Humans
* 🦆 Mallard Ducks
* 🐖 Yorkshire Pigs

##  Features

* Differential equation-based modeling with species-specific vaccination
* Graphical outputs and CSV export
* Modular code for easy extension and testing

## Repository Structure

```
sirv-influenza-model/
├── data/                       # Output CSV files
├── images/                     # Simulation plots 
├── model.py   
├── README.md                   # This file
├── requirements.txt            # Dependencies
└── LICENSE                     # Project license 
```

##  How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/sirv-influenza-model.git
cd sirv-influenza-model
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the model:

```bash
python model.py
```

The model will display plots and save the results to `data/sirv_influenza_all_species.csv`.

##  Data Sources

* **Humans**: CDC FluView 2024–2025 [CDC](https://www.cdc.gov/flu/weekly/index.htm)
* **Mallard Ducks**: USFWS Waterfowl Reports [FWS](https://www.fws.gov/media/2024-waterfowl-population-status-report)
* **Pigs**: USDA Quarterly Hogs and Pigs [USDA](https://downloads.usda.library.cornell.edu)
* **Vaccination Data**:

  * CDC flu coverage
  * Ducks Unlimited and USDA APHIS

##  References

* Biggerstaff et al. (2014), \emph{BMC Infectious Diseases}, 14(1):480
* Lessler et al. (2009), \emph{Lancet Infectious Diseases}, 9(5):291–300

## License

MIT License (or other appropriate license)

---

This project was developed for influenza modeling in a multi-species context with realistic parameterization and vaccination impact analysis.
