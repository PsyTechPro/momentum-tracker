# 60-Day Momentum Tracker

This project is a real-time momentum tracker that displays the 60-day percentage change for selected assets (cryptocurrencies, stocks, commodities, etc.).  
It automatically updates every 15 minutes using live market data and is deployed as a web app for instant viewing.  

The tracker provides an easy way to spot which assets are surging and which are lagging over a fixed time window, without having to check each asset individually.  

## Key Features
- Tracks multiple assets over the past 60 days
- Updates automatically on a 15-minute schedule
- Displays percentage change, starting price, and ending price
- Can be customized to track any asset supported by Yahoo Finance

---

## Customizing the Tracked Assets

This tracker is currently set to monitor **BTC-USD**, **ETH-USD**, **SOL-USD**, and **AAPL**.  
You can change these to any ticker symbols supported by Yahoo Finance by following the steps below.

### Step 1 — Update the Python Script
1. Open **`momentum_tracker.py`**  
2. Find the section where the symbols list is defined:
   ```python
   symbols = ["BTC-USD", "ETH-USD", "SOL-USD", "AAPL"]
Replace these with your own ticker symbols.  
Examples:  
- Tesla: `"TSLA"`  
- Microsoft: `"MSFT"`  
- Gold: `"GC=F"`  

### Step 2 — Update the HTML Display  
1. Open `index.html`  
2. Locate the table headers or display text where the asset names appear  
3. Update these names so they match your new ticker symbols for proper display  

---

## Running Locally  
If you want to test the tracker on your own machine:  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/your-username/momentum-tracker.git  
   cd momentum-tracker
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the Python script:
     bash
  python momentum_tracker.py
4. Open index.html in your browser to view the table with your updated data

## Deploying to the Web

If you want the tracker to update automatically and be accessible online (like the live version):

1. **Use GitHub Actions** (already included) to schedule updates
2. **Deploy the site to a hosting service**:
   - I highly recommend [Netlify](https://www.netlify.com/): Connect your GitHub repository, select your main branch, and deploy
3. **Ensure your hosting service**:
   - Has Python available
   - Installs dependencies from `requirements.txt`

Once deployed, the app will:
- Run on the schedule set in `.github/workflows/run.yml`
- Update automatically every 15 minutes

## Contact
If you have questions about using or customizing this tracker, or if you’d like the link to the GitHub repository for your own setup, feel free to reach out:

**Eric Weiser**  
Email: [eweiser622@gmail.com]  
GitHub: [https://github.com/PsyTechPro](https://github.com/PsyTechPro)



   
